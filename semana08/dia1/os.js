const os = require('os');
const { resolve } = require('path');

procesador = os.arch();
sistemaoperativo = os.platform();
cpu = os.cpus().length;
memoria = os.totalmem();

console.log("arquitectura del procesador : " + procesador);
console.log("sistema operativo : " + sistemaoperativo);
console.log("CPU : " + cpu);
console.log("Memoria Ram bytes: " + memoria);
memoria = memoria / 1024;
console.log("Memoria en KB : " + memoria );
memoria = memoria / 1024;
console.log("Memoria en MB : " + memoria );
memoria = memoria / 1024;
console.log("Memoria en gB : " + memoria );

//RETO 1 - CREAR UNA FUNCTION CON PROMESAS QUE RETORNE LA MEMORIA EN KB,MB,GB
function calcularMemoria(capacidad,tipo){
    return new Promise((res,rej)=>{
        let memoria_convertida = capacidad / 1024;
        console.log('MEMORIA EN ' + tipo + " : " + memoria_convertida.toFixed(2));
        res(memoria_convertida);
    })
}

calcularMemoria(os.totalmem(),'KB')
    .then((kb)=>calcularMemoria(kb,'MB'))
    .then((mb)=>calcularMemoria(mb,'GB'))