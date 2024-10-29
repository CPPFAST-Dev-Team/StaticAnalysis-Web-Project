<template>
  <div class="box">
    <div class="left">
      <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png">
      <h2>{{ githubUrl }}</h2>
    </div>

    <div class="center">
      <div class="innerBox">
        <h3>Issues: </h3>
        <div class="btn-group">
          <button class="btn-red"><text>{{ issueRed }}</text></button>
          <button class="btn-yellow"><text>{{ issueYellow }}</text></button>
          <button class="btn-blue"><text>{{ issueBlue }}</text></button>
        </div>
      </div>
    </div>

    <div class="right">
      <button class="btn-view"><text>Open</text></button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Display_project",
  props: {
    githubUrl: {
      type: String,
      required: true
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
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

.box {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  overflow: hidden;
  width: 80vw;
  height: 20vw;
  border: 1px solid black;
  padding: 10px;
  margin: 10px;
  border-radius: 50px;
  font-family: 'DM Sans', sans-serif; /* Apply DM Sans to the whole box */
}

.left, .center, .right, .innerBox, h2, h3, button {
  font-family: 'DM Sans', sans-serif; /* Ensure DM Sans applies to all inner elements */
}

.innerBox {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  overflow: hidden;
  width: 100%;
  height: 60%;
  border: 1px solid black;
  padding: 10px;
  border-radius: 20px;
}

.left {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 35%;
  height: 100%;
  padding: 5px;
  border: 1px solid transparent;
  border-radius: 15px;
}

.center {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50%;
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
  height: 20%;
  width: 15%;
  margin-right: 5%;
}

h2 {
  font-size: 2vw;
}

h3 {
  font-size: 1.5vw;
  margin: 10px;
}

.btn-group {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 50%;
  width: 100%;
}

.btn-group button {
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
  width: 100%;
  border-radius: 10px;
  cursor: pointer;
}

.btn-group button:hover, .btn-view:hover {
  opacity: 0.8;
}

text {
  margin: 5px;
  font-size: 1.5vw;
}

</style>
