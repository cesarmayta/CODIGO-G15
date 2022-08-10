const Sequelize = require('sequelize');

/*
para sqlite
const sequelize = new Sequelize({
    dialect : 'sqlite',
    storage : './database.sqlite'
})*/

//MYSQL
const sequelize = new Sequelize('db_sequelize','root','',{
    host:'localhost',
    dialect:'mysql'
});

sequelize.authenticate()
.then(()=>console.log("conexión establecida"))
.catch(err=>console.log("error : " + err))

//creación de modelos
const Alumnos = sequelize.define(
    'tbl_alumno',
    {
        nombre:Sequelize.STRING,
        email:Sequelize.STRING
    }
)

sequelize.sync()
.then(()=>{
    console.log("tablas migradas");
    Alumnos.bulkCreate(
        [
            {nombre:'César Mayta',email:'cesarmayta@gmail.com'},
            {nombre:'Claudia Gonzales',email:'claudiagonzalez@hotmail.com'}
        ]
    ).then(()=>{
        return Alumnos.findAll();
    }).then((alumnos)=>console.log(alumnos));
});