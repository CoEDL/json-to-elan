# JSON to ELAN

The script looks in a folder, and generates an ELAN file to match each JSON file.

## JSON format

It has been written for the JSON output from Huggingface ASR pipelines. Here's an example of the expected JSON format. 

```json
[
    {
        "text": "luanghan",
        "timestamp":
        [
            1.16,
            1.48
        ]
    },
    {
        "text": "ian",
        "timestamp":
        [
            1.56,
            1.7
        ]
    }
]
```

## Basic usage


Put your JSON files somewhere easily accessible, eg in a `data` folder in your working directory. Install it. Use it by providing a path to your data.

```python
pip install json-to-elan
```
```python
from json_to_elan import make_elan 
make_elan(data_dir="content")
```

## Using this in Colab? 

To use this in Google Colab, upload your JSON files into the File browser. Then define the data directory as:
```python
data_dir="/content"
``` 


## Options

You can also set a different tier name from the default (which is "default"). 

The ELAN file gets a linked media file written, for which we assume that the media file is  a WAV with the same name as the JSON file. If you want to change this to MP3, change the audio_format. 

Here's an example:
```python
make_elan(data_dir="content", tier_name="Words", audio_format="mp3")
```

