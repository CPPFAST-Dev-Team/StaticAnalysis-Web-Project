<template>
    <div class="box">
        <div class="header">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png">
            <a :href="repository_url">
              <h2>{{ name }}</h2>
            </a>
        </div>

        <div class="issues-wrapper">
            <h2>Issues</h2>
            <div class="btn-wrapper">
              <div class="btn-group">
                  <button class="btn-red">{{ high_vulnerabilities }}</button>
                  <button class="btn-yellow">{{ medium_vulnerabilities }}</button>
                  <button class="btn-blue">{{ low_vulnerabilities }}</button>
              </div>
              <div class="btn-group">
                  <button class="btn-view" @click="navigateToIssues">View All</button>
                  <button 
                    class="btn-red"
                    @click="showConfirm({
                      message: `Are you sure you want to delete project ${name}? This action is irreversible.`,
                      action: 'Delete',
                      handler: deleteProject,
                    })"
                  > 
                    Delete 
                  </button>
              </div>
            </div>
        </div>
    </div>
   </template>
   
<script setup>
  import { inject }from 'vue'
  import { useRouter } from 'vue-router';
  import api from '../api';

  const router = useRouter()
  const toggleNotification = inject('toggleNotification')
  const showConfirm = inject('showConfirm')
  // Define props
  const props = defineProps({
    id:{
      type: Number,
      required: true
    },
    name:{
      type: String,
      required: true
    },
    repository_url: {
      type: String,
      required: true
    },
    imgSrc:{
      type: String,
    },
    high_vulnerabilities: {
      type: Number,
      required: true
    },
    medium_vulnerabilities: {
      type: Number,
      required: true
    },
    low_vulnerabilities: {
      type: Number,
      required: true
    },
  });

  const emit = defineEmits(['delete'])

  function navigateToIssues(){
      router.push({name: "Issues", params: {projectId: props.id} })
  }
  async function deleteProject(){
    try{
      await api.delete(`api/projects/${props.id}/`)
      emit('delete')
      toggleNotification(`Project ${props.name} successfully deleted`, 'success')
    }
    catch(err){
      console.log(err)
    }
      
  }
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
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  height: 25%;
  border-bottom: 1px solid #063970;
  overflow-x: auto;
  overflow-y: hidden;
  white-space: nowrap;
}
.issues-wrapper{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 75%;
}
.btn-wrapper {
  display: flex;
  flex-direction: row;
  height: 100%;
  width: 100%;
  max-width: 400px;
  align-items: center;
}
.btn-group {
  display: flex;
  flex-direction: column;
  row-gap: 10px;
  align-items: center;
  height: 100%;
  width: 50%;
  padding: 10px;
}
img {
  display: block;
  height: 2rem;
  width: auto;
  margin: 10px;
}
.btn-group button, .btn-group a {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  max-width: 200px;
  border-radius: 5px;
  border: 1px solid black;
  cursor: pointer;
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

button, a {
  font-family: 'DM Sans', sans-serif;
}
h2 {
  font-size: clamp(1.25rem, 5%, 3rem);
  margin: 5px;
  word-break: break-word;
  color: #063970
}

</style>
   