import Lists from "./pages/react-quickstart/lists"
import Login from "./pages/login"
import Signup from "./pages/signup"
import Event from "./pages/react-quickstart/event"
import { useContext } from "react"
import AuthContext from "./context/authContext"
function App(){
  const {user} = useContext(AuthContext)
  console.log(user)
  return(
    <>
      <Login/>
      <Signup/>
      <Lists></Lists>
      <Event></Event>
      <div>
        <h1>ShopDesk</h1>
      </div>
    </>

  )
}

export default App