<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <form class="container" @submit.prevent>
        <div class="header">
            <h1>New Project</h1>
        </div>
        
        <div class="input-group">
            <label for="name">Project Name</label>
            <input type="text" id="name" v-model="nameInput">
        </div>
        <div class="input-group">
            <label for="repo">Repository Url</label>
            <input type="text" id="repo" v-model="repoInput">
        </div>
        <div class="input-group">
            <label for="description">Description</label>
            <textarea type="text" id="description" v-model="descriptionInput">
            </textarea>
        </div>
        <div class="create">
            <Loading v-if="loading"/>
            <button class="createbtn" @click="createProject">
                Create
            </button>
        </div>
    </form>
</template>

<script setup>
import Loading from "../components/Loading.vue";
import Dropdown from "../components/Dropdown.vue";
import api from "../api"

import axios from 'axios'
import { ref, inject } from 'vue'
import { useRouter } from 'vue-router'

const nameInput = ref('')
const repoInput = ref('')
const descriptionInput = ref('')
const loading = ref(false)

const router = useRouter();
const toggleNotification = inject('toggleNotification')

async function createProject(){
    if(nameInput.value === ''){
        toggleNotification('Please provid a project name', 'alert')
    }
    else if(!isValidURL(repoInput.value)){
        toggleNotification('Please provid a valid url', 'alert')
    }
    else if(descriptionInput.value === ''){
        toggleNotification('Please provide a project description', 'alert')
    }
    else{
        loading.value = true
        try{
            const formData = {
                name: nameInput.value,
                repository_url: repoInput.value,
                description: descriptionInput.value,
            }
            await api.post("api/projects/", formData)
            toggleNotification(`Project ${nameInput.value} successfully created`, 'success')
            router.push('/projects')
        }
        catch(error){
            console.log(error)
        }
        finally{
            loading.value = false
        }
    }
}

function isValidURL(url) {
    try {
        new URL(url);
        return true;
    } catch (e) {
        return false;
    }
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    row-gap: 15px;
    min-width: 300px;
    padding: 20px;
    font-family: 'DM Sans', sans-serif;
    width: 100%;
    height: 100%;
}

.header{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
    max-width: 500px;
    min-height: 50px;
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
    max-width: 500px;
}

.input-group input[type="text"] {
    height: 30px;
    width: 100%;
    border: 1px solid #063970;
    border-radius: 5px;
    color: #063970;
    margin: 0;
}
.input-group textarea {
    height: 100px;
    width: 100%;
    padding: 5px;
    resize: none;
    overflow-y: auto;
    border: 1px solid #063970;
    border-radius: 5px;
    color: #063970;
    margin: 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
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
    row-gap: 15px;
    width: 100%;
    height: 12%;
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
