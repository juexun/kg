<template>
  <div id="app">
    <KnowledgeGraph />
  </div>
</template>

<script>
import KnowledgeGraph from './components/KnowledgeGraph.vue'

export default {
  name: 'app',
  components: {
    KnowledgeGraph
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
