<template>
    <div class="container">
        <div class="header" v-if="!isMobile">
            <h1>Projects</h1>
            <router-link to="/new-project" class="btn-create">Create New</router-link>
        </div>
        <div class="project-wrapper" v-for="project in projects" v-if="!isMobile">
            <Display_project v-bind="project"/>
        </div>

        <div class="header-mobile" v-if="isMobile">
            <h1>Projects</h1>
            <router-link to="/new-project" class="btn-create">Create New</router-link>
        </div>
        <div class="project-wrapper-mobile" v-for="project in projects" v-if="isMobile">
            <Display_project_mobile v-bind="project"/>
        </div>
    </div>
    
</template>

<script>
    import Display_project from '../components/Display_project.vue'
    import Display_project_mobile from '@/components/Display_project_mobile.vue';
    import {projects} from "../projectsData.js"
    import axios from 'axios'
    export default{
        data(){
            return {
                isMobile: false,
                projects: [],
                // parameters: 
                // giithubUrl
                // imgSrc
                // issueRed
                // issueYellow
                // issueBlue
            }
        },
        mounted(){
            this.checkIsMobile();
            window.addEventListener('resize', this.checkIsMobile);
        },
        beforeUnmount() {
            window.removeEventListener('resize', this.checkIsMobile);
        },
        created(){
            this.getProjects()
        },
        //backend api call here to get projects
        methods: {
            async getProjects(){
                this.projects = projects;
            },
            checkIsMobile() {
                this.isMobile = window.innerWidth < 768;
            },
        },
        components: {
            Display_project,
            Display_project_mobile
        }
    }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
    .container{
        position: relative;
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        padding: 25px;
    }
    .project-wrapper{
        display: flex;
        justify-content: center;
        width: 100%;
        min-width: 800px;
        max-width: 2400px;
    }
    .project-wrapper-mobile{
        display: flex;
        justify-content: center;
        width: 100%;
    }
    .header{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        width: 90%;
        height: 10%;
        min-width: 800px;
        min-height: 100px;
        max-width: 1200px;
        max-height: 300px;
    }
    .header-mobile{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        width: 300px;
        height: 50px;
        margin: 25px;
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
</style>