<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <file-pond
      ref="filePond"
      v-if="showFilePond"
      label-idle="Drop files here or click to upload"
      @init="handleFilePondInit"
      @addfile="handleFileUpload"
    ></file-pond>
    <div class="buttons-container">
      <button @click="handleButtonClick('Music Genre')">Music Genre</button>
      <button @click="handleButtonClick('Lyric Analysis')">Lyric Analysis</button>
      <button @click="handleButtonClick('Speech Recognition')">Speech Recognition</button>
      <p>
        1. Select file to upload.<br>
        2. Click one of the 3 buttons.<br>
        3. Analysis is displayed below.<br>
        4. All in the same URL (try to not reload the page).<br>
        5. User can keep clicking the other buttons without having to upload again the song. 
      </p>
    </div>
  </div>
</template>

<script>
import vueFilePond from 'vue-filepond';
import 'filepond/dist/filepond.min.css';

export default {
  name: 'HomePage',
  props: {
    msg: String
  },
  data() {
    return {
      showFilePond: true
    };
  },
  components: {
    filePond: vueFilePond
  },
  methods: {
    handleButtonClick(buttonNumber) {
      // Send information to backend and process
      console.log(`Button ${buttonNumber} clicked!`);
    },
    handleFileUpload(files) {
      // Get file and save it
      const uploadedFile = files[0].file;
      console.log('Uploaded File:', uploadedFile);

      // Hide FilePond after uploading a file
      this.showFilePond = false;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
button {
  padding: 10px;
  margin: 5px;
  font-size: 16px;
}
</style>
