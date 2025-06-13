<script>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
onMounted(() => {
  router.push('/about')
})


</script>

<template>
  <h1>Hello App!</h1>
  <p>
    <strong>Current route path:</strong> {{ $route.fullPath }}
  </p>
  <nav>
    <RouterLink to="/">Go to Home</RouterLink>
    <RouterLink to="/about">Go to About</RouterLink>
    <RouterLink to="/users/love">Go to User "Love"</RouterLink>
    <RouterLink to="/users/derp">Go to User "Derp"</RouterLink>
  </nav>
  <main>
    <RouterView />
  </main>
</template>
