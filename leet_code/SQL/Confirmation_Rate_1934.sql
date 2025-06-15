-- Write your MySQL query statement below
-- this code still has issues with the test cases- RESOLVE iT!!!
with rt1 as (select
    s.user_id,
    sum( case when c.action = 'confirmed' then 1 else 0 end ) as "confirmed",
    sum( case when c.action = 'timeout' then 1 else 0 end ) as "timeout"
from
    confirmations as c
    right join
    signups as s
    on c.user_id = s.user_id
group by
    c.user_id)

select 
    rt1.user_id,
    coalesce((rt1.confirmed) / (rt1.confirmed + rt1.timeout),0) as confirmation_rate
from
    rt1;