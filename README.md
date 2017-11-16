**$OS_RELEASE** = Linux Ubuntu 16.04.3 LTS (Xenial) x64

----

##### **Install libraries, frameworks**
```
sudo chmod +x install initdb resetdb &&\
./install
```

##### **Create database**
```
mysql -h localhost -P 3306 -u root -p

CREATE DATABASE `translator` CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER DATABASE `translator` CHARACTER SET utf8 COLLATE utf8_bin;
GRANT ALL ON `translator`.* TO 'root'@'localhost';
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
