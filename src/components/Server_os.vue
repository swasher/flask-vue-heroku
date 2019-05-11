<template>
    <p> Server working on: {{ os }}</p>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Server_os',
  data() {
    return {
      os: 'Unknown',
    };
  },
  methods: {
    getOs() {
      const path = 'http://localhost:5000/json';
      axios.get(path)
        .then((response) => {
          this.os = response.data.platform;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getOs();
  },
};
</script>
