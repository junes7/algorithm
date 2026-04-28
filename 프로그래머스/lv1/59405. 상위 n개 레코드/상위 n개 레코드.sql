-- 코드를 입력하세요
select name
from animal_ins
where datetime in(select min(datetime)
                  from animal_ins);