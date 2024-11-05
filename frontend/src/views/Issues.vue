<template>
    <div>
    <Issue
        fileName="File.cpp"
        :line="123"
        errorText="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate..."
        :confidence="95"
    />
    <Issue
        fileName="File.java"
        :line="456"
        errorText="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate..."
        :confidence="52"
    />
    </div>
</template>

<script>
import Issue from '../components/Display_issue.vue'
    export default{
        components: {
            Issue 
        }
    }
</script>
