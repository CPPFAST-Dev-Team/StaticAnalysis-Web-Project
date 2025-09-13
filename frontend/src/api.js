import axios from 'axios'
import { isAuthenticated, refreshToken } from "./router";
import { useUserStore } from './stores/userStore';
import router from "./router"

const api = axios.create({
    baseURL: import.meta.env.VITE_BACKEND_URL
})

api.interceptors.request.use(
    async (config) => {
      const userStore = useUserStore()
      const token = localStorage.getItem('access') || userStore.access;
      if (isAuthenticated()) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      // Temporarily disabled refresh logic for testing
      // else {
      //   try{
      //       const refreshed = await refreshToken();
      //       if (!refreshed) {
      //           router.push("/");  
      //           return Promise.reject("Token refresh failed, redirecting.");
      //       }
      //       const newToken = localStorage.getItem('access');
      //       config.headers.Authorization = `Bearer ${newToken}`;
      //   }
      //   catch(err){
      //       console.log(err)
      //       return Promise.reject(err)
      //   }
      // }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

export default api