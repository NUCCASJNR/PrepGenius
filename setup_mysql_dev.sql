--- sql script


CREATE DATABASE IF NOT EXISTS prep_genius_db;
CREATE USER IF NOT EXISTS 'prep_genius_user'@'localhost' IDENTIFIED BY 'prep_genius_password';
GRANT ALL PRIVILEGES ON prep_genius_db.* TO 'prep_genius_user'@'localhost';
GRANT SELECT ON perfomance_schema.* TO 'prep_genius_user'@'localhost';
FLUSH PRIVILEGES;