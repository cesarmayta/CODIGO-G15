const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const UsuarioSchema = new Schema({
    usuario:{
        type:String,
        required:true,
        minlength:2,
        maxlength:20,
        unique:true
    },
    password:{
        type:String,
        required:true
    }
},
{
    timestamps:false,
    versionKey:false
}
)

module.exports = mongoose.model('usuarios',UsuarioSchema);