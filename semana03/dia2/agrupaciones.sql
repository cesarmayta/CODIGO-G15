--FUNCIONES DE AGRUPACIÓN
select count(*) from alumno;
select sum(nota) / count(*) from alumno;
select avg(nota),min(nota),max(nota) from alumno;
select min(pais),max(pais),avg(pais) from alumno;
select max(id) from alumno;
--GROUP BY
select pais,count(*) as cantidad from alumno
GROUP BY pais
order by count(*) desc;
--CREAR CONSULTA SQL QUE RETORNE LA NOTA PROMEDIO,MINIMA Y MAXIMA POR PAIS ORDANDO POR PROMEDIO MAS ALTO POR PAIS
select pais,avg(nota) as promedio,min(nota) as minimo,max(nota) as maximo
FROM alumno
where nota > 10
GROUP BY pais
HAVING avg(nota) < 15
order by avg(nota) desc;
--
select pais,avg(nota) as promedio
from alumno where nota > 10
GROUP BY pais