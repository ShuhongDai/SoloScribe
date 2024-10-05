# SoloScribe: A Lightweight Speech-to-Text Tool

SoloScribe is a Python-based tool that I developed to efficiently convert speech to text, leveraging reliable machine learning methods. The tool is designed to be lightweight and easy to use, offering seamless functionality for both individual and batch audio file transcription.  However, it is lightweight and easy to use. The tool provides functionalities for transcribing individual audio files or batch processing multiple files in a directory. The transcription results can be optionally saved to text files for later use.

## Features
- Transcribe individual audio files to text.
- Batch transcribe all audio files in a specified directory.
- Supports multiple audio formats: `.mp3`, `.wav`, `.flac`, `.ogg`.
- Option to save transcription results to text files.
- Uses a customized version of the Whisper model, available in various sizes (`tiny`, `base`, `small`, `medium`, `large`), adapted to provide efficient transcription in different scenarios.

## Prerequisites
- Python 3.7 or later
- FFmpeg (for handling various audio formats)
- Required Python packages: `whisper`, `argparse`, `logging`

To install the necessary dependencies, including Whisper and FFmpeg, run the following commands:
```sh
pip install git+https://github.com/openai/whisper.git
pip install ffmpeg-python
```
Ensure FFmpeg is installed and available in your system path.

## Usage
### Command Line Arguments
- `--model_size`: Specify the size of the Whisper model (`tiny`, `base`, `small`, `medium`, `large`). Default is `base`.
- `--audio_file`: Path to a single audio file to transcribe.
- `--audio_directory`: Path to a directory containing audio files for batch transcription.
- `--save_to_file`: Add this flag to save transcription results to text files.

### Examples
#### Transcribe a Single Audio File
```sh
python 1.py --model_size large --audio_file /root/SoloScribe/test.mp3
```
This command will use the `large` Whisper model to transcribe the audio file `/root/SoloScribe/test.mp3` and print the transcription to the console.

#### Transcribe and Save to File
```sh
python 1.py --model_size large --audio_file /root/Speech2Text/test.mp3 --save_to_file
```
This command will use the `large` Whisper model to transcribe the audio file `/root/SoloScribe/test.mp3` and save the transcription to `/root/SoloScribe/test.txt`.

#### Batch Transcribe Audio Files in a Directory
```sh
python 1.py --model_size base --audio_directory /root/SoloScribe/audio_files --save_to_file
```
This command will transcribe all audio files in the directory `/root/SoloScribe/audio_files` using the `base` model and save each transcription to a corresponding text file.

## Handling Common Issues
### Fixing Unterminated String Literal Errors
During the development of SoloScribe, I specifically tackled an issue related to unterminated string literals, which is a common syntax error in Python. This enhancement ensures a more robust and error-free experience for end users. This problem can occur when a string is not properly closed with quotation marks. To fix this issue, we ensured that all strings, especially those in formatted print statements, are properly closed to prevent runtime errors.

If you encounter similar issues, double-check that all strings in your code are correctly enclosed within matching quotation marks (`"` or `'`). This will help prevent syntax errors and ensure the code runs smoothly.

## Logging
The tool uses Python's logging module to log various stages of the transcription process, including loading models, processing files, and saving results. Logs are printed to the console for easy monitoring.

## License
This project uses OpenAI's Whisper, which is open-source. Please ensure you comply with any applicable licensing requirements.

## Acknowledgments
- OpenAI for the Whisper model.
- FFmpeg for handling different audio formats.
