SELECT PT_NAME, PT_NO, GEND_CD, AGE, ifnull(TLNO, 'NONE') 
from PATIENT
where GEND_CD = 'W' and age <= 12  
order by age desc, PT_NAME asc ;
