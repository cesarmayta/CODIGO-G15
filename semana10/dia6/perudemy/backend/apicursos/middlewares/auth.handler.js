const jwt = require('jsonwebtoken');

function verifyToken(req,res,next){
    const bearerToken = req.headers['authorization'];
    
    if(typeof bearerToken !== 'undefined'){
        //validamos el token
        const bearer = bearerToken.split(' ');
        const token = bearer[1];

        try{
            const decoded = jwt.verify(token,'django-insecure-3xv$-1ghpdx$#%jh0#!d@d2n_bff25*(tg9hy@ruxd5r&(p9v@')
        }catch(err){
            return res.status(401).json({
                status:false,
                content:'token invalido'
            })
        }
        return next();
    }else{
        res.status(403).json({
            status:false,
            content:'no se encontro el token'
        })
    }
}

module.exports =  {verifyToken}