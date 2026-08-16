import { useContext } from "react"
import AuthContext from "../context/authContext"

function Dashboard(){
    const {logout}=useContext(AuthContext)
    return (
        <div>
            <h1>ShopDesk Dashboard</h1>
            <br />

            <button onClick={logout}>Logout</button>
        </div>
    )
}

export default Dashboard