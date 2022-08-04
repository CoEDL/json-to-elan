import argparse
import os
import glob
from pathlib import Path
import json
from pympi.Elan import Eaf


def make_elan(tier_name: str = "default", data_dir: str = "data", audio_format: str = "wav"):
    """
    Make ELAN files based on JSON data.
    :param tier_name: The name of the tier to write into
    :param data_dir: Directory name of folder containing JSON files
    :param audio_format: File type of audio to add as linked media
    """
    json_files = glob.glob(data_dir + "/*.json", recursive=False)
    for file_path in json_files:
        basename, ext = os.path.splitext(os.path.basename(file_path))
        # read the JSON
        with open(file_path) as json_file:
            annotation_data = json.load(json_file)
        # Make EAF file
        # JSON format we expect is Huggingface pipeline ASR output. See README.md for an example.
        output_eaf = Eaf()
        for annotation in annotation_data:
            # HF time info is in seconds, but ELAN wants milliseconds
            start = int(annotation["timestamp"][0] * 1000)
            end = int(annotation["timestamp"][1] * 1000)
            output_eaf.add_annotation("default", start, end, value=annotation["text"])
        if tier_name != "default":
            output_eaf.rename_tier("default", tier_name)
        output_eaf.add_linked_file(f'{basename}.{audio_format}')
        output_eaf.to_file(str(Path(data_dir, f'{basename}.eaf')))


def main():
    parser = argparse.ArgumentParser(description='Make ELAN files from JSON data')
    parser.add_argument('-t', '--tier_name', help='Name of the tier', default='default')
    parser.add_argument('-d', '--data_dir', help='Folder of JSON files', default='data')
    parser.add_argument('-a', '--audio_format', help='Format of audio, WAV, MP3?', default='wav')
    args = parser.parse_args()
    make_elan(tier_name=args.tier_name,
               data_dir=args.data_dir,
               audio_format=args.audio_format)


if __name__ == '__main__':
    main()
