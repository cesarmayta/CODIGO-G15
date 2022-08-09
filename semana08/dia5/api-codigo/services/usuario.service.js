const MysqlLib  = require('../lib/mysql');

class UsuarioService{

    constructor(){
        this.sql = new MysqlLib();
    }

    async authenticate({usuario}){
        const sqlAuth = `select usuario_id as id,usuario_password as pwd from tbl_usuario
                        where usuario_nombre = '${usuario.usuario}'`;
        const result = await this.sql.querySql(sqlAuth);
        console.log('usuario id : ' + result[0].id);
        console.log('usuario pwd: ' + result[0].pwd);
        if(usuario.password == result[0].pwd){
            return true;
        }
        else{
            return false;
        }
    }
}

module.exports = UsuarioService;

