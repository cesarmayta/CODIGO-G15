const express = require('express');
const {config} = require('./config');

//importamos middleware
const cors = require('cors');
const {logsRequest} = require('./middlewares/logs.handler');

const app = express();

app.use(logsRequest);

app.set('port',config.port);

//middlewares
app.use(cors());
app.use(express.json());

app.get('/',(req,res)=>{
    res.json({
        status:true,
        content:'servidor activo'})
})

//rutas
app.use('/tarea',require('./routes/tarea.route'));

module.exports = app;
