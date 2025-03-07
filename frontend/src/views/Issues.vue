<template>
    <div class="container" v-if="issues.length > 0">
        <div class="header">
            <a :href="project.repository_url">
                <h1 class="word-wrap">
                    {{ project.name }}
                </h1>
            </a>
            <div class="btn-group">
                <FilterButton 
                    v-model="selectedFilters"
                    :leftColumnOptions="['High Severity', 'Medium Severity', 'Low Severity']"
                    :rightColumnOptions="['High Confidence', 'Low Confidence']"
                    @update:model-value="displayedIssues = paginateIssues(filterIssues(issues))"
                />
                <router-link :to="`/new-scan/${projectId}`" class="btn-scan">New Scan</router-link>
            </div>
        </div>
        <div class="issue-wrapper" v-for="issue in displayedIssues[page-1].interval">
            <component :is="issueComponent" v-bind="issue"/> <!-- dynamically assign issue component -->
        </div>
        <!-- use key to trigger rerender of component on filtering -->
        <Pagination
            :pages="displayedIssues.length"
            :key="displayedIssues.length"
            @change-page="handlePageChange"
            v-if="displayedIssues.length > 1"
        />
    </div>
    <div class="empty-container" v-else>
        <a :href="project.repository_url">
            <text class = "empty">
                {{ project.name }}
            </text>
        </a>
        <br/>
        <text class="empty-sub">No issues </text>
        <br/>
        <FontAwesomeIcon size="5x" color="#063970" icon="fa-solid fa-thumbs-up" />
        <br/>
        <div class="btn-group">
            <router-link to="/projects" class="btn-project">Back To Projects</router-link>
            <router-link :to="`/new-scan/${projectId}`" class="btn-scan">New Scan</router-link>
        </div>
    </div>
</template>

<script setup>
    import Display_issue_mobile from '../components/Display_issue_mobile.vue';
    import FilterButton from '../components/FilterButton.vue'
    import Issue from '../components/Display_issue.vue'
    import Pagination from '../components/Pagination.vue';
    import api from '../api';
    import { issuesData } from "../issuesData.js"

    import { ref, computed, onMounted, onUnmounted } from "vue"
    import { useRoute } from 'vue-router';

    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
    import { fas } from '@fortawesome/free-solid-svg-icons'
    import { library } from '@fortawesome/fontawesome-svg-core'

    // Add icons to the library
    library.add(fas)

    const route = useRoute()
    
    const projectId = route.params.projectId
    const project = ref({})
    const issues = ref([])
    const displayedIssues = ref([])
    const selectedFilters = ref(['High Severity', 'Medium Severity', 'Low Severity', 'High Confidence', 'Low Confidence']) //selectedFilters emitted from child component FilterButton
    const page = ref(1)
    const isMobile = ref(window.innerWidth < 768)
    const issueComponent = computed(() => isMobile.value ? Display_issue_mobile : Issue) //dynamically compute component based on isMobile, will recompute after each state change of isMobile

    onMounted(async () => {
        project.value = await getProject()

        const { returnedIssues, filteredIssues } = await getIssues()
        issues.value = returnedIssues
        console.log(issues.value)
        displayedIssues.value = paginateIssues(filteredIssues)

        window.addEventListener('resize', updateIsMobile) //add event listener to check if width is mobile
    })
    onUnmounted(() => {
        window.removeEventListener('resize', updateIsMobile) //remove event listener to check if width is mobile
    })

    async function getProject(){
        try{
            const projectResponse = await api.get(`api/projects/${projectId}/`)
            return projectResponse.data
        }
        catch(err){
            console.log(err)
        }
    }
    async function getIssues(){
        try{
            const issuesResponse = await api.get(`api/projects/${projectId}/vulnerabilities/`)
            const returnedIssues = issuesResponse.data.sort(function (issue1, issue2){
                const severityDifference = severityToInteger(issue2.severity) - severityToInteger(issue1.severity)
                const confidenceDifference = parseFloat(issue2.confidence) - parseFloat(issue1.confidence)
                return severityDifference || confidenceDifference
            })
            const filteredIssues = filterIssues(returnedIssues)
            return { returnedIssues, filteredIssues }
        }
        catch(err){
            console.log(err)
        }

        //assign int to determine hierarchy of severity category
        function severityToInteger(severity) {
            switch (severity) {
                case "SEVERE":
                    return 3;
                case "MEDIUM":
                    return 2;
                case "LOW":
                    return 1;
                default:
                    return 0;
            }
        }
    }
    function filterIssues(issues){
        return issues.filter(issue => {
            if(issue.severity === 'SEVERE' && selectedFilters.value.includes('High Severity')){
                return true
            }
            else if(issue.severity === 'MEDIUM' && selectedFilters.value.includes('Medium Severity')){
                return true
            }
            if(issue.severity === 'LOW' && selectedFilters.value.includes('Low Severity')){
                return true
            }

            if(parseFloat(issue.confidence) >= .75  && selectedFilters.value.includes('High Confidence')){
                return true
            } 
            else if(parseFloat(issue.confidence) < .75 && selectedFilters.value.includes('Low Confidence')){
                return true
            }
            return false
        })
    }
    function paginateIssues(issues){
        const temp = []
        for(let i=0; i<issues.length; i+=10){
            const interval = issues.slice(i, Math.min(i+10, issues.length))
            temp.push({
                page: (i/10)+1,
                interval
            })
        }
        return temp
    }
    function handlePageChange(newPage){
        page.value = newPage
    }
    function updateIsMobile(){
        isMobile.value = window.innerWidth < 768
    }

    function testPopulateIssues(){
        let temp = []
        for(let i=0; i<196; i++){
            const severityNum = Math.ceil(Math.random() * 3)
            const severity = severityNum === 1 ? 'SEVERE' : (severityNum === 2 ? 'MEDIUM' : 'LOW')
            temp.push({
                confidence: (Math.random()).toFixed(2).toString(),
                file_location: "Some Location",
                id: 1,
                line: Math.floor(Math.random() * 3000),
                name: "Some Issue",
                project: 14,
                severity,
                summary: "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deserunt, consequuntur ullam. Neque ratione corrupti, id tempora facere illum laborum fugit dignissimos eaque numquam, culpa pariatur voluptatem error possimus voluptatibus officiis necessitatibus itaque inventore quam enim. Cumque dolore provident qui suscipit",
                vuln_id: ""
            })
        }
        const returnedIssues = temp.sort(function (issue1, issue2){
            const severityDifference = severityToInteger(issue2.severity) - severityToInteger(issue1.severity)
            const confidenceDifference = parseFloat(issue2.confidence) - parseFloat(issue1.confidence)
            return severityDifference || confidenceDifference
        })
        const filteredIssues = filterIssues(returnedIssues)
        return { returnedIssues, filteredIssues }

        //assign int to determine hierarchy of severity category
        function severityToInteger(severity) {
            switch (severity) {
                case "SEVERE":
                    return 3;
                case "MEDIUM":
                    return 2;
                case "LOW":
                    return 1;
                default:
                    return 0;
            }
        }
    }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
