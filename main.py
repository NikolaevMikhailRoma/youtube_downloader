
from src.youtube_downloader import run_downloader

if __name__ == "__main__":
    # Main entry point to run the downloader.
    # Set low_quality=True to download videos in 360p.
    run_downloader(low_quality=False)
