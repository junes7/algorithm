select id,length
from fish_info
where  1=1 and length is not null
order by length desc, id asc
limit 10;