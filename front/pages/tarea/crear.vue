<template>
  <v-row>
    <v-col cols="6">
      <v-form>
        <v-select
          v-model="materia"
          :items="materias"
          label="¿De qué materia es tu tarea?"
          outlined
        ></v-select>
        <v-text-field
          outlined
          name="name"
          label="Nombre de la tarea"
          id="id"
        ></v-text-field>
        <v-row>
          <v-col cols="6">
            <v-date-picker v-model="date"></v-date-picker>
          </v-col>
          <v-col cols="6">
            <v-time-picker
              v-model="time"
              :allowed-minutes="allowedStep"
              format="24hr"
            ></v-time-picker>
          </v-col>
        </v-row>
      </v-form>
    </v-col>
    <v-col cols="6">
      <v-textarea
        outlined
        name="input-7-4"
        label="Descripción de tu tarea"
        value=""
      ></v-textarea>
      <v-switch v-model="esEquipo" label="¿Es en equipo?"></v-switch>
      <v-select
        v-if="equipo"
        v-model="equipo"
        :items="items"
        label="Select"
        multiple
        chips
        outlined
        hint="Elige a tus compañeros de equipo"
      ></v-select>
    </v-col>
  </v-row>
</template>
<script>
export default {
  data() {
    return {
      equipo: [],
      materia: null,
      materias: ["Materia 1", "Materia 2", "Materia 3"],
      items: ["Juan", "Luis", "Pedro"],
      esEquipo: false,
      date: null,
      time: null,
    };
  },
};
</script>
