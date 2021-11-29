# Инструкция по запуску
1. Установить зависимости:
```
pip3 install -r requirements.txt
```
2. Запустить образ с SMTP сервером:
```
sudo docker run -it -p 2500:2500 -p 8080:8080 -p 8085:8085 --rm marcopas/docker-mailslurpe
```
3. Запустить скрипт, указав имя SMTP сервера и порт (2500 в случае с примером выше):
```
python3 script.py 0.0.0.0 2500
```
