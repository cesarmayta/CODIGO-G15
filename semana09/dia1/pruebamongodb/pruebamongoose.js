const mongoose = require('mongoose');

async function main(){
    //conexión a mongodb
    await mongoose.connect('mongodb://localhost:27017/db-mongoose');

    //creamos schema
    const PeliculaSchema = new mongoose.Schema({
        nombre:String,
        fecha:{type:Date,default:Date.now},
        rating:{type:Number,required:[true,'necesita un rating']}
    });

    const Pelicula = mongoose.model('col_pelicula',PeliculaSchema);

    const drama = new Pelicula({nombre:'los chotanos',rating:10});
    await drama.save();
    //const pelicula2 = new Pelicula({nombre:'Rapidos y furiosos 5'});
    //await pelicula2.save();

    const listadoPeliculas = await Pelicula.find();
    console.log(listadoPeliculas);


}

main().catch(err=>console.log(err));
