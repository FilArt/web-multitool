/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import App from "@/App.vue";
import { registerPlugins } from "@/plugins";
// Composables
import { createApp } from "vue";

const app = createApp(App);

registerPlugins(app);

app.mount("#app");
