<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <div class="input-container">
        <div class="alert" v-if="showAlert">
            <i class="fa fa-exclamation-circle" aria-hidden="true"></i>
            <text class="alert-text">{{alertOutput}}</text>
        </div>
        <div class="success" v-if="showSuccess">
            <i class="fa fa-exclamation-circle" aria-hidden="true"></i>
            <text class="alert-text">{{alertOutput}}</text>
        </div>
        <div class="icon-login">
            <i class="fa fa-user-o" aria-hidden="true"></i>
        </div>
        <div class="input-group">
            <label for="repo">Username</label>
            <input type="text" v-model="username"><br><br>
        </div>

        <div class="input-group">
            <label for="token">Password</label>
            <input type="password" v-model="password"><br><br>
        </div>

        <div class="btn-group-login">
            <a class="loginbtn" @click="submitLogin">Login</a>
            <a class="registerbtn" @click="submitRegister">Register</a>
        </div>
        
    </div>
</template>

<script>
import axios from 'axios'
export default{
    data(){
        return{
            username: '',
            password: '',
            alertOutput: '',
            showAlert: false,
            showSuccess: false,
        }
    },
    methods: {
        async submitLogin(){
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            try{
                const response = await axios.post("api/auth/login/", formData)

                const access = response.data.access
                const refresh = response.data.refresh

                axios.defaults.headers.common["Authorization"] = `Bearer ${access}`
                localStorage.setItem("access", access)
                localStorage.setItem('refresh', refresh)

                this.$router.push('/projects')
            }
            catch (error){
                if (error.response) {
                        console.log(error.response.data)
                        if(error.response.data.error == 'Invalid credentials'){
                            this.alertOutput = 'Invalid credentials. '
                            this.toggleAlert()
                        }
                        else{
                            this.alertOutput = 'Enter valid username and password. '
                            this.toggleAlert()
                        }
                    } else {
                        this.alertOutput = 'Something went wrong. Please try again. '
                        this.toggleAlert()
                        console.log(JSON.stringify(error))
                    }
            }
        },
        async submitRegister(){
                if(this.username === ''){
                    this.alertOutput = 'Enter a username. '
                    this.toggleAlert()
                }
                else if(this.password === ''){
                    this.alertOutput = 'Enter a password. '
                    this.toggleAlert()
                }
                else{
                    const formData = {
                        username: this.username,
                        password: this.password
                    }

                    axios
                        .post("api/auth/register/", formData)
                        .then(response => {
                            this.alertOutput = "Account created, please login with same credentials."
                            this.toggleSuccess()
                        })
                        .catch(error =>{
                            if(error.response){
                                if(error.response.data.username){
                                    this.alertOutput = error.response.data.username[0];
                                    this.toggleAlert();
                                    console.log(JSON.stringify(error.response.data))
                                }
                            }
                            this.alertOutput = 'Something went wrong. Please try again. '
                            this.toggleAlert()
                            console.log(JSON.stringify(error))
                        })
                }
        },
        toggleAlert(){
            this.showAlert = true;
            setTimeout(() => {
                this.showAlert = false;
            }, 3000);
        },
        toggleSuccess(){
            this.showSuccess = true;
            setTimeout(() => {
                this.showSuccess = false;
            }, 3000);
        },
    }
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
    .alert{
        display: flex;
        align-items: center;
        height: 40px;
        width: 50%;
        background-color: #FFCCCB;
        border: 1px solid red;
    }
    .alert i, .success i{
        margin-left: 10px;
        margin-right: 10px;
    }
    .alert text, .success text{
        color: darkslategrey;
        font-size: 20px;
    }
    .success{
        display: flex;
        align-items: center;
        height: 40px;
        width: 50%;
        background-color: #0fb36f;
        border: 1px solid green;
    }
    text{
        text-decoration: none;
    }

</style>