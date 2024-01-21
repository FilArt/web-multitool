<template>
  <v-card max-width="640" class="ma-auto">
    <v-card-title>
      URL Shortener
    </v-card-title>
    <v-form  @submit.prevent="onSubmit">
    <v-card-text>
      <v-text-field  label="URL" />
    </v-card-text>

    <v-card-actions>
      <v-btn type="submit">Generate short URL</v-btn>
    </v-card-actions>
  </v-form>
  </v-card>
</template>
  

<script setup>
const onSubmit = (e) => {
  alert(e)
}
</script>