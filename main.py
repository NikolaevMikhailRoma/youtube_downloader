from src.youtube_downloader import run_downloader

if __name__ == "__main__":
    """
    Main script to run the downloader.
    Set low_quality=True to download in low quality.
    """
    # Set low_quality=True to download in 360p
    run_downloader(low_quality=False)