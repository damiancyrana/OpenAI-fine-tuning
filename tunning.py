#by Damian Cyrana
import os
import time
import logging
from openai import OpenAI
from dotenv import load_dotenv


MODEL = "gpt-4o-mini-2024-07-18"
"""
https://platform.openai.com/docs/guides/fine-tuning

Fine-tuning is currently 28.09.2024 available for the following models:
gpt-4o-2024-08-06
gpt-4o-mini-2024-07-18
gpt-4-0613
gpt-3.5-turbo-0125
gpt-3.5-turbo-1106
gpt-3.5-turbo-0613
babbage-002
davinci-002
"""
FILE_PATH_TO_TRAINING_FILE = "train_data_prepared.jsonl"


# Inicjalizacja instancji klienta OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Przesyłanie pliku treningowego
try:
    with open(FILE_PATH_TO_TRAINING_FILE, "rb") as f:
        training_file_response = client.files.create(
            file=f,
            purpose="fine-tune"
        )
    training_file_id = training_file_response.id
    logging.info(f"Przesłano plik treningowy: {training_file_id}")
except Exception as e:
    logging.error(f"Błąd podczas przesyłania pliku treningowego: {e}")
    exit(1)

# Tworzenie zadania fine-tuning
try:
    fine_tune_response = client.fine_tuning.jobs.create(
        training_file=training_file_id,
        model=MODEL,

    )
    fine_tune_id = fine_tune_response.id
    logging.info(f"Utworzono zadanie fine-tuning: {fine_tune_id}")
except Exception as e:
    logging.error(f"Błąd podczas tworzenia zadania fine-tuning: {e}")
    exit(1)

# Monitorowanie zadania
try:
    while True:
        status_response = client.fine_tuning.jobs.retrieve(fine_tune_id)
        status = status_response.status
        logging.info(f"Status zadania: {status}")
        if status in ['succeeded', 'failed']:
            break
        time.sleep(10)

    if status == 'succeeded':
        fine_tuned_model = status_response.fine_tuned_model
        logging.info(f"Model fine-tuned: {fine_tuned_model}")
    elif status == 'failed':
        error_message = status_response.error.message if status_response.error else "Unknown error"
        logging.error(f"Fine-tuning zakończył się niepowodzeniem: {error_message}")
except Exception as e:
    logging.error(f"Błąd podczas monitorowania zadania fine-tuning: {e}")
    exit(1)
