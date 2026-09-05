import axios from 'axios';
import { getAccessToken, setAccessToken, clearAccessToken } from "./authToken";

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

// Response interceptor to handle 401 errors
api.interceptors.response.use(
    (response) => {
        // Any status code that lie within the range of 2xx cause this function to trigger
        return response;
    },
    async (error) => {
        const originalRequest = error.config;

        // If error is 401, and we haven't already tried to refresh the token
        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true; // Mark as retried to avoid infinite loops

            try {
                // Try to get a new access token using the refresh cookie
                // We use a clean axios instance here to avoid interceptor loops
                const refreshResponse = await axios.post("http://127.0.0.1:8000/api/token/refresh/", {}, {
                    withCredentials: true // Important: send the HttpOnly cookie
                });

                const newAccessToken = refreshResponse.data.access;
                
                // Save the new access token
                setAccessToken(newAccessToken);

                // Update the Authorization header for the failed request and retry it
                originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
                return api(originalRequest);
                
            } catch (refreshError) {
                // If refresh fails (e.g. refresh token expired), clear the token
                clearAccessToken();
                // Optionally redirect to login or let the AuthContext handle the null user
                return Promise.reject(refreshError);
            }
        }

        // Return any other errors as normal
        return Promise.reject(error);
    }
);

export default api;