<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <div class="input-container">
        <div class="header">
            <h1>New Project</h1>
        </div>

        <form class="input-group">
            <label for="repo">Repo</label>
            <input type="text" id="repo" v-model="repoInput">
        </form>

        <form class="input-group">
            <label for="token">Token</label>
            <input type="text" id="token" v-model="tokenInput">
        </form>

        <form class="input-group">
            <label for="team">Team</label>
            <Dropdown
                id="team"
                selectFiller="Select Team"
                :options="teams"
                v-model="selectedTeam"
            />
        </form>


        <div class="create">
            <router-link to="/projects" class="createbtn">
                <span>Create</span>
            </router-link>
        </div>
        
    </div>
</template>

<script setup>
import Dropdown from "../components/Dropdown.vue";

import { ref, onMounted } from 'vue'

const repoInput = ref('')
const tokenInput = ref('')
const teams = ref([])
const selectedTeam = ref(null)

onMounted(() => {
    teams.value = getTeams()
})

function getTeams(){
    return ['Team1', 'Hackers', 'Coders'] //fetch teams here
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

.input-container {
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

.header{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
    height: 10%;
    min-width: 250px;
    max-width: 500px;
    min-height: 50px;
    margin-bottom: 20px;
}
.header h1{
    color:#063970;
}

.input-group {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    width: 100%;
    height: 50px;
    min-width: 250px;
    max-width: 500px;
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
    color: #063970;
    font-size: clamp(1rem, 50%, 2rem);
}

.create {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 12%;
    min-width: 250px;
    max-width: 500px;
    min-height: 100px;
}

.createbtn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 80%;
    height: 30%;
    min-width: 200px;
    background-color: #063970;
    color: white;
    border-radius: 10px;
    cursor: pointer;
    text-decoration: none;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
}
</style>
