<template>
    <div class="wrapper">
        <div :class="mobile ? 'box-mobile' : 'box'" v-for="n in 3" :key="n">
            
        </div>
    </div>
</template>

<script setup>
    import { ref, onMounted, onUnmounted } from 'vue'
    const mobile = ref(window.innerWidth < 768)
    onMounted(() => {
        window.addEventListener('resize', handleResize)
        handleResize()
    })
    onUnmounted(() => {
        window.removeEventListener('resize', handleResize)
    })
    function handleResize(){
        mobile.value = window.innerWidth < 768
    }
</script>

<style scoped>
.wrapper{
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    row-gap: 20px;
    overflow-y: auto;
}
.box {
    height: 200px;
    width: 100%;
    border: 1px solid #063970;
    border-radius: 50px;
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    animation: shimmer 1.5s infinite;
}
.box-mobile {
    width: 100%;
    height: 200px;
    border: 1px solid #063970;
    border-radius: 20px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    animation: shimmer 3.0s infinite;
}

@keyframes shimmer {
    0% {
        background-position: 200% 0;
    }
    100% {
        background-position: -200% 0;
    }
}
</style>