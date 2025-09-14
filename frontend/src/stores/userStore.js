import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('user', () => {
    const username = ref('')
    const access = ref('')

    function setUsername(name){
        username.value = name
    }
    function setAccess(token){
        access.value = token
    }
    function isAuthenticated(){
        if(!access.value) return false;

        const payload = JSON.parse(atob(access.value.split(".")[1]));
        const expirationTime = payload.exp * 1000

        // Check if the token is expired
        if(Date.now() >= expirationTime){
            clearUser()
            return false
        }

        return Date.now() < expirationTime
    }
    function clearUser(){
        username.value = ''
        access.value = ''
    }

    return {
        username, access,
        setUsername, setAccess,
        isAuthenticated, clearUser
    }
}, {
    persist: {
        key: 'userStore',
        storage: localStorage
    }
})