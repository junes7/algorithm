select count(*) as FISH_COUNT, FISH_NAME
from FISH_INFO as fi
left join FISH_NAME_INFO as fni
on fi.FISH_TYPE=fni.FISH_TYPE
group by fni.FISH_TYPE
order by FISH_COUNT desc;