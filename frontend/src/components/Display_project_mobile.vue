<template>
    <div class="box">
        <div class="header">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png">
            <h3>{{githubUrl}}</h3>
        </div>

        <div class="issues-wrapper">
            <h2>Issues</h2>
            <div class="btn-group">
                <router-link to="/issues" class="btn-red"><text>{{ issueRed }}</text></router-link>
                <router-link to="/issues" class="btn-yellow"><text>{{ issueYellow }}</text></router-link>
            </div>
            <div class="btn-group">
                <router-link to="/issues" class="btn-blue"><text>{{ issueBlue }}</text></router-link>
                <router-link to="/issues" class="btn-view"><text>View All</text></router-link>
            </div>
        </div>
    </div>
   </template>
   
<script setup>
// Define props
  defineProps({
    githubUrl: {
      type: String,
      required: true
    },
    imgSrc:{
      type: String,
      required: true,
    },
    issueRed: {
      type: Number,
      required: true
    },
    issueYellow: {
      type: Number,
      required: true
    },
    issueBlue: {
      type: Number,
      required: true
    },
  });
</script>
   
   
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
.box {
display: flex;
flex-direction: column;
justify-content: flex-start;
align-items: flex-start;
overflow: hidden;
width: 30px;
height: 50px;
min-width: 300px;
min-height: 200px;
max-width: 500px;
max-height: 800px;
border: 1px solid #063970;
padding: 10px;
margin: 10px;
border-radius: 20px;
font-family: 'DM Sans', sans-serif;
box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}  
.header{
display: flex;
flex-direction: row;
justify-content: flex-start;
align-items: center;
width: 100%;
height: 25%;
border-bottom: 1px solid #063970;
overflow-x: auto;
overflow-y: hidden;
white-space: nowrap;
}
.issues-wrapper{
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
width: 100%;
height: 75%;
}
.btn-group {
display: flex;
flex-direction: row;
justify-content: space-evenly;
align-items: space-between;
height: 50%;
width: 100%;
padding: 10px;
}
img {
display: block;
width: 10%;
height: auto;
margin: 10px;
}
.btn-group button, .btn-group a {
display: flex;
justify-content: center;
align-items: center;
border-radius: 5px;
height: 100%;
width: 40%;
border: 1px solid black;
cursor: pointer;
}
.btn-red {
background-color: #E51400;
color: white;
}
.btn-yellow {
background-color: #FFFF66;
color: black;
}
.btn-blue {
background-color: #063970;
color: white;
}
.btn-view {
display: flex;
align-items: center;
justify-content: center;
background-color: #063970;
color: white;
height: 15%;
width: 30%;
border-radius: 10px;
cursor: pointer;
}
h3, button, a {
font-family: 'DM Sans', sans-serif;
}
h3{
color: #063970;
}
h2 {
font-size: clamp(1.25rem, 5%, 3rem);
margin: 5px;
word-break: break-word;
color: #063970
}
text {
font-size: clamp(0.8rem, 1%, 1rem);
}
</style>
   