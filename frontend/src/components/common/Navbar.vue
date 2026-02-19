<template>
  <header
    class="fixed top-0 inset-x-0 bg-white shadow-md z-[1000]"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-1">
      <nav class="w-full">
        <div class="flex justify-between items-center">
          <!-- Logo -->
          <a href="#" class="flex items-center h-14 overflow-hidden">
            <img 
              src="@/assets/imagenes/LOGO.svg" 
              alt="Fullness Logo"
              class="h-12 translate-y-2 object-contain transition-transform duration-300"
            >
          </a>

          <!-- Menú Hamburguesa (Mobile) -->
          <button
            @click="toggleMenu"
            class="md:hidden p-2 text-[#104e75] focus:outline-none"
          >
            <svg
              class="w-8 h-8"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
          </button>

          <!-- Enlaces de navegación (Desktop) - SIN CAMBIOS -->
          <div class="hidden md:flex gap-6 md:gap-12 items-center">
            <a
              href="#"
              class="text-[#104e75] hover:text-[#003157] transition-colors duration-300 font-medium text-base"
            >
              Inicio
            </a>
            <a
              href="#agendar-cita"
              class="text-[#104e75] hover:text-[#003157] transition-colors duration-300 font-medium text-base"
            >
              Servicio
            </a>
            <a
              href="#video-section"
              class="text-[#104e75] hover:text-[#003157] transition-colors duration-300 font-medium text-base"
            >
              Nosotros
            </a>
            <a
              href="#contacto"
              class="text-[#104e75] hover:text-[#003157] transition-colors duration-300 font-medium text-base"
            >
              Contacto
            </a>

            <div class="flex gap-4 ml-8">
              <template v-if="!isAuthenticated">
                <a
                  href="/login"
                  class="bg-[#104e75] text-white px-4 py-2 rounded-lg hover:bg-[#003157] transition-colors duration-300 font-medium text-base"
                >
                  Iniciar Sesión
                </a>
                <router-link
                  to="/registro"
                  class="bg-white text-[#104e75] border-2 border-[#104e75] px-4 py-2 rounded-lg hover:bg-[#104e75] hover:text-white transition-colors duration-300 font-medium text-base"
                >
                  Crear cuenta
                </router-link>
              </template>

              <div v-else class="flex items-center gap-4">
                <div
                  @click="logout"
                  class="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity"
                >
                  <div
                    class="w-8 h-8 bg-[#104e75] rounded-full flex items-center justify-center text-white"
                  >
                    <i class="fas fa-user"></i>
                  </div>
                  <span class="text-[#104e75] font-medium">Usuario</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- MENÚ MÓVIL MEJORADO (MISMAS FUNCIONALIDADES QUE DESKTOP) -->
        <div
          v-show="isMenuOpen"
          class="md:hidden fixed inset-0 z-[9999] bg-black/30 backdrop-blur-sm transition-all duration-300"
          :class="isMenuOpen ? 'opacity-100' : 'opacity-0 pointer-events-none'"
          @click="toggleMenu"
        >
          <div
            class="absolute top-0 right-0 w-[320px] h-full bg-white shadow-2xl transform transition-transform duration-500 ease-[cubic-bezier(0.22,1,0.36,1)]"
            :class="isMenuOpen ? 'translate-x-0' : 'translate-x-full'"
            @click.stop
          >
            <div class="h-full flex flex-col">
              <!-- Encabezado con logo -->
              <div
                class="px-6 py-5 border-b border-[#104e75]/10 flex items-center justify-between"
              >
                <img
                  src="@/assets/imagenes/LOGO.svg"
                  alt="Logo"
                  class="h-10 w-auto"
                />
                <button
                  @click="closeMenu"
                  class="w-8 h-8 flex items-center justify-center rounded-full bg-[#104e75]/10 hover:bg-[#104e75]/20 transition-colors"
                >
                  <svg
                    class="w-5 h-5 text-[#104e75]"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                </button>
              </div>

              <!-- Contenido del Menú -->
              <nav class="flex-1 overflow-y-auto px-6 py-6">
                <!-- Items de Navegación -->
                <div class="space-y-2 mb-6">
                  <a 
                    href="#" 
                    class="block px-4 py-3 rounded-lg text-[#104e75] hover:bg-[#f0f8ff] transition-colors font-medium"
                    @click="closeMenu"
                  >
                    Inicio
                  </a>
                  <a 
                    href="#agendar-cita" 
                    class="block px-4 py-3 rounded-lg text-[#104e75] hover:bg-[#f0f8ff] transition-colors font-medium"
                    @click="closeMenu"
                  >
                    Servicio
                  </a>
                  <a 
                    href="#video-section" 
                    class="block px-4 py-3 rounded-lg text-[#104e75] hover:bg-[#f0f8ff] transition-colors font-medium"
                    @click="closeMenu"
                  >
                    Nosotros
                  </a>
                  <a 
                    href="#contacto" 
                    class="block px-4 py-3 rounded-lg text-[#104e75] hover:bg-[#f0f8ff] transition-colors font-medium"
                    @click="closeMenu"
                  >
                    Contacto
                  </a>
                </div>

                <!-- Separador -->
                <div class="relative my-6">
                  <div class="absolute inset-0 flex items-center">
                    <div class="w-full border-t border-[#104e75]/10"></div>
                  </div>
                  <div class="relative flex justify-center">
                    <span class="px-3 bg-white text-xs text-[#448ba9] font-medium">ACCESO RÁPIDO</span>
                  </div>
                </div>

                <!-- Sección de Autenticación (IGUAL QUE DESKTOP PERO ADAPTADO A MÓVIL) -->
                <div class="space-y-4">
                  <template v-if="!isAuthenticated">
                    <a
                      href="/login"
                      class="block w-full bg-[#104e75] text-white px-6 py-3 rounded-lg font-medium text-center hover:bg-[#003157] transition-colors"
                    >
                      Iniciar Sesión
                    </a>
                    <router-link
                      to="/registro"
                      class="block w-full bg-white text-[#104e75] border-2 border-[#104e75] px-6 py-3 rounded-lg font-medium text-center hover:bg-[#104e75] hover:text-white transition-colors"
                    >
                      Crear cuenta
                    </router-link>
                  </template>

                  <div v-else class="space-y-3">
                    <div
                      @click="logout"
                      class="flex items-center gap-3 p-4 rounded-lg cursor-pointer hover:bg-[#f0f8ff] transition-colors"
                    >
                      <div
                        class="w-10 h-10 bg-[#104e75] rounded-full flex items-center justify-center text-white"
                      >
                        <i class="fas fa-user"></i>
                      </div>
                      <div>
                        <p class="text-[#104e75] font-medium">Usuario</p>
                        <p class="text-xs text-[#448ba9]">Ver perfil</p>
                      </div>
                    </div>
                    <button
                      @click="logout"
                      class="w-full text-[#104e75] hover:text-[#003157] py-2 transition-colors text-left px-4"
                    >
                      Cerrar sesión
                    </button>
                  </div>
                </div>

                <!-- Footer del menú -->
                <div class="mt-8 pt-6 border-t border-[#104e75]/10 text-center">
                  <p class="text-xs text-[#448ba9]">© 2024 Fullness</p>
                </div>
              </nav>
            </div>
          </div>
        </div>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      isMenuOpen: false,
      isAuthenticated: false
    }
  },
  created() {
    const isLoggedIn = localStorage.getItem("isAuthenticated") === "true";
    this.isAuthenticated = isLoggedIn;
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    closeMenu() {
      this.isMenuOpen = false;
    },
    logout() {
      localStorage.removeItem('isAuthenticated');
      this.isAuthenticated = false;
      this.isMenuOpen = false;
      window.location.reload();
    }
  }
}
</script>

<style scoped>
/* Estilos extraídos de HomeView que aplicaban al menú */
@keyframes menuEntry {
   0% {
     transform: translateX(100%);
     opacity: 0;
   }
   100% {
     transform: translateX(0);
     opacity: 1;
   }
 }

 .backdrop-blur-sm {
   backdrop-filter: blur(4px);
 }

 .ease-\[cubic-bezier\(0\.4\,0\,0\.2\,1\)\] {
   transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
 }
</style>
