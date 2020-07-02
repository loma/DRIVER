#!/bin/sh

psql postgres postgres <<EOF
insert into auth_group (name) values ('Superadmin');
insert into auth_group (name) values ('Public');
insert into driver_advanced_auth_groupdetail (name,description,group_id,is_admin) values ('Superadmin','superadmin',1 , True);
insert into driver_advanced_auth_groupdetail (name,description,group_id , is_admin) values ('Public','public',2 , False);
insert into driver_advanced_auth_userdetail ( password, username, first_name, last_name, email, is_active,date_joined,updated_on, user_id ,is_role_requested,is_staff,is_superuser , is_analyst , is_tech_analyst) select password, username, first_name, last_name, email,is_active,date_joined,last_login, id , 0 , is_staff,is_superuser , False ,False from auth_user where id = 1 ;
insert into authtoken_token (key,created,user_id) values ('36df3ade778ca4fcf66ba998506bdefa54fdff1c',now(),1);
insert into auth_user_groups (user_id , group_id) values (1,1);
insert into driver_advanced_auth_userdetail_groups (userdetail_id , group_id) values (1,1);
EOF
