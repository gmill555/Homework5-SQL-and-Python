create database if not exists db_registra;
use db_registra;

create table if not exists tbl_student (
    st_ID int auto_increment primary key,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    birth_date date not null,
    email varchar(100) not null
);

select * from tbl_student;
