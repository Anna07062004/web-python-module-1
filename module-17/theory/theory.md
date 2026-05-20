# База данных

### `CREATE`

Создает объект: Таблица, база, индекс
```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    salary NUMERIC
)
```

### `TABLE`

Указывает, что создается или изменяется таблица
```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT
)
```
### `ALTER`

Изменяет существующий объект

```sql
ALTER TABLE employees
ADD COLUMN email TEXT
```
### `ADD`

Добовляет колонку ограничения

```sql
ALTER TABLE employees
ADD COLUMN phone TEXT
```

### `DROP`

Удаляет объект (таблицу)

```sql
DROP TABLE projects;
```

### `IF EXISTS`

Позволяет избежать ошибки, если объекта нет

```sql
DROP TABLE IF EXISTS old_projects;
```

### `IF NOT EXISTS`

Создает объект только если он не существует

```sql
CREATE TABLE IF NOT EXISTS departaments(
id SERIAL PRImARY KEY,
name TEXT
)
```

### `RENAME`

Переминовывает объекты

```sql
ALTER TABLE emloyees
RENAME COLUMN name to full_name;
```

### `TRUNCATE`

Быстро очищает таблицу

```sql
TRUNCATE TABLE projects;
```

## 2. Работа с данными
### `SELECT`

Выберает данные
```sql
SELECT name, salary FROM employees;
```

### `FROM`
```sql
SELECT name, salary FROM employees,
```

### `INSERT`
Добавляет строки
```sql
INSERT INTO  employees (name, salary, demaptent_id)
VALUES ('Anna', 12000, 1);
```

### `VALUES`
Передает конкретные значения

```sql
INSERT INTO projekt(name, employees_id, budget)
VALUES ('CRM SYSTEM', 1, 5000000)
```

## 9. Типы данных

### `INT / INTEGER`
Хранит целые числа без дробной части

```sql
CREATE TABLE employees(
    id INT,
    name TEXT,
    age INT
)
```

### `SMALLINT`
Хранит небольшие целые числа
```sql
CREATE TABLE products(
    id INT,
    name TEXT,
    rating SMALLINT
)
```
### `BIGINT`
Хранит очень большие числа
```sql
CREATE TABLE videos(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    videos BIGINT DEFAULT 0
)
```

### `SERIAL`
Создает фвтоматически увеличивающийся числовой id
```sql
CREATE TABLE departments(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
)
```

### `GENERATED`
Генерирует значение средствами базы данных
```sql
CREATE TABLE departments(
    id INT GENERATED  ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
)
```

### `ALWAYS`
вСЕГДА ГЕНЕРИРУЕТ ЗНАЧЕНИЯ ФВТОМАТИЧЕСКИ
```sql
CREATE TABLE departments(
    id INT GENERATED  ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
)
```

### `TEXT`
Хранит текст без огранечений
```sql
CREATE TABLE departments(
    id INT GENERATED  ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    bio  TEXT
)
```

### `VARCHAR`
Хранит текст с ограниченной длинной
```sql
CREATE TABLE user(
    id INT GENERATED  ALWAYS AS IDENTITY PRIMARY KEY,
    email VARCHAR(255),
    username VARCHAR(50)
)
```

### `CHAR`
Хранит строку фиксированной длины
```sql
CREATE TABLE departments(
    id INT GENERATED  ALWAYS AS IDENTITY PRIMARY KEY,
    code VARCHAR(255),
    name TEXT NOT NULL
)
```

### `NUMERIC`
Хранит точные числовые  значения
```sql
CREATE TABLE products(
    id INT GENERATED  ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    salary NUMERIC(10, 2)
)
```

### `DECIMAL`
Хранит точные дробные числа
```sql
CREATE TABLE products(
    id INT GENERATED  ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL
    price DECIMAL(10, 2)
)
```
### `BOOLEAN`
хранит логическое значение true or falce
```sql
CREATE TABLE users(
    id INT GENERATED  ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    is_active BOOLEAN DEFI
)
```

### `ENUM`
ограничивает значение заданным набором
```sql
CREATE TYPE order_status AS ENUM ('new', 'paid', 'shipped', 'cancelled')
CREATE TABLE orders(
    id INT GENERATED  ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    status_order order_status DECIMAL 'new'
)
```

### `NULL`
обозначаеьт отсутствие значения
```sql
CREATE TABLE users(
    id INT GENERATED  ALWAYS AS IDENTITY PRIMARY KEY,
    first_name TEXT NOT NULL,
    middle_name TEXT
)
```

## 10. Условные выражения

### `CASE`
Условная логика внутри SQL
```sql
SELECT name,
     salary,
    CASE
        WHEN salary >= 15000 Then 'high'
        WHEN salary >= 80000 Then 'medium'
        ELSE 'low'
    END AS salary_level
FROM employees;   
```

### `WHEN`
сщздает условие внутри case
```sql

    CASE
        WHEN salary >= 15000 Then 'high'
        WHEN salary >= 80000 Then 'medium'
        ELSE 'low'
    END AS salary_level  
```


### `THEN`
сщздает условие внутри case
```sql
    CASE
        WHEN salary >= 15000 Then 'high'
        WHEN salary >= 80000 Then 'medium'
        ELSE 'low'
    END AS salary_level  
```


### `ELSE`
задает результат, если ни одно условие when не подошлр
```sql
    CASE
        WHEN salary >= 15000 Then 'high'
        WHEN salary >= 80000 Then 'medium'
        ELSE 'low'
    END AS salary_level
```


### `СOALESCE`
возвращает 1 значение которое не является null
```sql
    SELECT 
        name,
        COAALESCE(salary, 0) as salary
    FROM employees;   
```