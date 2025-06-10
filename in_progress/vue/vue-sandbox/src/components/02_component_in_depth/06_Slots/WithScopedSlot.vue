<script setup>
const greetingMessage = 'Greetings'
</script>

<template>
  <div>
    <slot :text="greetingMessage" :count="1"></slot>
  </div>
</template>
