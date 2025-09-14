import subprocess
import argparse


def convert_mov_to_mp4(input_file, output_file):
    """
    Конвертирует MOV файл в MP4 файл, используя ffmpeg.
    """
    # Формируем команду для конвертации
    command = ["ffmpeg", "-i", input_file, output_file]

    try:
        subprocess.run(command, check=True)
        print("Конвертация успешно завершена.")
    except subprocess.CalledProcessError as e:
        print("Произошла ошибка во время конвертации:")
        print(e)


def main():
    parser = argparse.ArgumentParser(description="Конвертер MOV в MP4")
    parser.add_argument("input", help="Путь к входному MOV файлу")
    parser.add_argument("output", help="Путь к выходному MP4 файлу")
    args = parser.parse_args()

    convert_mov_to_mp4(args.input, args.output)


if __name__ == "__main__":
    # main()
    convert_mov_to_mp4('/Users/admin/Desktop/Screen Recording 2025-02-13 at 23.48.36.mov',
                       'output.mp4')
# '/Users/admin/Desktop/Screen Recording 2025-02-13 at 23.48.36.mov'
# python converter.py input.mov output.mp4
