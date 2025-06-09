<template>
  <h1>Lifecycle Hooks</h1>
  <h2>Registering Lifecycle Hooks</h2>
  <p>
    For example, the <code>onMounted</code> hook can be used to run code after the component has
    finished the initial rendering and created the DOM nodes:
  </p>
  <pre>
  &lt;script setup>
  import { onMounted } from 'vue'

  onMounted(() => {
    console.log(`the component is now mounted.`)
  })
  &lt;/script>
</pre
  >
  <p>
    There are also other hooks which will be called at different stages of the instance's lifecycle,
    with the most commonly used being <code>onMounted</code>, <code>onUpdated</code>, and
    <code>onUnmounted</code>.
  </p>
  <p>
    When calling <code>onMounted</code>, Vue automatically associates the registered callback
    function with the current active component instance. This requires these hooks to be registered
    <strong>synchronously</strong> during component setup. For example, do not do this:
  </p>
  <pre>
  setTimeout(() => {
    onMounted(() => {
      // this won't work.
    })
  }, 100)
</pre
  >
  <p>
    Do note this doesn't mean that the call must be placed lexically inside <code>setup()</code> or
    <code>&lt;script setup&gt;</code>. <code>onMounted()</code> can be called in an external
    function as long as the call stack is synchronous and originates from within
    <code>setup()</code>.
  </p>
</template>
