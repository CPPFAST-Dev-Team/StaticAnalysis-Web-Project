import { createRouter, createWebHistory} from 'vue-router'

import Projects from '../views/Projects.vue'
import Issues from '../views/Issues.vue'
import New_Project from '../views/New_Project.vue'
import Login from '../views/Login.vue'
import New_Scan from '../views/New_Scan.vue'

const routes = [
    {
        path:'/',
        name: 'Login',
        component: Login,
    },
    {
        path: '/projects',
        name: 'Projects',
        component: Projects
    },
    {
        path:'/issues/',
        name:'Issues',
        component: Issues,
    },
    {
        path:'/new-project',
        name:'New_Project',
        component: New_Project
    },
    {
        path:'/new-scan',
        name:'New_Scan',
        component: New_Scan
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
