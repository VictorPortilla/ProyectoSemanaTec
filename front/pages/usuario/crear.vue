<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <h2>Crear un usuario</h2>
        <v-form>
          <v-text-field
            name="name"
            v-model="newUser.name"
            outlined
            label="Nombre"
            id="id"
          ></v-text-field>
          <v-text-field
            label="E-mail"
            v-model="newUser.email"
            outlined
          ></v-text-field>
          <v-text-field
            label="Password"
            outlined
            v-model="newUser.password"
          ></v-text-field>
        </v-form>
        <v-btn
          @click="saveUser()"
          :loading="saving"
          rounded
          color="primary"
          :disabled="saved"
          >Guardar</v-btn
        >
      </v-col>
    </v-row>
    <v-snackbar
      :timeout="-1"
      :value="true"
      absolute
      v-model="saved"
      bottom
      color="success"
      outlined
      right
    >
      Tu usuario se creó con éxito
      <template v-slot:action="{ attrs }">
        <v-btn color="pink" text v-bind="attrs" @click="saved = false">
          Cerrar
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      saving: false,
      saved: false,
      newUser: {},
    };
  },
  methods: {
    saveUser() {
      this.saving = true;
      this.$axios
        .$post("http://localhost:5000/user/create", this.newUser)
        .then((response) => {
          console.log(response);
          this.saved = true;
          this.saving = false;
        });
    },
  },
};
</script>
