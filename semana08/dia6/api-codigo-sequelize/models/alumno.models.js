const {Model,DataTypes,Sequelize} = require('sequelize');

const TABLE_NAME = 'tbl_alumno';


const AlumnoSchema = {
    id:{
        allowNull:false,
        autoIncrement:true,
        primaryKey:true,
        type:DataTypes.INTEGER,
        field:'alumno_id'
    },
    nombre:{
        allowNull:false,
        type: DataTypes.STRING,
        field:'alumno_nombre'
    },
    email:{
        allowNull:false,
        type: DataTypes.STRING,
        field:'alumno_email'
    }
}

class Alumno extends Model {
    static associate(){

    }

    static config(sequelize){
        return {
            sequelize,
            tableName: TABLE_NAME,
            modelName:'Alumno',
            timestamps:false
        }
    }
}

module.exports =  {TABLE_NAME,AlumnoSchema,Alumno}