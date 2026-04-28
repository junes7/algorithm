-- 코드를 입력하세요
select animal_type, ifnull(name, "No name") name, sex_upon_intake
from animal_ins
order by animal_id;