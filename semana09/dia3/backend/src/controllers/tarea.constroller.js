const tareaController = {};

const tareaModel = require('../models/tarea.model');
const boom = require('@hapi/boom');

tareaController.getAll = async (req,res) =>{
    const tareas = await tareaModel.find();
    res.json({
        status:true,
        content:tareas
    });
}

tareaController.create = async (req,res) =>{
    //const {nombre,estado} = req.body;
    try{
        console.log(req.body);
        const nuevaTarea = new tareaModel(req.body)
        await nuevaTarea.save();
        res.json({
            status:true,
            content:nuevaTarea
        });
    } catch(error){
        /*res.status(500).json({
            status:false,
            content:'Error :' + error
        })*/
        res.status(502).json(boom.badGateway(error))
    }
    
}

tareaController.update = async (req,res) =>{
    const {id} = req.params;
    //await tareaModel.updateOne({_id: id },req.body);
    //const tareaEditada = await tareaModel.findOne({_id: id });
    
    const tareaEditada = await tareaModel.findOneAndUpdate({_id: id },req.body,{
        returnOriginal: false
    })

    res.json({
        status:true,
        content:tareaEditada
    });
}

tareaController.deleteOne = async (req,res) =>{
    const {id} = req.params;
    /*await tareaModel.remove({_id:id});
    res.json({
        status:true,
        content:'tarea eliminada'
    })*/
    tareaModel.findByIdAndDelete(id,function(err,docs){
        if(err){
            console.log(err)
        }
        else{
            res.json({
                status:true,
                content:docs
            })
        }
    })
}

module.exports = tareaController;