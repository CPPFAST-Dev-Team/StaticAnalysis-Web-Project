<template>
    <div class="dropdown-wrapper" ref="Dropdown">
        <div class="dropdown-selected-option" @click="isDropdownVisible=!isDropdownVisible">
            {{ selectedOption || selectFiller}}
            <i class="fa fa-caret-down" aria-hidden="true"></i>
        </div>
        <div 
            class="options-wrapper"
            v-if="isDropdownVisible"
        >
            <div class="option" 
                v-for="option in options"
                :key="option.id"
                @click="toggleOptionSelect(option)"
            >
              <p>{{ option.name }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
  import { ref, onMounted, onUnmounted } from 'vue'
  const Dropdown = ref(null)
  const selectedOption = ref(null)
  const isDropdownVisible = ref(false)
  const props = defineProps({
    selectFiller: String,
    options: Array,
  })

  const emit = defineEmits(['update:modelValue']) //defines what events the child can emit to the parent

  function toggleOptionSelect(option) {
    selectedOption.value = option.name;
    emit('update:modelValue', option); //tell parent to update parent value from child component's selectedOption
    isDropdownVisible.value = false;
  }

  function closeDropdown(event) {
    if (Dropdown.value && !Dropdown.value.contains(event.target)) { //access ref attached to DOM element of Dropdown
      isDropdownVisible.value = false;
    }
  }

  onMounted(() => {
    window.addEventListener('click', closeDropdown);
  })
  onUnmounted(() => {
    window.removeEventListener('click', closeDropdown);
  })
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
.dropdown-wrapper{
    position: relative;
    cursor: pointer;
    height: 100%;
    width: 100%;
    margin: 0;
}
.options-wrapper{
    position: absolute;
    top: 100%;
    z-index: 10;
    cursor: pointer;
    background-color: white;
    height: 100%;
    width: 100%;
    margin: 0;
}
.dropdown-selected-option{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 5px;
    width: 100%;
    border: 1px solid #063970;
    border-radius: 5px;
    color: #063970;
    box-sizing: border-box;
}
.option{
    display: flex;
    align-items: center;
    padding: 8px;
    width: 100%;
    border: solid 1px #063970;
    border-bottom: solid 1px transparent;
    box-sizing: border-box;
    background: white;
    overflow-wrap: break-word;
}
.option:hover{
    background: #c5c5c5;
}
.option:last-of-type{
    border-bottom-left-radius: 8px;
    border-bottom-right-radius: 8px;
    border-bottom: solid 1px #063970;
}
</style>