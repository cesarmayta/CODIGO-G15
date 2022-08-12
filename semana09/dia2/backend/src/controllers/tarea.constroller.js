const tareaController = {};

const TareaModel = require('../models/tarea.model');

tareaController.getAll = async (req,res) =>{
    const tareas = await TareaModel.find();
    res.json(tareas);
}

module.exports = tareaController;