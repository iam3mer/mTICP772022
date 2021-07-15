-- employees
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