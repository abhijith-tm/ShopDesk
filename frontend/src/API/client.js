import axios from 'axios';
import { getAccessToken } from "./authToken";

const api = axios.create({
    baseURL:"http://127.0.0.1:8000/api/",
    withCredentials: true,
})



// Before every API request, get the current access token
// and put it in the Authorization header.

api.interceptors.request.use((config) => {
    const accessToken = getAccessToken();

    if (accessToken) {
        config.headers.Authorization = `Bearer ${accessToken}`;
    }

    return config;
});

// "Axios, before you send any request through `api`, 
// run this function. Give me the request configuration 
// so I can modify it, then I'll give it back to you."  
//  we are adding the bearer for auth 

export default api;