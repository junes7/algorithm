select CAR_TYPE, count(*) as CARS
from car_rental_company_car
where options regexp '통풍시트|열선시트|가죽시트'
group by CAR_TYPE
order by CAR_TYPE;