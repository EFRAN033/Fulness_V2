<template>
  <div class="relative w-full min-h-[550px] lg:min-h-[600px] overflow-hidden flex items-center">
    <!-- Background Image -->
    <img 
      src="@/assets/imagenes/imagen-de-fondo.jpg" 
      alt="Imagen de Fondo"
      class="absolute inset-0 w-full h-full object-cover z-0"
    >

    <!-- Overlay -->
    <div class="absolute inset-0 bg-black/40 z-0"></div>

    <!-- Main Content Container (Relative now, for content-driven height) -->
    <div class="relative z-10 w-full py-12 md:py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center">
        <!-- Sección de Marketing Izquierda -->
        <div class="text-white max-w-2xl space-y-8 w-full md:w-1/2">
          <h1 class="text-4xl md:text-5xl font-bold leading-tight">
            Fisioterapia Profesional 
            <span class="bg-gradient-to-r from-[#448ba9] to-[#87CEEB] bg-clip-text text-transparent">en tu Domicilio</span>
          </h1>
          
          <div class="space-y-5">
            <div class="flex items-center space-x-4">
              <div class="w-9 h-9 bg-[#104e75] rounded-full flex items-center justify-center shrink-0">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
              </div>
              <p class="text-lg font-semibold">Servicio 100% domiciliario - Sin costos adicionales</p>
            </div>
            
            <div class="flex items-center space-x-4">
              <div class="w-9 h-9 bg-[#104e75] rounded-full flex items-center justify-center shrink-0">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <p class="text-lg font-semibold">Primera sesión con 20% de descuento inmediato</p>
            </div>
          </div>

          <div class="bg-white/10 p-6 rounded-xl backdrop-blur-sm border border-white/20">
            <div class="flex items-center gap-4 mb-3">
              <div class="bg-[#448ba9] text-white px-4 py-1 rounded-full text-sm font-medium">
                +3000 pacientes
              </div>
              <p class="text-lg font-semibold">atendidos en su domicilio</p>
            </div>
            <div class="border-l-2 border-[#448ba9] pl-4">
              <p class="text-sm opacity-90 mb-2">Especialidades principales:</p>
              <ul class="space-y-1 font-medium">
                <li>• Rehabilitación física integral en casa</li>
                <li>• Terapia para lesiones deportivas</li>
                <li>• Manejo de dolor crónico</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Formulario Derecho - Versión Desktop (Relative inside flex) -->
        <div class="hidden md:flex w-1/2 justify-end pointer-events-none">
           <div class="pointer-events-auto w-[90%] max-w-md">
      <form @submit.prevent="guardarCita" class="bg-white p-6 rounded-xl shadow-2xl w-full backdrop-blur-sm border border-white/20 relative">
        <!-- Badge -->
        <div class="absolute -top-3 left-1/2 -translate-x-1/2 bg-[#003157] text-white px-4 py-1 rounded-full text-sm font-medium shadow-lg flex items-center">
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
          </svg>
          Agenda Prioritizada
        </div>

        <h2 class="text-xl font-bold text-center mb-4 text-[#104e75]">
          <span class="text-[#003157]">Reserva tu Cita</span>
          <span class="block text-sm font-normal text-[#448ba9] mt-1">en 3 simples pasos</span>
        </h2>

        <!-- Indicador -->
        <div class="text-center mb-4">
          <div class="inline-flex items-center bg-[#b7ebfa] px-3 py-1 rounded-full text-sm text-[#003157]">
            <span class="w-2 h-2 bg-[#448ba9] rounded-full animate-pulse mr-2"></span>
            <span>Horarios disponibles hoy</span>
          </div>
        </div>

        <div class="space-y-4">
          <div class="grid grid-cols-2 gap-3">
            <div>
              <label class="block text-xs font-semibold text-[#104e75] mb-1">Nombre</label>
              <input 
                  v-model="formData.nombre"
                  type="text" 
                  class="w-full px-3 py-2.5 border-2 border-[#dee3e9] rounded-lg placeholder-[#448ba9] text-sm focus:border-[#003157] focus:ring-2 focus:ring-[#b7ebfa] transition-all outline-none" 
                  placeholder="Ej: María"
                >
            </div>
            
            <div>
              <label class="block text-xs font-semibold text-[#104e75] mb-1">Apellido</label>
              <input 
                v-model="formData.apellido"
                type="text" 
                class="w-full px-3 py-2.5 border-2 border-[#dee3e9] rounded-lg placeholder-[#448ba9] text-sm focus:border-[#003157] focus:ring-2 focus:ring-[#b7ebfa] transition-all outline-none" 
                placeholder="Ej: González"
              >
            </div>
          </div>

          <div>
            <label class="block text-xs font-semibold text-[#104e75] mb-1">Tipo de Paciente *</label>
            <div class="grid grid-cols-2 gap-2">
              <button 
                type="button"
                @click="formData.tipo_paciente = 'nuevo'"
                :class="[
                  'text-sm py-2 px-3 rounded-lg transition-all font-medium flex items-center justify-center',
                  formData.tipo_paciente === 'nuevo' 
                    ? 'border-2 border-[#003157] bg-[#e3f6fd] text-[#003157] shadow-inner'
                    : 'border-2 border-[#dee3e9] bg-white hover:border-[#448ba9]'
                ]"
              >
                <svg 
                  v-if="formData.tipo_paciente === 'nuevo'"
                  class="w-4 h-4 mr-1 text-[#003157]" 
                  fill="none" 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                Nuevo Paciente
              </button>
              
              <button 
                type="button"
                @click="formData.tipo_paciente = 'antiguo'"
                :class="[
                  'text-sm py-2 px-3 rounded-lg transition-all font-medium flex items-center justify-center',
                  formData.tipo_paciente === 'antiguo' 
                    ? 'border-2 border-[#003157] bg-[#e3f6fd] text-[#003157] shadow-inner'
                    : 'border-2 border-[#dee3e9] bg-white hover:border-[#448ba9]'
                ]"
              >
                <svg 
                  v-if="formData.tipo_paciente === 'antiguo'"
                  class="w-4 h-4 mr-1 text-[#003157]" 
                  fill="none" 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                Paciente Antiguo
              </button>
            </div>
            <p v-if="!formData.tipo_paciente" class="text-red-500 text-xs mt-1">* Debes seleccionar un tipo de paciente</p>
          </div>

          <div>
            <label class="block text-xs font-semibold text-[#104e75] mb-1">Correo Electrónico</label>
            <input 
              v-model="formData.email"
              type="email" 
              class="w-full px-3 py-2.5 border-2 border-[#dee3e9] rounded-lg placeholder-[#448ba9] text-sm focus:border-[#003157] focus:ring-2 focus:ring-[#b7ebfa] transition-all outline-none" 
              placeholder="tucorreo@gm.com"
            >
          </div>

          <div>
            <label class="block text-xs font-semibold text-[#104e75] mb-1">Celular</label>
            <input 
              v-model="formData.celular"
              type="tel" 
              class="w-full px-3 py-2.5 border-2 border-[#dee3e9] rounded-lg placeholder-[#448ba9] text-sm focus:border-[#003157] focus:ring-2 focus:ring-[#b7ebfa] transition-all outline-none" 
              placeholder="Ej: 999 999 999"
            >
          </div>

          <div class="grid grid-cols-2 gap-3">
            <div>
              <label class="block text-xs font-semibold text-[#104e75] mb-1">Distrito</label>
              <select 
                v-model="formData.distrito"
                class="w-full px-3 py-2.5 border-2 border-[#dee3e9] rounded-lg text-sm focus:border-[#003157] focus:ring-2 focus:ring-[#b7ebfa] transition-all outline-none appearance-none bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cG9seWxpbmUgcG9pbnRzPSI2IDkgMTIgMTUgMTggOSIvPjwvc3ZnPg==')] bg-no-repeat bg-[right:0.75rem_center] bg-[length:1em]"
              >
                <option value="" class="text-[#448ba9]">Seleccione distrito</option>
                <option>Jesús María</option>
                <option>Miraflores</option>
                <option>San Isidro</option>
              </select>
            </div>

            <div>
              <label class="block text-xs font-semibold text-[#104e75] mb-1">Servicio</label>
              <select 
                v-model="formData.servicio"
                class="w-full px-3 py-2.5 border-2 border-[#dee3e9] rounded-lg text-sm focus:border-[#003157] focus:ring-2 focus:ring-[#b7ebfa] transition-all outline-none appearance-none bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cG9seWxpbmUgcG9pbnRzPSI2IDkgMTIgMTUgMTggOSIvPjwvc3ZnPg==')] bg-no-repeat bg-[right:0.75rem_center] bg-[length:1em]"
              >
                <option value="" class="text-[#448ba9]">Seleccione servicio</option>
                <option>Fisioterapia Domiciliaria</option>
                <option>Consulta Virtual</option>
              </select>
            </div>
          </div>
        </div>

        <button 
          type="submit"
          class="w-full bg-gradient-to-r from-[#003157] to-[#104e75] text-white py-3 rounded-lg font-semibold text-sm hover:from-[#00203a] hover:to-[#0d3a5d] transition-all duration-300 shadow-md hover:shadow-lg mt-4 flex items-center justify-center"
        >
          Confirmar Reserva
          <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
          </svg>
        </button>

        <!-- Garantía -->
        <div class="text-center mt-4">
          <p class="text-xs text-[#448ba9] flex items-center justify-center space-x-2">
            <svg class="w-4 h-4 text-[#003157]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
            </svg>
            <span>Protección de datos garantizada · Sin cargos ocultos</span>
          </p>
        </div>
      </form>
        </div>
       </div> <!-- Closing md:flex w-1/2 -->
      </div> <!-- Closing max-w-7xl -->
    </div> <!-- Closing relative z-10 w-full -->

    <!-- Botón flotante móvil (MOVED OUTSIDE) -->
    <button 
      @click="showForm = true"
      class="md:hidden fixed bottom-6 right-4 bg-[#104e75] text-white px-6 py-3 rounded-full shadow-xl z-50 flex items-center gap-2 animate-bounce"
    >
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
      </svg>
      Reservar Cita
    </button>
  </div> <!-- Closing main wrapper -->

    <!-- Formulario Derecho - Versión Mobile -->
    <div 
      v-show="showForm"
      class="md:hidden fixed inset-0 bg-black/50 z-[2000] flex items-center justify-center p-4"
      @click.self="showForm = false"
    >
      <form class="bg-white p-6 rounded-xl w-full max-w-md max-h-[90vh] overflow-y-auto relative">
        <!-- Badge -->
        <div class="absolute -top-3 left-1/2 -translate-x-1/2 bg-[#003157] text-white px-4 py-1 rounded-full text-sm font-medium shadow-lg flex items-center">
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
          </svg>
          Agenda Prioritizada
        </div>

        <!-- Botón cerrar -->
        <button 
          @click="showForm = false"
          class="absolute top-4 right-4 text-[#448ba9] hover:text-[#003157]"
        >
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>

        <h2 class="text-xl font-bold text-center mb-4 text-[#104e75] pt-4">
          <span class="text-[#003157]">Reserva tu Cita</span>
          <span class="block text-sm font-normal text-[#448ba9] mt-1">en 3 simples pasos</span>
        </h2>

        <!-- Indicador -->
        <div class="text-center mb-4">
          <div class="inline-flex items-center bg-[#b7ebfa] px-3 py-1 rounded-full text-sm text-[#003157]">
            <span class="w-2 h-2 bg-[#448ba9] rounded-full animate-pulse mr-2"></span>
            <span>Horarios disponibles hoy</span>
          </div>
        </div>

        <div class="space-y-4">
          <div class="grid grid-cols-1 gap-3">
            <div>
              <label class="block text-xs font-semibold text-[#104e75] mb-1">Nombre</label>
              <input type="text" v-model="formData.nombre" class="w-full px-3 py-2.5 border-2 border-[#dee3e9] rounded-lg placeholder-[#448ba9] text-sm focus:border-[#003157] focus:ring-2 focus:ring-[#b7ebfa] transition-all outline-none" placeholder="Ej: María">
            </div>
            
            <div>
              <label class="block text-xs font-semibold text-[#104e75] mb-1">Apellido</label>
              <input type="text" v-model="formData.apellido" class="w-full px-3 py-2.5 border-2 border-[#dee3e9] rounded-lg placeholder-[#448ba9] text-sm focus:border-[#003157] focus:ring-2 focus:ring-[#b7ebfa] transition-all outline-none" placeholder="Ej: González">
            </div>
          </div>

          <div>
            <label class="block text-xs font-semibold text-[#104e75] mb-1">Tipo de Paciente *</label>
            <div class="grid grid-cols-2 gap-2">
              <button 
                type="button"
                @click="selectPatientType('nuevo')"
                :class="[
                  'text-sm py-2 px-3 rounded-lg transition-all font-medium flex items-center justify-center',
                  selectedPatientType === 'nuevo' 
                    ? 'border-2 border-[#003157] bg-[#e3f6fd] text-[#003157] shadow-inner'
                    : 'border-2 border-[#dee3e9] bg-white hover:border-[#448ba9]'
                ]"
              >
                <svg 
                  v-if="selectedPatientType === 'nuevo'"
                  class="w-4 h-4 mr-1 text-[#003157]" 
                  fill="none" 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                Nuevo Paciente
              </button>
              
              <button 
                type="button"
                @click="selectPatientType('antiguo')"
                :class="[
                  'text-sm py-2 px-3 rounded-lg transition-all font-medium flex items-center justify-center',
                  selectedPatientType === 'antiguo' 
                    ? 'border-2 border-[#003157] bg-[#e3f6fd] text-[#003157] shadow-inner'
                    : 'border-2 border-[#dee3e9] bg-white hover:border-[#448ba9]'
                ]"
              >
                <svg 
                  v-if="selectedPatientType === 'antiguo'"
                  class="w-4 h-4 mr-1 text-[#003157]" 
                  fill="none" 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                Paciente Antiguo
              </button>
            </div>
            <p v-if="!selectedPatientType" class="text-red-500 text-xs mt-1">* Debes seleccionar un tipo de paciente</p>
          </div>

          <div>
            <label class="block text-xs font-semibold text-[#104e75] mb-1">Correo Electrónico</label>
            <input type="email" v-model="formData.email" class="w-full px-3 py-2.5 border-2 border-[#dee3e9] rounded-lg placeholder-[#448ba9] text-sm focus:border-[#003157] focus:ring-2 focus:ring-[#b7ebfa] transition-all outline-none" placeholder="tucorreo@gm.com">
          </div>

          <div>
            <label class="block text-xs font-semibold text-[#104e75] mb-1">Celular</label>
            <input type="tel" v-model="formData.celular" class="w-full px-3 py-2.5 border-2 border-[#dee3e9] rounded-lg placeholder-[#448ba9] text-sm focus:border-[#003157] focus:ring-2 focus:ring-[#b7ebfa] transition-all outline-none" placeholder="Ej: 999 999 999">
          </div>

          <div class="grid grid-cols-1 gap-3">
            <div>
              <label class="block text-xs font-semibold text-[#104e75] mb-1">Distrito</label>
              <select v-model="formData.distrito" class="w-full px-3 py-2.5 border-2 border-[#dee3e9] rounded-lg text-sm focus:border-[#003157] focus:ring-2 focus:ring-[#b7ebfa] transition-all outline-none appearance-none bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cG9seWxpbmUgcG9pbnRzPSI2IDkgMTIgMTUgMTggOSIvPjwvc3ZnPg==')] bg-no-repeat bg-[right:0.75rem_center] bg-[length:1em]">
                <option class="text-[#448ba9]">Seleccione distrito</option>
                <option>Jesus Maria</option>
                <option>Miraflores</option>
                <option>San Isidro</option>
              </select>
            </div>

            <div>
              <label class="block text-xs font-semibold text-[#104e75] mb-1">Servicio</label>
              <select v-model="formData.servicio" class="w-full px-3 py-2.5 border-2 border-[#dee3e9] rounded-lg text-sm focus:border-[#003157] focus:ring-2 focus:ring-[#b7ebfa] transition-all outline-none appearance-none bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cG9seWxpbmUgcG9pbnRzPSI2IDkgMTIgMTUgMTggOSIvPjwvc3ZnPg==')] bg-no-repeat bg-[right:0.75rem_center] bg-[length:1em]">
                <option class="text-[#448ba9]">Seleccione servicio</option>
                <option>Fisioterapia Domiciliaria</option>
                <option>Consulta Virtual</option>
              </select>
            </div>
          </div>
        </div>

        <button @click="guardarCita" type="button" class="w-full bg-gradient-to-r from-[#003157] to-[#104e75] text-white py-3 rounded-lg font-semibold text-sm hover:from-[#00203a] hover:to-[#0d3a5d] transition-all duration-300 shadow-md hover:shadow-lg mt-4 flex items-center justify-center">
          Confirmar Reserva
          <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
          </svg>
        </button>

        <!-- Garantía -->
        <div class="text-center mt-4">
          <p class="text-xs text-[#448ba9] flex items-center justify-center space-x-2">
            <svg class="w-4 h-4 text-[#003157]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
            </svg>
            <span>Protección de datos garantizada · Sin cargos ocultos</span>
          </p>
        </div>
      </form>
    </div>

