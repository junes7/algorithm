select count(*) as fish_count, fish_name
from fish_info as fi
left join fish_name_info as fni
on fi.fish_type=fni.fish_type
group by fni.fish_type
order by fish_count desc;