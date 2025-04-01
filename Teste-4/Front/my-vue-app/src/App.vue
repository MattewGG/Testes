<template>
  <div id="app">
    <CarrierSearch />
  </div>
</template>

<script>
import CarrierSearch from './components/CarrierSearch.vue';

export default {
  name: 'App',
  components: {
    CarrierSearch
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>