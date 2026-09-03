import AuthContext from "../authentication/AuthContext";
import { useContext } from "react";
import { Navigate } from "react-router-dom";

function ProtectedRoute({children}){
    const {user,loading} = useContext(AuthContext)

    console.log("user:", user);
    console.log("loading:", loading);

    if(loading){
        return <h1>Loading...</h1>
    }

    if (user){
        return children
    }else{
        return (
            <Navigate to="/login"/>
        )
    }
}
export default ProtectedRoute