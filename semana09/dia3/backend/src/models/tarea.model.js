const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const TareaSchema = new Schema({
    nombre:{
        type:String,
        required:true,
        minlength:2,
        maxlength:100
    },
    estado:{
        type:String,
        required:true,
        enum:['pendiente','terminado']
    }
},
{
    timestamps:true,
    versionKey:false
}
)

module.exports = mongoose.model('tareas',TareaSchema);