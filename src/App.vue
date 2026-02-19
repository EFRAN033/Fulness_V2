<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import MainLayout from '@/layouts/MainLayout.vue'

const route = useRoute()

const layout = computed(() => {
  return route.meta.layout === 'MainLayout' ? MainLayout : 'div'
})
</script>

<template>
  <component :is="layout">
    <router-view />
  </component>
</template>