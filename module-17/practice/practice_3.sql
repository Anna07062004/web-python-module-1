--Задание 1
SELECT *
FROM fruits_vegetables
WHERE type = 'овощ' AND calories < 50;

SELECT *
FROM fruits_vegetables
WHERE type = 'фрукт' AND calories BETWEEN 30 AND 90;

SELECT *
FROM fruits_vegetables
WHERE type = 'овощ' AND name ILIKE '%капуста%';

SELECT *
FROM fruits_vegetables
WHERE description ILIKE '%гемоглобин%';

SELECT *
FROM fruits_vegetables
WHERE color IN ('жёлтый', 'красный');

--Задание 2
SELECT COUNT(*) as vegetable_count
FROM fruits_vegetables
WHERE type = 'овощ';

SELECT COUNT(*) as fruit_count
FROM fruits_vegetables
WHERE type = 'фрукт';

SELECT COUNT(*) as countbycolor
FROM fruits_vegetables
WHERE color = 'красный';

SELECT color, COUNT(*) as count
FROM fruits_vegetables
GROUP BY color;

select COUNT(*) as vegetable_count
from fruits_vegetables
where type = 'овощ';

select COUNT(*) as fruit_count
from fruits_vegetables
where type = 'фрукт';

select COUNT(*) as countbycolor
from fruits_vegetables
where color = 'красный';

select color, COUNT(*) as count
from fruits_vegetables
group by color
order by count desc;

select color, COUNT(*) as min_count
from fruits_vegetables
group by color
order by min_count ASC
limit 1;

select color, COUNT(*) as max_count
from fruits_vegetables
group by color
order by max_count DESC
limit 1;

select MIN(calories) as min_calories
from fruits_vegetables;

select MAX(calories) as max_calories
from fruits_vegetables;

select ROUND(AVG(calories),2) as avg_calories
from fruits_vegetables;

select *
from fruits_vegetables
where type = 'фрукт'
order by calories asc
limit 1;

select *
from fruits_vegetables
where type = 'фрукт'
order by calories DESC
limit 1;