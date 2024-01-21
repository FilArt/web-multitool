<template>
  <v-app full-height>
    <v-main >
      <v-card flat>
        <v-card-title>
          <v-app-bar>
            <v-app-bar-nav-icon>
              <v-btn to="/">
                <v-icon icon="mdi-home"></v-icon>
              </v-btn>
            </v-app-bar-nav-icon>
            <v-app-bar-title>
              Web Multitool
            </v-app-bar-title>
            <v-toolbar-items>
              <v-btn to="/url-shortener">Url Shortener</v-btn>
            </v-toolbar-items>
          </v-app-bar>
        </v-card-title>
        <v-card-text>
          <router-view />
        </v-card-text>
      </v-card>
    </v-main>
  </v-app>
</template>

