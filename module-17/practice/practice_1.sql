select
	name,
	salary,
	case 
		when salary >= 150000 then 'high'
		when salary >= 100000 then 'middle'
		else 'low'
	end as salary_level
from employees;
	
----------------------------------------------

select 
	e.name as employee_name, 
	coalesce(d.name, 'Без отдела') as department_name
from employees e 
left join departments d on e.department_id  = d.id;

------------------------------------------------------

select 
	d.id,
	d.name
from departments d 
where exists (
	select 1 from employees e 
	where e.department_id = d.id
)

-------------------------------------------------------

select
	e.id,
	e.name
from employees e
where exists(
	select 1 from projects p
	where p.employee_id = e.id);

-----------------------------------------------------

select 
	name as project_name,
	budget,
	case 
		when is_active = true then 'active'
		else 'close'
	end as projects_status
from projects;

-----------------------------------------------------

select 
	e.name as employee_name,
	count(p.id) as projects_count
from employees e 
left join projects p on p.employee_id = e.id
group by e.id, e.name 
order by projects_count desc;

----------------------------------------------------

UPDATE projects
SET budget = budget + 50000
where is_active = true
returning id,name,employee_id, budget,is_active;

----------------------------------------------------

delete from projects  
where is_active = false 
returning id, name;
