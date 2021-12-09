create database kalkulator;
use kalkulator;

create table Input(
id int auto_increment primary key,
navn varchar(30) not null,
resultat int not null,
dato varchar(30));

select * from Input;