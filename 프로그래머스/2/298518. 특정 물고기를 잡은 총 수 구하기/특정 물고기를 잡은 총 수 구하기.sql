select count(*) as FISH_COUNT
from FISH_INFO as fi
left join FISH_NAME_INFO as fni
on fi.fish_type = fni.fish_type
where fni.fish_name in ('BASS','SNAPPER');