import os
import yt_dlp
import shutil

# Выбор качества
LOW_QUALITY = False  # Переключи на True для низкого качества

# Путь к файлу со ссылками
file_path = "youtube_urls.txt"
download_dir = "downloads"

# Очищаем
# if os.path.exists(download_dir):
#     shutil.rmtree(download_dir)
# и создаем папку заново
# os.makedirs(download_dir)

# Читаем ссылки из файла
with open(file_path, "r") as file:
    urls = [line.strip() for line in file if line.strip()]

# Функция для получения названия плейлиста
def get_playlist_title(url):
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

# Функция для скачивания видео и аудио
def download_video(url, output_folder):
    if LOW_QUALITY:
        # Ограничиваем качество до 360p и лучшее аудио
        format_option = 'bestvideo[height<=360]+bestaudio/best[height<=360]'
        # format_option = 'bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]/best[height<=360]'

    else:
        # Лучшее качество
        format_option = 'bestvideo+bestaudio/best'
    
    # Проверяем, если это плейлист
    if 'playlist' in url:
        playlist_title = get_playlist_title(url)
        output_folder = os.path.join(output_folder, playlist_title)
        os.makedirs(output_folder, exist_ok=True)
        noplaylist = False
    else:
        noplaylist = True
    
    # Настройка шаблона имени файла для плейлистов
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
        # Дополнительные параметры для оптимизации загрузки
        'noplaylist': noplaylist,  # Для плейлистов разрешаем скачивание всех видео
        'restrictfilenames': False,  # Разрешаем специальные символы в именах
        'throttled-rate': '1M',  # Ограничение скорости загрузки для стабильности
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Запускаем загрузку для всех ссылок
for url in urls:
    print(f"Скачивание: {url}")
    download_video(url, download_dir)

print("✅ Загрузка завершена!")