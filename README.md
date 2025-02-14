# Парсер текстовых трансляций матчей с flashscorekz.com

## Установка

*Для работы программы нужен установленный [python](https://www.python.org/downloads/)*

1. Скачайте проект (или только нужный **скрипт** и **requirements.txt**)
  
3. Создайте виртуальное окружение (здесь и далее команды в консоль, запускать из каталога со скачанным скриптом)

```sh
python -m venv .venv
```

3. Активируйте виртуальное окружение

**Windows:**

```sh
./.venv/Scripts/activate
```

**Linux/MacOS**

```sh
source .venv/bin/activate
```

4. Установите зависимости

```sh
pip install -r requirements.txt
```

5. Всё готово к использованию

## Запуск

### from_console.py

Запустите скрипт

```sh
python from_console.py
```

и введите в консоль ссылку на матч в формате

> https://www.flashscorekz.com/match/{id_матча}/#/match-summary/live-commentary/0

### from_txt.py

Создайте файл **input.txt** в каталоге со скриптом, в который введите нужные ссылки каждая с новой строки и запустите скрипт

```sh
python from_txt.py
```

## Результат

По завершении работы скрипта в каталоге **results** появятся файлы с текстовыми трансляциями матчей
