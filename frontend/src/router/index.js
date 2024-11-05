import { createRouter, createWebHistory} from 'vue-router'

import Projects from '../views/Projects.vue'
import Issues from '../views/Issues.vue'
import New_Project from '../views/New_Project.vue'

const routes = [
    {
        path: '/projects',
        name: 'Projects',
        component: Projects
    },
    {
        path:'/issues',
        name:'Issues',
        component: Issues
    },
    {
        path:'/new-project',
        name:'New_Project',
        component: New_Project
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
