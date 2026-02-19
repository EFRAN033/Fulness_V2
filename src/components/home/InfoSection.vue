<template>
  <div>
    <!-- Separador de sección -->
    <div class="h-[1px] bg-gradient-to-r from-transparent via-blue-200 to-transparent"></div>
    <!-- Sección Calendly - Con Acceso a Video Tutorial -->
    <div class="bg-gradient-to-br from-gray-50 to-blue-50 py-8 md:py-12" id="agendar-cita">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-2 gap-7 lg:gap-9 items-start">
          <!-- Contenido Informativo -->
          <div class="text-center lg:text-left space-y-5">
            <div class="space-y-4">
              <h2 class="text-3xl md:text-4xl font-bold text-brand-dark leading-tight">
                <span class="block text-brand-primary mb-2">Agenda Tu Sesión</span>
                <span class="block text-xl md:text-2xl text-brand-accent font-medium">Fisioterapia a Domicilio</span>
              </h2>
            
              <div class="inline-flex items-center bg-white px-4 py-2 rounded-lg shadow-sm border border-brand-light hover:border-brand-accent transition-colors">
                <svg class="w-5 h-5 text-brand-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <div class="text-left">
                  <p class="text-brand-secondary font-medium text-sm md:text-base">Sesión de 30 min</p>
                  <p class="text-xs md:text-sm text-brand-accent">Evaluación completa incluida</p>
                </div>
              </div>
            </div>

            <!-- Tarjeta de Precio -->
            <div class="bg-gradient-to-br from-brand-primary to-brand-secondary rounded-xl p-4 shadow-lg">
              <div class="flex items-center justify-between text-white">
                <div>
                  <p class="text-lg md:text-xl font-bold">Evaluación Inicial</p>
                  <p class="text-xs md:text-sm opacity-90 mt-1">Diagnóstico personalizado</p>
                </div>
                <div class="text-right">
                  <p class="text-3xl md:text-4xl font-bold">S/xxx</p>
                  <p class="text-[0.7rem] md:text-xs opacity-90">precio único</p>
                </div>
              </div>
              <div class="mt-3 pt-3 border-t border-brand-light/30 flex items-center">
                <svg class="w-4 h-4 text-brand-light mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                </svg>
                <span class="text-xs md:text-sm font-medium text-brand-light">Cobertura: Jesús María, San Isidro, Miraflores</span>
              </div>
            </div>

            <!-- Acceso a Video Tutorial -->
            <div class="group transition-transform hover:scale-[1.02]">
              <a href="#video-tutorial" target="_blank" class="inline-flex items-center w-full bg-brand-light hover:bg-brand-primary px-4 py-2.5 rounded-lg shadow-sm transition-colors">
                <svg class="w-5 h-5 text-brand-secondary group-hover:text-white mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <div class="text-left">
                  <p class="text-sm md:text-base font-medium text-brand-secondary group-hover:text-white">¿Cómo agendar?</p>
                  <p class="text-xs md:text-sm text-brand-accent group-hover:text-brand-light">Ver video tutorial</p>
                </div>
              </a>
            </div>

            <!-- Beneficios -->
            <div class="grid gap-3">
              <div class="p-3 bg-white rounded-lg shadow-sm border border-[#dee3e9] hover:border-brand-accent transition-colors flex items-center">
                <div class="w-8 h-8 bg-brand-light rounded-md flex items-center justify-center mr-3">
                  <svg class="w-4 h-4 text-brand-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                </div>
                <div>
                  <p class="text-sm md:text-base text-brand-secondary">Cancelación flexible</p>
                  <p class="text-xs md:text-sm text-brand-accent">Gratuita hasta 24h antes</p>
                </div>
              </div>
            
              <div class="p-3 bg-white rounded-lg shadow-sm border border-[#dee3e9] hover:border-brand-accent transition-colors flex items-center">
                <div class="w-8 h-8 bg-brand-light rounded-md flex items-center justify-center mr-3">
                  <svg class="w-4 h-4 text-brand-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
                  </svg>
                </div>
                <div>
                  <p class="text-sm md:text-base text-brand-secondary">Privacidad total</p>
                  <p class="text-xs md:text-sm text-brand-accent">Tus datos están protegidos</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Widget Calendly -->
          <div class="relative bg-white rounded-xl shadow-lg border border-[#dee3e9] overflow-hidden h-[450px] md:h-[550px] lg:h-[600px]">
            <div class="calendly-inline-widget w-full h-full" 
                 data-url="https://calendly.com/citafullness/30min" 
                 style="min-width:320px;height:600px;"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Sección de Video (Nosotros) -->
    <section id="video-section" class="py-12 md:py-16 bg-gradient-to-b from-white to-brand-bg overflow-hidden relative">
      <!-- Elementos decorativos de fondo -->
      <div class="absolute top-0 left-0 w-full h-32 bg-gradient-to-b from-blue-50/50 to-transparent"></div>
      <div class="absolute -left-20 top-40 w-64 h-64 bg-brand-light/20 rounded-full blur-3xl"></div>
      <div class="absolute -right-20 bottom-40 w-64 h-64 bg-brand-primary/10 rounded-full blur-3xl"></div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <!-- Encabezado de sección -->
        <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
          <h2 class="text-3xl md:text-4xl font-bold text-brand-primary">
            Conoce a <span class="text-brand-secondary">Tu Especialista</span>
          </h2>
          <div class="h-1 w-24 bg-gradient-to-r from-brand-primary to-brand-accent mx-auto rounded-full"></div>
          <p class="text-gray-600 text-lg md:text-xl font-light">
            Descubre cómo transformamos vidas a través de la fisioterapia personalizada
          </p>
        </div>

        <div class="grid lg:grid-cols-2 gap-12 items-center">
          <!-- Columna de Video -->
          <div class="relative group">
            <!-- Marco decorativo del video -->
            <div class="absolute -inset-4 bg-gradient-to-tr from-brand-primary to-brand-accent rounded-2xl opacity-20 group-hover:opacity-30 transition-opacity duration-300 transform rotate-2"></div>
          
            <div class="relative rounded-xl overflow-hidden shadow-2xl bg-black aspect-video">
              <!-- Thumbnail / Placeholder antes de cargar -->
              <div class="absolute inset-0 bg-cover bg-center opacity-80" style="background-image: url(@/assets/imagenes/video-thumbnail.jpg)"></div>
            
              <video 
                class="w-full h-full object-cover" 
                controls
                poster="@/assets/imagenes/video-thumbnail.jpg"
              >
                <source src="@/assets/videos/presentacion-fullness.mp4" type="video/mp4">
                Tu navegador no soporta el video.
              </video>
            </div>
          
            <!-- Badge flotante -->
            <div class="absolute -bottom-6 -right-6 bg-white p-4 rounded-lg shadow-xl border-l-4 border-brand-primary hidden md:block">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-[#e3f6fd] rounded-full flex items-center justify-center text-brand-primary">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </div>
                <div>
                  <p class="text-brand-secondary font-bold text-sm">Experiencia Fullness</p>
                  <p class="text-xs text-gray-500">2:45 min de bienestar</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Columna de Contenido -->
          <div class="space-y-8">
            <div class="space-y-6">
              <h3 class="text-2xl font-bold text-brand-secondary">¿Por qué elegirnos?</h3>
              <p class="text-gray-600 leading-relaxed">
                En Fullness no solo tratamos dolencias, recuperamos tu calidad de vida. Nuestro enfoque integral combina las últimas técnicas fisioterapéuticas con la comodidad y seguridad de tu hogar.
              </p>
            
              <ul class="space-y-4">
                <li class="flex items-start gap-4">
                  <div class="w-8 h-8 bg-[#e3f6fd] rounded-full flex items-center justify-center shrink-0 mt-1">
                    <svg class="w-4 h-4 text-brand-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                    </svg>
                  </div>
                  <div>
                    <h4 class="font-bold text-brand-primary">Profesionales Acreditados</h4>
                    <p class="text-sm text-gray-600">Todos nuestros especialistas cuentan con colegiatura y amplia experiencia clínica.</p>
                  </div>
                </li>
                <li class="flex items-start gap-4">
                  <div class="w-8 h-8 bg-[#e3f6fd] rounded-full flex items-center justify-center shrink-0 mt-1">
                    <svg class="w-4 h-4 text-brand-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                  </div>
                  <div>
                    <h4 class="font-bold text-brand-primary">Tecnología y Equipamiento</h4>
                    <p class="text-sm text-gray-600">Llevamos todo el equipo necesario para garantizar una sesión efectiva.</p>
                  </div>
                </li>
                <li class="flex items-start gap-4">
                  <div class="w-8 h-8 bg-[#e3f6fd] rounded-full flex items-center justify-center shrink-0 mt-1">
                    <svg class="w-4 h-4 text-brand-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
                    </svg>
                  </div>
                  <div>
                    <h4 class="font-bold text-brand-primary">Seguridad Garantizada</h4>
                    <p class="text-sm text-gray-600">Protocolos estrictos de bioseguridad y verificación de identidad.</p>
                  </div>
                </li>
              </ul>
            </div>

            <a 
              href="#agendar-cita" 
              class="inline-block bg-brand-primary text-white px-8 py-3 rounded-lg font-medium shadow-lg hover:bg-brand-secondary hover:-translate-y-0.5 transition-all duration-300"
            >
              Reservar mi sesión ahora
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Sección FAQ (Acordeón) -->
    <section class="py-10 bg-white border-t border-[#dee3e9]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-10">
          <h2 class="text-2xl md:text-3xl font-bold text-brand-primary mb-2">Preguntas Frecuentes</h2>
          <p class="text-brand-accent">Resolvemos tus dudas sobre el servicio a domicilio</p>
        </div>

        <div class="space-y-4">
          <FaqItem 
            v-for="faq in faqs" 
            :key="faq.id" 
            :question="faq.question" 
            :answer="faq.answer" 
            :is-open="activeFaq === faq.id"
            @toggle="toggleFaq(faq.id)"
          />
        </div>

        <!-- CTA Final -->
        <div class="mt-12 text-center space-y-3">
          <p class="text-gray-600 text-sm">¿Necesitas más información?</p>
          <button class="bg-gradient-to-r from-brand-primary to-brand-secondary text-white px-6 py-2.5 rounded-full text-sm font-medium hover:from-brand-secondary hover:to-brand-primary transition-all inline-flex items-center gap-2 transform hover:scale-[1.02] active:scale-95">
            Contáctanos ahora
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h18M3 12h18m-18 7h18"/>
            </svg>
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import FaqItem from './FaqItem.vue';
import { faqs } from '@/data/faqs';

export default {
  name: "InfoSection",
  components: {
    FaqItem
  },
  data() {
    return {
      activeFaq: null,
      faqs: faqs
    };
  },
  mounted() {
    const scriptSrc = "https://assets.calendly.com/assets/external/widget.js";
    if (!document.querySelector(`script[src="${scriptSrc}"]`)) {
      const script = document.createElement("script");
      script.type = "text/javascript";
      script.src = scriptSrc;
      script.async = true;
      document.head.appendChild(script);
    }
  },
  methods: {
    toggleFaq(id) {
      this.activeFaq = this.activeFaq === id ? null : id;
    }
  }
}
</script>

<style scoped>
.faq-enter-active,
 .faq-leave-active {
   transition: all 0.3s ease;
   transform-origin: top;
 }
 .faq-enter,
 .faq-leave-to {
   opacity: 0;
   transform: scaleY(0.9);
 }
</style>
