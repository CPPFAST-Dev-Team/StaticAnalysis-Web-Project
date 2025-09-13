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

        if(Date.now() < expirationTime){
            clearUser()
            return true
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