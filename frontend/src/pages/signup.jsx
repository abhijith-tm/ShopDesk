import { useState } from "react"
import {createUserWithEmailAndPassword} from "firebase/auth"
import auth from "../firebase/auth";


import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import Stack from "@mui/material/Stack";

function Signup(){

    const [email,setEmail] =useState("") 
    const [password, setPassword] = useState("");


    const handleSignup = async (e)=>{
        e.preventDefault() // prevents default browser action of submiting form 

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
        <Box     sx={{
                minHeight: "100vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
            }}>
            <Card>
                <Stack spacing={2}>
                    <Typography variant="h4">
                        Create your account
                    </Typography>

                    <TextField label="Name" />
                    <TextField label="Email" />
                    <TextField label="Password" type="password" />
                    <TextField
                        label="Confirm Password"
                        type="password"
                    />

                    <Button variant="contained">
                        Sign Up
                    </Button>
                </Stack>
            </Card>
        </Box>
    );

}
export default Signup