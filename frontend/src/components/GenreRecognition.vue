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
                    blues: 0,
                    classical: 0,
                    country: 0,
                    disco: 0,
                    hiphop: 0,
                    jazz: 0,
                    metal: 0,
                    pop: 0,
                    reggae: 0,
                    rock: 0
                },
                options: {
                    animationEnabled: true,
                    exportEnabled: true,
                    title: {
                        text: "Genre Recognition"
                    },
                    axisX: {
                        labelTextAlign: "right",
                        gridThickness: 0
                    },
                    axisY: {
                        title: "",
                        minimum: 0,
                        maximum: 1, 
                        interval: 0.1,
                        gridThickness: 0.2
                    },
                    data: [{
                        type: "bar",
                        dataPoints: [
                            { label: "Blues", y: 0 },
                            { label: "Classical", y: 0 },
                            { label: "Country", y: 0 },
                            { label: "Disco", y: 0 },
                            { label: "HipHop", y: 0 },
                            { label: "Jazz", y: 0 },
                            { label: "Metal", y: 0 },
                            { label: "Pop", y: 0 },
                            { label: "Reggae", y: 0 },
                            { label: "Rock", y: 0 },
                        ];
                    }];
                };
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
                    this.options.title.text = `${this.songName} Genre`;

                    // Update chart
                    this.options.data[0].dataPoints = [
                        { label: "Blues", y: this.predictions.blues || 0 },
                        { label: "Classical", y: this.predictions.classical || 0 },
                        { label: "Country", y: this.predictions.country || 0 },
                        { label: "Disco", y: this.predictions.disco || 0 },
                        { label: "HipHop", y: this.predictions.hiphop || 0 },
                        { label: "Jazz", y: this.predictions.jazz || 0 },
                        { label: "Metal", y: this.predictions.metal || 0 },
                        { label: "Pop", y: this.predictions.pop || 0 },
                        { label: "Reggae", y: this.predictions.reggae || 0 },
                        { label: "Rock", y: this.predictions.rock || 0 },
                    ];

                    // Force re-render the chart component if necessary
                    this.chart = {...this.options};
                } catch (error){
                    console.error('There was an error during the file upload: ', error);
                }
            },
        }    
    };
</script>
  
<style scoped>
    .main-container {
        display: flex;
        justify-content: space-around;
        align-items: start;
        padding: 20px;
    }

    .sentiment-classification, .barchart-results {
        flex: 1;
        padding: 10px; /* Ensures padding inside the containers */
        box-sizing: border-box; /* Ensures padding is included in the width calculation */
    }

    @media (max-width: 800px) {
        .main-container {
            flex-direction: column;
        }
    }
</style>  