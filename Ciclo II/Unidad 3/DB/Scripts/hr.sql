-- SELECT
SELECT last_name "Apellidos", salary "Salario", salary + 200 "Proyección Aumento"
FROM employees;

SELECT last_name "Apellidos", salary as Salario, salary + 200 "Proyección Aumento"
FROM employees
WHERE Salario < 4000;

SELECT first_name||" "||last_name "Apellidos", salary as Salario, salary + 200 "Proyección Aumento"
FROM employees
WHERE Salario < 4000;

SELECT DISTINCT department_id 
FROM employees;

-- Ejercicios
SELECT employee_id, last_name, job_id, hire_date "STARTDATE"
FROM employees;

SELECT DISTINCT job_id
FROM employees;

SELECT employee_id "Emp #", last_name "Employee", job_id "Job", hire_date "HIRE DATE"
FROM employees;

SELECT employee_id "Emp #", last_name "Employee", job_id "Job", hire_date "HIRE DATE"
FROM employees
WHERE job_id NOT IN (9 ,13 ,17);

SELECT last_name, salary
FROM employees
WHERE salary > 12000;

SELECT last_name, department_id
FROM employees
WHERE employee_id = 176;

SELECT last_name, salary
FROM employees
WHERE salary NOT BETWEEN 5000 AND 12000
ORDER BY salary DESC;

SELECT last_name, department_id AS dept
FROM employees e 
WHERE dept = 8 OR dept = 10;

SELECT last_name, job_id, hire_date
FROM employees e
WHERE last_name = 'Taylor' OR last_name = 'Matos'
ORDER BY hire_date;

SELECT last_name 'Employee', salary 'Monthly Salary'
FROM employees
WHERE salary BETWEEN 5000 AND 12000 AND (department_id = 8 OR department_id = 10);

SELECT last_name, hire_date
FROM employees e 
WHERE hire_date LIKE '1994%';

SELECT last_name, job_id
FROM employees e 
WHERE manager_id IS NULL;

SELECT last_name, salary
FROM employees e 
WHERE job_id = 16
ORDER BY 2 DESC;

SELECT first_name, last_name
FROM employees e 
WHERE first_name LIKE '__a%';

SELECT last_name
FROM employees e 
WHERE last_name LIKE '%a%' AND last_name LIKE '%e%';

SELECT employee_id, last_name, salary, ceil(salary * 0.155) 'Increase'
FROM employees e;

SELECT
	employee_id,
	last_name,
	salary,
	ceil(salary * 0.155) AS 'Increase',
	'Increase' + salary 'New Salary'
FROM employees e;

SELECT
	upper(substr(last_name,1,1))||lower(substr(last_name,2,LENGTH(last_name))) Apellidos,
	length(last_name) Longitud
FROM employees e 
WHERE first_name LIKE 'J%' OR first_name LIKE 'M%' OR first_name LIKE 'A';

SELECT 
	substr(last_name,1,8),
	salary,
	substr('***********************',1,round(salary/1000))
FROM employees e;

SELECT AVG(salary), MIN(salary), max(salary), SUM(salary) 
from employees e;

SELECT AVG(salary), MIN(salary), max(salary), SUM(salary) 
from employees e
WHERE job_id = 13;

SELECT job_id, AVG(salary), MIN(salary), max(salary), SUM(salary) total
from employees e
group by job_id
ORDER by total desc;

SELECT count(phone_number)
from employees e ;

SELECT department_id, job_id, count(last_name)
from employees e
group by department_id, job_id ;

SELECT department_id, MAX(salary)
from employees
group by department_id
HAVING MAX(salary) > 10000;

SELECT round(AVG(salary)) Promedio, MIN(salary) Minimo, max(salary) Maximo, SUM(salary) Total 
from employees e;

SELECT job_id, round(AVG(salary)) Promedio, MIN(salary) Minimo, max(salary) Maximo, SUM(salary) Total 
from employees e
group by job_id;

SELECT job_id, COUNT(job_id)
from employees e 
group by job_id ;

SELECT COUNT(job_id) 'Number of Managers.'
from employees e 
where job_id IN (2,7,10,14,15,19);

SELECT MAX(salary) - MIN(salary) 'DIFFERENCE'
from employees e ;

