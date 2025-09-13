import { createRouter, createWebHistory} from 'vue-router'

import Projects from '../views/Projects.vue'
import Issues from '../views/Issues.vue'
import New_Project from '../views/New_Project.vue'
import Login from '../views/Login.vue'
import New_Scan from '../views/New_Scan.vue'
import axios from 'axios'

const routes = [
    {
        path:'/',
        name: 'Login',
        component: Login,
    },
    {
        path: '/projects/',
        name: 'Projects',
        component: Projects
    },
    {
        path:'/issues/:projectId/',
        name:'Issues',
        component: Issues,
    },
    {
        path:'/new-project/',
        name:'New_Project',
        component: New_Project
    },
    {
        path:'/new-scan/:projectId',
        name:'New_Scan',
        component: New_Scan
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export function isAuthenticated(){
    const access = localStorage.getItem("access");
    if(!access) return false;

    const payload = JSON.parse(atob(access.split(".")[1]));
    const expirationTime = payload.exp * 1000

    return Date.now() < expirationTime
}

export async function refreshToken(){
    const refresh = localStorage.getItem("refresh");
    if(!refresh){
        localStorage.removeItem('access')
        localStorage.removeItem('refresh')
        return false;
    }
    try {
        const res = await axios.post("api/auth/token/refresh/", { refresh });
        const access = res.data.access;
        localStorage.setItem("access", access);
        axios.defaults.headers.common["Authorization"] = `Bearer ${access}`
        return true;
    } catch (err) {
        console.error({ 'Error': err });
        localStorage.removeItem('access');
        localStorage.removeItem('refresh');
        return false;
    }
}

router.beforeEach(async (to, from) => {
    if (to.name === "Login") 
    {
      return true;
    }

    // TODO: Refactor to account for github auth
    // if(!isAuthenticated()){
    //     const refreshed = await refreshToken();
    //     console.log({'refreshed': refreshed})
    //     if(refreshed){
    //         return true;
    //     }
    //     if(!refreshed){
    //         console.log("We are returning to login")
    //         return {name: "Login"}
    //     }
    // }
    return true;
  })

export default router
