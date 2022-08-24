const express = require('express');
const {config} = require('./config');
const cors = require('cors');

//swagger
const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./swagger.json');

const app = express();

//middlewares
app.use(cors());
app.use(express.json());

app.set('port',config.port);

/*app.get('/',(req,res)=>{
    res.json({
        status:true,
        content:'servidor activo cursos'
    })
})*/

app.use('/', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

//routes
app.use('/curso',require('./routes/curso.routes'));

module.exports = app;
