<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <div class="input-container"> 
        <div :class="notification.class" v-if="notification.show"> <!--dynamically assign class of div element and render based on show property of notification-->
            <i class="fa fa-exclamation-circle" aria-hidden="true"></i>
            <text class="alert-text">{{notification.message}}</text>
        </div>
        <div class="icon-login">
            <i class="fa fa-user-o" aria-hidden="true"></i>
        </div>
        <div class="input-group">
            <label>Username</label>
            <input type="text" v-model="username"><br><br>
        </div>

        <div class="input-group">
            <label>Password</label>
            <input type="password" v-model="password"><br><br>
        </div>

        <div class="btn-group-login">
            <a class="loginbtn" @click="submitLogin">Login</a>
            <a class="registerbtn" @click="submitRegister">Register</a>
        </div>
        
    </div>
</template>

<script setup>
    import { ref, reactive } from 'vue'
    import { useRouter } from 'vue-router'
    import axios from 'axios'

    const username = ref('')
    const password = ref('')
    const notification = reactive({ //state variable to handle notifications, use through toggleNotification(*message, *type of notification, alert or message)
        show: false,
        class: '',
        message: '',
    })

    const router = useRouter();

    async function submitLogin (){
        if(username.value === ''){
            toggleNotification('Please provide a username', "alert") //Check for username input
        }
        else if(password.value === ''){
            toggleNotification('Please provide a password', "alert") //Check for password input
        }
        else{
            try{ //catch any errors returned from backend
                axios.defaults.headers.common["Authorization"] = "" //remove access token from header if there is one

                localStorage.removeItem("access") //remove existing tokens
                localStorage.removeItem("refresh")

                const formData = {
                    username: username.value,
                    password: password.value
                }

                const response = await axios.post("api/auth/login/", formData) //send post request and retrieve JWT tokens from response

                const access = response.data.access
                const refresh = response.data.refresh

                axios.defaults.headers.common["Authorization"] = `Bearer ${access}` //add access token to axios header
                localStorage.setItem("access", access)
                localStorage.setItem('refresh', refresh)

                router.push('/projects')
            }
            catch (error){
                error?.response?.data?.error ? toggleNotification('Invalid credentials', 'alert'): toggleNotification('Something went wrong. Please try again', 'alert')
            }
        }
    }
    async function submitRegister(){
        if(username.value === ''){
            toggleNotification('Please provide a username', "alert") //Check for username input
        }
        else if(password.value === ''){
            toggleNotification('Please provide a password', "alert") //Check for password input
        }
        else{
            const formData = {
                username: username.value,
                password: password.value
            }
            
            try{
                const response = await axios.post('api/auth/register/', formData) //send post request to create user in backend
                let message = "Account created, please login with same credentials."
                toggleNotification(message, "success")
            } 
            catch(err){
                if(err?.response?.data?.username){
                    toggleNotification('Username is already taken. Please provide a different one', 'alert')
                }
                else{
                    toggleNotification('Something went wrong. Please try again', 'alert')
                }
            }
        }
    }

    function toggleNotification(message, className){ //function to toggle a notification for three seconds
        notification.show = true
        notification.class = className
        notification.message = message

        setTimeout(() => (notification.show = false), 3000)
    }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
    .input-container{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding: 20px;
        padding-top: 20vh;
        font-family: 'DM Sans', sans-serif;
        min-width: 300px;
        width: 100%;
        height: 100%;
    }
    .input-group{
        width: 90%;
        height: 8%;
        min-width: 250px;
        max-width: 500px;
        min-height: 50px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
        margin-bottom: 15px;
    }
    .input-group input{
        height: 100%;
        width: 100%;
        min-height: 30px;
        border: 1px solid #063970;
        border-radius: 5px;
        color: #063970;
        margin: 0;
    }
    .input-group label{
        margin: 0;
        font-family: 'DM Sans', sans-serif;
        font-size: clamp(1rem, 50%, 2rem);
    }
    .icon-login{
        display: flex;
        align-items: center;
        justify-content: center;
        height: 20%;
        width: 20%;
        margin-bottom: 20px;
    }
    .icon-login i{
        color:#063970;
        font-size: 5em;
    }
    .btn-group-login{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;
        width: 40%;
        height: 12%;
        min-width: 250px;
        max-width: 500px;
        min-height: 100px;
    }
    .loginbtn, .registerbtn{
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 80%;
        height: 30%;
        min-width: 200px;
        margin-bottom: 10px;
    }
    .loginbtn{
        background-color:#063970;
        color: white;
        border-radius: 10px;
        cursor: pointer;
    }
    .registerbtn{
        background-color: white;
        color:#063970;
        border: 1px solid #063970;
        border-radius: 10px;
        cursor: pointer;
    }
    .alert, .success{
        display: flex;
        align-items: center;
        height: fit-content;
        box-sizing: border-box;
        padding: 0px 10px 0px 10px;
        width: fit-content;
        max-width: 300px;
        background-color: #FFCCCB;
        border: 1px solid red;
    }
    .alert i, .success i{
        margin-right: 10px;
    }
    .alert text, .success text{
        color: darkslategrey;
        font-size: 20px;
    }
    .success{
        background-color: #0fb36f;
        border: 1px solid green;
    }
    text{
        text-decoration: none;
    }

</style>