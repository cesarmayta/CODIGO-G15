const {Profesor,ProfesorSchema} = require('./profesor.models');
const {Alumno,AlumnoSchema} = require('./alumno.models');

function setupModels(sequelize){
    Profesor.init(ProfesorSchema,Profesor.config(sequelize))
    Alumno.init(AlumnoSchema,Alumno.config(sequelize))
}

module.exports = setupModels;