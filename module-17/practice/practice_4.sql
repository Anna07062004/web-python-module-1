--часть 3

CREATE TABLE Faculties (
    faculty_id SERIAL PRIMARY KEY,
    faculty_name TEXT NOT NULL UNIQUE,
    dean_name TEXT
);

CREATE TABLE Departments (
    department_id SERIAL PRIMARY KEY,
    department_name TEXT NOT NULL,
    faculty_id INTEGER NOT NULL REFERENCES Faculties(faculty_id) ON DELETE CASCADE,
    headofdepartment TEXT,
    UNIQUE(department_name, faculty_id)
);

CREATE TABLE Groups (
    group_id SERIAL PRIMARY KEY,
    group_name TEXT NOT NULL UNIQUE,
    faculty_id INTEGER NOT NULL REFERENCES Faculties(faculty_id) ON DELETE CASCADE,
    year_of_study INTEGER CHECK (year_of_study BETWEEN 1 AND 6)
);

CREATE TABLE Teachers (
    teacher_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT,
    salary DECIMAL(12, 2) CHECK (salary >= 0),
    hire_date DATE NOT NULL,
    department_id INTEGER REFERENCES Departments(department_id) ON DELETE SET NULL,
    email TEXT,
    phone TEXT
);

INSERT INTO Faculties (faculty_name, dean_name) VALUES
('факультет информационных технологий (бакалавриат)', 'Иванов А.В.'),
('факультет экономики (бакалавриат)', 'Петрова М.Л.');

INSERT INTO Departments (department_name, faculty_id, headofdepartment) VALUES
('кафедра программирования (основная)', 1, 'Смирнов В.П.'),
('кафедра анализа данных (базовая)', 1, 'Кузнецова Е.А.'),
('кафедра финансов (аналитический блок)', 2, 'Орлов Д.М.');

INSERT INTO Groups (group_name, faculty_id, year_of_study) VALUES
('ИТ-101А', 1, 1),
('ИТ-201А', 1, 2),
('ЭК-301А', 2, 3);

INSERT INTO Teachers (first_name, last_name, salary, hire_date, department_id, email, phone) VALUES
('Иван', 'Петров', 75000.00, '2020-03-15', 1, 'i.petrov@academy.ru', '+7-999-123-45-67'),
('Мария', 'Сидорова', 82000.00, '2019-07-22', 2, 'm.sidorova@academy.ru', '+7-999-234-56-78'),
('Samantha', 'Adams', 68000.00, '2021-01-10', 3, 'a.kozlov@academy.ru', '+7-999-345-67-89');

SELECT department_name, faculty_id, department_id
FROM Departments;

SELECT group_name AS "Groups.Name"
FROM Groups;

SELECT
last_name,
salary,
'No premium column' AS note
FROM Teachers;

SELECT 'The dean of faculty ' || faculty_name || ' is ' || dean_name || '.' AS faculty_info
FROM Faculties;

SELECT last_name
FROM Teachers
WHERE salary > 75000;

SELECT department_name
FROM Departments
WHERE department_id < 2 OR department_id > 3;

SELECT faculty_name
FROM Faculties
WHERE faculty_name != 'факультет информационных технологий (бакалавриат)';

SELECT first_name, last_name, hire_date
FROM Teachers;

SELECT first_name, last_name, salary
FROM Teachers;

SELECT last_name, salary
FROM Teachers;

SELECT last_name, hire_date
FROM Teachers
WHERE hire_date < '2020-01-01';

SELECT department_name AS "Name of Department"
FROM Departments
WHERE department_name < 'Кафедра финансов(аналитический блок)'
ORDER BY department_name;

SELECT last_name
FROM Teachers
WHERE salary <= 70000;

SELECT group_name
FROM Groups
WHERE year_of_study BETWEEN 1 AND 2;

SELECT last_name
FROM Teachers
WHERE salary < 70000;