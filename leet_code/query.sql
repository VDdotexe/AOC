SELECT 
    (SELECT SUM(AA.NoOfResponse) FROM (SELECT client_email, COUNT(score) AS NoOfResponse, AVG(score) AS Avg_Score 
FROM
     net_promoter_scores
GROUP BY
     client_email, response_datetime
HAVING
     AVG(score) BETWEEN 9 AND 10 AND response_datetime > dateadd(mm,-6,getdate())) AA)
* 100/
(SELECT
     SUM(AA.NoOfResponse) FROM (SELECT client_email, COUNT(score) AS NoOfResponse, AVG(score) AS Avg_Score 
FROM
     net_promoter_scores
GROUP BY
     client_email, response_datetime
HAVING
     response_datetime > dateadd(mm,-6,getdate())) AA)
-
(SELECT
     SUM(AA.NoOfResponse) FROM (SELECT client_email, COUNT(score) AS NoOfResponse, AVG(score) AS Avg_Score 
FROM
     net_promoter_scores
GROUP BY
     client_email, response_datetime
HAVING
     AVG(score) BETWEEN 0 AND 6 AND response_datetime > dateadd(mm,-6,getdate())) AA)
* 100/
(SELECT
     SUM(AA.NoOfResponse) FROM (SELECT client_email, COUNT(score) AS NoOfResponse, AVG(score) AS Avg_Score 
FROM
     net_promoter_scores
GROUP BY
     client_email, response_datetime
HAVING
     response_datetime > dateadd(mm,-6,getdate())) AA) AS net_promoter_score



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


