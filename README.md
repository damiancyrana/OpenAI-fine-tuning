# Instrukcja uruchomienia

## Krok 1: Utwórz plik `.env`
W katalogu głównym swojego projektu stwórz nowy plik o nazwie `.env`. Możesz to zrobić bezpośrednio w edytorze tekstowym lub za pomocą terminala (np. w systemie Linux/MacOS)

**Przykład w terminalu:**

```bash
touch .env
```

## Krok 2: Dodaj klucz API do pliku .env
Otwórz plik .env w edytorze tekstowym i dodaj klucz API w następującym formacie:

`OPENAI_API_KEY="twój_klucz_api"`

Zastąp twój_klucz_api swoim prawdziwym kluczem API.

## Krok 3: Zapisz plik
Po dodaniu klucza, zapisz plik .env i upewnij się, że znajduje się on w tym samym katalogu, co Twój skrypt Python

## Krok 4: Zainstaluj biblioteki z pliku requirements.txt
1. Utworzenie wirtualnego środowiska:
`python -m venv venv`

2. Aktywacja wirtualnego środowiska:
    - Na Windows: `venv\Scripts\activate`
    - Na Mac/Linux: `source venv/bin/activate`

3. Użyj poniższego polecenia, aby zainstalować wszystkie pakiety wymienione w pliku requirements.txt:
`pip install -r requirements.txt`

## Krok 5: Uruchom program
Otwórz terminal i uruchom polecenie `python tunning.py`, po wykonaniu programu otrzymasz jako odpowiedź nazwę wytrenowanego modelu
