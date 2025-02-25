<template>
    <div class="box">
        <div class="header">
            <h3>Potential Buffer Overflow</h3>
            <div class="subheader">
                <!-- issue and severity require props -->
                <h5>{{ file_location }}</h5>
                <h5>Line: {{ line }}</h5>
                <h5>Confidence: {{ confidenceAsPercentage }}%</h5>
            </div>
        </div>

        <div class="body-wrapper">
            <div class="btn-row">
                <button :class="getIssueButton">{{ name }}</button>
                <button :class="getIssueButton">Severity: {{ severity }}</button>
            </div>

            <div class="body-wrapper-columns">
              <div>
                <p>{{ summary }}</p>
              </div>
              <div>
                <div class="btn-column">
                    <button class="btn-white">Why?</button>
                    <button class="btn-blue">View</button>
                </div>
              </div>
            </div>
        </div>
    </div>
   </template>
   
   
   <script setup>
    import { computed } from 'vue'
    // Define props
    const props = defineProps({
      id: {
        type: Number,
        required: true
      },
      name: {
        type: String,
        required: true,
      },
      file_location: {
        type: String,
        required: true,
      },
      line: {
        type: Number,
        required: true,
      },
      summary: {
        type: String,
        required: true,
      },
      severity: {
        type: String,
        required: true
      },
      confidence: {
        type: String,
        required: true,
      },
    });
 
   const getIssueButton = computed(() => {
     if (props.severity === "SEVERE") {
       return 'btn-red';
     } else if (props.severity === "MEDIUM") {
       return 'btn-yellow';
     } else {
       return 'btn-blue';
     }
   });
 
   const confidenceAsPercentage = computed(() => {
     return `${parseFloat(props.confidence) * 100}%`
   })
 </script>
   
   
   
<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
  .box {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    width: 100%;
    min-height: 200px;
    border: 1px solid #063970;
    padding: 10px;
    border-radius: 20px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    overflow: hidden;
    font-family: 'DM Sans', sans-serif;
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
    width: 100%;
  }
  .body-wrapper-columns div{
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 50%;
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
  .btn-yellow {
    background-color: yellow;
    border: 1px solid gray;
    color: black;
  }
  .body-wrapper-columns p{
    display: flex;
    justify-content: center;
    align-items: flex-start;
    width: 100%;
    overflow-y: auto;
    padding: 5px;
    font-size: 10px;
  }
  .btn-column{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100%;
    width: 100%;
    min-width: 100px;
    padding: 5px;
  }
  .btn-column button, .btn-column a{
    height: fit-content;
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
   