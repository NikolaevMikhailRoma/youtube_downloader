import subprocess
import argparse


def def convert_mov_to_mp4(input_file, output_file):
    """Converts a MOV file to MP4 using ffmpeg."""
    # Build the conversion command
    command = ["ffmpeg", "-i", input_file, output_file]

    try:
        subprocess.run(command, check=True)
        print("Conversion finished successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred during conversion:")
        print(e)


def main():
    parser = argparse.ArgumentParser(description="MOV to MP4 converter")
    parser.add_argument("input", help="Input MOV file path")
    parser.add_argument("output", help="Output MP4 file path")
    args = parser.parse_args()

    convert_mov_to_mp4(args.input, args.output)


if __name__ == "__main__":
    # main()
    convert_mov_to_mp4('/Users/admin/Desktop/Screen Recording 2025-02-13 at 23.48.36.mov',
                       'output.mp4')
# '/Users/admin/Desktop/Screen Recording 2025-02-13 at 23.48.36.mov'
# python converter.py input.mov output.mp4