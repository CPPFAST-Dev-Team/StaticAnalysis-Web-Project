<template>
  <div class="box">
    <div class="left">
      <h2>Issue</h2>
      <h2>{{fileName}}</h2>
      <h2>Line: {{line}}</h2>
    </div>
    <div class="center">
      <div class="btn-group">
        <button class="btn-red"><text>{{ issueName }}</text></button>
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
  flex-direction: row;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  height: 200px;
  width: 100%;
  border: 1px solid #063970;
  padding: 10px;
  border-radius: 50px;
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

/* button styles */
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
/* issues high, medium, and low */
.btn-group .btn-red { 
  background-color: #E51400;
  border-color: darkred;
  color: white;
}
.btn-group .btn-yellow {
  background-color: #FFFF66;
  color: black;
}
.btn-group .btn-blue {
  background-color: #063970;
  border-color: black;
  color: white;
}
.btn-group .btn-white {
  background-color: white;
  border-color: #063970;
  color: black;
}
/* separate smaller button for opening issue */
.btn-view {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #063970;
  color: white;
  height: 15%;
  width: 30%;
  border-radius: 5px;
  cursor: pointer;
}
.btn-group button:hover, .btn-view:hover {
  opacity: 0.8;
}

/* text area */
.text-space {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 10px;
  height: 100%;
  width: 130%;
  overflow:auto;
}

/* text styles */
h2 {
  display: inline-block;
  font-size: clamp(1rem, 2%, 1rem);
  margin: 10px;
  margin-right: 5px;
  margin-left: 5px;
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