<template>
    <div class="container">
        <div class="header">
        <h1>Github.com/example</h1>
        <button class="btn-filter">Filter</button>
        <router-link to="/new-scan" class="btn-scan">New Scan</router-link>
    </div>

    <Issue
        fileName="File.cpp"
        :line="123"
        errorText="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate..."
        :confidence="95"
    />
    <Issue
        fileName="File.java"
        :line="456"
        errorText="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate..."
        :confidence="52"
    />
    </div>
</template>

<script>
import Issue from '../components/Display_issue.vue'
    export default{
        components: {
            Issue 
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
.header h1, .header button, .header a{
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 25px;
}
h1{
    color: #063970;
    font-size: 30px;
    font-family: 'DM Sans', sans-serif;
}
.btn-filter, .btn-scan{
    height: 30%;
    width: 10%;
    min-width: 100px;
    border: 1px solid #063970;
    border-radius: 10px;
    font-size: 1rem;
}
.btn-filter{
    background-color: #063970;
    color: white;
}
.btn-scan{
    background-color: white;
    color: #063970;
}
</style>
