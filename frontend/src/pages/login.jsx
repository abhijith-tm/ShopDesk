import { useState } from "react"
import auth from "../firebase/auth"
import { signInWithEmailAndPassword } from "firebase/auth"
function Login(){

    const [email,setEmail] = useState("")
    const [password, setPassword] = useState("");

    const handleLogin = async(e)=>{
        e.preventDefault()

        try{
            const userCredential = await signInWithEmailAndPassword(
                auth,email,password
            )
        console.log(userCredential.user)
        }catch (error){
            console.error(error)
        }
    }

    return (
        <div>
            <h1>Login</h1>
            <form onSubmit={handleLogin}>
                <input type="email" placeholder="Email" value={email} onChange={(e)=>setEmail(e.target.value)} />
                <br/>
                <input type="password" placeholder="Password" value={password} onChange={(e)=>setPassword(e.target.value)} />
                <br />

                <button type="submit">Login</button>
            </form>

        </div>
    )
}

export default Login