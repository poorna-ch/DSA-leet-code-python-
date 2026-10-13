-- # Write your MySQL query statement below
-- select eu.unique_id,e.name
-- from Employees e
-- left join EmployeeUNI eu
-- on e.id =eu.id
select unique_id,name
from Employees 
left join EmployeeUNI
on Employees.id=EmployeeUNI.id