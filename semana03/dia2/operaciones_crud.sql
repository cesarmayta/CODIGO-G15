--operaciones CRUD(CREATE,READ,UPDATE,DELETE)
--READ => SELECT
select * from alumno;
select nombre,pais from alumno;
select distinct pais from alumno;
select * from alumno WHERE pais = 'Perú';

select * from alumno WHERE id = 7;
--CREATE => INSERT
insert into alumno(nombre,email,pais) values('Luis Garcia','luis@gmail.com','Chile');

ALTER TABLE alumno ADD column NOTA INT NOT NULL DEFAULT 0;
insert into alumno(nombre,email,pais,nota) values('Jose Rodriguez','joserod@hotmail.com','Bolivia',15);

insert into alumno(nombre) values ('Carlos Perez'),('Fabiola Rivera'),('Olga Huaman');

--UPDATE
update alumno set nota = 11 where id = 1;
update alumno
set email = CONCAT(lower(replace(nombre,' ','.')),'@codigo.edu.pe')
--select nombre,email,CONCAT(lower(replace(nombre,' ','.')),'@codigo.edu.pe')
--from alumno
where email IS NULL;

--DELETE
delete from alumno where id = 5;
insert into alumno(id,nombre,email) values(5,'Oscar Morales','oscarmorales@gmail.com');
truncate table alumno