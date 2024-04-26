<template>
  <v-app style="background-color: white;" >
    <div class="button-container">
      <v-btn color="primary" @click="showGenreComponent" class="genre_button">Genre Recognition</v-btn>
      <v-btn color="primary" @click="showSentimentComponent" class="sentiment_button">Sentiment Classification</v-btn>
    </div>
    <div class="content">
      <GenreRecognition v-if="showGenre" />
      <SentimentClassification v-if="showSentiment" />
    </div>
  </v-app>
</template>

<script>
import GenreRecognition from './components/GenreRecognition.vue';
import SentimentClassification from './components/SentimentClassification.vue';

export default {
  name: 'App',
  components: {
    GenreRecognition,
    SentimentClassification
  },
  data() {
    return {
      showGenre: false,
      showSentiment: false
    };
  },
  methods: {
    showGenreComponent() {
      this.showGenre = true;
      this.showSentiment = false;
    },
    showSentimentComponent() {
      this.showGenre = false;
      this.showSentiment = true;
    }
  }
};
</script>

<style>
#app {
  text-align: center;
}
.container {
  margin-top: 20px;
}
button {
  margin: 0 10px;
}
.button-container {
  position: fixed;
  bottom: 50%;
  left: 20%;
  right: 20%;
  display: flex;
  justify-content: space-between;
}

.left-button {
  /* Adjust margin or padding if necessary */
  margin-right: auto; /* Pushes the button to the left */
}

.right-button {
  /* Adjust margin or padding if necessary */
  margin-left: auto; /* Pushes the button to the right */
}
.content {
  margin-top: 20px;
}
</style>