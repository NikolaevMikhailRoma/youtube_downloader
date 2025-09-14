Download this code to one directory with txt file youtube_urls.txt. It is the file with links, delete links and add your with enter separator

# Instalation

First launch (go to terminal)
```bash
git clone https://github.com/NikolaevMikhailRoma/youtube_downloader.git 
cd youtube_downloader
brew install python@3.12 ffmpeg git
python3 -m venv .venv
source .venv/bin/activate
pip install yt-dlp
python main.py
```

Not first launch:
Add urls in youtube_urls.txt
```bash
source .venv/bin/activate
python main.py
```

# IF PROBLEBs:
## Install Homebrew if not installed
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
## Install Python, FFmpeg and Git
```bash
brew install python@3.12 ffmpeg git
```
## Drop directory and start "First launch" instalaiton


