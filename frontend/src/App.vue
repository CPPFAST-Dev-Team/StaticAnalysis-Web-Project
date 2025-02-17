<script setup>
  import Navbar from './components/Navbar.vue'
  import { reactive, provide } from 'vue';
  import axios from 'axios'

  const token = localStorage.getItem('access')
  if(token){
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
  }

  provide('toggleNotification', toggleNotification)
  const notification = reactive({ //state variable to handle notifications, use through toggleNotification(*message, *type of notification, alert or message)
      show: false,
      class: '',
      message: '',
  })
  function toggleNotification(message, className){ //function to toggle a notification for three seconds
      notification.show = true
      notification.class = className
      notification.message = message

      setTimeout(() => (notification.show = false), 3000)
  }
</script>

<template>
  <div class="wrapper">
    <Navbar/>
    <div class="main">
      <router-view/>
    </div>
  </div>
  <div class="notification-container">
    <div :class="notification.class" v-if="notification.show"> <!--dynamically assign class of div element and render based on show property of notification-->
        <i class="fa fa-exclamation-circle" aria-hidden="true"></i>
        <text class="alert-text">{{notification.message}}</text>
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
  .main{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    width: 100vw;
    height: calc(100vh - 50px);
  }
  .notification-container{
    position: fixed;
    top: 20vh;
    width: 100vw;
    display: flex;
    justify-content: center;
    z-index: 100;
  }
  .alert, .success{
    display: flex;
    align-items: center;
    height: fit-content;
    box-sizing: border-box;
    padding: 0px 10px 0px 10px;
    width: 100%;
    max-width: 300px;
    background-color: #FFCCCB;
    border: 1px solid red;
    opacity: 0.75;
  }
  .alert i, .success i{
    margin-right: 10px;
  }
  .alert text, .success text{
    color: darkslategrey;
    font-size: 20px;
  }
  .success{
    background-color: #0fb36f;
    border: 1px solid green;
  }

</style>

