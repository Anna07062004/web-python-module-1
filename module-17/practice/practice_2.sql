CREATE DATABASE Birds;

---------------------------------------

ALTER DATABASE Birds RENAME TO Cats;

------------------------------------------

DROP DATABASE Cats;

------------------------------------------

CREATE TABLE fruits_vegetables (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('овощ', 'фрукт')),
    color TEXT,
    calories INTEGER,
    description TEXT
);

INSERT INTO fruits_vegetables (name, type, color, calories, description)
VALUES
('Яблоко', 'фрукт', 'красный', 52, 'Сладкий и сочный фрукт.'),
('Апельсин', 'фрукт', 'оранжевый', 47, 'Сочный цитрусовый фрукт, источник витамина С.'),
('Огурец', 'овощ', 'зелёный', 16, 'Хрустящий овощ.'),
('Капуста', 'овощ', 'зелёный', 25, 'Листовой овощ, используется в свежем и квашеном виде.');

SELECT * FROM fruits_vegetables;

SELECT * FROM fruits_vegetables WHERE type = 'овощ';

SELECT * FROM fruits_vegetables WHERE type = 'фрукт';

SELECT name FROM fruits_vegetables;

SELECT DISTINCT color FROM fruits_vegetables;

SELECT * FROM fruits_vegetables
WHERE type = 'фрукт' AND color = 'красный';

SELECT * FROM fruits_vegetables
WHERE type = 'овощ' AND color = 'оранжевый';