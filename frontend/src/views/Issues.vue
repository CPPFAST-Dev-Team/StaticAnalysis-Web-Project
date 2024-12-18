<template>
    <div class="container">
        <!-- normal view -->
        <div class="header" v-if="!isMobile">
            <h1>{{ projectName }}</h1>

            <!-- Filter button -->
            <div>
                <button class="btn-filter" @click="showFilters=!showFilters">
                    <span class="left">Filter</span>
                    <span class="right">
                        <i class="fa fa-caret-square-o-down" aria-hidden="true"></i>
                    </span>
                </button>
                <div class="options-wrapper" v-if="showFilters">
                    <div class="row">
                        <div class="column">
                            <label><input name="high-severity" type="checkbox"> High Severity</label>
                            <label><input name="medium-severity" type="checkbox"> Medium Severity</label>
                            <label><input name="low-severity" type="checkbox"> Low Severity</label>
                        </div>
                        <div class="column">
                            <label><input name="high-confidence" type="checkbox"> High Confidence</label>
                            <label><input name="low-confidence" type="checkbox"> Low Confidence</label>
                        </div>
                    </div>

                    <footer>
                        <button @click="showFilters=false">Filter</button>
                    </footer>
                </div>
            </div>
            <router-link to="/new-scan" class="btn-scan">New Scan</router-link>
        </div>
        <div class="issue-wrapper" v-for="issue in issues" v-if="!isMobile">
            <Issue v-bind="issue"/>
        </div>

        <!-- mobile view -->
        <div class="header-mobile" v-if="isMobile">
            <h2>Placholder.com</h2>
            <div class="btn-group">

                <!-- filter button -->
                <div class="filter">
                    <button class="btn-filter" @click="showFiltersMobile=!showFiltersMobile">
                        <span class="left">Filter</span>
                        <span class="right">
                            <i class="fa fa-caret-square-o-down" aria-hidden="true"></i>
                        </span>
                    </button>
                    <div class="options-wrapper-mobile" v-if="showFiltersMobile">
                        <label><input name="high-severity" type="checkbox"> High Severity</label>
                        <label><input name="medium-severity" type="checkbox"> Medium Severity</label>
                        <label><input name="low-severity" type="checkbox"> Low Severity</label>
                        <label><input name="high-confidence" type="checkbox"> High Confidence</label>
                        <label><input name="low-confidence" type="checkbox"> Low Confidence</label>

                        <footer>
                            <button @click="showFiltersMobile=false">Filter</button>
                        </footer>
                    </div>
                </div>

                <router-link to="/new-scan" class="btn-scan">
                    New Scan
                </router-link>
            </div>
        </div>
        <div class="issue-wrapper" v-for="issue in issues" v-if="isMobile">
            <Display_issue_mobile v-bind="issue"/>
        </div>
    </div>
</template>

<script>
import Issue from '../components/Display_issue.vue'
import Display_issue_mobile from '@/components/Display_issue_mobile.vue';
import { issues } from "../issuesData.js"
    export default{
        data(){
            return {
                issues: [],
                projectName: "",
                showFilters: false,
                showFiltersMobile: false,
                isMobile: false,
                // parameters: 
                // fileName
                // issueName
                // line
                // errorText
                // confidence
            }
        },
        mounted(){
            this.checkIsMobile();
            window.addEventListener('resize', this.checkIsMobile);
        },
        beforeUnmount() {
            window.removeEventListener('resize', this.checkIsMobile);
        },
        created(){
            this.getIssues()
        },
        //backend api call here to get issues
        methods: {
            async getIssues(){
                this.issues = issues;
                this.projectName = "Placeholder.com";
            },
            checkIsMobile(){
                this.isMobile = window.innerWidth < 768;
            },
        },
        components: {
            Issue,
            Display_issue_mobile
        }
    }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
.container{
    position: relative;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 25px;
}
.issue-wrapper{
    display: flex;
    justify-content: center;
    width: 100%;
}
.header{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    width: 90%;
    height: 10%;
    min-width: 800px;
    min-height: 100px;
    max-width: 1200px;
    max-height: 300px;
}
.header h1, .header button, .header a{
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 25px;
    padding: 5px;
}
.header-mobile{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    width: 300px;
    height: 100px;
    margin: 20px;
}
.header-mobile .btn-group{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 40%;
    height: 100%;
}
.header-mobile .btn-group .btn-filter, .header-mobile .btn-group .btn-scan{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 20px;
    width: 100px;
    border-radius: 5px;
}
.header-mobile .btn-group .filter, .header-mobile .btn-group .btn-scan{
    margin-bottom: 5px;
}
h1{
    color: #063970;
    font-size: 30px;
    font-family: 'DM Sans', sans-serif;
}
.btn-filter, .btn-scan{
    height: 30px;
    width: 200px;
    border: 1px solid #063970;
    border-radius: 10px;
    font-size: 1rem;
    padding: 10px;
}
.btn-filter{
    background-color: #063970;
    color: white;
}
.btn-filter .left{
    display: flex;
    justify-content: center;
    width: 90%;
}
.btn-filter .right{
    width: 10%;
}
.btn-scan{
    background-color: white;
    color: #063970;
}
button:hover{
    cursor: pointer;
    opacity: 0.8;
}

/* filter */
.options-wrapper{
    display: flex;
    flex-direction: column;
    position: absolute;
    height: 150px;
    width: 350px;
    border: solid 1px #063970;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    background-color: rgb(239, 239, 239);
    padding: 15px;
    color: #063970;
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

/* text styles */
h1, h2{
    color: #063970;
    font-family: 'DM Sans', sans-serif;
}
</style>
