<template>
    <div class="box">
        <div class="header">
            <h3>Potential Buffer Overflow</h3>
            <div class="subheader">
                <!-- issue and severity require props -->
                <h5>{{ fileName }}</h5>
                <h5>Line: {{ line }}</h5>
                <h5>Confidence: {{ confidence }}%</h5>
            </div>
        </div>

        <div class="body-wrapper">
            <div class="btn-row">
                <button class="btn-red">{{ issueName }}</button>
                <button class="btn-red">Severity: High</button>
            </div>

            <div class="body-wrapper-columns">
                <p>{{ errorText }}</p>
                <div class="btn-column">
                    <button class="btn-white">Why?</button>
                    <button class="btn-blue">View</button>
                </div>
            </div>
        </div>
    </div>
   </template>
   
   
   <script setup>
   // Define props
   defineProps({
     fileName: {
       type: String,
       required: true,
     },
     issueName: {
       type: String,
       required: true,
     },
     line: {
       type: Number,
       required: true,
     },
     errorText: {
       type: String,
       required: true,
     },
     confidence: {
       type: Number,
       required: true,
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
width: 300px;
height: 300px;
border: 1px solid #063970;
padding: 10px;
margin: 10px;
border-radius: 20px;
font-family: 'DM Sans', sans-serif;
box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}  
.header{
display: flex;
flex-direction: column;
justify-content: flex-start;
align-items: center;
width: 100%;
height: 25%;
padding: 5px;
border-bottom: 1px solid #063970;
}
.subheader{
display: flex;
flex-direction: row;
justify-content: space-evenly;
align-items: center;
width: 100%;
overflow-x: auto;
overflow-y: hidden;
white-space: nowrap;
}
.subheader h5{
margin-right: 10px;
}
.body-wrapper{
display: flex;
flex-direction: column;
justify-content: flex-start;
align-items: center;
height: 75%;
width: 100%;
}
.body-wrapper-columns{
display: flex;
flex-direction: row;
height: 70%;
}
.btn-row {
display: flex;
flex-direction: row;
justify-content: space-evenly;
align-items: space-between;
height: 10%;
width: 100%;
margin-top: 10px;
margin-bottom: 10px;
}
.btn-row button, .btn-row a {
display: flex;
justify-content: center;
align-items: center;
border-radius: 5px;
height: 100%;
width: 45%;
border: 1px solid black;
cursor: pointer;
}
.btn-red {
background-color: #E51400;
color: white;
}
.body-wrapper-columns p{
display: flex;
align-items: flex-start;
width: 70%;
overflow-y: auto;
padding: 5px;
font-size: 10px;
}
.btn-column{
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
height: 100%;
width: 30%;
padding: 5px;
}
.btn-column button, .btn-columns a{
height: 20%;
width: 100%;
border-radius: 5px;
margin-bottom: 10px;
}
.btn-white{
background-color: white;
color: #063970;
}
.btn-blue{
background-color: #063970;
color: white;
}


h3, button, a {
font-family: 'DM Sans', sans-serif;
}
h3{
color: #063970;
font-size: 20px;
}
text {
font-size: clamp(0.8rem, 1%, 1rem);
}
</style>
   