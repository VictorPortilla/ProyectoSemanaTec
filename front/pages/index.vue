<template>
  <div>
    <v-card
    color="primary"
    width="width"
    >
    <v-card-title class="white--text text--lighten-1">
      Bienvenido a la plataforma de tareas
    </v-card-title>
  </v-card>
  <v-row color="red" style="padding: 20px;">
    <v-col cols="6">
      <v-btn 
      color="primary" 
      style="min-width:300px; min-height: 50px; display: block; margin: auto;"
      @click="toLogin()">Iniciar Sesión</v-btn>
    </v-col>
    <v-col cols="6">
      <v-btn
      color="primary"
      style="min-width:300px; min-height: 50px; display: block; margin: auto;"
      @click="toRegister()">Registrarme</v-btn>
    </v-col>
  </v-row>
  </div>
</template>

<script>
export default {
  data(){
    return {
      selectedPokemon:null,
    }
  },
  methods:{
    toLogin(){
      this.$router.push('/login');
    },
    toRegister(){
      this.$router.push('/usuario/crear');
    }
  }
};
</script>
