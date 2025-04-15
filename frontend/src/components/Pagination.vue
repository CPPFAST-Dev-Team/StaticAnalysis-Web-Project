<template>
    <nav>
        <ul class="pagination-wrapper">
            <span @click="decrementPage"> 
                <FontAwesomeIcon color="#063970" icon="fa-solid fa-caret-left" />
            </span>
            <li 
                v-for="page in pageRange"
                :class="{ 'selected-pagination-box': page === current, 'pagination-box': page !== current }"
                @click="() => selectPage(page)"
            >
                {{ page }}
            </li>
            <span @click="incrementPage"> 
                <FontAwesomeIcon color="#063970" icon="fa-solid fa-caret-right" />
            </span>
        </ul>
    </nav>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { fas } from '@fortawesome/free-solid-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'

// Add icons to the library
library.add(fas)

const current = ref(1)
const pageRange = ref()

const props = defineProps({
    pages: {
        type: Number,
        required: true
    }
})
const emit = defineEmits(['changePage'])

function getPages(){
    if(current.value - 4 < 1){
        pageRange.value = getArray(1, Math.min(10, props.pages))
    }
    else if(current.value + 5 > props.pages){
        pageRange.value = getArray(Math.max(1, props.pages-9), Math.min(current.value+5, props.pages))
    }
    else{
        pageRange.value = getArray(current.value-4, current.value+5)
    }

    function getArray(min, max){
        const res = []
        for(let i=min; i<=max; i++){
            res.push(i)
        }
        return res
    }
}
function incrementPage(){
    if(current.value !== props.pages){
        current.value += 1
        getPages()
        emit('changePage', current.value)
    }
}
function decrementPage(){
    if(current.value !== 1){
        current.value -= 1
        getPages()
        emit('changePage', current.value)
    }
}
function selectPage(newPage){
    current.value = newPage
    getPages()
    emit('changePage', current.value)
}

onMounted(() => {
    getPages()
})

</script>

<style>
.pagination-wrapper{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    min-height: 75px;
    width: 100%;
    column-gap: 5px;
}
.pagination-box, .selected-pagination-box{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 20px;
    width: 30px;
    border: 1px solid #063970;
}
.selected-pagination-box{
    background-color: #063970;
    color: white;
}
.pagination-spread{
    display: flex;
    justify-content: center;
    align-items: center;
}
.pagination-wrapper i{
    color: #063970;
}
.pagination-box:hover, .pagination-spread:hover, .pagination-wrapper i:hover{
    cursor: pointer;
}
.pagination-box:hover{
    background-color: lightgray;
}
</style>