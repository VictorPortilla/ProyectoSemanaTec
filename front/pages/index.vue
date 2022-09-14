<template>
  <v-row justify="center" align="center">
    <v-col cols="6" v-if="!loading">
      {{selectedPokemon}}
      <v-text-field
        name="name"
        v-model="selectedPokemon"
        label="Número de pokemon"
      ></v-text-field>
      <v-btn color="success" @click="goToPokemon">Buscar</v-btn>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data(){
    return {
      selectedPokemon:null,
    }
  },
  methods:{
    goToPokemon(){
      this.$router.push('/pokemon/'+this.selectedPokemon);
    }
  }
};
</script>
