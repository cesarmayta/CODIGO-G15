const cursoController = {}

const cursoModel = require('../models/curso.models');

cursoController.getAll = async(req,res)=>{
    const cursos = await cursoModel.find();
    res.json({
        status:true,
        content:cursos
    })
}

module.exports = cursoController;
