
DELIMITER $$
DROP PROCEDURE IF EXISTS sp_matricular_alumno$$
CREATE PROCEDURE sp_matricular_alumno(IN alu_id INT,IN niv_id INT,IN  mod_id INT)
BEGIN
    --variables
    DECLARE matriculaId INT;
    DECLARE cursoId INT;
    DECLARE totalCursos INT;
    set matriculaId = 0;
    set cursoId = 1;
    set totalCursos = 0;

    --insertamos datos
    insert into tbl_matricula(alumno_id,nivel_id,modulo_id)
    values (alu_id,niv_id,mod_id);

    select max(matricula_id) into matriculaId from tbl_matricula;

    select count(*) into totalCursos from tbl_curso;

    WHILE cursoId <= totalCursos DO 
        insert into tbl_matricula_curso(matricula_id,curso_id)
        values (matriculaId,cursoId);

        SET cursoId = cursoId + 1;
    END WHILE;
END
$$

DELIMITER ;
CALL sp_matricular_alumno(1,1,1);

select * from tbl_matricula;
select * from tbl_matricula_curso;
