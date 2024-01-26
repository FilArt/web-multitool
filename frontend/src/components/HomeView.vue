<template>
    <div class="d-flex flex-row flex-wrap">

    <v-card v-for="app in apps" :key="app.title" :to="app.path" :title="app.meta.title">
    </v-card>
</div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const apps = useRouter().getRoutes().filter(r => !!r?.meta?.title)
</script>