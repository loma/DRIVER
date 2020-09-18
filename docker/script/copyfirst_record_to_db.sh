#!/bin/sh

psql postgres postgres <<EOF
insert into auth_group (id,name) values (1,'Superadmin'),(2,'Public');
UPDATE auth_user SET email='test@gmail.com', first_name='driver', last_name='driver' WHERE username=(SELECT username FROM auth_user ORDER BY date_joined ASC LIMIT 1);
insert into driver_advanced_auth_groupdetail (name,description,group_id,is_admin) values ('Superadmin', 'superadmin', 1, True),('Public','public',2, False);
insert into driver_advanced_auth_userdetail ( password, username, first_name, last_name, email, is_active,date_joined,
                                              updated_on, user_id ,is_role_requested,is_staff,
                                              is_superuser , is_analyst , is_tech_analyst, google_user)
                                              select password, username, first_name, last_name, email,
                                              is_active,date_joined,last_login, id , False ,
                                              is_staff,is_superuser , False ,False, False from auth_user where id = (select auth_user.id from auth_user);
insert into authtoken_token (key,created,user_id) values ('36df3ade778ca4fcf66ba998506bdefa54fdff1c',now(),(select auth_user.id from auth_user));
insert into auth_user_groups (user_id , group_id) values ((select auth_user.id from auth_user),1);
insert into driver_advanced_auth_userdetail_groups (userdetail_id , group_id) values ((select driver_advanced_auth_userdetail.id from driver_advanced_auth_userdetail),1);
insert into driver_advanced_auth_countryinfo (country_code, country_name, archived, latitude, longitude) values ('ph', 'Philippines', True, 14.689881366618774, 121.02539062500001);
EOF
