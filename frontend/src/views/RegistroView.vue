<template>
  <AuthLayout>
    <!-- Título y Descripción -->
    <div class="text-center mb-6">
      <h1 class="text-2xl font-bold bg-gradient-to-r from-brand-primary to-brand-secondary bg-clip-text text-transparent mb-1 font-sans">
        Comienza tu experiencia Fullness
      </h1>
      <p class="text-brand-primary text-sm">Crea tu cuenta en simples pasos</p>
    </div>

    <!-- Selector de perfil -->
    <div class="grid grid-cols-2 gap-3 mb-6">
      <button 
        @click="isFisio = false"
        type="button"
        class="group relative p-3 rounded-lg border-2 transition-all duration-200"
        :class="!isFisio 
          ? 'border-brand-primary bg-brand-light text-brand-primary shadow-sm' 
          : 'border-gray-200 hover:border-brand-accent text-gray-500 hover:text-gray-700'"
      >
        <div class="flex flex-col items-center gap-1">
          <i class="fas fa-user-circle text-xl"></i>
          <span class="font-medium text-xs">Soy Paciente</span>
        </div>
        <div v-if="!isFisio" class="absolute -top-2 -right-2 bg-brand-primary text-white w-5 h-5 rounded-full flex items-center justify-center text-xs shadow-sm">
          <i class="fas fa-check"></i>
        </div>
      </button>

      <button 
        @click="isFisio = true"
        type="button"
        class="group relative p-3 rounded-lg border-2 transition-all duration-200"
        :class="isFisio 
          ? 'border-brand-primary bg-brand-light text-brand-primary shadow-sm' 
          : 'border-gray-200 hover:border-brand-accent text-gray-500 hover:text-gray-700'"
      >
        <div class="flex flex-col items-center gap-1">
          <i class="fas fa-user-md text-xl"></i>
          <span class="font-medium text-xs">Soy Especialista</span>
        </div>
        <div v-if="isFisio" class="absolute -top-2 -right-2 bg-brand-primary text-white w-5 h-5 rounded-full flex items-center justify-center text-xs shadow-sm">
          <i class="fas fa-check"></i>
        </div>
      </button>
    </div>

    <!-- Formulario -->
    <form @submit.prevent="handleSubmit" class="space-y-4">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <BaseInput
          v-model="form.nombre"
          label="Nombre completo"
          placeholder="Juan Pérez"
          icon="fas fa-user-tag"
          required
        />
        
        <BaseInput
          v-model="form.dni"
          label="DNI / Identificación"
          placeholder="12345678"
          icon="fas fa-id-card"
          required
        />

        <BaseInput
          v-model="form.email"
          label="Correo electrónico"
          type="email"
          placeholder="ejemplo@gmail.com"
          icon="fas fa-envelope"
          required
        />

        <BaseInput
          v-model="form.telefono"
          label="Teléfono"
          type="tel"
          placeholder="999 999 999"
          icon="fas fa-mobile-alt"
          required
        />
        
        <div class="md:col-span-2">
          <BaseInput
            v-model="form.password"
            label="Contraseña segura"
            type="password"
            placeholder="••••••••"
            icon="fas fa-lock"
            required
          />
        </div>
      </div>

      <!-- Campos Especialista (Condicional) -->
      <div v-if="isFisio" class="grid grid-cols-1 md:grid-cols-2 gap-4 animate-fade-in">
        <BaseInput
          v-model="form.num_colegiado"
          label="N° Colegiado"
          placeholder="CMP-12345"
          icon="fas fa-certificate"
        />
        
        <div>
          <label class="block text-sm font-medium text-brand-secondary mb-2">Especialidad</label>
          <div class="relative">
            <select
              v-model="form.especialidad"
              class="w-full pl-4 pr-10 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-accent focus:border-brand-accent transition-all appearance-none bg-white"
            >
              <option value="">Selecciona especialidad</option>
              <option value="1">Fisioterapia Deportiva</option>
              <option value="2">Rehabilitación Neurológica</option>
              <option value="3">Traumatología</option>
            </select>
            <i class="fas fa-stethoscope absolute right-3 top-3.5 text-brand-primary pointer-events-none"></i>
          </div>
        </div>
      </div>

      <!-- Términos -->
      <div class="flex items-start mt-2">
        <input
          id="terms"
          type="checkbox"
          v-model="form.terms"
          required
          class="w-4 h-4 text-brand-primary border-gray-300 rounded focus:ring-brand-primary mt-1"
        >
        <label for="terms" class="ml-2 text-sm text-gray-600 leading-tight">
          Acepto los <a href="#" class="text-brand-primary font-medium hover:underline">términos</a> y 
          <a href="#" class="text-brand-primary font-medium hover:underline">privacidad</a>
        </label>
      </div>

      <!-- Botón Submit -->
      <BaseButton type="submit" :disabled="loading">
        <span v-if="!loading">Comenzar ahora</span>
        <span v-else><i class="fas fa-spinner fa-spin mr-2"></i>Creando cuenta...</span>
      </BaseButton>

      <!-- Divisor -->
      <div class="relative py-2">
        <div class="absolute inset-0 flex items-center">
          <div class="w-full border-t border-gray-300"></div>
        </div>
        <div class="relative flex justify-center">
          <span class="px-2 bg-white text-gray-500 text-xs uppercase tracking-wider">O continúa con</span>
        </div>
      </div>

      <!-- Botones Sociales -->
      <div class="flex gap-2">
        <BaseButton variant="social" icon="fab fa-google" @click="socialLogin('google')" type="button" class="flex-1">
          <span class="hidden md:inline">Google</span>
        </BaseButton>
        <BaseButton variant="social" icon="fab fa-facebook-f" @click="socialLogin('facebook')" type="button" class="flex-1">
          <span class="hidden md:inline">Facebook</span>
        </BaseButton>
        <BaseButton variant="social" icon="fab fa-linkedin-in" @click="socialLogin('linkedin')" type="button" class="flex-1">
          <span class="hidden md:inline">LinkedIn</span>
        </BaseButton>
        <div id="googleSignInButton" class="hidden"></div> 
      </div>

      <!-- Link Login -->
      <p class="text-center text-sm text-gray-600">
        ¿Ya tienes cuenta? 
        <router-link to="/login" class="text-brand-primary font-semibold hover:underline">
          Accede aquí
        </router-link>
      </p>
    </form>
  </AuthLayout>
