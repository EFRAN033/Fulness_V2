<template>
  <footer class="bg-gradient-to-b from-[#104e75] to-[#003157] text-[#dee3e9] shadow-xl" id="contacto">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4 md:gap-6 py-6 border-b border-[#b7ebfa]/20">
        
        <!-- Logo y Especialidades -->
        <div class="space-y-2 md:space-y-3">
          <div class="flex items-center gap-2">
            <img 
              src="@/assets/imagenes/LOGO.svg" 
              alt="Fullness"
              class="h-14 w-14 md:h-16 md:w-16 object-contain rounded-none fill-current text-[#dee3e9]"
            >
            <div>
              <span class="text-base md:text-lg font-bold text-[#dee3e9]">Fullness</span>
              <p class="text-[0.6rem] md:text-[0.7rem] text-[#448ba9]/90 mt-0.5">Colegiados CIP N° 28456</p>
            </div>
          </div>
          <ul class="hidden md:block space-y-1 md:space-y-1.5 text-xs text-[#448ba9]">
            <li class="flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5 text-[#448ba9]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
              </svg>
              Rehabilitación integral
            </li>
            <li class="flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5 text-[#448ba9]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
              </svg>
              Lesiones deportivas
            </li>
            <li class="flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5 text-[#448ba9]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
              </svg>
              Dolor crónico
            </li>
          </ul>
        </div>

        <!-- Garantías -->
        <div class="space-y-2 md:space-y-3">
          <h4 class="text-[#dee3e9] font-medium text-xs uppercase tracking-wide mb-1 flex items-center gap-1.5">
            <svg class="w-4 h-4 text-[#448ba9]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            Garantía
          </h4>
          <div class="space-y-2 text-xs">
            <div class="bg-[#003157]/30 p-1.5 md:p-2 rounded-md flex items-center gap-2">
              <svg class="w-4 h-4 text-[#448ba9] flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <div>
                <p class="text-[#dee3e9] text-sm md:text-base">Satisfacción</p>
                <p class="text-[0.6rem] md:text-[0.65rem] text-[#448ba9]/90">Reembolso 1ra sesión</p>
              </div>
            </div>
            <div class="bg-[#003157]/30 p-1.5 md:p-2 rounded-md flex items-center gap-2">
              <svg class="w-4 h-4 text-[#448ba9] flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
              </svg>
              <div>
                <p class="text-[#dee3e9] text-sm md:text-base">8 Distritos</p>
                <p class="text-[0.6rem] md:text-[0.65rem] text-[#448ba9]/90">Incluyendo JM y MF</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Contacto -->
        <div class="space-y-2 md:space-y-3">
          <h4 class="text-[#dee3e9] font-medium text-xs uppercase tracking-wide mb-1 flex items-center gap-1.5">
            <svg class="w-4 h-4 text-[#448ba9]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h18M3 12h18m-18 7h18"/>
            </svg>
            Contacto
          </h4>
          <div class="space-y-2 text-xs">
            <a href="tel:+51987654321" class="flex items-center gap-2 group">
              <div class="p-1 bg-[#003157]/30 rounded-md group-hover:bg-[#104e75]/40 transition-colors">
                <svg class="w-4 h-4 text-[#448ba9]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h18M3 12h18m-18 7h18"/>
                </svg>
              </div>
              <div>
                <p class="text-[#dee3e9] text-sm md:text-base">+51 941 609 887</p>
                <p class="text-[0.6rem] md:text-[0.65rem] text-[#448ba9]/90">Llamada/WhatsApp</p>
              </div>
            </a>
            <a href="mailto:hola@fiofulnes.com" class="flex items-center gap-2 group">
              <div class="p-1 bg-[#003157]/30 rounded-md group-hover:bg-[#104e75]/40 transition-colors">
                <svg class="w-4 h-4 text-[#448ba9]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                </svg>
              </div>
              <div>
                <p class="text-[#dee3e9] text-sm md:text-base">hola@fiofulnes.com</p>
                <p class="text-[0.6rem] md:text-[0.65rem] text-[#448ba9]/90">Respuesta en 24h</p>
              </div>
            </a>
          </div>
        </div>

        <!-- Redes Sociales -->
        <div class="space-y-2 md:space-y-3">
          <h4 class="text-[#dee3e9] font-medium text-xs uppercase tracking-wide mb-1 flex items-center gap-1.5">
            <svg class="w-4 h-4 text-[#448ba9]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
            </svg>
            Redes
          </h4>
          <div class="grid grid-cols-3 gap-1 md:gap-2">
            <a href="https://wa.me/51987654321" target="_blank" class="p-1.5 md:p-2 bg-[#003157]/30 hover:bg-[#104e75]/40 rounded-md flex flex-col items-center transition-all group">
              <svg class="w-5 h-5 text-[#448ba9] group-hover:text-[#b7ebfa] mb-1" fill="currentColor" viewBox="0 0 24 24">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
              </svg>
              <span class="text-[0.6rem] md:text-[0.65rem] text-[#448ba9] group-hover:text-[#b7ebfa]">WhatsApp</span>
            </a>
            <a href="https://facebook.com" target="_blank" class="p-1.5 md:p-2 bg-[#003157]/30 hover:bg-[#104e75]/40 rounded-md flex flex-col items-center transition-all group">
              <svg class="w-5 h-5 text-[#448ba9] group-hover:text-[#b7ebfa] mb-1" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm3 8h-1.35c-.538 0-.65.221-.65.778v1.222h2l-.209 2h-1.791v7h-3v-7h-2v-2h2v-2.308c0-1.769.931-2.692 3.029-2.692h1.971v3z"/>
              </svg>
              <span class="text-[0.6rem] md:text-[0.65rem] text-[#448ba9] group-hover:text-[#b7ebfa]">Facebook</span>
            </a>
            <a href="https://instagram.com" target="_blank" class="p-1.5 md:p-2 bg-[#003157]/30 hover:bg-[#104e75]/40 rounded-md flex flex-col items-center transition-all group">
              <svg class="w-5 h-5 text-[#448ba9] group-hover:text-[#b7ebfa] mb-1" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
              </svg>
              <span class="text-[0.6rem] md:text-[0.65rem] text-[#448ba9] group-hover:text-[#b7ebfa]">Instagram</span>
            </a>
          </div>
        </div>
      </div>
      <div class="py-4 flex flex-col md:flex-row justify-between items-center gap-2 text-[0.6rem] md:text-[0.65rem]">
        <div class="text-[#448ba9]/80 text-center order-last md:order-first">
          © 2024 Fulness - Todos los derechos reservados
        </div>
        <div class="flex flex-col md:flex-row items-center divide-x-0 md:divide-x divide-[#104e75]">
          <a href="#" class="px-2 text-[#448ba9]/80 hover:text-[#dee3e9]">Políticas</a>
          <a href="#" class="px-2 text-[#448ba9]/80 hover:text-[#dee3e9]">Términos</a>
          <a href="#" class="px-2 text-[#448ba9]/80 hover:text-[#dee3e9]">Soporte</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer"
}
</script>
