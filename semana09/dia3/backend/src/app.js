const express = require('express');
const {config} = require('./config');

//importamos middleware
const cors = require('cors');
const {logsRequest} = require('./middlewares/logs.handler');
const {errorHandler} = require('./middlewares/error.handler');

const app = express();

app.use(logsRequest);

app.set('port',config.port);

//middlewares
app.use(cors());
app.use(express.json());

app.get('/',(req,res)=>{
    console.log(a +3);
    res.json({
        status:true,
        content:'servidor activo'})
})

//rutas
app.use('/tarea',require('./routes/tarea.route'));
app.use('/usuario',require('./routes/usuario.route'));


//middlewares de errores
app.use(errorHandler);
module.exports = app;
