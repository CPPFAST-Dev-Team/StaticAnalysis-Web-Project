<template>
    <div class="container">
        <div class="header" v-if="!isMobile">
            <h1>Projects of {{username}}</h1>
            <router-link to="/new-project" class="btn-create">Create New</router-link>
        </div>
        <div class="project-wrapper" v-for="project in projects" v-if="!isMobile">
            <Display_project v-bind="project"/>
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

        <div class="pagination-wrapper" v-if="pages.length <= 10">
            <i class="fa fa-caret-left" aria-hidden="true" @click="goToPreviousPage"></i>
            <span
                v-for="page in pages"
                :key="page"
                class="pagination-box"
                :class="{'selected-pagination-box': page === selectedPage}"
                @click="selectPage(page)"
            >
                {{ page }}
            </span>
            <i class="fa fa-caret-right" aria-hidden="true" @click="goToNextPage"></i>
        </div>

        <div class="pagination-wrapper" v-if="pages.length > 10">
            <i class="fa fa-caret-left" aria-hidden="true" @click="goToPreviousPage"></i>
            <span 
                v-for="page in firstPages" 
                :key="page" 
                class="pagination-box" 
                :class="{ 'selected-pagination-box': selectedPage === page }"
                @click="selectPage(page)"
            >
                {{ page }}
            </span>
            <span v-if="selectedPage > 5" class="pagination-box" @click="goToLeftSpread">...</span>
            <span 
                v-if="(selectedPage > 3) && (selectedPage < pages.length-2)"
                v-for="page in middlePages"
                :key="page"
                class = "pagination-box"
                :class = "{'selected-pagination-box': selectedPage === page}"
                @click="selectPage(page)"
            >
                {{ page }}
            </span>
            <span v-if="selectedPage < pages.length-4" class="pagination-box" @click="goToRightSpread">...</span>
            <span 
                v-for="page in lastPages" 
                :key="page" 
                class="pagination-box" 
                :class="{ 'selected-pagination-box': selectedPage === page }"
                @click="selectPage(page)"
            >
                {{ page }}
            </span>
            <i class="fa fa-caret-right" aria-hidden="true" @click="goToNextPage"></i>
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
                username: null,
                selectedPage: 1,
                pages: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
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
            this.getUser()
            this.getProjects()
        },
        computed: {
            firstPages(){
                return this.pages.slice(0, 3)
            },
            middlePages(){
                return this.pages.slice(Math.max(3, this.selectedPage-2), Math.min(this.pages.length-3, this.selectedPage+1))
            },
            lastPages(){
                return this.pages.slice(this.pages.length-3, this.pages.length)
            },
        },
        //backend api call here to get projects
        methods: {
            async getUser(){
                const token = localStorage.getItem('access')
                if(!token)  return
                axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
                await axios
                    .get("/api/auth/info/")
                    .then((response) => {
                        this.username = response.data.username;
                    })
                    .catch((err) => {
                        console.log(err)
                        this.username = null
                    })
            },
            async getProjects(){
                this.projects = projects;
            },
            checkIsMobile() {
                this.isMobile = window.innerWidth < 768;
            },
            selectPage(page) {
                this.selectedPage = page;
            },
            goToPreviousPage() {
                if (this.selectedPage > 1) {
                    this.selectedPage--;
                }
            },
            goToNextPage() {
                if (this.selectedPage < this.pages.length) {
                    this.selectedPage++;
                }
            },
            goToLeftSpread(){
                this.selectedPage = Math.floor((3 + this.selectedPage)/2)
            },
            goToRightSpread(){
                this.selectedPage = Math.ceil((this.selectedPage + this.pages.length-2)/2)
            }
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