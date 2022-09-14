<template>
  <v-container>
    <h1>Referencia de componentes Vuetify Hola:{{nombre}}</h1>
    <v-row>
      <v-col>
        <v-btn
          elevation="2"
          rounded
          dark
          raised
          class="ma-2 white--text"
          color="blue"
          >Prueba
          <v-icon right dark> mdi-cloud-upload </v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-expansion-panels>
          <v-expansion-panel v-for="(item, i) in itemsExpansion" :key="i">
            <v-expansion-panel-header>
              {{ item.titulo }}
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              {{ item.texto }}
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-data-table :items="materias" :headers="headers"></v-data-table>
      </v-col>
    </v-row>
    <v-row>
        <v-text-field
            label="Nombre(s)"
            placeholder=""
            v-model="nombre"
            outlined
          ></v-text-field>
    </v-row>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
        nombre:null,
        headers: [
          { text: 'Nombre de la materia', value: 'nombre' },
          { text: 'Profesor', value: 'profesor' },
        ],
        materias:[
            {
                nombre:"Semana Tec",
                profesor:"Andrés Torres"
            },
            {
                nombre:"Aplicaciones Móviles",
                profesor:"David Escárcega"
            }
        ],
      itemsExpansion: [
        {
          titulo: "Mi titulo 1",
          texto:
            "Sed posuere consectetur est at lobortis. Etiam porta sem malesuada magna mollis euismod. Cras mattis consectetur purus sit amet fermentum. Donec id elit non mi porta gravida at eget metus. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Nullam id dolor id nibh ultricies vehicula ut id elit. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
        },
        {
          titulo: "Mi titulo 2",
          texto:
            "Sed posuere consectetur est at lobortis. Etiam porta sem malesuada magna mollis euismod. Cras mattis consectetur purus sit amet fermentum. Donec id elit non mi porta gravida at eget metus. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Nullam id dolor id nibh ultricies vehicula ut id elit. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
        },
        {
          titulo: "Mi titulo 3",
          texto:
            "Sed posuere consectetur est at lobortis. Etiam porta sem malesuada magna mollis euismod. Cras mattis consectetur purus sit amet fermentum. Donec id elit non mi porta gravida at eget metus. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Nullam id dolor id nibh ultricies vehicula ut id elit. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
        },
        {
          titulo: "Mi titulo 4",
          texto:
            "Sed posuere consectetur est at lobortis. Etiam porta sem malesuada magna mollis euismod. Cras mattis consectetur purus sit amet fermentum. Donec id elit non mi porta gravida at eget metus. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Nullam id dolor id nibh ultricies vehicula ut id elit. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
        },
      ],
    };
  },
};
</script>
