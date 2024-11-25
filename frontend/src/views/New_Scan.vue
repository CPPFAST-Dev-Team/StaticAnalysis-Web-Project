<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <div class="input-container">
        <div class="header">
            <h1>New Scan of Placeholder.com/example </h1>
        </div>

        <div class="input-group">
            <label>Branch</label>
            <Dropdown
            selectFiller="Select branch"
            :options="options"
            v-model="parentSelectedOption"
            />
        </div>

        <div class="input-group">
            <label>Commit</label>
            <input type="text" v-model="commit"><br><br>
        </div>

        <div class="create">
            <router-link to="/issues" class="createbtn">
                <text>Initiate</text>
            </router-link>
        </div>
        
    </div>
</template>

<script>
import Dropdown from "../components/Dropdown.vue";

export default {
    data(){
        return{
            options: [],
            parentSelectedOption: null,
            commit: "",
        };
    },
    created(){
        //get request to backend api for project branches
        this.options = ["Branch1", "Frontend Branch", "Another Branch"];
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
}

.header{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    min-height: 100px;
    height: 10%;
    width: 40%;
    white-space: nowrap;
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
