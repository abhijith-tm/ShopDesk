import Lists from "./pages/react-quickstart/lists"
import Login from "./pages/login"
import Signup from "./pages/signup"
import Event from "./pages/react-quickstart/event"
function App(){
  return(
    <>
      <Login/>
      <Signup/>
      <Lists></Lists>
      <Event></Event>
    </>
  )
}

export default App