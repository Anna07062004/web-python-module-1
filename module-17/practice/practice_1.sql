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

----------------------------------------------------------

create table employee_profiles (
	id SERIAL primary key,
	employee_id INT unique references employees (id),
	phone TEXT unique,
	address TEXT,
	birth_data DATE
);

insert into employee_profiles(employee_id, phone, address, birth_data)
values 
	(1, '+70000000000', 'address-1', '1980-05-25'),
	(2, '+70000000001', 'address-2', '1981-05-25'),
	(3, '+70000000002', 'address-3', '1982-05-25');

select 
	e.name as employee_name,
	ep.phone,
	ep.address,
	ep.birth_data
from employees e
join employee_profiles ep on ep.employee_id = e.id;

insert into employee_profiles(employee_id, phone, address, birth_data)
values
	(1, '+70000000003', 'address-4', '1985-05-25');

----------------------------------------------------------------------------

-- N - N
create table skills(
	id SERIAL primary key,
	name TEXT not null unique 
);

create table employee_skills(
	employee_id INT references employees(id),
	skill_id int references skills(id),
	primary key (employee_id, skill_id)
);

insert into skills(name)
values 
	('SQL'),
	('PostgreSQL'),
	('MySQL'),
	('Excel');

insert into employee_skills(employee_id, skill_id)
values 
	(1,1),
	(2,1),
	(3,1),
	(1,2),
	(2,2),
	(3,2),
	(1,4);

select 
	e.name as employee_name,
	s.name as skill_name
from employee_skills es
join employees e on es.employee_id = e.id
join skills s on es.skill_id = s.id 
order by e.name, s.name;

---------------------------------------------------------------

select 
	e.name as employee_name,
	e.salary,
	d.name as department_name,
	ep.phone,
	ep.address,
	p.name as project_name,
	s.name as skill_name
from employees e
left join departments d on e.id = d.id
left join employee_profiles ep on e.id = ep.id
left join projects p on e.id = p.id
left join employee_skills es on es.employee_id = e.id
left join skills s on es.skill_id = s.id
order by e.name, p.name, s.name

----------------------------------------------------------------

select 
	e.name as employee_name,
	coalesce(sum(p.budget), 0) as total_budget
from employees e
left join projects p on e.id = p.id
group by e.id, e.name
order by total_budget desc, e.name;

----------------------------------------------------------------

select 
	p.name as project_name,
	p.budget,
	e.name as employee_name,
	d.name as department_name
from projects p
join employees e  on p.employee_id = e.id
join departments d on e.department_id = d.id
where is_active = true 
	and p.budget > 200000
order by p.budget desc;

-----------------------------------------------------------------