.container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    max-width: 1200px;
    padding: 25px;
}
.issue-wrapper{
    margin-bottom: 20px;
}
.header{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    height: 10%;
    min-height: fit-content;
    gap: 1rem;
    margin-bottom: 20px;
}
@media(max-width: 768px){
    .header{
        flex-direction: column;
        justify-content: center;
        gap: 0.2rem;
    }
}
.header h1, .header button, .header a{
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 5px;
}

.btn-group{
    display: flex;
    flex-direction: row;
    gap: 1rem;
}
@media(max-width: 768px){
    .btn-group{
        min-width: 50vw;
        flex-direction: column;
        gap: 0.2rem;
    }
}


h1{
    color: #063970;
    font-size: 1.5rem;
    font-family: 'DM Sans', sans-serif;
}
.btn-scan, .btn-project{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 30px;
    width: 200px;
    max-width: 100%;
    padding: 10px;
    background-color: white;
    color: #063970;
    border: 1px solid #063970;
    border-radius: 10px;
    font-size: 1rem;
}
.btn-project{
    background-color: #063970;
    color: white;
}
@media(max-width: 768px){
    .btn-scan{
        width: 100%;
    }
    .btn-project{
        width: 100%;
    }
}
button:hover{
    cursor: pointer;
    opacity: 0.8;
}

/* filter */

/* filter mobile */
.filter{
    position: relative;
}
.options-wrapper-mobile{
    display: flex;
    flex-direction: column;
    position: absolute;
    left: 0;
    width: 120px;
    border: solid 1px #063970;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    background-color: rgb(239, 239, 239);
    padding: 15px;
    color: #063970;
    z-index: 1000;
}
.options-wrapper-mobile label {
    display: block;
    margin-bottom: 8px; 
    font-size: 14px; 
    line-height: 1.5; 
}
.options-wrapper-mobile footer{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
.options-wrapper-mobile footer button{
    background-color: #063970;
    color: white;
    height: 20px;
    width: 100%;
    border-radius: 5px;
    margin: 0px;
}
.options-wrapper footer button:hover{
    cursor: pointer;
    opacity: 0.8;
}

.empty-container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    max-width: 1200px;
    padding: 25px;
}
.empty, .empty-sub{
    text-align: "center";
    color: #063970;
    font-size: 2rem;
    font-family: 'DM Sans', sans-serif;
}
.empty-sub{
    font-size: 1.5rem;
}

/* text styles */
h1, h2{
    color: #063970;
    font-family: 'DM Sans', sans-serif;
}
.word-wrap{
    max-width: 100vh;
    overflow: hidden;
    overflow-wrap: break-word;
    word-break: break-word;
}
</style>
