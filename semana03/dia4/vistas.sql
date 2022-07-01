--vistas
CREATE VIEW vw_matricula_alumno as
select
a.alumno_nombre as alumno,
n.nivel_nombre as nivel,
m.modulo_nombre as modulo
from tbl_matricula mat
inner join tbl_alumno a on mat.alumno_id = a.alumno_id
inner join tbl_nivel n on mat.nivel_id = n.nivel_id
inner join tbl_modulo m on mat.modulo_id = m.modulo_id;

select * from vw_matricula_alumno;