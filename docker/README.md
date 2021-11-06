### Создание образа из Dockerfile в текущем каталоге
sudo docker build --tag=crud .

### Вывод списка имеющихся образов
sudo docker image ls

### Запуск контейнера с существующим образом
sudo docker run -d -p 8000:8000 crud

### Вывод списка запущенных контейнеров
sudo docker ps

### Подключение к консоли запущенного контейнера
sudo docker exec -ti %container_id% sh