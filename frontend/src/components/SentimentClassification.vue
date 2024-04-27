<template>
    <div class="main-container">
        <div class="sentiment-classification">
            <h2>Sentiment Classification</h2>
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
        <div class="barchart-results">
            <CanvasJSChart :options="chart"/>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'sentimentClassification',
        // Component logic goes here
        data() {
            return {
                selectedFile: null,
                fileFormData: null,
                chart: null,
                songName: "Hotel California", // Default song name
                predictions: {
                    happy: 0,
                    sad: 0,
                    angry: 0,
                    relaxed: 0
                },
                options: {
                    animationEnabled: true,
                    exportEnabled: true,
                    title:{
                    text: "Hotel California Sentiment"
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
                        { label: "Happy", y: 0.4 },
                        { label: "Sad", y: 0.1},
                        { label: "Angry", y: 0.05 },
                        { label: "Relaxed", y: 0.45 },
                    ]
                    }]
                }
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
                    const response = await axios.post('http://localhost:8000/sentiment-prediction/', this.fileFormData, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    });
                    this.songName = response.data.name;
                    this.predictions = response.data.prediction;

                    // Update the chart title
                    this.options.title.text = `${this.songName} Sentiment`;

                    // Update the data points
                    this.options.data[0].dataPoints = [
                        { label: "Happy", y: this.predictions.happy || 0 },
                        { label: "Sad", y: this.predictions.sad || 0 },
                        { label: "Angry", y: this.predictions.angry || 0 },
                        { label: "Relaxed", y: this.predictions.relaxed || 0 },
                    ];

                    // Force re-render the chart component if necessary
                    this.chart = {...this.options};
                } catch (error) {
                    console.error('There was an error during the file upload:', error);
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

