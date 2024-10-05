import os
import whisper
import logging
import argparse
import subprocess

# Set up logging configuration to record system operations
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SpeechToText:
    def __init__(self, model_size="base"):
        """
        Initialize the model.
        :param model_size: Whisper model size, can be 'tiny', 'base', 'small', 'medium', 'large'
        """
        logging.info(f"Loading Whisper model: {model_size}")
        self.model = whisper.load_model(model_size)
        logging.info("Model loaded successfully.")

    def transcribe(self, audio_path, save_to_file=False):
        """
        Transcribe the given audio file to text.
        :param audio_path: Path to the audio file
        :param save_to_file: Whether to save the transcription to a text file
        :return: Transcribed text
        """
        try:
            logging.info(f"Transcribing audio file: {audio_path}")
            result = self.model.transcribe(audio_path)
            logging.info("Transcription completed successfully.")
            transcription = result["text"]

            if save_to_file:
                txt_file_path = os.path.splitext(audio_path)[0] + ".txt"
                with open(txt_file_path, "w") as txt_file:
                    txt_file.write(transcription)
                logging.info(f"Transcription saved to {txt_file_path}")

            return transcription
        except Exception as e:
            logging.error(f"Error during transcription: {e}")
            return None

    def transcribe_directory(self, directory_path, save_to_file=False):
        """
        Batch transcribe all audio files in the directory.
        :param directory_path: Path to the audio files directory
        :param save_to_file: Whether to save each transcription to a text file
        :return: Dictionary containing transcription results for each file
        """
        transcriptions = {}
        for filename in os.listdir(directory_path):
            if filename.endswith(('.mp3', '.wav', '.flac', '.ogg')):
                audio_path = os.path.join(directory_path, filename)
                transcription = self.transcribe(audio_path, save_to_file=save_to_file)
                if transcription:
                    transcriptions[filename] = transcription
        return transcriptions

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Speech to Text using OpenAI Whisper")
    parser.add_argument("--model_size", type=str, default="base", help="Whisper model size: tiny, base, small, medium, large")
    parser.add_argument("--audio_file", type=str, help="Path to the audio file to transcribe")
    parser.add_argument("--audio_directory", type=str, help="Path to the directory containing audio files to transcribe")
    parser.add_argument("--save_to_file", action="store_true", help="Save the transcription to a text file")

    args = parser.parse_args()

    # Instantiate the class and specify the model size
    speech_to_text = SpeechToText(model_size=args.model_size)

    # Transcribe a single audio file if provided
    if args.audio_file:
        transcription = speech_to_text.transcribe(args.audio_file, save_to_file=args.save_to_file)
        if transcription:
            print(f"Transcription for {args.audio_file}:\n{transcription}")

    # Batch transcribe audio files in the directory if provided
    if args.audio_directory:
        transcriptions = speech_to_text.transcribe_directory(args.audio_directory, save_to_file=args.save_to_file)
        for filename, text in transcriptions.items():
            print(f"Transcription for {filename}:\n{text}")