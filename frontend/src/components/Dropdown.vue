<template>
    <div class="dropdown-wrapper" ref="Dropdown">
        <div class="dropdown-selected-option" @click="isDropdownVisible=true">
            <div class="dropdown-selected-option-left">
                {{ selectedOption || selectFiller}}
            </div>
            <div class="dropdown-selected-option-right">
                <i class="fa fa-caret-down" aria-hidden="true"></i>
            </div>
        </div>
        <div 
            class="options-wrapper"
            v-if="isDropdownVisible"
        >
            <div class="option" 
            v-for="(option,index) in options"
            :key="index"
            @click="toggleOptionSelect(option)"
            >
              {{ option }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
  props: {
    selectFiller: {
      type: String,
      required: true,
    },
    options: {
      type: Array,
      required: true,
    },
    modelValue: {
      default: null,
    },
  },
  data() {
    return {
      selectedOption: null,
      isDropdownVisible: false,
    };
  },
  mounted() {
    window.addEventListener('click', this.closeDropdown);
  },
  beforeDestroy() {
    window.removeEventListener('click', this.closeDropdown);
  },
  methods: {
    toggleOptionSelect(option) {
      this.selectedOption = option;
      this.$emit('update:modelValue', option);
      this.isDropdownVisible = false;
    },
    closeDropdown(event) {
      if (this.$refs.Dropdown && !this.$refs.Dropdown.contains(event.target)) {
        this.isDropdownVisible = false;
      }
    },
  },
};


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
    z-index: 1000;
    cursor: pointer;
    background-color: white;
    height: 100%;
    width: 100%;
    margin: 0;
}
.dropdown-selected-option{
    display: flex;
    flex-direction: row;
    justify-content: center;
    padding-left: 8px;
    padding-right: 8px;
    height: 100%;
    width: 100%;
    border: 1px solid #063970;
    border-radius: 5px;
    color: #063970;
    box-sizing: border-box;
}
.dropdown-selected-option-left{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    width: 90%;
}
.dropdown-selected-option-right{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-end;
    width: 10%;
}

.option{
    display: flex;
    align-items: center;
    padding-left: 8px;
    height: 100%;
    width: 100%;
    border: solid 1px #063970;
    border-bottom: solid 1px transparent;
    box-sizing: border-box;
    background: white;
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