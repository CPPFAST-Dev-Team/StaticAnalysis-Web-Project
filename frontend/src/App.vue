<script>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import Display_project from './components/Display_project.vue'
import Display_report from './components/Display_report.vue'

export default{
  name: 'App',
  components: {
    HelloWorld,
    TheWelcome,
    Display_project,
    Display_report,
  }
}
</script>

<template>
  <div>
    <Display_project
      githubUrl = "Github.com/example"
      issueRed = "1234"
      issueYellow = "5678"
      issueBlue = "9000"
    />
    <Display_report
      fileName = "File.cpp"
      line = "123"
      errorText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate..."
      confidence = "90"
    />
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
}
div{
  display: flex;
  flex-direction: column;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
