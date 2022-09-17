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
                    <v-card-title primary-title>
                        <div>
                            <h3 class="headline mb-0">Tus tareas para hoy son:</h3>
                        </div>
                    </v-card-title>
                    <v-card
                    v-for="(tarea, index) in this.arrayTareas"
                    v-if="Date.parse(tarea.due_date) <= currentDate && !tarea.completed"
                    v-bind:key="tarea.id"
                    elevation-8
                    style="margin: 10px;"
                    >
                        <v-card-title primary-title>
                            {{tarea.name}}
                        </v-card-title>
                        <div v-if="tarea.description != null" style="margin: 0 15px;">
                            {{tarea.description}}
                        </div>
                        <div style="margin: 0 15px;">
                            Fecha limite: {{formatDate(tarea.due_date)}}
                        </div>
                        <v-card-actions>
                            <v-btn color="primary" @click="deleteAssignment(index)">
                                Marcar como completa
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-card>
            </v-col>
            <v-col cols="6">
                <v-card outlined>
                    <v-card-title primary-title>
                        <div>
                            <h3 class="headline mb-0">Tus tareas para mañana son:</h3>
                        </div>
                    </v-card-title>
                    <v-card
                    v-for="(tarea, index) in this.arrayTareas"
                    v-if="Date.parse(tarea.due_date) > currentDate && !tarea.completed"
                    v-bind:key="tarea.id"
                    elevation-8
                    style="margin: 10px;"
                    >
                        <v-card-title primary-title>
                            {{tarea.name}}
                        </v-card-title>
                        <div v-if="tarea.description != null" style="margin: 0 15px;">
                            {{tarea.description}}
                        </div>
                        <div style="margin: 0 15px;">
                            Fecha limite: {{formatDate(tarea.due_date)}}
                        </div>
                        <v-card-actions>
                            <v-btn color="primary" @click="deleteAssignment(index)">
                                Marcar como completa
                            </v-btn>
                        </v-card-actions>
                    </v-card>
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
            userID: 1,
            currentDate: "",
            arrayTareas: []
        }
    },
    beforeMount() {
        this.$axios.$get('/user/assignments/'+ this.userID).then(response=>{
        this.arrayTareas = response
        console.log(Date.parse(this.arrayTareas[2].due_date))
        this.currentDate = new Date();
        this.currentDate.setHours(23,59,59,999)
        })  
    },
    methods:{
        toNewAssignment(){
            this.$router.push('/tarea/crear')
        },
        formatDate(date){
            return date.replace("T", ", a las ")
        },
        deleteAssignment(index){
            this.$axios.$post('/assignment/complete', this.arrayTareas[index])
            this.arrayTareas[index].completed = true
        }
    }
}
</script>
