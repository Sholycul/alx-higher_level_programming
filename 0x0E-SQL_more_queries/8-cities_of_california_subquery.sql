-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- The states table contains only one record where name = California (but with different id)


SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
