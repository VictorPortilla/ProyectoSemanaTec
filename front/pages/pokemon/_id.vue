<template>
    <v-row justify="center" align="center">

      <v-col cols="6" v-if="!loading">
        <v-card elevation="2" outlined shaped>
          <v-card-title>{{pokemon.name}}
            <img :src="pokemon.sprites.front_default"/>
          </v-card-title>
          <v-card-subtitle>
            <h2>Types</h2>
            <p v-for="pokemon_type in pokemon.types" v-bind:key="pokemon_type.type.name">
              {{pokemon_type.type.name}}
            </p>
          </v-card-subtitle>
          <v-card-text>
            <h2>Abilities</h2>
            <v-row>
              <v-col cols="4" v-for="move in pokemon.moves" v-bind:key="move.move.name">
                {{move.move.name}}
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </template>
  
  <script>
  export default {
    name: "Pokem",
    data() {
      return {
        loading:true,
        pokemon:null
      };
    },
    mounted(){
      this.loadPokemon();
    },
    methods:{
      loadPokemon(){
        this.loading=true;
        this.$axios.$get('https://pokeapi.co/api/v2/pokemon/'+this.$route.params.id+'/').then(response=>{
          this.loading=false;
          this.pokemon=response;
          console.log(response);
        })
      }
    }
  };
  </script>
  
