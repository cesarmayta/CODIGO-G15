const express = require('express');
const {config} = require('./config');

const app = express();

app.set('port',config.port);

app.get('/',(req,res)=>{
    res.json({
        status:true,
        content:'servidor activo'
    })
})

module.exports = app;