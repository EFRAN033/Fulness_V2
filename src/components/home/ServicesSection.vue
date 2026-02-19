<template>
  <div class="relative py-8 md:py-10 bg-gradient-to-br from-[#dee3e9]/10 to-[#b7ebfa]/10 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="relative bg-white sm:rounded-xl shadow-lg border-y sm:border border-[#dee3e9]">
        <div class="absolute -left-6 -top-6 w-24 h-24 bg-[#448ba9]/5 rounded-full blur"></div>
        <div class="absolute -right-6 -bottom-6 w-24 h-24 bg-[#104e75]/5 rounded-full blur"></div>
        
        <div class="p-6 sm:p-8 lg:p-10">
          <div class="text-center space-y-6">
            <!-- Encabezado -->
            <div class="space-y-2">
              <h3 class="text-2xl sm:text-3xl font-bold text-[#104e75]">
                Disponibilidad Inmediata
              </h3>
              <p class="text-lg sm:text-xl text-[#448ba9] font-medium">
                Nuestros fisioterapeutas están listos para atenderte
              </p>
            </div>

            <!-- Botón principal -->
            <button 
              @click="showModal = true"
              class="bg-gradient-to-r from-[#003157] to-[#104e75] text-white px-8 py-3.5 rounded-full font-semibold hover:from-[#00203a] hover:to-[#0d3a5d] transition-all duration-300 shadow-md hover:shadow-lg flex items-center justify-center mx-auto group relative w-full max-w-xs sm:max-w-sm"
            >
              <span class="relative z-10 flex items-center">
                Seleccionar profesional
                <svg class="w-4 h-4 ml-2 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                </svg>
              </span>
            </button>

            <!-- Info adicional -->
            <div class="flex items-center justify-center space-x-3 text-sm sm:text-base text-[#448ba9]">
              <svg class="w-5 h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <span>Horarios flexibles de 7:00 AM a 9:00 PM</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Ola decorativa inferior -->
    <div class="absolute inset-x-0 bottom-0 h-24 -mb-1">
      <svg viewBox="0 0 1440 120" class="w-full h-full text-[#b7ebfa]/20">
        <path fill="currentColor" d="M0,96L48,90.7C96,85,192,75,288,74.7C384,75,480,85,576,106.7C672,128,768,160,864,160C960,160,1056,128,1152,106.7C1248,85,1344,75,1392,69.3L1440,64L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
      </svg>
    </div>
  

    <!-- Modal -->
    <div v-if="showModal" class="fixed inset-0 bg-black/50 z-[2000] flex items-center justify-center p-4">
      <div class="bg-[#dee3e9] rounded-xl max-w-md w-full shadow-2xl border border-[#104e75]">
        <div class="p-5 border-b border-[#104e75] flex justify-between items-center">
          <h3 class="text-lg font-semibold text-[#003157]">Selecciona un fisioterapeuta y fecha</h3>
          <button @click="showModal = false" class="text-[#448ba9] hover:text-[#003157] transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>

        <div class="p-6 space-y-5">
          <div>
            <label class="block text-sm font-medium text-[#104e75] mb-2">Fisioterapeuta:</label>
            <select class="w-full px-4 py-2.5 border-2 border-[#dee3e9] rounded-lg focus:border-[#104e75] focus:ring-2 focus:ring-[#b7ebfa] text-sm transition-all">
              <option disabled selected class="text-[#448ba9]">Seleccione profesional</option>
              <option class="text-[#003157]">Rodrigo Fernández</option>
              <option class="text-[#003157]">Ana Martínez</option>
              <option class="text-[#003157]">Carlos Gutierrez</option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-medium text-[#104e75] mb-2">Fecha de atención:</label>
            <input 
              type="date" 
              class="w-full px-4 py-2.5 border-2 border-[#dee3e9] rounded-lg focus:border-[#104e75] focus:ring-2 focus:ring-[#b7ebfa] text-sm transition-all"
              placeholder="dd/mm/aaaa"
            >
          </div>

          <div>
            <label class="block text-sm font-medium text-[#104e75] mb-2">Describe tu dolencia:</label>
            <textarea 
              rows="3"
              class="w-full px-4 py-2.5 border-2 border-[#dee3e9] rounded-lg focus:border-[#104e75] focus:ring-2 focus:ring-[#b7ebfa] text-sm placeholder-[#448ba9] transition-all"
              placeholder="Ej. Dolor de espalda, lesión deportiva..."
            ></textarea>
          </div>

          <button class="w-full bg-gradient-to-r from-[#003157] to-[#104e75] text-white py-2.5 rounded-lg font-medium hover:from-[#00203a] hover:to-[#0d3a5d] transition-all flex items-center justify-center gap-2">
            <svg class="w-4 h-4 text-[#b7ebfa]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
            </svg>
            Confirmar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ServicesSection",
  data() {
    return {
      showModal: false
    }
  }
}
</script>
