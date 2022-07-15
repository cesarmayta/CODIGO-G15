INSERT INTO `tbl_categoria` (`categoria_id`, `categoria_nom`) VALUES
	(2, 'PIQUEOS'),
	(3, 'COMBOS'),
	(4, 'BEBIDAS');
INSERT INTO `tbl_mesa` (`mesa_id`, `mesa_nro`, `mesa_cap`) VALUES
	(1, '1', 10),
	(2, '2', 5);
INSERT INTO `tbl_plato` (`plato_id`, `plato_nom`, `plato_img`, `plato_pre`, `categoria_id`) VALUES
	(1, 'ANTICUCHO', 'image/upload/v1657767775/ofgvtfcahvh80rm49amd.jpg', 15.00, 2),
	(2, 'YUQUITAS FRITAS', 'image/upload/v1657767790/reze6ishda4xx0voang7.jpg', 10.00, 2),
	(3, 'LOMO SALTADO', 'image/upload/v1657767810/a8ntpvgsvh1jvumzi5cl.jpg', 30.00, 3),
	(4, 'COMBO MARINO', 'image/upload/v1657767824/upsve4kvsrrebynylpjr.jpg', 50.00, 3),
	(5, 'PILSEN', 'image/upload/v1657767843/gqzaleyoz4s6mlyoqy3g.jpg', 10.00, 4),
	(6, 'LIMONADA FROZEN', 'image/upload/v1657767855/gwf6tgmkkaelq2tibvpd.jpg', 16.00, 4),
	(7, 'PISCO SOUR', 'image/upload/v1657767867/lazyabeqk1bxjnjgthob.jpg', 20.00, 4),
	(8, 'DESAYUNO CRIOLLO', 'image/upload/v1657767899/j2nl1qzx1skfpm3j7zsr.jpg', 20.00, 3),
	(9, 'SALTEÑAS', 'image/upload/v1657771279/vfohesemfrgxoqigadfz.jpg', 4.00, 2);