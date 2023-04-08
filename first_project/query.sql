-- user_id=1

select p.id as post_id,u.id as user_id from 
socialnetwork_post as p join
socialnetwork_post_like as pl on p.id=pl.post_id
join accounts_userprofile as u on pl.userprofile_id=u.id where user_id=1;