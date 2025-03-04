<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <div class="navbar">
        <div class="left">
            <router-link to="/"><text>Code Assessor</text></router-link>
        </div>

        <div class="right">
            
            <div class="dropdown">
                <button class="dropbtn" @click="toggleDropdown">
                    <i class="fa fa-bars"></i>
                </button>
                <div class="dropdown-content" v-if="showDropdown && logged" @click="showDropdown=false">
                    <router-link to="/projects">Projects</router-link>
                    <router-link to="/new-project">New Project</router-link>
                    <span @click="logout">Logout</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
const showDropdown = ref(false)

const route = useRoute()
const router = useRouter()
const logged = computed(() => !!localStorage.getItem('access'))

function logout(){
    showDropdown.value = false
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');

    router.push('/')
}

watch(route, () => {
    showDropdown.value = false;
})

function toggleDropdown(){
    showDropdown.value = !showDropdown.value
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

.navbar {
    display: flex;
    flex-direction: row;
    width: 100vw;
    height: 50px;
    background-color: white;
    border-top: 2px solid #063970;
    border-bottom: 2px solid #063970;
    left: 0;
    right: 0;
    top: 0;
    padding: 10px 0;
}

.navbar .left {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 50%;
    margin-left: 10px;
}

.navbar .right {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    width: 50%;
    margin-right: 10px;
}

.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown .dropbtn {
    font-size: 16px;
    border: none;
    outline: none;
    color: #063970;
    padding: 8px 16px;
    background-color: inherit;
    font-family: inherit;
    cursor: pointer;
}

.dropdown-content {
    display: block;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1000;

    right: 0;
}

.dropdown-content a, .dropdown-content span {
    font-family: 'DM Sans', sans-serif;
    color: #063970;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
}

.dropdown-content a:hover, .dropdown-content span:hover {
    cursor: pointer;
    background-color: #ddd;
}

.navbar text {
    font-family: 'DM Sans', sans-serif;
    font-size: clamp(1rem, 10%, 3rem);
    color: #063970;
}
</style>

