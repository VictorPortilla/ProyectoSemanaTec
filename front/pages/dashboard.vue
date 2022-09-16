<template>
    <div>
        <v-row>
            <v-col cols="12">
                <v-btn color="primary" @click="toNewAssignment()">
                    <v-icon>mdi-plus-thick</v-icon>
                    Crear nueva tarea
                </v-btn>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="6">
                <v-card outlined>
                    <v-card-media  src="src" height="200px">
                    </v-card-media>
                    <v-card-title primary-title>
                        <div>
                            <h3 class="headline mb-0">Tus tareas para hoy son:</h3>
                        </div>
                    </v-card-title>
                    <v-card-actions>
                        <v-btn text color="primary">Ver mis tareas</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-col cols="6">
                <v-card outlined>
                    <v-card-media src="src" height="200px">
                    </v-card-media>
                    <v-card-title primary-title>
                        <div>
                            <h3 class="headline mb-0">Tus tareas para mañana son:</h3>
                        </div>
                    </v-card-title>
                    <v-card-actions>
                        <v-btn text color="primary">Ver mis tareas</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>        
        </v-row>
    </div>
    
</template>
<script>
export default {
    middleware:['authenticated'],
    data (){
        return{

        }
    },
    methods:{
        toNewAssignment(){
            this.$router.push('/tarea/crear')
        }
    }
}
</script>
