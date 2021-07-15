--drop table EMP;
--drop table DEPT;

create table DEPT (
	ID integer,
	NAME varchar(25), 
	constraint dept_pk primary key (ID)
	);

create table EMP (
	ID integer,
	LAST_NAME varchar(25),
	FIRST_NAME varchar(25),
	DEPT_ID integer,
	constraint emp_PK primary key (ID),
	constraint dept_FK foreign key (DEPT_ID) references DEPT(ID) on DELETE restrict on UPDATE restrict
	);

insert into DEPT (NAME) values ("Sistemas");
insert into EMP (LAST_NAME, FIRST_NAME, DEPT_ID) values ("Barrera", "Jhonatan", 1);
insert into EMP (LAST_NAME, FIRST_NAME, DEPT_ID) values ("Carvajal", "Maria", 1);
insert into EMP (LAST_NAME, FIRST_NAME, DEPT_ID) values ("Calderón", "Genny", 1);
insert into EMP (LAST_NAME, FIRST_NAME, DEPT_ID) values ("Moreno", "Cesar", 1);

insert into DEPT (NAME) values ("Contabilidad");
insert into EMP (LAST_NAME, FIRST_NAME, DEPT_ID) values ("Jaramillo", "Alejandra", 2);
insert into EMP (LAST_NAME, FIRST_NAME, DEPT_ID) values ("Guarin", "Eliana", 2);

select LAST_NAME , FIRST_NAME from EMP where DEPT_ID = 2;



