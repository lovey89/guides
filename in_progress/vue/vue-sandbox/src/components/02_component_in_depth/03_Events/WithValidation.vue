<script setup>
import { ref } from 'vue'

const num = ref(0)

const emit = defineEmits({
  // No validation
  //click: null,

  // Validate submit event
  submit: (num) => {
    if (num % 2 == 0) {
      return true
    }
    console.log('Derp')
    return false
  },
})

function submitNum() {
  emit('submit', num.value)
}
</script>

<template>
  <input type="number" v-model="num" />
  <button @click="submitNum">Emit event with given value. Only even numbers will pass</button>
</template>
