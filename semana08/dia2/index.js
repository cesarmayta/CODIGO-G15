const express = require('express');

const app = express();
const port = 5000;

app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'content':'Mi primer app web con express Js - César Mayta'
    })
})

app.listen(port,()=>{
    console.log('servidor activo en http://localhost:'+port);
})