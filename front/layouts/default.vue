<template>
  <v-app>
    <v-container fluid>
      <Menu></Menu>
      <v-main>
        <Nuxt />
      </v-main>
    </v-container>
  </v-app>
</template>

<script>
import Menu from "../components/Menu.vue";
export default {
  components:{
    Menu
  }
};
</script>
