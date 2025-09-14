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
    import subprocess
import argparse

def convert_mov_to_mp4(input_file: str, output_file: str) -> None:
    """Converts a MOV file to MP4 using the ffmpeg tool."""
    # This command uses ffmpeg to convert the input file to MP4.
    command = ["ffmpeg", "-i", input_file, output_file]

    try:
        # Executes the command and checks for errors.
        subprocess.run(command, check=True)
        print("Conversion finished successfully.")
    except subprocess.CalledProcessError as e:
        # Reports any errors that occur during conversion.
        print(f"An error occurred during conversion: {e}")
    except FileNotFoundError:
        # Handles cases where ffmpeg is not installed.
        print("Error: 'ffmpeg' is not installed. Please install it to use this script.")

def main() -> None:
    """Parses command-line arguments and runs the conversion."""
    parser = argparse.ArgumentParser(description="MOV to MP4 converter")
    parser.add_argument("input", help="Input MOV file path")
    parser.add_argument("output", help="Output MP4 file path")
    args = parser.parse_args()

    convert_mov_to_mp4(args.input, args.output)

if __name__ == "__main__":
    # To use this script, run it from the command line with the input and output file paths:
    # python tools/mov2mp4.py input.mov output.mp4
    main()

# '/Users/admin/Desktop/Screen Recording 2025-02-13 at 23.48.36.mov'
# python converter.py input.mov output.mp4