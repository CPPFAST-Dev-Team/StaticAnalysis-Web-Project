<script setup>
    import { onMounted } from 'vue';
    import api from '@/api';

    function loginWithGithub() {
        const clientId = import.meta.env.VITE_OAUTH_CLIENT_ID;
        const redirectUri = import.meta.env.VITE_OAUTH_REDIRECT_URI
        const githubAuthUrl = `https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${encodeURIComponent(
            redirectUri
        )}&scope=repo%20user`;
        window.location.href = githubAuthUrl;
    }

    // Access url params on mount and hit backend to exchange code for token
    onMounted(async () => {
        const urlParams = new URLSearchParams(window.location.search);
        const code = urlParams.get('code');
        if (!code) {
            return
        }
        console.log(code)
        try{
            const res = await api.post('/users/github/', { code: code });
            console.log(res.data)
        }
        catch(err){
            console.error(err)
        }
    });

</script>

<template>
    <button @click="loginWithGithub">
        <i class="fa fa-github"></i>
        Login with Github
    </button>
</template>

<style scoped>
button{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 10px 20px;
    width: 100%;
    column-gap: 10px;
    background-color: white;
    color: var(--primary);
    font-size: 1rem;
    border: 1px solid black;
    border-radius: 10px;
}
button:hover{
    cursor: pointer;
}
i{
    font-size: 1.2rem;
}
</style>