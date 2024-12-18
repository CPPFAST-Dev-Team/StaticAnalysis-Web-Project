<script>
import Navbar from './components/Navbar.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    Navbar,
  },
  beforeCreate(){
    const token = localStorage.getItem('token')
    if(token){
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  }
}
</script>

<template>
  <div class="wrapper">
    <div class="nav">
      <Navbar/>
    </div>
    <div class="main">
      <router-view/>
    </div>
    </div>
</template>

<style scoped>
.wrapper{
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  flex-direction: column;
}
.nav{
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  width: 100vw;
  height: 5vh;
}
.main{
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  width: 100vw;
  height: 95vh;
}

</style>

