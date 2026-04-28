-- 코드를 입력하세요
select animal_type, count(*) count
from animal_ins
group by animal_type
order by 1