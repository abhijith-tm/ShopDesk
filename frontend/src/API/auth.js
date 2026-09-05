import api from "./client";

export const login = (username,password) =>{
    return api.post("token/",{
        username,
        password
    })
}

export const getMe = () => {
    return api.get("auth/me/");
}
