<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <div class="navbar">
        <div class="left">
            <span>Code Assessor</span>
        </div>

        <div class="right">
            
            <div class="dropdown">
                <button class="dropbtn">
                    <i class="fa fa-bars"></i>
                </button>
                <div class="dropdown-content">
                    <router-link to="/projects">Projects</router-link>
                    <router-link to="/issues">Issues</router-link>
                    <router-link to="/new-project">New Project</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

.navbar {
    display: flex;
    flex-direction: row;
    width: 100%;
    background-color: white;
    border-top: 2px solid #063970;
    border-bottom: 2px solid #063970;
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    padding: 10px 0;
}

.navbar .left {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 50%;
    margin-left: 10px;
}

.navbar .right {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    width: 50%;
    margin-right: 10px;
}

.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown .dropbtn {
    font-size: 16px;
    border: none;
    outline: none;
    color: #063970;
    padding: 8px 16px;
    background-color: inherit;
    font-family: inherit;
    cursor: pointer;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1000;

    right: 0;
}

.dropdown-content a, .dropdown-content router-link {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
}

.dropdown-content a:hover {
    background-color: #ddd;
}

.dropdown:hover .dropdown-content {
    display: block;
}

.navbar span {
    font-family: 'DM Sans', sans-serif;
    font-size: clamp(1rem, 10%, 3rem);
    color: #063970;
}
</style>

<script>
export default {
    name: "Navbar",
};
</script>
