import dataset

db = dataset.connect('postgresql://postgres:root@localhost:5432/reversia')

# CREATE TABLE `reversia`.`users` (`userId` BIGINT NOT NULL AUTO_INCREMENT , `username` VARCHAR(50) NOT NULL , `email` VARCHAR(255) NOT NULL , `password` VARCHAR(50) NOT NULL , PRIMARY KEY (`userId`), UNIQUE (`email`)) ENGINE = MyISAM; 