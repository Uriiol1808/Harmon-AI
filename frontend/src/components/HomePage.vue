<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <input type="file" @change="handleFileUpload" />
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
export default {
  name: 'HomePage',
  props: {
    msg: String
  },
  methods: {
    handleButtonClick(buttonNumber) {
      // Send information to backend and process
      console.log(`Button ${buttonNumber} clicked!`);
    },
    handleFileUpload(event) {
      // Get file and save it
      const uploadedFile = event.target.files[0];
      console.log('Uploaded File:', uploadedFile);
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
