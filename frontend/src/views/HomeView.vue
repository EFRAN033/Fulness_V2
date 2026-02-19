<template>
  <div class="home">
    <HeroSection />
    <ServicesSection />
    <InfoSection />
  </div>
</template>

<script>
// Components
import HeroSection from '@/components/home/HeroSection.vue'
import ServicesSection from '@/components/home/ServicesSection.vue'
import InfoSection from '@/components/home/InfoSection.vue'

export default {
  name: 'HomeView',
  components: {
    HeroSection,
    ServicesSection,
    InfoSection
  }
}
</script>