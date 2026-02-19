<template>
  <div>
    <label v-if="label" class="block text-sm font-medium text-brand-secondary mb-2">{{ label }}</label>
    <div class="relative">
      <input
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        v-bind="$attrs"
        class="w-full pl-4 pr-10 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-accent focus:border-brand-accent transition-all duration-200 ease-in-out"
        :class="{ 'border-red-500 focus:ring-red-500 focus:border-red-500': error }"
      >
      <i v-if="icon" :class="[icon, 'absolute right-3 top-3.5 text-brand-primary']"></i>
    </div>
    <p v-if="error" class="mt-1 text-xs text-red-500">{{ error }}</p>
  </div>
</template>

<script>
export default {
  name: 'BaseInput',
  props: {
    modelValue: {
      type: [String, Number],
      default: ''
    },
    label: {
      type: String,
      default: ''
    },
    icon: {
      type: String,
      default: ''
    },
    error: {
      type: String,
      default: ''
    }
  },
  emits: ['update:modelValue']
}
</script>
