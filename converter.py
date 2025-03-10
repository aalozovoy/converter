import os
import tempfile
import moviepy.editor as mp
from pydub import AudioSegment
import speech_recognition as sr


def get_file_type(file_path: str) -> str:
    """
    Определяет тип файла по расширению.

    Возвращает:
        'audio' - для аудиофайлов
        'video' - для видеофайлов
        'unknown' - для других форматов
    """
    audio_ext = {'.mp3', '.wav', '.ogg', '.flac'}
    video_ext = {'.mp4', '.avi', '.mov', '.mkv', '.mpeg'}
    ext = os.path.splitext(file_path)[1].lower()
    return 'audio' if ext in audio_ext else 'video' if ext in video_ext else 'unknown'


def extract_audio_from_video(video_path: str, output_path: str) -> tuple[bool, str]:
    """
    Извлекает аудио из видео в формате MP3.
    """
    try:
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(output_path)
        return True, ""
    except Exception as e:
        return False, str(e)


def transcribe_audio(audio_path: str) -> tuple[bool, str]:
    """
    Транскрибирует аудио любого размера через chunk-обработку.
    """
    try:
        audio = AudioSegment.from_file(audio_path)
        audio = audio.set_frame_rate(16000).set_channels(1)

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as tmp_wav:
            audio.export(tmp_wav.name, format="wav", bitrate="16k")
            recognizer = sr.Recognizer()
            full_text = []

            with sr.AudioFile(tmp_wav.name) as source:
                duration = source.DURATION
                chunk_size = 30  # seconds

                for i in range(0, int(duration), chunk_size):
                    print(f"Обработка: {i}-{i + chunk_size} сек...")
                    chunk = recognizer.record(source, duration=chunk_size, offset=i)
                    try:
                        text = recognizer.recognize_google(chunk, language="ru-RU")
                        full_text.append(text)
                    except sr.UnknownValueError:
                        full_text.append("[неразборчиво]")
                    except Exception as e:
                        return False, f"Ошибка на {i} сек: {str(e)}"

            return True, "\n".join(full_text)
    except Exception as e:
        return False, str(e)


def transcribe_video(video_path: str) -> tuple[bool, str]:
    """
    Транскрибирует видео через временный аудиофайл.
    """
    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as tmp_audio:
            success, msg = extract_audio_from_video(video_path, tmp_audio.name)
            if not success:
                return False, msg
            return transcribe_audio(tmp_audio.name)
    except Exception as e:
        return False, str(e)


def get_output_path(input_path: str, suffix: str) -> str:
    """
    Генерирует путь для выходного файла.
    Пример:
        input.mp4 + "_audio.mp3" → input_audio.mp3
    """
    base = os.path.splitext(input_path)[0]
    return f"{base}{suffix}"