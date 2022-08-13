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

usuarioController.auth = async (req,res)=>{
    const {usuario,password} = req.body;

    const authUsuario = await usuarioModel.findOne({usuario});

    if(authUsuario && (await bcrypt.compare(password,authUsuario.password))){
        //datos de auth correctos
        const token = jwt.sign(
            {usu_id:authUsuario._id,usu_name:authUsuario.usuario},
            'qwerty123',
            {
                expiresIn:'1h'
            }
        )

        let dataResponse = {
            status:true,
            content:token
        }

        res.status(200).json(dataResponse);
    }
    else{
        res.status(400).json({
            status:false,
            content:'usuario o password invalidos'
        })
    }
}

module.exports = usuarioController;

