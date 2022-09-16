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
          v-model="loginRequest.username"
          label="Correo"
          id="id"
          outlined
        ></v-text-field>
        <v-text-field
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required]"
          v-model="loginRequest.password"
          :type="showPassword ? 'text' : 'password'"
          label="Password"
          counter
          outlined
          @click:append="showPassword = !showPassword"
        ></v-text-field>
        <p style="color:red;" v-if="loginError">Credenciales inválidas</p>
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
      loginRequest:{
        username:"",
        password:""
      },
      loadingLogin: false,
      password: null,
      loginError:false,
      showPassword: false,
      rules: {
        required: (value) => !!value || "Campo obligatorio.",
      },
    };
  },
  methods: {
    login() {
      this.loadingLogin = true;
      this.$axios.$post('/auth',this.loginRequest).then(response=>{
        this.$cookies.set('token',response.access_token);
        this.$cookies.set('token',response.access_token);
        this.$axios.setToken(this.$cookies.get('token'))
        this.$router.push('/dashboard');
      }).catch(exception=>{
        this.loginError=true; 
        this.loadingLogin=false;
        console.log(exception)
      });
    },
  },
};
</script>
