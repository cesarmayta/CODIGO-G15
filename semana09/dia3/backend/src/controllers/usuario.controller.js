const usuarioController = {}

const usuarioModel = require('../models/usuario.model');
const boom = require('@hapi/boom');
const jwt = require('jsonwebtoken');

const bcrypt = require('bcryptjs');

usuarioController.create = async (req,res)=>{
    const {usuario,password} = req.body

    passwordEncriptado = await bcrypt.hash(password,10);
    console.log("password encriptado : " + passwordEncriptado)

    let data ={
        usuario:usuario,
        password:passwordEncriptado
    }

    const nuevoUsuario = new usuarioModel(data)
    await nuevoUsuario.save()

    let dataResponse = {
        id:nuevoUsuario._id,
        usuario:nuevoUsuario.usuario
    }

    res.json({
        status:true,
        content:dataResponse
    })
}

module.exports = usuarioController;

