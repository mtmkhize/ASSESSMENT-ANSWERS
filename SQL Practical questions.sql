Joining of data with the different types of joins
1.1 Write a query to return all clients and the respective departments that they work in:
vbnet
Copy code
SELECT client_info.client_id, client_info.client_name, client_info.client_gender, client_info.client_age, company.department
FROM client_info
JOIN company
ON client_info.client_id = company.client_id;
1.2 The type of join that would result in all the fields from the Client Info table and only the matching fields from the Company Table is an INNER JOIN.

sql
Copy code
SELECT client_info.*, company.department
FROM client_info
INNER JOIN company
ON client_info.client_id = company.client_id;
1.3.1 Write a query to return all employees with their manager:

vbnet
Copy code
SELECT employee_name, manager.employee_name AS manager
FROM employee
JOIN employee manager
ON employee.manager_id = manager.id;
1.3.2 To find the boss, we can modify the above query to only return employees who don't have a manager_id:

sql
Copy code
SELECT employee_name
FROM employee
WHERE manager_id IS NULL;
Apply the correct aggregate function to get certain answers: SUM, COUNT, AVERAGE
2.1 To calculate the sum of all negative values of S and all positive values of S:
vbnet
Copy code
WITH data (s) AS (
  SELECT S
  FROM (VALUES
    (2), (3), (-6), (-1), (7), (-10), (5)
  ) AS t (S)
)
SELECT 
  SUM(CASE WHEN s < 0 THEN s END) AS sum_of_negatives,
  SUM(CASE WHEN s >= 0 THEN s END) AS sum_of_positives
FROM data;
Query the dataset to identify the duplicate entries in the query output
3.1 To determine the 3rd oldest employee in the department:
sql
Copy code
WITH data AS (
  SELECT id, employee_name, department_id, manager_id, Age,
    ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY Age DESC) AS rn
  FROM employee
)
SELECT id, employee_name, department_id, manager_id, Age
FROM data
WHERE rn = 3;
Create two tables with the following fields and limit it to 5 rows per table
Table 1
sql
Copy code
CREATE TABLE car_info (
  Make varchar(50) NOT NULL,
  Model varchar(50) NOT NULL,
  Manufacture_Date date NOT NULL,
  Cost decimal(10, 2) NOT NULL,
  Model_id int PRIMARY KEY IDENTITY(1,1)
);

INSERT INTO car_info (Make, Model, Manufacture_Date, Cost)
VALUES 
  ('Toyota', 'Camry', '2022-01-01', 25000),
  ('Honda', 'Civic', '2022-02-01', 20000),
  ('Nissan', 'Altima', '2022-03-01', 22000),
  ('Ford', 'Mustang', '20



