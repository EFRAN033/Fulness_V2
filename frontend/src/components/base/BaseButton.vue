<template>
  <button
    v-bind="$attrs"
    class="w-full flex items-center justify-center gap-2 rounded-lg font-semibold transition-all transform active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed"
    :class="variantClasses"
  >
    <i v-if="icon" :class="icon"></i>
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'BaseButton',
  props: {
    variant: {
      type: String,
      default: 'primary',
      validator: (value) => ['primary', 'outline', 'social'].includes(value)
    },
    icon: {
      type: String,
      default: ''
    }
  },
  computed: {
    variantClasses() {
      switch (this.variant) {
        case 'primary':
          return 'bg-gradient-to-r from-brand-primary to-brand-secondary text-white py-3.5 hover:from-brand-secondary hover:to-brand-primary shadow-md hover:scale-[1.02]';
        case 'outline':
          return 'border border-brand-primary text-brand-primary hover:bg-brand-light py-2 px-4';
        case 'social':
          return 'border border-gray-300 py-2 px-3 hover:bg-[#dee3e9] text-gray-700 text-sm';
        default:
          return '';
      }
    }
  }
}
</script>
