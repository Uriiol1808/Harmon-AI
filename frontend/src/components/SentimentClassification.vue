<template>
    <div class="sentiment-classfication">
        <h2>Sentiment Classification</h2>
        <!-- Add your genre recognition UI elements here -->
        <v-container>
            <v-file-input
                v-model="selectedFile"
                label="Select a file"
                show-size
                @change="uploadFile"
            ></v-file-input>
        
            <v-btn @click="submit">Submit</v-btn>
        </v-container>
    </div>    
</template>

<script>
    export default {
        name: 'sentimentClassification',
        // Component logic goes here
        data() {
            return {
                selectedFile: null,
                fileFormData: null
            };
        },
        methods: {
            uploadFile() {
                // Update fileFormData whenever the file changes
                this.fileFormData = new FormData();
                this.fileFormData.append('file', this.selectedFile);
            },
            submit() {
                // Perform file upload here using this.fileFormData
                // You can use Axios or any other HTTP client library to make the API request
                // Example:
                // axios.post('/api/upload', this.fileFormData)
                //   .then(response => {
                //     console.log(response.data);
                //   })
                //   .catch(error => {
                //     console.error(error);
                //   });
            }
        }    
    };

</script>

<style scoped>
/* Add your CSS for sentimentClassification here */
</style>