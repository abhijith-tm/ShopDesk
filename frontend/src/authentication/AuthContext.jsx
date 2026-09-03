import { createContext, useState } from "react";
import {
    setAccessToken,
    clearAccessToken,
} from "../API/authToken";

const AuthContext = createContext();

function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [accessToken, setAccessTokenState] = useState(null);
    const [loading, setLoading] = useState(false);

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