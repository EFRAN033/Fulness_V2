<template>
  <div class="min-h-screen bg-[#f5f9fc] flex">
    <!-- Header -->
    <!-- Header -->
    <header class="fixed top-0 inset-x-0 bg-white shadow-md z-[1000] h-[70px] md:h-[60px]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full">
        <nav class="w-full h-full flex items-center justify-between">
          <div class="flex items-center gap-4">
            <router-link 
              to="/" 
              class="flex items-center gap-2 text-brand-primary hover:text-brand-secondary transition-colors group"
            >
              <!-- Icono de flecha  -->
              <div class="relative w-8 h-8 flex items-center justify-center rounded-full bg-gradient-to-r from-brand-primary to-brand-accent group-hover:scale-105 transition-transform">
                <i class="fas fa-chevron-left text-white text-sm"></i>
              </div>
              <span class="hidden md:inline text-sm font-medium">Volver</span>
            </router-link>
            <a href="#" class="flex items-center h-14 overflow-hidden">
              <img 
                src="@/assets/imagenes/LOGO.svg" 
                alt="Fullness Logo"
                class="h-12 translate-y-2 object-contain transition-transform duration-300"
              >
            </a>
          </div>
        </nav>
      </div>
    </header>
    
    <!-- Espacio para el Header -->
    <div class="h-[70px] md:h-[60px]"></div>

    <!-- Sección de Formulario (Slot) -->
    <div class="w-full md:w-1/2 bg-white flex items-center justify-center p-6 md:p-12 lg:p-20 mt-[70px] md:mt-0">
      <div class="w-full max-w-md space-y-8">
        <slot></slot>
      </div>
    </div>

    <!-- Sección de Imagen -->
    <div class="hidden md:block w-1/2 bg-gradient-to-br from-brand-primary/80 to-brand-secondary/80 relative fixed right-0 top-0 bottom-0 z-0 mt-[60px]">
      <img 
        src="https://img.freepik.com/foto-gratis/tiro-medio-terapia-rehabilitacion-fisica_23-2149173475.jpg" 
        class="absolute inset-0 w-full h-full object-cover mix-blend-multiply"
        alt="Fisioterapia">
      
      <!-- Overlay de Contacto -->
      <div class="absolute bottom-6 right-6 bg-white/10 backdrop-blur-sm p-4 rounded-lg text-white space-y-2">
        <div class="flex items-center space-x-2">
          <i class="fas fa-phone"></i>
          <span>(+51) 941-609-887</span>
        </div>
        <div class="flex items-center space-x-2">
          <i class="fas fa-envelope"></i>
          <span>contacto@fullness.org</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AuthLayout'
}
</script>
