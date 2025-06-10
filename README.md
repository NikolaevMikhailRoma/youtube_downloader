1. Download this code to one directory with txt file youtube_urls.txt
2. youtube_urls.txt is the file with links, delete links and add your with enter separator
3. go to terminal (command+spase, write terminal, first app)
4. if you simple download this repo, type in terminal
'''cd ./Download/youtube_downloader/'''
5. write
'''python youtube_downloader.py'''

IF DONT WORK:
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Install Python, FFmpeg and Git
brew install python@3.12 ffmpeg git
# Create and activate virtual environment
python3 -m venv youtube_env
source youtube_env/bin/activate
# Install required packages
pip install yt-dlp
# Run the script
python youtube_downloader.py
