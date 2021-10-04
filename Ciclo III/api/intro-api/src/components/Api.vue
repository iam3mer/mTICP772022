<template>
    <div>
        <div v-if="result">
            <p>albumId: {{ result.albumId }}</p>
            <p>id: {{ result.id }}</p>
            <p>title: {{ result.title }}</p>
            <p>thumbnailUrl: {{ result.thumbnailUrl }}</p>
            <p>url: {{ result.url }}</p>
        </div>
        
    </div>
</template>

<script>
import axios from "axios"
export default {
    data: () => ({
        result: null,
    }),
    created () {
        // GET ---------------------------------------------------
        axios
            .get("https://jsonplaceholder.typicode.com/photos/4852")
            .then((result) => {
                // console.log(result.data)
                this.result = result.data
            })
        // DELETE ---------------------------------------------------
        axios
            .delete("https://jsonplaceholder.typicode.com/photos/4251")
            // opcional
            .then((result) => {
                console.log(result)
            })
            // Gestión de errores (catch)
            .catch(error => {
                console.log(error)
            })
        // POST ---------------------------------------------------
        // let photo = {
        //     albumId: 5001,
        //     id: 5001,
        //     title: 'Titulo de la nueva foto',
        //     thumbnailUrl: 'url_min',
        //     url: 'url_photo',
        // }
        // axios
        //     .post("https://jsonplaceholder.typicode.com/photos", photo)
        //     .then((result) => {
        //         console.log(result)
        //     })
        // PUT ---------------------------------------------------
        // let photo = {
        //     albumId: 3165,
        //     id: 3165,
        //     title: 'Un nuevo titulo',
        //     thumbnailUrl: 'url_min',
        //     url: 'url_photo',
        // }
        // axios
        //     .put("https://jsonplaceholder.typicode.com/photos/3165", photo)
        //     .then((result) => {
        //         console.log(result)
        //     })
        this.addPhoto()
        this.getAllPhotos()
    },
    // async / await ---------------------------------------------------
    // async created () {
    //     let response = await axios.get("https://jsonplaceholder.typicode.com/photos/4852")
    //     this.result = response.data
    // },
    methods: {
        // Con gestión de errores (try/catch)
        async getAllPhotos () {
            try {
                let response = await axios.get("https://jsonplaceholder.typicode.com/photos")
                console.log(response)
            } catch (error) {
                console.log(error)
            }
        },
        async addPhoto () {
            let photo = {
                albumId: 5001,
                id: 5001,
                title: 'Titulo de la nueva foto',
                thumbnailUrl: 'url_min',
                url: 'url_photo',
            }
            let response = axios.post("https://jsonplaceholder.typicode.com/photos", photo)
            console.log(response)
        }
    }
}
</script>