</template>

<script>
export default {
  name: "HeroSection",
  data() {
    return {
      showForm: false,
      loading: false,
      selectedPatientType: "",
      formData: {
        nombre: "",
        apellido: "",
        email: "",
        celular: "",
        distrito: "",
        servicio: "",
        tipo_paciente: "",
      },
      errors: {
        email: "",
        celular: "",
      },
    };
  },
  methods: {
    selectPatientType(type) {
      this.selectedPatientType = type;
      this.formData.tipo_paciente = type;
    },
    validateEmail() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!this.formData.email) {
        this.errors.email = "El email es requerido";
      } else if (!emailRegex.test(this.formData.email)) {
        this.errors.email = "Ingresa un email válido";
      } else {
        this.errors.email = "";
      }
    },
    validateCelular() {
      if (!this.formData.celular) {
        this.errors.celular = "El celular es requerido";
      } else if (this.formData.celular.length !== 9 || !/^[0-9]+$/.test(this.formData.celular)) {
        this.errors.celular = "Ingresa un número válido (9 dígitos)";
      } else {
        this.errors.celular = "";
      }
    },
    validateForm() {
      this.validateEmail();
      this.validateCelular();
      if (!this.formData.tipo_paciente) {
        return false;
      }
      const requiredFields = ["nombre", "apellido", "email", "celular", "distrito", "servicio"];
      const isValid = requiredFields.every((field) => !!this.formData[field]);
      const hasErrors = Object.values(this.errors).some((error) => error !== "");
      return isValid && !hasErrors;
    },
    async guardarCita() {
      try {
        if (!this.validateForm()) {
          console.log("Validación de formulario fallida");
          return;
        }
        this.loading = true;
        const ahora = new Date();
        const fechaHora = ahora.toISOString();
        const servicioId = this.formData.servicio === "Fisioterapia Domiciliaria" ? 1 : 2;
        const citaData = {
          id_paciente: 1, // Esto debería venir de algún lado, pero por ahora lo dejo fijo como estaba
          id_especialista: 1,
          id_servicio: servicioId,
          fecha_hora: fechaHora,
          dolencia: "Consulta inicial - " + this.formData.distrito,
        };
        const response = await fetch("http://localhost:5000/api/citas/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(citaData),
        });
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.message || "Error al guardar la cita");
        }
        const result = await response.json();
        alert("¡Cita reservada con éxito!");
        console.log("Cita creada:", result);
        this.resetForm();
        this.showForm = false;
      } catch (error) {
        console.error("Error al guardar cita:", error);
        alert(`Error: ${error.message}`);
      } finally {
        this.loading = false;
      }
    },
    resetForm() {
      this.formData = {
        nombre: "",
        apellido: "",
        email: "",
        celular: "",
        distrito: "",
        servicio: "",
        tipo_paciente: "",
      };
      this.errors = { email: "", celular: "" };
      this.selectedPatientType = "";
    },
  },
};
</script>
