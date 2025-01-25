<template>
    <div>
        <button ref="FilterButton" class="btn-filter">
            <span class="left">Filter</span>
            <span class="right" @click="toggleFilter">
                <i 
                    :class="showFilter ? 'fa fa-caret-square-o-up':'fa fa-caret-square-o-down'"
                    aria-hidden="true">
                </i>
            </span>
        </button>

        <div ref="FilterOptions" class="options-wrapper" v-if="showFilter">
            <div :class="{ row: !isSmallScreen }">
                <div :class="{ column: !isSmallScreen }">
                    <div v-for="option in leftColumnOptions">
                        <input 
                            name="option" 
                            type="checkbox" 
                            :checked="selectedOptions.includes(option)" 
                            @click="() => toggleFilterOptions(option)"
                        > 
                        {{ option }}
                    </div>
                </div>
                <div :class="{ column: !isSmallScreen }">
                    <div v-for="option in rightColumnOptions">
                        <input 
                            name="option" 
                            type="checkbox" 
                            :checked="selectedOptions.includes(option)" 
                            @click="() => toggleFilterOptions(option)"
                        > 
                        {{ option }}
                    </div>
                </div>
            </div>

            <footer>
                <button @click="handleFilterSubmit">Filter</button>
            </footer>
        </div>
    </div>
</template>

<script setup>
    import { ref, onMounted, onUnmounted } from 'vue'

    const FilterButton = ref(null)
    const FilterOptions = ref(null)
    const showFilter = ref(false)
    const selectedOptions = ref([])

    const leftColumnOptions = ['High Severity', 'Medium Severity', 'Low Severity']
    const rightColumnOptions = ['High Confidence', 'Low Confidence']

    const isSmallScreen = ref(window.innerWidth < 400)

    function toggleFilter(){
        showFilter.value = !showFilter.value
    }
    function toggleFilterOptions(option){
        if(selectedOptions.value.includes(option)){
            selectedOptions.value = selectedOptions.value.filter(listOption => listOption !== option)
        }
        else{
            selectedOptions.value.push(option)
        }
    }
    function closeFilterOptions(event){
        //clicking FilterButton alerts event listener, so we check that the event does not originate from FilterButton
        if(
            FilterButton.value && 
            !FilterButton.value.contains(event.target) &&
            FilterOptions.value && 
            !FilterOptions.value.contains(event.target))
        {
            showFilter.value = false
        }
    }
    function handleFilterSubmit(){
        showFilter.value = false
        
        //logic here to filter...
        console.log(selectedOptions.value)
    }

    function updateIsSmallScreen(){
        isSmallScreen.value = window.innerWidth < 400
    }

    onMounted(() => {
        window.addEventListener('click', closeFilterOptions)
        window.addEventListener('resize', updateIsSmallScreen)
    })
    onUnmounted(() => {
        window.removeEventListener('click', closeFilterOptions)
        window.removeEventListener('resize', updateIsSmallScreen)
    })
</script>

<style scoped>
.btn-filter{
    display: flex;
    flex-direction: row;
    align-items: center;
    height: 30px;
    width: 200px;
    border: 1px solid #063970;
    border-radius: 10px;
    font-size: 1rem;
    padding: 10px;
    background-color: #063970;
    color: white;
}
@media(max-width: 768px){
    .btn-filter{
        width: 100%;
    }
}
.btn-filter .left{
    display: flex;
    justify-content: center;
    width: 90%;
}
.btn-filter .right{
    width: 10%;
}

.options-wrapper{
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 100;
    height: fit-content;
    width: 350px;
    max-width: 350px;
    border: solid 1px #063970;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    background-color: rgb(239, 239, 239);
    padding: 15px;
    color: #063970;
}
@media(max-width: 768px){
    .options-wrapper{
        height: fit-content;
        width: 70vw;
    }
}
.options-wrapper .row{
    display: flex;
    flex-direction: row;
}
.options-wrapper .column{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: left;
    height: 90%;
    width: 50%;
    gap: 0.5rem;
}
.options-wrapper input{
    margin-bottom: 15px;
}
.options-wrapper footer{
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    width: 100%;
}
.options-wrapper footer button{
    background-color: #063970;
    color: white;
    height: 20px;
    width: 80px;
    border-radius: 5px;
    margin: 0px;
}
.options-wrapper footer button:hover{
    cursor: pointer;
    opacity: 0.8;
}
.option{
    font-size: 1rem;
    line-height: 0.5;
}
</style>