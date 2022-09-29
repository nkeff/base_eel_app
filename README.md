# Шаблон приложения на EEL
Кроссплатформенное web-view приложение на Python

## Установка
```
git clone https://github.com/nkeff/base_eel_app
```
Linux ->
```
python -m venv env && source ./env/bin/activate && pip install -r requirements.txt
```
Windows ->
```
python -m venv env
env/Script/activate.bat
python -m pip install -r requirements.txt
```
Скачать [отсюда](https://download-chromium.appspot.com/) версию chromium для своей платформы и распаковать ее в ./resourses/driver (путь до исполняемого файла должен быть ./resourses/driver/chrome)

## Запуск
```
python run.py
```

## Сборка в исполняемый файл
Настроить имя приложения можно в pyinstaller.py
```
python pyinstaller.py
```
Исполняемый файл с необходимыми ресурсами появится в папке **dist**
