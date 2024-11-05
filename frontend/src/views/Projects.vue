<template>
    <div class="container">
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

<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
    .container{
    height: 30vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 50px;
    }
    h1{
        font-size: clamp(1rem, 5%, 3rem);
        font-family: 'DM Sans', sans-serif;
        color: #063970;
    }
</style>