<template>
  <div class="box">
    <div class="left">
      <h2>Issue</h2>
      <h2>{{fileName}}</h2>
      <h2>Line: {{line}}</h2>
    </div>
    <div class="center">
      <div class="btn-group">
        <button class="btn-red"><text>CWE-123456</text></button>
        <button class="btn-red"><text>Severity: High</text></button>
      </div>
      <div class="text-space">
        <text>{{ errorText }}</text>
      </div>
    </div>
    <div class="right">
      <div class="btn-group">
        <button class="btn-blue"><text>Confidence: {{ confidence }}%</text></button>
        <button class="btn-white"><text>Why?</text></button>
      </div>
      <button class="btn-view"><text>View</text></button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Display_issue",
  props:{
      fileName:{
          type: String,
          required: true,
      },
      line:{
          type: Number,
          required: true,
      },
      errorText:{
          type: String,
          required: true,
      },
      confidence:{
          type: Number,
          required: true,
      },
  }
}
</script>

 <style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
.container{
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}
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
 .left, .center, .right {
  font-family: 'DM Sans', sans-serif;
}
 h2, h3, button, .text-space, .btn-view {
  font-family: 'DM Sans', sans-serif;
}
 .left {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  width: 15%;
  height: 100%;
  margin: 0;
  padding: 5px;
  border: 1px solid transparent;
  border-radius: 15px;
}
 .center {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 60%;
  height: 100%;
  margin: 5px;
  padding: 5px;
  border: 1px solid transparent;
  border-radius: 15px;
}
 .right {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 25%;
  height: 100%;
  margin: 0;
  padding: 5px;
  border: 1px solid transparent;
  border-radius: 15px;
}
 .btn-group {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  height: 50%;
  width: 60%;
  margin-right: 10px;
  margin-bottom: 10px;
}
 .btn-group button {
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  height: 50%;
  width: 100%;
  border: 1px solid black;
  padding: 10px;
  cursor: pointer;
  margin: 5px;
  margin-right: 20px;
  white-space: nowrap;
  text-align: center;
}
 .btn-red {
  background-color: #E51400;
  border-color: darkred;
  color: white;
}
 .btn-blue {
  background-color: #063970;
  border-color: black;
  color: white;
}
 .btn-white {
  background-color: white;
  border-color: transparent;
  color: black;
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
 .btn-group button:hover, .btn-view:hover {
  opacity: 0.8;
}
 .text-space {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 10px;
  height: 100%;
  width: 130%;
  overflow:auto;
}
h2 {
font-size: clamp(1rem, 2%, 1rem);
margin: 10px;
}


h3 {
  font-size: clamp(1rem, 2%, 1rem);
  margin: 10px;
}


text {
  font-size: clamp(0.8rem, 1%, 1rem);
}
 </style>