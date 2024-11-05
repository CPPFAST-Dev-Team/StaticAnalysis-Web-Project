<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <div class="input-container">
        <div class="input-group">
            <label for="repo">Repo</label>
            <input type="text" id="frepo" name="repo"><br><br>
        </div>

        <div class="input-group">
            <label for="token">Token</label>
            <input type="text" id="ftoken" name="token"><br><br>
        </div>

        <div class="input-group">
            <div class="dropdown-input">
                <button class="dropbtn-input">
                    <span class="dropdown-input-left">
                        <span>Team</span>
                    </span>
                    <span class="dropdown-input-right">
                        <i class="fa fa-caret-down" aria-hidden="true"></i>
                    </span>
                </button>
                <div id="teamDropdown" class="dropdown-content-input">
                    <span>Team1</span>
                    <span>Team2</span>
                </div>
            </div>
        </div>

        <div class="create">
            <button class="createbtn">
                <span>Create</span>
            </button>

        </div>
    </div>
</template>

<script>
export default{

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');
    .input-container{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-width: 100px;
        width: 100%;
        max-width: 1000px;
        min-height: 50px;
        height: 80%;
        max-height: 800px;
    }
    .input-group{
        width: 40%;
        height: 10%;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
        margin-bottom: 30px;
    }
    .input-group input[type="text"]{
        height: 100%;
        width: 100%;
        min-height: 30px;
        border: 1px solid #063970;
        border-radius: 5px;
        color: #063970;
        margin: 0;
    }
    .input-group label{
        margin: 0;
        font-family: 'DM Sans', sans-serif;
        font-size: clamp(1rem, 50%, 2rem);
    }
    .dropdown-input {
        position: relative;
        display: inline-block;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%;
    }
    .dropbtn-input {
        display: flex;
        align-items: center;
        justify-content: space-between;
        height:4vh;
        width: 100%;
        margin: 0;
        border: 1px solid #063970;
        border-radius: 5px;
        color:#063970;
        cursor: pointer;
    }
    .dropbtn-input-left{
        text-align: left;
        width: 50%;
    }
    .dropbtn-input-right{
        text-align: right;
        width: 50%;
    }
    .dropdown-input .dropdown-content-input {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;

        left: 0;
    }
    .dropdown-content-input span{
        padding: 12px 16px;
        text-decoration: none;
        display: block;
        text-align: left;
    }
    .dropdown-input:hover .dropdown-content-input {
        display: block;
        cursor: pointer;
    }
    .dropdown-content-input span:hover{
        background-color: #ddd;
    }
    .create{
        display: flex;
        align-items: center;
        justify-content: center;
        width: 40%;
        height: 5%;
    }
    .createbtn{
        width: 40%;
        height: 100%;
        background-color:#063970;
        color: white;
        border-radius: 10px;
        cursor: pointer;
    }


</style>