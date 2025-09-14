import os
import yt_dlp

def _get_playlist_title(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info.get('title', 'Unknown_Playlist').replace('/', '_').replace('\\', '_')
        except:
            return 'Unknown_Playlist'

def _download_video(url, output_folder, low_quality):
    if low_quality:
        format_option = 'bestvideo[height<=360]+bestaudio/best[height<=360]'
    else:
        format_option = 'bestvideo+bestaudio/best'
    
    if 'playlist' in url:
        playlist_title = _get_playlist_title(url)
        output_folder = os.path.join(output_folder, playlist_title)
        os.makedirs(output_folder, exist_ok=True)
        noplaylist = False
    else:
        noplaylist = True
    
    if 'playlist' in url:
        outtmpl = os.path.join(output_folder, '%(playlist_index)s_%(title)s.%(ext)s')
    else:
        outtmpl = os.path.join(output_folder, '%(title)s.%(ext)s')
    
    ydl_opts = {
        'format': format_option,
        'outtmpl': outtmpl,
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'noplaylist': noplaylist,
        'restrictfilenames': False,
        'throttled-rate': '1M',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def run_downloader(low_quality: bool = False, urls_file: str = "youtube_urls.txt", download_dir: str = "vidoses"):
    """
    Runs the YouTube video download process.

    :param low_quality: True for low quality (max 360p), False for best quality.
    :param urls_file: Path to the file with video URLs.
    :param download_dir: Directory to save videos.
    """
    try:
        with open(urls_file, "r") as file:
            urls = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{urls_file}' not found. Please create it and add video URLs.")
        return

    if not urls:
        print(f"File '{urls_file}' is empty. Add URLs to download.")
        return

    os.makedirs(download_dir, exist_ok=True)

    for url in urls:
        print(f"Downloading: {url}")
        try:
            _download_video(url, download_dir, low_quality)
        except Exception as e:
            print(f"Failed to download {url}. Error: {e}")

    print("Download finished!")