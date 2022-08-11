const { Model, DataTypes,Sequelize} = require('sequelize');

const PROFESOR_TABLE = 'tbl_profesor';

const ProfesorSchema = {
    id:{
        allowNull:false,
        autoIncrement:true,
        primaryKey:true,
        type: DataTypes.INTEGER,
        field:'profesor_id'
    },
    nombre:{
        allowNull:false,
        type: DataTypes.STRING,
        field:'profesor_nombre'
    },
    email:{
        allowNull:false,
        type: DataTypes.STRING,
        field:'profesor_email'
    }
}

class Profesor extends Model {
    static associate(){

    }

    static config(sequelize){
        return {
            sequelize,
            tableName: PROFESOR_TABLE,
            modelName: 'Profesor',
            timestamps: false
        }
    }
}

module.exports = {PROFESOR_TABLE,ProfesorSchema,Profesor}