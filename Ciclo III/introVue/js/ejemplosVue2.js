let Contador = new Vue({
    el: '#contador',
    data: {
        cont: 0
    },
    mounted() {
        setInterval(() => {
            this.cont++
        }, 1000);
    }
})

let Mensaje = new Vue({
    el: '#reverso',
    data: {
        mensaje: 'Voy a ser revertido',
        esVisible: true
    },
    methods: {
        // get
        reverso: function () {
            this.mensaje = this.mensaje.split('').reverse().join('')
        }
    }
})

let Modelo = new Vue({
    el: '#modelo',
    data: {
        mensaje: 'Esta es la dirección de correo!',
        correo: 'jhonatan@mail.com'
    }
})

let listaElementos = new Vue({
    el: '#lista',
    data: {
        inputElemento: '',
        elementos: []
    },
    methods: {
        agregarElemento() {
            if (this.inputElemento != ''){
                this.elementos.push(this.inputElemento),
                this.inputElemento = ''
            }
        },
        eliminarElemento(indice) {
            this.elementos.splice(indice,1)
        }
    }
})