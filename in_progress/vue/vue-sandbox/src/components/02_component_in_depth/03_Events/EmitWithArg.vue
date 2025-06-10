<script setup>
import { ref } from 'vue'

const num = ref(0)
</script>

<template>
  <input type="number" v-model="num" />
  <button @click="$emit('someEvent', num)">Emit event with given value</button>
</template>
