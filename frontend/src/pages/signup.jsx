import { useState } from "react"
import {createUserWithEmailAndPassword} from "firebase/auth"
import auth from "../firebase/auth";
import app from "../firebase/config"
function Signup(){

    const [email,setEmail] =useState("") 
    const [password, setPassword] = useState("");


    const handleSignup = async(e)=>{
        e.preventDefault()

        try{
            const userCredential = await createUserWithEmailAndPassword(
                auth,email,password
            )
        console.log(userCredential.user)
        }catch (error){
            console.error(error)
        }
    }
    return (

        
        <div>
             <h1>Signup</h1>
            <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <br/>
            <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <br />

            <button onClick={handleSignup}>Signup</button>
        </div>
    )
}
export default Signup