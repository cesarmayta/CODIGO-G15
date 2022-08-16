const productoController = {};

const productoModel = require('../models/producto.models');

productoController.getAll = async (req,res)=>{
    const productos = await productoModel.find();
    res.json({
        success: true,
        message: "Los productos se han cargado correctamente",
        content:productos
    })
}

module.exports = productoController;