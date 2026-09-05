import { createContext, useState, useEffect } from "react";
import {
    setAccessToken,
    clearAccessToken,
} from "../API/authToken";
import { getMe } from "../API/auth";
import axios from "axios";

const AuthContext = createContext();

function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [accessToken, setAccessTokenState] = useState(null);
    const [loading, setLoading] = useState(true); // Start loading as true so we don't flash login screens

    useEffect(() => {
        const restoreAuth = async () => {
            try {
                // 1. Try to get a new access token using the refresh cookie
                const refreshResponse = await axios.post("http://127.0.0.1:8000/api/token/refresh/", {}, {
                    withCredentials: true
                });
                
                const newAccessToken = refreshResponse.data.access;
                
                // 2. Save token so Axios interceptors can use it
                setAccessToken(newAccessToken);
                setAccessTokenState(newAccessToken);

                // 3. Fetch the user's details and restore context
                const meResponse = await getMe();
                setUser(meResponse.data);
            } catch (error) {
                // If anything fails, they are logged out. Clear memory.
                clearAccessToken();
                setAccessTokenState(null);
                setUser(null);
            } finally {
                setLoading(false); // Done checking auth
            }
        };

        restoreAuth();
    }, []);

    const login = (token) => {
        setAccessToken(token);
        setAccessTokenState(token);
    };

    const logout = () => {
        clearAccessToken();
        setAccessTokenState(null);
        setUser(null);
    };

    return (
        <AuthContext.Provider
            value={{
                user,
                setUser,
                accessToken,
                login,
                logout,
                loading,
            }}
        >
            {children}
        </AuthContext.Provider>
    );
}

export { AuthProvider };
export default AuthContext;