-- Como consultar para otros departamentos y obtener su total
SELECT job_id, SUM(salary) Dept3
from employees e 
group by job_id 
HAVING department_id IN (10,3,8);

SELECT department_name, city
from departments d 
natural join locations l;

SELECT department_name, city
from departments d, locations l 
WHERE d.location_id = l.location_id;

SELECT department_name, city
from departments join locations
using (location_id);

SELECT department_name, city
from departments d join locations l 
on (d.location_id = l.location_id);

SELECT e.last_name, e.department_id, d.department_name
from employees e 
left outer join departments d on (e.department_id = d.department_id);

-- rigth no se soporta en sqlite, simulado
SELECT e.last_name, e.department_id, d.department_name
from departments d
left outer join employees e on (e.department_id = d.department_id);

SELECT last_name, department_name
from employees e 
cross join departments d;

SELECT location_id, street_address, city, state_province, country_name
from locations l 
natural join countries c ;

SELECT last_name, department_id, department_name
from employees e 
natural join departments d ;

SELECT e.last_name, e.department_id, d.department_name
from employees e 
left outer join departments d on (e.department_id = d.department_id);

SELECT e.last_name, e.job_id, e.department_id, d.department_name
from employees e 
left outer join departments d on (e.department_id = d.department_id);

SELECT e.last_name, e.job_id, e.department_id, d.department_name
from employees e
join departments d on (e.department_id = d.department_id)
NATURAL JOIN locations l 
WHERE l.city = 'Toronto';

SELECT last_name, employee_id
from employees e2 
WHERE manager_id IN (
	SELECT employee_id
		from employees e 
		where job_id IN (2,7,10,14,15,19)
);

SELECT department_id, first_name, last_name, salary
from employees e 
WHERE salary >= (
	SELECT max(salary) 
	from employees e2
	group by department_id
);

SELECT round(salary_avg, 2)
from (
	SELECT AVG(salary) salary_avg
	from employees e 
	group by department_id
);

SELECT employee_id, manager_id, department_id
from employees e 
WHERE (manager_id, department_id) IN (
	SELECT manager_id, department_id
	from employees e 
	WHERE first_name = 'John'
	)
AND first_name <> 'John';

SELECT department_name
from departments d 
where (
	SELECT 1
	FROM employees e 
	WHERE salary > 10000
	and d.department_id = e.department_id 
);

SELECT last_name
from
employees e 
where department_id in (
	SELECT department_id
	from departments d
	WHERE location_id in (
		SELECT location_id
		from locations l 
		WHERE country_id = (
			SELECT country_id
			from countries c 
			WHERE country_name = 'United Kingdom'
		)
	));

with
uk as (
	SELECT country_id
	from countries c 
	WHERE country_name = 'United Kingdom'
),
lUK as (
	SELECT location_id
	from locations l 
	WHERE l.country_id in uk
)
,
depsUK as (
	SELECT department_id
	from departments d 
	WHERE location_id in lUK
)

SELECT last_name
from
employees e 
where department_id in depsUK;

SELECT department_id , last_name
from employees e 
union
SELECT department_id, department_name
from departments d;

-- INSERT
INSERT INTO departments (department_id, department_name, location_id)
values (12, 'Public Relations', 1700);

INSERT into departments (department_name, location_id)
values ('New Department', 1800);

INSERT INTO departments 
values (14, 'Other new department', 1500);

CREATE TABLE sales_reps (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT(60),
	salary REAL NOT NULL
);

INSERT into sales_reps (id, name, salary)
	select employee_id, first_name||' '||last_name, salary
	from employees 
	WHERE  job_id IN (
		SELECT job_id
		from jobs 
		WHERE job_title LIKE '%REP%'
	);
	
UPDATE employees 
set salary = 4800
WHERE employee_id = 107;

UPDATE employees 
set salary = salary + 200
where job_id = 9;

DELETE from sales_reps
WHERE salary < 7000;

CREATE TABLE my_employee (
	id NUMBER(4) NOT NULL,
	last_name VARCHAR2(25),
	first_name VARCHAR2(25),
	userid VARCHAR2(8),
	salary NUMBER(9,2)
);

INSERT into my_employee 
values (1, 'Patel', 'Ralph', 'rpatel', 895);

INSERT into my_employee (id, last_name, first_name, userid, salary)
values (2, 'Dancs', 'Betty', 'bdancs', 860);