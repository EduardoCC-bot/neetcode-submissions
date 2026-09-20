-- Write your query below
WITH orange AS (
    SELECT 
        sale_date,
        fruit, 
        sold_num
    FROM sales
    WHERE fruit = 'oranges'
), 
apples AS (
    SELECT 
        sale_date,
        fruit, 
        sold_num
    FROM sales
    WHERE fruit = 'apples'
)
SELECT
    o.sale_date,
    (a.sold_num - o.sold_num) AS diff
FROM orange o
INNER JOIN apples a
on o.sale_date = a.sale_date
ORDER BY o.sale_date
