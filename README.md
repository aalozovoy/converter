# 🎥 Видео/Аудио Конвертер и Транскриптор 🎧

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

Проект для извлечения аудио из видео и транскрибации медиафайлов.  
**Поддерживаемые форматы**: MP4, AVI, MOV, MKV, MP3, WAV.

---

## 🛠️ Установка зависимостей (все в одной команде!)

# Установите всё одной строкой! (для Linux/macOS)
sudo apt update && sudo apt install ffmpeg -y && pip install moviepy speechrecognition pydub && pip freeze | grep -E "moviepy|SpeechRecognition|pydub" > requirements.txt

Что делает скрипт:
🔄 Обновляет пакеты (sudo apt update)
📥 Устанавливает FFmpeg (обязательная зависимость)
📦 Ставит Python-библиотеки:
moviepy (работа с видео)
speechrecognition (транскрибация)
pydub (конвертация аудио)
💾 Сохраняет зависимости в requirements.txt

▶️ Быстрый старт
# 1. Активируйте виртуальное окружение (рекомендуется)
python -m venv .venv && source .venv/bin/activate

# 2. Запустите скрипт
python main.py


🚨 Если возникли ошибки:
# Переустановите зависимости через requirements.txt
pip install -r requirements.txt

# Проверьте FFmpeg
ffmpeg -version

⚠️ ВАЖНО: Для Windows скачайте FFmpeg, добавьте в PATH, затем выполните:
pip install moviepy speechrecognition pydub


Удачного кодинга! 🚀