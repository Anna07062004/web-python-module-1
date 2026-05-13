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