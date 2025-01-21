<template>
  <div class="box">
    <div class="left">
      <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png">
      <a href="https://www.github.com"><h2>{{ githubUrl }}</h2></a>
    </div>
 
 
    <div class="center">
      <div class="innerBox">
        <h3>Issues: </h3>
        <div class="btn-group">
          <router-link to="/issues" class="btn-red"><text>{{ issueRed }}</text></router-link>
          <router-link to="/issues" class="btn-yellow"><text>{{ issueYellow }}</text></router-link>
          <router-link to="/issues" class="btn-blue"><text>{{ issueBlue }}</text></router-link>
        </div>
      </div>
    </div>
 
 
    <div class="right">
      <router-link to="/issues" class="btn-view">
        <text>Open</text>
      </router-link>
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
  flex-direction: row;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  width: 90%;
  height: 20%;
  min-width: 800px;
  min-height: 200px;
  max-width: 1200px;
  max-height: 300px;
  border: 1px solid #063970;
  padding: 10px;
  margin: 10px;
  border-radius: 50px;
  font-family: 'DM Sans', sans-serif;
}
 
 
 .left, .center, .right, .innerBox, h2, h3, button, a {
  font-family: 'DM Sans', sans-serif;
 }

 h2, h3{
  color: black;
 }
 
 
 .innerBox {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  overflow: hidden;
  width: 100%;
  height: 60%;
  border: 1px solid #063970;
  padding: 10px;
  border-radius: 20px;
 }
 
 
 .left {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  width: 30%;
  height: 100%;
  border: 1px solid transparent;
  border-radius: 15px;
  padding: 16px;
 }
 
 
 .center {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 55%;
  height: 100%;
  margin: 0;
  padding: 5px;
  border: 1px solid transparent;
  border-radius: 15px;
 }
 
 
 .right {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 15%;
  height: 100%;
  margin: 0;
  padding: 5px;
  border: 1px solid transparent;
  border-radius: 15px;
 }
 
 
 img {
  display: block;
  width: 20%;
  height: auto;
 }
 
 
 .btn-group {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 50%;
  width: 100%;
 }
 
 
 .btn-group button, .btn-group a {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  height: 100%;
  width: 40%;
  border: 1px solid black;
  cursor: pointer;
  margin-right: 10px;
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
 
 
 .btn-group:after {
  content: "";
  clear: both;
  display: table;
 }
 
 
 .btn-view {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #063970;
  color: white;
  height: 15%;
  width: 80%;
  border-radius: 10px;
  cursor: pointer;
 }
 
 
 .btn-group button:hover, .btn-group a:hover, .btn-view:hover {
  opacity: 0.8;
 }

 a h2:hover{
  text-decoration: underline;
 }
 
 
 h2 {
  font-size: clamp(1rem, 5%, 3rem);
  margin: 10px;
  word-break: break-word;
 }


  h3 {
  font-size: clamp(1rem, 2%, 1rem);
  margin: 10px;
 }


  text {
    font-size: clamp(0.8rem, 1%, 1rem);
  }
 
 
 </style>
 