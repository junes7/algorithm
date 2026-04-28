-- 코드를 입력하세요
select animal_id, name
from animal_ins
where animal_type='Dog' and 
name like '%el%'
order by 2;