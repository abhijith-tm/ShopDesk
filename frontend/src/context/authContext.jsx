//how does Dashboard know user is logged in or wich user it is so we need this

import { createContext,useState,useEffect } from "react";
import { onAuthStateChanged,signOut } from "firebase/auth";
import auth from "../firebase/auth";

//creates a shared data channel.
const AuthContext = createContext();

//something that actually provides data through that context.
// AuthProvider is simply a React component that provides the auth data to its children.
function AuthProvider({children}){

    const [user,setUser] = useState(null);
    const [loading,setLoading] = useState(true)

    //used to handle things outside of react render
    useEffect(()=>{
        const unsubscribe = onAuthStateChanged(auth,(currentUser)=>{ //on stste change the arrow ftn runs
            setUser(currentUser)
            setLoading(false)
    
        })
        return unsubscribe //unsubscribe stores the function that is given finally to stop listening
    },[])

    const logout = () => {
        return signOut(auth)
    }
    return(
        //Context object(AuthContext) provides a special React component:<AuthContext,provider>
        <AuthContext.Provider value={{user,logout,loading}}>  {/* user is a object literal */}
            {/* "Everything inside me can access the data I'm providing." */}
            {children}
        </AuthContext.Provider>
    )
}

export {AuthProvider}
export default AuthContext;