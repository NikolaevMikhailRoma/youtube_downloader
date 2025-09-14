
import os
import yt_dlp

class MyLogger:
    def debug(self, msg):
        if "has already been downloaded" in msg:
            print("  File already downloaded.")
        elif msg.startswith('[Merger]'):
            print('  Converting to mp4...')

    def info(self, msg):
        if msg.startswith('[Merger]'):
            print('  Converting to mp4...')

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

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

def _download_video(url, output_folder, low_quality, file_num, total_files):
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

    printed_filename = False
    def _progress_hook(d):
        nonlocal printed_filename
        if d['status'] == 'downloading':
            if not printed_filename:
                filename = os.path.basename(d['info_dict'].get('_filename', ''))
                print(f"File {file_num}/{total_files}: {filename}")
                printed_filename = True
            
            percent_str = d.get('_percent_str', '---.-%').strip()
            speed_str = d.get('_speed_str', '----.-B/s').strip()
            eta_str = d.get('_eta_str', 'N/A').strip()
            print(f'  Downloading: {percent_str} at {speed_str} ETA: {eta_str}   ', end='\r')
        elif d['status'] == 'finished':
            elapsed_time = d.get('elapsed')
            if elapsed_time:
                minutes, seconds = divmod(int(elapsed_time), 60)
                print(f'Download finished in {minutes}m {seconds}s.')
    
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
        'logger': MyLogger(),
        'progress_hooks': [_progress_hook],
        'no_warnings': True,
        'noprogress': True,
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

    total_urls = len(urls)
    for i, url in enumerate(urls):
        print(f"Downloading: {url}")
        try:
            _download_video(url, download_dir, low_quality, i + 1, total_urls)
        except Exception as e:
            print(f"Failed to download {url}. Error: {e}")

    print("\nDownload finished!")
