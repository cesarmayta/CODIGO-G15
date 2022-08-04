function hola(nombre,primercallback){
    setTimeout(function(){
        console.log('Hola ' + nombre);    
        primercallback(nombre)
    },1000);
}

function hablar(nombre,segundocallback){
    setTimeout(function(){
        console.log("como estas " + nombre);
        segundocallback(nombre);
    })
}

function adios(nombre){
    console.log('adios ' + nombre);
}

hola('César',function(nombre){
    //console.log('como estas ' + nombre);
    hablar(nombre,function(nombre){
       adios(nombre);
    })
});
