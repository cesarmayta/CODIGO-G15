import axios from 'axios';

const API_URL = 'http://localhost:8000'

class AuthService{

    login(usuario,password){
        return axios
        .post(API_URL + "/login",{
            usuario,
            password
        })
        .then(res=>{
            if(res.data){
                localStorage.setItem('token',JSON.stringify(res.data))
            }

            return res.data;
        })
    }

}

export default new AuthService();