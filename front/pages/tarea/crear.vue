<template>
  <div>
    <v-row>
      <v-col cols="6">
        <v-form>
          <v-select
            v-model="materia"
            :items="arrayMaterias"
            item-text="name"
            item-value="id"
            @change="updateClassmates()"
            label="¿De qué materia es tu tarea?"
            outlined
          ></v-select>
          <v-text-field
            v-model="assignment.name"
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
                
                format="24hr"
              ></v-time-picker><!--:allowed-minutes="allowedStep"-->
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
          v-if="esEquipo && equipo.length > 0"
          v-model="assignment.users"
          :items="equipo"
          item-text="name"
          item-value="id"
          label="Select"
          multiple
          chips
          outlined
          hint="Elige a tus compañeros de equipo"
        ></v-select>
        <p v-if="esEquipo && equipo.length == 0" style="color: red;">
          La materia no cuenta con compañeros disponibles
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn color="primary" @click="uploadAssignment()">
          <v-icon>mdi-content-save</v-icon> Crear tarea
        </v-btn>
      </v-col>
    </v-row>
  </div>
</template>
<script>
export default {
  data() {
    return {
      arrayMaterias: [],
      materia: null,
      materias: ["Materia 1", "Materia 2", "Materia 3"],
      equipo: [],
      //items: ["Juan", "Luis", "Pedro"],
      esEquipo: false,
      date: null,
      time: null,
      assignment: {},
      userID: 1
    };
  },
  mounted() {
    this.$axios.$get('/user/classes/'+ this.userID).then(response=>{
      this.arrayMaterias = response
      console.log(this.arrayMaterias)
    })
  },
  methods:{
    uploadAssignment(){
      this.assignment.due_date = this.date + 'T' + this.time
      console.log(this.assignment)
      this.$axios.$post('/assignment/create', this.assignment).then(response=>{
      console.log(response)
    })
    },
    updateClassmates(){
      this.$axios.$get('/class/users/' + this.materia).then(response=>{
      this.equipo = response.filter(data => data.id != this.userID) //borra al usuario del array
      console.log(this.equipo)
      })
    }
  }
};
</script>
