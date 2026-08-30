import Lists from "./pages/react-quickstart/lists"
import Login from "./pages/login"
import SignUp from "./pages/sign-up/SignUp"
import Event from "./pages/react-quickstart/event"
import { useContext } from "react"
import AuthContext from "./context/authContext"
import {BrowserRouter,Routes,Route} from "react-router-dom"
import Dashboard from "./pages/dashboard"
import ProtectedRoute from "./components/protectedRoute"
import SignInSide from "./pages/sign-in-side/SignInSide"
function App(){
  const {user,logout} = useContext(AuthContext)
  return(
    <>
            <BrowserRouter>
            <Routes>

                <Route path="/login" element={<SignInSide/>} />
                <Route path="/signup" element={<SignUp />} />

                <Route
                path="/dashboard"
                element={
                  <ProtectedRoute>
                    <Dashboard/>
                  </ProtectedRoute>}/>

            </Routes>
        </BrowserRouter>


      {/* <div>
        {user&&(
          <button onClick={logout}>
            Logout
          </button>
        )}
        <h1>ShopDesk</h1>
      </div> */}
    </>

  )
}

export default App