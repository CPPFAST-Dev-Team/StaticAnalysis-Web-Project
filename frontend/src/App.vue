<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Navbar,
  }
}
</script>

<template>
  <Navbar/>
  <div class="main">
    <router-view/>
  </div>
</template>

<style scoped>
.main{
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  width: 100vw;
  height: 90vh;
  margin-top: clamp(50px, 5vh, 200vh);
  overflow: hidden;
  }

</style>

