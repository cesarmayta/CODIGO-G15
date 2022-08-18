const {config} = require('../config');

const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth').OAuth2Strategy;

const UsuarioModel = require('../models/usuario.models');

passport.serializeUser(function(user, done) {
    done(null, user);
  });
  
passport.deserializeUser(function(user, done) {
    done(null, user);
});

passport.use(new GoogleStrategy({
    clientID:config.google.clientId,
    clientSecret:config.google.clientSecret,
    callbackURL:"http://localhost:5000/auth/callback"
},function(accessToken,refresToken,profile,done){
    console.log(profile);

    const usuarioData = {
        usuario:profile.displayName,
        password:profile.id
    };
    UsuarioModel.create(usuarioData,(err,dataResponse)=>{
            if(err){
                return done(err,null);
            }
            return done(null,dataResponse);
        })

}))

passport.initialize();
passport.session();

module.exports = passport;