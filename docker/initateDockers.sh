docker run -d --name dsin_db -e MYSQL_ROOT_PASSWORD=dsin_password -e MYSQL_DATABASE=export -e MYSQL_USER=dsin_user -p 25060:3306 mariadb:latest;

docker run --name myadmin -d -p 8081:80 -e PMA_USER=root -e PMA_HOST=172.17.0.2 -e PMA_PASSWORD=dsin_password phpmyadmin
