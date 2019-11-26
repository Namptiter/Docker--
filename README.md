#Python pakages
$ python3 -m pip install mysql-connector
$ python3 -m pip install -U matplotlib

#Install docker
---

#Install mySQL container
$ docker pull mysql

#Install phpmyadmin container
$ docker pull phpmyadmin/phpmyadmin

# Option
$ docker stop <image>
$ docker start <image> 
$ docker restart <image>

$ docker ps -a
$ docker ps
$ docker images

---
#Config mySQL & phpmyAdmin
$ docker run --name mysql_1 -e MYSQL_ROOT_PASSWORD=yourpass -p 3306:3306 -d mysql
$ docker exec -it mysql_1 mysql -uroot -p

mysql>  CREATE USER 'admin'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpass';
		GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
		CREATE USER 'admin'@'%' IDENTIFIED WITH mysql_native_password BY 'yourpass';
		GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH GRANT OPTION;
		#
		CREATE DATABASE IF NOT EXISTS `yourdb` COLLATE 'utf8_general_ci' ;
		GRANT ALL ON `yourdb`.* TO 'admin'@'%' ;
		FLUSH PRIVILEGES ;

$ docker run --name myadmin -d --link mysql_1:db -p 8080:80 phpmyadmin/phpmyadmin

#Open localhost:8080
