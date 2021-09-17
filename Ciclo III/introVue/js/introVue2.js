objData = {
    saludo: 'Hola Tripulantes',
    anio: '<p style="color:blue">2021</p>',
    suma: 5 + 2,
    ver: false,
    textT: 'ver (v-if) es verdadero',
    textF: 'ver (v-else) es falso',
    url: 'https://www.google.com',
    target: '_blank'
}

let app = new Vue({
    el: '#saludar',
    data: objData,
    computed: {
        reverso: function () {
            return this.saludo.split('').reverse().join('')
        }
    },
    methods: {
        // get
        reversoF: function () {
            return this.saludo.split('').reverse().join('')
        }
    }
})

// Vue3
/*
const Saludar = {
    data () {
        return objData
    }
}

Vue.createApp(Saludar).mount('#saludar')
*/