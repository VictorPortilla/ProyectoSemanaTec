<template>
  <v-container>
    <v-card
      :loading="loadingLogin"
      elevation="18"
      outlined
      tile
      style="padding: 35px"
    >
      <v-card-title primary-title>
        <div>
          <h3 class="headline mb-0">Iniciar sesión</h3>
        </div>
      </v-card-title>
      <div style="padding: 35">
        <v-text-field
          name="name"
          label="Correo"
          id="id"
          outlined
        ></v-text-field>
        <v-text-field
          v-model="password"
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required]"
          :type="showPassword ? 'text' : 'password'"
          label="Password"
          counter
          outlined
          @click:append="showPassword = !showPassword"
        ></v-text-field>
      </div>
      <v-card-actions>
        <v-btn :loading="loadingLogin" @click="login()" color="primary"
          >Iniciar sesión</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
export default {
    layout: 'login',
  data() {
    return {
      loadingLogin: false,
      password: null,
      showPassword: false,
      rules: {
        required: (value) => !!value || "Campo obligatorio.",
      },
    };
  },
  methods: {
    login() {
      this.loadingLogin = true;
    },
  },
};
</script>
