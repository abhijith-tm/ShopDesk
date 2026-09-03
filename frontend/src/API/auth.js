import api from "./client";

export const login = (username,password) =>{
    return api.post("token/",{
        username,
        password
    })
}
