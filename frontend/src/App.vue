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
              <v-btn icon="mdi-theme-light-dark" @click="toggleTheme"></v-btn>
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

<script setup>
import { useStorage } from '@vueuse/core';
import { useTheme } from 'vuetify';

const theme = useTheme()
const themeState = useStorage('wt-theme-state')

function toggleTheme () {
  const newValue = theme.global.current.value.dark ? 'light' : 'dark'
  theme.global.name.value = newValue
  themeState.value = newValue
}

</script>