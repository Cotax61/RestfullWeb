CREATE DATABASE IF NOT EXISTS epytodo;
USE epytodo;

CREATE TABLE IF NOT EXISTS user
    (
        user_id INT NOT NULL PRIMARY auto_increment KEY,
        username CHAR(16) NOT NULL,
        password CHAR(100) NOT NULL
    );

CREATE TABLE IF NOT EXISTS task
    (
        task_id INT NOT NULL auto_increment PRIMARY KEY,
        title CHAR(60) NOT NULL,
        begin TIMESTAMP,
        end TIMESTAMP,
        status ENUM('not started' DEFAULT, 'in progress', 'done')
    );

CREATE TABLE IF NOT EXISTS user_has_task
    (
        fk_user_id INT NOT NULL,
        fk_task_id INT NOT NULL,
        INDEX (fk_user_id),
        FOREIGN KEY (fk_user_id) REFERENCES user(user_id),
        INDEX (fk_task_id),
        FOREIGN KEY (fk_task_id) REFERENCES task(task_id),
        PRIMARY KEY (fk_task_id, fk_user_id)
    );