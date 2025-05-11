-- Create the database
CREATE DATABASE IF NOT EXISTS LateComersDB;
USE LateComersDB;

-- Table: PTEs (Physical Training Educators)
CREATE TABLE IF NOT EXISTS ptes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Table: SchoolRecords (Students)
CREATE TABLE IF NOT EXISTS SchoolRecords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    admission_no VARCHAR(20) UNIQUE NOT NULL,
    student_name VARCHAR(100) NOT NULL,
    parent_email VARCHAR(100) NOT NULL
);

-- Table: LateRecords (Late Entries)
CREATE TABLE IF NOT EXISTS LateRecords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    admission_no VARCHAR(20) NOT NULL,
    date DATE NOT NULL,
    reason TEXT,
    FOREIGN KEY (admission_no) REFERENCES SchoolRecords(admission_no) ON DELETE CASCADE
);
