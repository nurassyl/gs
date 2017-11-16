**$OS_RELEASE** = Linux Ubuntu 16.04.3 LTS (Xenial) x64

----

##### **Install libraries, frameworks**
```
sudo chmod +x install initdb resetdb &&\
./install
```

##### **Run the MySQL database server**
```
sudo service mysql start
```

##### **Create database**
```
mysql -h localhost -P 3306 -u root -p

DROP DATABASE IF EXISTS `gs`;
CREATE DATABASE `gs` CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER DATABASE `gs` CHARACTER SET utf8 COLLATE utf8_bin;
GRANT ALL ON `gs`.* TO 'root'@'localhost';
system clear;
exit
```

##### **Configure database**
```
./initdb
```

##### **Drop all tables**
```
./resetdb
```

##### **Run the HTTP server**
```
python3.6 server.py
```

##### **Configuration**
```
export _APP_NAME=GS
export FLASK_DEBUG=1

export _MYSQL_HOST=127.0.0.1
export _MYSQL_PORT=3306
export _MYSQL_USER=root
export _MYSQL_PASSWORD=12345

export _HTTP_HOST=127.0.0.1
export _HTTP_PORT=9000
```

##### **Migrate**
```
python3.6 migrate.py
```
