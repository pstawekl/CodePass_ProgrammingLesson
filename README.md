# Projekt na zaliczenie przedmiotu Programowanie
Aplikacja API przygotowana na zaliczenie przedmiotu Programowanie przez Jakuba Stawskiego

## Autor
Jakub Stawski
II semestr
Informatyka NST PUW
WSPA Lublin

### Opis instalacji oraz uruchomienia projektu
Do instalacji aplikacji potrzebujemy środowiska Python, minimalna wymagana wersja to 3.11.0 oraz narzędzia do instalowania paczek pythonowych PIP.
Aby zainstalować niezbędne paczki wymagane do uruchomienia projektu należy skorzystać z pliku requirements.txt, zawartego w folderze.
Korzystając z Powershell'a należy przejść do folderu projektu, następnie skorzystac z komendy

pip install -r requirements.txt

Ta komenda uruchomi skrypt instalujący niezbędne paczki dla środowiska python, które zostały przez autora określone w pliku requirements.txt.

Po udanej instalacji paczek, aplikacja powinna być możliwa do uruchomienia.
Aby uruchomić aplikację za pomocą Powershella należy z poziomu tego samego folderu, w którym znajduje się plik requirements.txt, uruchomić aplikację jako moduł za pomocą komendy

py -m project_api

### Wywołanie zapytania do uruchomionego API
Aby wywołać zapytanie do uruchomionego API oraz uzyskać od niego odpowiedź należy skorzystać z dowolnej przeglądarki internetowej.
Do następujących zapytań należy wywołać linki:
- lista obiektów:
    127.0.0.1:8000/object
- konkretny obiekt:
    127.0.0.1:8000/object/id_obiektu

