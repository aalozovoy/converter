# /home/aa_lozovoy/Рабочий стол/123/123.MP4
# /home/aa_lozovoy/Рабочий стол/123/123_audio.mp3
import os
from converter import (
    get_file_type,
    extract_audio_from_video,
    transcribe_audio,
    transcribe_video,
    get_output_path
)


def process_video_file(file_path: str) -> None:
    """
    Обрабатывает видеофайл по выбору пользователя.
    """
    print("\nВыберите действие:")
    print("1. Извлечь аудио из видео")
    print("2. Транскрибировать видео")
    choice = input("Ваш выбор: ").strip()

    if choice == '1':
        output_path = get_output_path(file_path, "_audio.mp3")
        success, msg = extract_audio_from_video(file_path, output_path)
        if success:
            print(f"\n✅ Аудио сохранено: {os.path.basename(output_path)}")
        else:
            print(f"\n❌ Ошибка: {msg}")

    elif choice == '2':
        output_path = get_output_path(file_path, "_transcript.txt")
        success, text = transcribe_video(file_path)
        if success:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"\n✅ Транскрипт сохранён: {os.path.basename(output_path)}")
        else:
            print(f"\n❌ Ошибка: {text}")

    else:
        print("\n❌ Неверный выбор!")


def process_audio_file(file_path: str) -> None:
    """
    Обрабатывает аудиофайл автоматической транскрибацией.
    """
    output_path = get_output_path(file_path, "_transcript.txt")
    success, text = transcribe_audio(file_path)

    if success:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"\n✅ Транскрипт сохранён: {os.path.basename(output_path)}")
    else:
        print(f"\n❌ Ошибка: {text}")


def main():
    print("\n=== Видео/Аудио Конвертер ===")
    file_path = input("Введите полный путь к файлу: ").strip()

    if not os.path.exists(file_path):
        print("\n❌ Файл не найден!")
        return

    file_type = get_file_type(file_path)

    if file_type == 'video':
        process_video_file(file_path)
    elif file_type == 'audio':
        process_audio_file(file_path)
    else:
        print("\n❌ Формат файла не поддерживается")


if __name__ == "__main__":
    main()