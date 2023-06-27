--- This file is used to setup the database for the quiz app.

--- A user is created with the name quiz_app_user and password quiz_app_password.
--- The user is granted all privileges on the quiz_app_db database.
--- The user is granted select privileges on the performance_schema database.
--- The database is created if it does not exist.
--- The user is created if it does not exist.


CREATE DATABASE IF NOT EXISTS quiz_app_db;
CREATE USER IF NOT EXISTS 'quiz_app_user'@'localhost' IDENTIFIED BY 'quiz_app_password';
GRANT ALL PRIVILEGES ON quiz_app_db.* TO 'quiz_app_user'@'localhost';
GRANT SELECT ON perfomance_schema.* TO 'quiz_app_user'@'localhost';
FLUSH PRIVILEGES;