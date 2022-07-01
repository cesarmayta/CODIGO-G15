--funciones
DROP FUNCTION IF EXISTS fn_contar_cursos;
DELIMITER $$
CREATE FUNCTION fn_contar_cursos(alumnoId INT)
    RETURNS INT UNSIGNED
BEGIN
    DECLARE total INT UNSIGNED;

    select count(*) into total
    from tbl_matricula_curso mc
    inner join tbl_matricula m on mc.matricula_id = m.matricula_id 
    where m.alumno_id = alumnoId;

    RETURN total;
END
$$


DELIMITER ;

select fn_contar_cursos(1);

select alumno_nombre,fn_contar_cursos(alumno_id)
from tbl_alumno
