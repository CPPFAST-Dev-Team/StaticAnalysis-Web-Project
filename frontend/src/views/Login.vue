<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <div class="input-container">
        <div class="alert" v-if="showAlert">
            <i class="fa fa-exclamation-circle" aria-hidden="true"></i>
            <text class="alert-text">Username or password is incorrect. Please try again</text>
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
            <input type="text" v-model="password"><br><br>
        </div>

        <div class="btn-group-login">
            <router-link to="/projects" class="loginbtn">Login</router-link>
            <a class="registerbtn" @click="toggleAlert">Register</a>
        </div>
        
    </div>
</template>

<script>
export default{
    data(){
        return{
            username: '',
            password: '',
            showAlert: false,
        }
    },
    methods: {
        toggleAlert(){
            this.showAlert = true;
            setTimeout(() => {
                this.showAlert = false;
            }, 3000);
        }
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
    .input-container{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-family: 'DM Sans', sans-serif;
        min-width: 1024px;
        width: 100%;
        height: 75%;
    }
    .input-group{
        width: 40%;
        height: 10%;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
        margin-bottom: 15px;
    }
    .input-group input[type="text"]{
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
        height: 15%;
        width: 15%;
        margin: 15px;
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
        height: 15%;
    }
    .loginbtn, .registerbtn{
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 60%;
        height: 30%;
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
    .alert i{
        margin-left: 10px;
        margin-right: 10px;
    }
    .alert text{
        color: gray;
        font-size: 20px;
    }
    text{
        text-decoration: none;
    }

</style>