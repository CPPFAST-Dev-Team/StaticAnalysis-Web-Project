<template>
    <div class="container">
        <div class="header">
            <h1>Projects</h1>
            <router-link to="/new-project" class="btn-create">Create New</router-link>
        </div>
        <Display_project
        githubUrl="Github.com/example"
        :issueRed="1234"
        :issueYellow="5678"
        :issueBlue="9000"
        />

        <Display_project
        githubUrl="Github.com/repo"
        :issueRed="1234"
        :issueYellow="5678"
        :issueBlue="9000"
        />
    </div>
    
</template>

<script>
    import Display_project from '../components/Display_project.vue'
    import Navbar from '../components/Navbar.vue'
    export default{
        components: {
            Display_project
        }
    }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
    .container{
        position: relative;
        height: 100%;
        width: 100%;
        min-height: 200px;
        max-height: 1200px;
        min-width: 800px;
        max-width: 2400px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        padding: 50px;
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
        border: 1px solid #063970;
        border-radius: 10px;
        background-color:#063970;
        color: white;
        font-size: 1rem;
        cursor: pointer;
    }
</style>