CREATE DATABASE IF NOT EXISTS learning;

USE learning;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email) VALUES
('Alice', 'alice@email.ro'),
('Bob', 'alice@email.ro'),
('Charlie', 'alice@email.ro'),
('David', 'alice@email.ro');

SELECT * FROM users;
SELECT * FROM users WHERE id = 1;
SELECT * FROM users WHERE id = 1 AND name = 'Alice';
SELECT email FROM users WHERE id = 1;
SELECT name, email FROM users WHERE id in (1, 2, 3);

ALTER TABLE users ADD COLUMN age INT;
ALTER TABLE users ADD COLUMN age INT DEFAULT 0;
ALTER TABLE users MODIFY COLUMN age INT DEFAULT 18;
ALTER TABLE users DROP COLUMN age;
ALTER TABLE users CHANGE COLUMN age user_age INT DEFAULT 18;
ALTER TABLE users RENAME COLUMN user_age TO age;

DROP TABLE IF EXISTS users;
DROP DATABASE IF EXISTS learning;