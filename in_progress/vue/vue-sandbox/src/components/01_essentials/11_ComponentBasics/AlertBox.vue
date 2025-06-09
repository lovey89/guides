<template>
  <div class="alert-box">
    <strong>This is an Error for Demo Purposes</strong>
    <br />
    <slot style="color: gray" />
  </div>
</template>

<style scoped>
.alert-box {
  border: 1px solid red;
  background-color: gainsboro;
}
strong {
  color: red;
}
</style>
