Use mouli;
show tables;

select * from covid_19_cases;

SELECT age_group,
       SUM(CASE WHEN current_status = 'Laboratory-confirmed case' THEN 1 ELSE 0 END) AS confirmed_cases,
       SUM(CASE WHEN current_status = 'Probable Case' THEN 1 ELSE 0 END) AS probable_cases
FROM covid_19_cases
GROUP BY age_group;

SELECT sex,
       SUM(CASE WHEN current_status = 'Laboratory-confirmed case' THEN 1 ELSE 0 END) AS confirmed_cases,
       SUM(CASE WHEN current_status = 'Probable Case' THEN 1 ELSE 0 END) AS probable_cases
FROM covid_19_cases
GROUP BY sex;

SELECT race,
       SUM(CASE WHEN current_status = 'Laboratory-confirmed case' THEN 1 ELSE 0 END) AS confirmed_cases,
       SUM(CASE WHEN current_status = 'Probable Case' THEN 1 ELSE 0 END) AS probable_cases
FROM covid_19_cases
GROUP BY race;

SELECT ethnicity,
       SUM(CASE WHEN current_status = 'Laboratory-confirmed case' THEN 1 ELSE 0 END) AS confirmed_cases,
       SUM(CASE WHEN current_status = 'Probable Case' THEN 1 ELSE 0 END) AS probable_cases
FROM covid_19_cases
GROUP BY ethnicity;
