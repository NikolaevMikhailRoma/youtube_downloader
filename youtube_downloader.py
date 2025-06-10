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

# Функция для скачивания видео и аудио
def download_video(url, output_folder):
    if LOW_QUALITY:
        # Ограничиваем качество до 360p и лучшее аудио
        format_option = 'bestvideo[height<=360]+bestaudio/best[height<=360]'
        # format_option = 'bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]/best[height<=360]'

    else:
        # Лучшее качество
        format_option = 'bestvideo+bestaudio/best'
    
    ydl_opts = {
        'format': format_option,
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Используем название видео
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        # Дополнительные параметры для оптимизации загрузки
        'noplaylist': True,  # Только одно видео, не плейлист
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