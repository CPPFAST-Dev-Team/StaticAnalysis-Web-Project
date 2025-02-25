<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <div class="container" v-if="projects.length>0">
        <div class="header">
            <h1>Projects</h1>
            <router-link to="/new-project" class="btn-create">Create New</router-link>
        </div>
        <div class="project-wrapper" v-for="project in projects">
            <!-- dynamically assign component based on isMobile -->
            <component
                :is="projectComponent"
                v-bind="project" 
                @delete="getProjects"
            />
        </div>
        <br/>
    </div>
    <div class="empty-container" v-else>
        <text class="empty">No Projects Yet</text>
        <br/>
        <FontAwesomeIcon size="5x" color="#063970" icon="fa-solid fa-face-sad-tear" />
        <br/>
        <router-link to="/new-project" class="btn-start-project">Create First Project</router-link>
    </div>
    
</template>

<script setup>
    import Display_project from '../components/Display_project.vue'
    import Display_project_mobile from '@/components/Display_project_mobile.vue';
    import api from '../api'

    import { ref, computed, onMounted, onUnmounted } from 'vue'

    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
    import { fas } from '@fortawesome/free-solid-svg-icons'
    import { library } from '@fortawesome/fontawesome-svg-core'

    // Add icons to the library
    library.add(fas)


    const projects = ref([])
    const isMobile = ref(window.innerWidth < 768)
    const projectComponent = computed(() => isMobile.value ? Display_project_mobile : Display_project) //dynamically compute component based on isMobile

    onMounted(() => {
        projects.value = getProjects()
        window.addEventListener('resize', updateIsMobile) //add event listener to check if width is mobile
    })
    onUnmounted(() => {
        window.removeEventListener('resize', updateIsMobile)//remove event listener
    })

    function updateIsMobile(){
        isMobile.value = window.innerWidth < 768;
    }

    async function getProjects(){
        const projectsResponse = await api.get("api/projects/")
        let temp = []
        console.log(projectsResponse.data)
        for (const project of projectsResponse.data){
            const vulnerabilities = await api.get(`api/projects/${project.id}/vulnerabilities/`)
            
            const { SEVERE: high_vulnerabilities = 0, MEDIUM: medium_vulnerabilities = 0, LOW: low_vulnerabilities = 0 } =
                vulnerabilities.data.reduce((acc, vulnerability) => {
                    acc[vulnerability.severity] = (acc[vulnerability.severity] || 0) + 1;
                    return acc;
                }, {});
                
            temp.push({
                ...project,
                high_vulnerabilities,
                medium_vulnerabilities,
                low_vulnerabilities,
            })
        }
        projects.value = temp;
    }

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
    .container{
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 100%;
        max-width: 1200px;
        padding: 25px;
    }
    .project-wrapper{
        margin-bottom: 20px;
    }
    .header{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        height: 10%;
        min-height: fit-content;
        margin-bottom: 20px;
    }
    @media(max-width: 767px){
        .header{
            justify-content: center;
        }
    }
    .header h1, .header button{
        margin-right: 25px;
    }
    h1{
        color: #063970;
        font-size: 30px;
        font-family: 'DM Sans', sans-serif;
    }
    .btn-create{
        display: flex;
        align-items: center;
        justify-content: center;
        height: 30%;
        width: 20%;
        min-width: 150px;
        max-width: 300px;
        min-height: 25px;
        border: 1px solid #063970;
        border-radius: 10px;
        background-color:#063970;
        color: white;
        font-size: 1rem;
        cursor: pointer;
    }
    .btn-create:hover{
        opacity: 0.8;
    }

    .empty-container{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: fit-content;
        height: 100%;
        max-width: 1200px;
        padding: 25px;
    }
    .empty{
        text-align: "center";
        color: #063970;
        font-size: 2rem;
        font-family: 'DM Sans', sans-serif;
    }
    .btn-start-project{
        height: "fit-content";
        max-width: "500px";
        padding: 10px 10px 10px 10px;
        border-radius: 5px;
        background-color:#063970;
        color: white;
        font-size: 1rem;
        cursor: pointer;
    }
    .btn-start-project:hover{
        opacity: 0.5;
    }

    .pagination-wrapper{
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        min-height: 75px;
        width: 100%;
    }
    .pagination-box, .selected-pagination-box{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 20px;
        width: 30px;
        margin-right: 10px;
        border: 1px solid #063970;
    }
    .selected-pagination-box{
        background-color: #063970;
        color: white;
    }
    .pagination-spread{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-right: 10px;
    }
    .pagination-wrapper i{
        color: #063970;
        margin-right: 10px;
    }
    .pagination-box:hover, .pagination-spread:hover, .pagination-wrapper i:hover{
        cursor: pointer;
    }
    .pagination-box:hover{
        background-color: lightgray;
    }
</style>