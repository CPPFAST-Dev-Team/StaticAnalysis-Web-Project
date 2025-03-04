<script setup>
  import Navbar from './components/Navbar.vue'
  import { reactive, provide } from 'vue';
  import axios from 'axios'

  const token = localStorage.getItem('access')
  if(token){
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
  }

  provide('toggleNotification', toggleNotification)
  provide('showConfirm', showConfirm)
  const notification = reactive({ //state variable to handle notifications, use through toggleNotification(*message, *type of notification, alert or message)
      show: false,
      class: '',
      message: '',
  })
  function toggleNotification(message, className){ //function to toggle a notification for three seconds
    notification.show = true
    notification.class = className
    notification.message = message

    setTimeout(() => {
      notification.show = false
    }, 3000);
  }

  const confirm = reactive({
    show: false,
    message: 'Are you sure you want to delete this project?',
    action: 'Delete',
    handler: null,
  })
  function showConfirm({ message, action, handler }){
    confirm.show = true
    confirm.message = message
    confirm.action = action
    confirm.handler = handler
  }
  function handleConfirmation(){
    confirm.handler()
    confirm.show=false
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
      <Transition name="notification">
        <div :class="notification.class" v-if="notification.show"> <!--dynamically assign class of div element and render based on show property of notification-->
            <i class="fa fa-exclamation-circle" aria-hidden="true"></i>
            <text class="alert-text">{{notification.message}}</text>
        </div>
      </Transition>
  </div>
  <div class="confirm-overlay" v-if="confirm.show">
    <div class="confirm-container">
      <div class="confirm-popup"> <!--dynamically assign class of div element and render based on show property of notification-->
          <div class="confirm-header">
            <text class="confirm-message">{{ confirm.message }}</text>
          </div>
          <div class="confirm-btn-group">
            <button class="btn-confirm" @click="handleConfirmation">
              {{ confirm.action }}
            </button>
            <button class="btn-cancel" @click="confirm.show=false">
              Cancel
            </button>
          </div>
      </div>
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
  .notification-enter-active, .notification-leave-active {
    transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out;
  }
  .notification-enter-from, .notification-leave-to {
    transform: translateY(-40px);
    opacity: 0;
  }
  .notification-enter-to, .notification-leave-from {
    transform: translateY(0);
    opacity: 1;
  }
  .alert, .success{
    display: flex;
    align-items: center;
    height: fit-content;
    box-sizing: border-box;
    padding: 0px 10px 0px 10px;
    width: 100%;
    max-width: min(500px, 70vw);
    background-color: #FFCCCB;
    border: 1px solid red;
    opacity: 0.9;
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

  .confirm-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.5); /* Darkens background */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 999;
  }
  .confirm-popup{
    justify-content: center;
    min-height: 120px;
    min-width: 300px;
    width: 50vw;
    z-index: 1000;
    background-color: white;
    border: 1px solid #063970;
  }
  .confirm-header{
    display: flex;
    min-height: 70%;
    padding: 20px;
    background-color: lightgray;
  }
  .confirm-btn-group{
    display: flex;
    flex-direction: row-reverse;
    align-items: center;
    min-height: 30%;
    padding: 10px;
    column-gap: 10px;
  }
  .confirm-message{
    font-size: 1.5rem;
    color: #063970
  }
  .btn-cancel, .btn-confirm{
    display: flex;
    justify-content: center;
    width: 75px;
    background-color: #063970;
    color: white;
    border: 1px solid black;
    border-radius: 5px;
  }
  .btn-confirm{
    background-color: red;
  }
  .btn-cancel:hover, .btn-confirm:hover{
    cursor: pointer;
    opacity: 0.8;
  }

</style>

