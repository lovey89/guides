<script setup>
const [model, modifiers] = defineModel({
  set(value) {
    // How it's transformed from Child -> Parent
    if (modifiers.capitalize) {
      return value.charAt(0).toUpperCase() + value.slice(1).toLowerCase()
    }
    return value
  },
  get(value) {
    // How it's transformed from Parent -> Child
    if (modifiers.capitalize) {
      return value.charAt(0).toLowerCase() + value.slice(1).toUpperCase()
    }
    return value
  },
})
</script>

<template>
  <input type="text" v-model="model" />
</template>
