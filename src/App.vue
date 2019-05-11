<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <img alt="Vue logo" src="/public/jpg.jpg">
    <Os/>
  </div>
</template>

<script>
import Os from './components/Server_os.vue';

export default {
  name: 'App',
  components: {
    Os,
  },
};
</script>