</template>

<script>
import AuthLayout from '@/layouts/AuthLayout.vue'
import BaseInput from '@/components/base/BaseInput.vue'
import BaseButton from '@/components/base/BaseButton.vue'

export default {
  name: 'RegistroView',
  components: {
    AuthLayout,
    BaseInput,
    BaseButton
  },
  data() {
    return {
      showLoader: true,
      loading: false,
      isFisio: false,
      googleClientId: '488360135215-3fbij1cj0rijjlhh4lbo9vt0kvoenh55.apps.googleusercontent.com',
      form: {
        nombre: '',
        dni: '',
        telefono: '',
        email: '',
        password: '',
        num_colegiado: '',
        especialidad: '',
        terms: false,
        tipo_usuario: 'paciente'
      }
    }
  },
  mounted() {
    setTimeout(() => {
      this.showLoader = false
    }, 2200);
    // Inicializa Google Sign-In después de montar el componente
    this.$nextTick(() => {
      if (window.google) {
        window.google.accounts.id.initialize({
          client_id: this.googleClientId,
          callback: this.handleGoogleCredentialResponse,
          ux_mode: 'popup',
          context: 'signup'
        });
        // Personaliza el botón
        window.google.accounts.id.renderButton(
          document.getElementById('googleSignInButton'),
          { 
            theme: 'outline',
            size: 'medium',
            text: 'signup_with',
            shape: 'rectangular',
            width: 300
          }
        );
      }
    });
  },
  methods: {
    async handleSubmit() {
      this.loading = true;
      try {
        const payload = {
          email: this.form.email,
          password: this.form.password,
          full_name: this.form.nombre,
          identification: this.form.dni,
          phone: this.form.telefono,
          role: this.isFisio ? 'especialista' : 'paciente',
          medical_license: this.isFisio ? this.form.num_colegiado : null,
          specialty: this.isFisio ? this.form.especialidad : null
        };

        const response = await fetch('http://127.0.0.1:8000/auth/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok) {
          throw new Error(data.detail || 'Error en el registro');
        }

        // Registro exitoso
        alert('Cuenta creada exitosamente. Por favor inicia sesión.');
        this.$router.push('/login');

      } catch (error) {
        console.error('Error:', error);
        alert(error.message);
      } finally {
        this.loading = false;
      }
    },
    async handleGoogleCredentialResponse(response) {
      try {
        this.loading = true;
        // 1. Enviar credencial al backend
        const res = await fetch('http://localhost:5000/auth/google/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            credential: response.credential,
            isFisio: this.isFisio
          })
        });
        const data = await res.json();
        if (data.success) {
          // 2. Redirigir al dashboard después del registro
          this.$router.push('/dashboard');
        } else {
          console.error('Error en registro Google:', data.error);
        }
      } catch (error) {
        console.error('Error al procesar Google Sign-In:', error);
      } finally {
        this.loading = false;
      }
    },
    socialLogin(provider) {
      if (provider === 'google') {
        window.google.accounts.id.prompt();
      } else {
        console.log(`Iniciando sesión con ${provider}`);
      }
    }
  }
}
</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.3s ease-in-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>