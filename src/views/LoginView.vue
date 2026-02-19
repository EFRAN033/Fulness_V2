<template>
  <AuthLayout>
    <!-- Logo y Título -->
    <div class="text-center space-y-4">
      <img src="@/assets/imagenes/logo(1).png" alt="Logo Fullness" class="w-40 mx-auto">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-brand-primary to-brand-secondary bg-clip-text text-transparent">
        Iniciar Sesión
      </h1>
      <p class="text-gray-600">Accede para agendar tus sesiones de fisioterapia</p>
    </div>

    <!-- Formulario -->
    <form class="space-y-6" @submit.prevent="handleLogin">
      <BaseInput
        v-model="form.email"
        label="Correo electrónico"
        type="email"
        placeholder="ejemplo@gmail.com"
        icon="fas fa-envelope"
        required
      />

      <BaseInput
        v-model="form.password"
        label="Contraseña"
        type="password"
        placeholder="••••••••"
        icon="fas fa-lock"
        required
      />

      <div class="flex items-center justify-between">
        <label class="flex items-center space-x-2">
          <input
            type="checkbox"
            v-model="form.remember"
            class="w-4 h-4 text-brand-primary border-gray-300 rounded focus:ring-brand-primary">
          <span class="text-sm text-gray-600">Mantener sesión activa</span>
        </label>
        <router-link to="/forgot-password" class="text-sm text-brand-primary hover:underline">
          ¿Olvidó su contraseña?
        </router-link>
      </div>

      <BaseButton type="submit">
        Iniciar Sesión
      </BaseButton>
    </form>

    <!-- Divisor -->
    <div class="relative">
      <div class="absolute inset-0 flex items-center">
        <div class="w-full border-t border-gray-300"></div>
      </div>
      <div class="relative flex justify-center">
        <span class="px-2 bg-white text-sm text-gray-500">O CONTINUAR CON</span>
      </div>
    </div>

    <!-- Botones Sociales -->
    <div class="flex gap-2">
      <BaseButton variant="social" icon="fab fa-google" @click="socialLogin('google')" class="flex-1">
        <span class="hidden md:inline">Google</span>
      </BaseButton>
      <BaseButton variant="social" icon="fab fa-facebook-f" @click="socialLogin('facebook')" class="flex-1">
        <span class="hidden md:inline">Facebook</span>
      </BaseButton>
      <BaseButton variant="social" icon="fab fa-linkedin-in" @click="socialLogin('linkedin')" class="flex-1">
        <span class="hidden md:inline">LinkedIn</span>
      </BaseButton>
    </div>

    <!-- Enlaces adicionales -->
    <p class="text-center text-sm text-gray-600">
      ¿No tienes cuenta? 
      <router-link to="/registro" class="text-brand-primary font-semibold hover:underline">
        Regístrate
      </router-link>
    </p>
  </AuthLayout>
</template>

<script>
import AuthLayout from '@/layouts/AuthLayout.vue'
import BaseInput from '@/components/base/BaseInput.vue'
import BaseButton from '@/components/base/BaseButton.vue'

export default {
  name: 'LoginView',
  components: {
    AuthLayout,
    BaseInput,
    BaseButton
  },
  data() {
    return {
      form: {
        email: '',
        password: '',
        remember: false
      }
    }
  },
  //Isaac
  methods: {
    handleLogin() {
      // Validación de credenciales
      if (this.form.email === 'abc@gmail.com' && this.form.password === '123456') {
        // Guardar estado de autenticación en localStorage
        localStorage.setItem('isAuthenticated', 'true');
        // Redirigir al usuario a la página de inicio
        this.$router.push('/');
      } else {
        // Mostrar mensaje de error
        alert('Credenciales incorrectas. Por favor, intente nuevamente.');
      }
    },
    socialLogin(provider) {
      // Lógica para login social
    }
  }
  //Isaac Fin
}
</script>

<style>
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
.animate-float {
  animation: float 3s ease-in-out infinite;
}

@media (max-width: 768px) {
  .login-container {
    grid-template-columns: 1fr;
  }
}
</style>