import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import 'vuetify/styles'; // Ensure you are using css


// Create a new instance of Vuetify
const vuetify = createVuetify({
    components,
    directives,
});

const app = createApp(App);

// Use Vuetify instance
app.use(vuetify);

app.mount('#app');