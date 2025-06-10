1. Download this code to one directory with txt file youtube_urls.txt
2. youtube_urls.txt is the file with links, delete links and add your with enter separator
3. go to terminal (command+spase, write terminal, first app)
4. if you simple download this repo, type in terminal
'''cd ./Download/youtube_downloader/'''
5. write
'''python youtube_downloader.py'''

# Instalation

First launch
```bash
git clone https://github.com/NikolaevMikhailRoma/youtube_downloader.git 
cd youtube_downloader
brew install python@3.12 ffmpeg git
python3 -m venv youtube_env
source youtube_env/bin/activate
pip install yt-dlp
python youtube_downloader.py
```

Not first launch:
Add urls in youtube_urls.txt
```bash
source youtube_env/bin/activate
python youtube_downloader.py
```




# IF PROBLEB:
## Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
## Install Python, FFmpeg and Git
brew install python@3.12 ffmpeg git
## Create and activate virtual environment
python3 -m venv youtube_env
source youtube_env/bin/activate
## Install required packages
pip install yt-dlp
## Run the script
python youtube_downloader.py

