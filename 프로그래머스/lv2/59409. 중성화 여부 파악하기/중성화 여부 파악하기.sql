-- 코드를 입력하세요
select animal_id, name,
case when sex_upon_intake like 'intact%' then 'X' else 'O' end 중성화
from animal_ins
order by 1;