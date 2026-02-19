<template>
  <div class="border rounded-xl bg-white transition-all duration-200" 
       :class="{ 'shadow-md': isOpen }">
    <button 
      @click="$emit('toggle')"
      class="w-full px-5 py-4 text-left flex items-center justify-between group">
      <h3 class="text-lg font-semibold text-gray-800 pr-2">{{ question }}</h3>
      <svg class="w-6 h-6 text-brand-secondary transform transition-transform duration-200" 
           :class="{ 'rotate-180': isOpen }" 
           fill="none" 
           stroke="currentColor" 
           viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
      </svg>
    </button>
    <transition name="faq">
      <div v-show="isOpen" class="px-5 pb-4 pt-0">
        <!-- eslint-disable-next-line vue/no-v-html -->
        <div v-html="answer"></div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "FaqItem",
  props: {
    question: {
      type: String,
      required: true
    },
    answer: {
      type: String,
      required: true
    },
    isOpen: {
      type: Boolean,
      default: false
    }
  },
  emits: ['toggle']
}
</script>

<style scoped>
.faq-enter-active,
.faq-leave-active {
  transition: all 0.3s ease;
  transform-origin: top;
}
.faq-enter-from,
.faq-leave-to {
  opacity: 0;
  transform: scaleY(0.9);
}
</style>
