<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <div class="input-container">
        <div class="header">
            <h1>New Project</h1>
        </div>

        <div class="input-group">
            <label>Repo</label>
            <input type="text" v-model="repo"><br><br>
        </div>

        <div class="input-group">
            <label>Token</label>
            <input type="text" v-model="token"><br><br>
        </div>

        <div class="input-group">
            <label>Team</label>
            <Dropdown
            selectFiller="Select Team"
            :options="options"
            v-model="parentSelectedOption"
            />
        </div>

        <div class="create">
            <router-link to="/projects" class="createbtn">
                <span>Create</span>
            </router-link>
        </div>
        
    </div>
</template>

<script>
import Dropdown from "../components/Dropdown.vue";

export default {
    data(){
        return{
            repo: "",
            token: "",
            options: [],
            parentSelectedOption: null,
        };
    },
    created(){
        //backend api get teams from User
        this.options=["Team1","Coders","Hackers"];
    },
    components: {
        Dropdown
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

.input-container {
    position: relative;
    min-height: 600px;
    height: 60vh;
    min-width: 400px;
    width: 100vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 50px;
    margin-bottom: 50px;
}

.header{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    min-height: 100px;
    height: 10%;
    width: 40%;
}
.header h1{
    color:#063970;
}

.input-group {
    width: 40%;
    height: 10%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 15px;
}

.input-group input[type="text"] {
    height: 100%;
    width: 100%;
    min-height: 30px;
    border: 1px solid #063970;
    border-radius: 5px;
    color: #063970;
    margin: 0;
}

.input-group label {
    margin: 0;
    font-family: 'DM Sans', sans-serif;
    font-size: clamp(1rem, 50%, 2rem);
}

.create {
    margin: 25px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40%;
    height: 5%;
    z-index: 0;
}

.createbtn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40%;
    height: 100%;
    background-color: #063970;
    color: white;
    border-radius: 10px;
    cursor: pointer;
    text-decoration: none;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
}
</style>
