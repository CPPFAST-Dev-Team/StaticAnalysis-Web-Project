<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <form class="input-container" @submit.prevent v-if="isMounted">
        <div class="header">
            <h1>New Scan of {{ projectName }} </h1>
        </div>
        <div class="input-group">
            <label for="branch">Branch</label>
            <Dropdown
                id="branch"
                selectFiller="Select branch"
                :options="branches"
                v-model="selectedBranch"
            />
        </div>

        <div class="input-group">
            <label for="commit">Commit</label>
            <input type="text" id="commit" v-model="commitInput">
        </div>

        <div class="create">
            <Loading v-if="loading"/>
            <button @click="postNewScan" class="createbtn">
                <text>Initiate</text>
            </button>
        </div>
    </form>
    <div class="input-container" v-if="!isMounted">
        <Loading />
    </div>
</template>

<script setup>
import Dropdown from '../components/Dropdown.vue'
import Loading from '../components/Loading.vue'
import api from '../api'

import { ref, inject, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const projectName = ref('')
const commitInput = ref('')
const branches = ref([])
const selectedBranch = ref(null)
const loading = ref(false)
const isMounted = ref(false)

const router = useRouter()
const route = useRoute()
const toggleNotification = inject('toggleNotification')
const projectId = route.params.projectId

onMounted(async () => {
    loading.value = true
    try{
        await getProjects()
    }
    catch(err){
        console.log(err)
    }
    finally{
        loading.value = false
        isMounted.value = true
    }
})

async function getProjects(){
    try{
        const response = await api.get(`/api/projects/${projectId}/`)
        projectName.value = response.data.name
        branches.value = ['Branch', 'Frontend Branch', 'BackendBranch']
    }
    catch(err){
        console.log(err)
    }
}

async function postNewScan(){
    try{
        loading.value = true
        const formData = new FormData();
        formData.append("project_id", projectId);

        const response = await api.post(`/api/scan/${projectId}/`, formData);

        if(response?.data?.message){
            toggleNotification(response.data.message, 'success')
        }
        router.push({ name: Issues, params: { projectId: projectId} })
    }
    catch(err){
        if(err?.response?.data?.error){
            toggleNotification(err.response.data.error, 'alert')
        }
        console.log(err)
    }
    finally{
        loading.value = false
    }
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

.input-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-width: 300px;
    padding: 20px;
    row-gap: 15px;
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
    min-width: 250px;
    max-width: 500px;
    min-height: 50px;
}
.header h1, .header h3{
    color:#063970;
    word-break: break-word;
}

.input-group {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-around;
    width: 100%;
    height: 50px;
    min-width: 250px;
    max-width: 500px;
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
    row-gap: 15px;
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
