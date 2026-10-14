# Write your MySQL query statement below
select product_name,year,price
From sales
left join
product
on sales.product_id=product.product_id
