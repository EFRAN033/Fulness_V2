<template>
  <div class="min-h-screen flex flex-col">
    <Navbar />
    <!-- Espacio para compensar el header fixed -->
    <div class="h-[60px]"></div>
    
    <!-- Contenido Principal -->
    <main class="flex-grow">
      <slot />
    </main>
    
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/common/Navbar.vue'
import Footer from '@/components/common/Footer.vue'

export default {
  name: "MainLayout",
  components: {
    Navbar,
    Footer
  }
}
</script>
