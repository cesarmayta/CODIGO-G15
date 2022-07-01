--registro de factura_cabecera
DELIMITER $$
--DROP PROCEDURE IF EXISTS sp_registrar_factura$$
CREATE PROCEDURE sp_registrar_factura(IN nrofactura VARCHAR(20),IN fechaemision DATE,IN moneda VARCHAR(20),IN valorventa DOUBLE,IN emisorId INT,IN clienteId INT)
BEGIN
    DECLARE facturaId INT;
    DECLARE impuestoId INT;
    DECLARE totalImpuestos INT;
    DECLARE facturaImpuestoMonto DOUBLE;

    set facturaId = 0;
    set impuestoId = 1;
    set totalImpuestos = 0;
    set facturaImpuestoMonto = 0.0;

    --INSERTARMOS LA FACTURA    
    insert into tbl_factura(factura_nro,factura_fecha_emision,factura_tipo_moneda,factura_valor_venta,
    factura_importe_total,emisor_id,cliente_id)
    values(nrofactura,fechaemision,moneda,valorventa,0,emisorId,clienteId);
    --obtenemos el ultimo id registrado
    set facturaId = LAST_INSERT_ID();

    select count(*) into totalImpuestos from tbl_impuesto;
    --insertar los impuestos
    WHILE impuestoId <= totalImpuestos DO 
        select (impuesto_porcentaje / 100) * valorventa into facturaImpuestoMonto
        from tbl_impuesto where impuesto_id = impuestoId;

        insert into tbl_factura_impuesto(facimp_monto,factura_id,impuesto_id)
        values(facturaImpuestoMonto,facturaId,impuestoId);

        SET impuestoId = impuestoId + 1;
    END WHILE;
    --ACTUALIZAMOS EL MONTO TOTAL  
    update tbl_factura 
    set factura_importe_total = (select sum(facimp_monto) from tbl_factura_impuesto where factura_id = facturaId) + factura_valor_venta
    where factura_id = facturaId;
END
$$

DELIMITER ;

CALL sp_registrar_factura('E001-1213','2022-06-30','SOLES',100,1,2);

select * from tbl_factura;
select * from tbl_factura_impuesto where factura_id = 2;
