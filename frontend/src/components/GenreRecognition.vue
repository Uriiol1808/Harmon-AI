<template>
    <div class="genre-recognition">
      <h2 >Genre Recognition</h2>
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
        name: 'GenreRecognition',
        // Component logic goes here
        data() {
            return {
                selectedFile: null,
                fileFormData: null,
                chart: null,
                songName: "Hotel California", // Default song name
                predictions: {
                    rock: 0
                    // ...
                },
                
            };
        },
        methods: {
            uploadFile() {
                // Update fileFormData whenever the file changes
                this.fileFormData = new FormData();
                this.fileFormData.append('file', this.selectedFile);
            },
            async submit() {
                try {
                    const response = await axios.post('http://localhost:8000/genre-recognition/', this.fileFormData, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    });
                    this.songName = response.data.name;
                    this.predictions = response.data.predictions;

                    // Update the chart title
                    this.options.title.text = `${this.songName} Genre`

                    // Update chart


                } catch (error){
                    console.error('There was an error during the file upload: ', error)
                }
            },
        }    
    };
</script>
  
<style scoped>
  /* Add your CSS for GenreRecognition here */
</style>  