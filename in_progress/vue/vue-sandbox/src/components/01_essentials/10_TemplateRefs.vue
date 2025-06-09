<template>
  <h1>Template Refs</h1>
  <p>
    While Vue's declarative rendering model abstracts away most of the direct DOM operations for
    you, there may still be cases where we need direct access to the underlying DOM elements. To
    achieve this, we can use the special <code>ref</code> attribute:
  </p>
  <pre>
  &lt;input ref="input">
</pre
  >
  <p>
    It allows us to obtain a direct reference to a specific DOM element or child component instance
    after it's mounted. This may be useful when you want to, for example, programmatically focus an
    input on component mount, or initialize a 3rd party library on an element.
  </p>

  <h2>Accessing the Refs</h2>
  <p>
    To obtain the reference with Composition API, we can use the
    <code>useTemplateRef()</code> helper:
  </p>
  <pre>
  &lt;script setup>
  import { useTemplateRef, onMounted } from 'vue'

  // the first argument must match the ref value in the template
  const input = useTemplateRef('my-input')

  onMounted(() => {
    input.value.focus()
  })
  &lt;/script>

  &lt;template>
    &lt;input ref="my-input" />
  &lt;/template>
</pre
  >
  <p>
    Note that you can only access the ref after the component is mounted. If you try to access
    <code>input</code> in a template expression, it will be <code>null</code> on the first render.
    This is because the element doesn't exist until after the first render!
  </p>
  <p>
    If you are trying to watch the changes of a template ref, make sure to account for the case
    where the ref has null value:
  </p>
  <pre>
  watchEffect(() => {
    if (input.value) {
      input.value.focus()
    } else {
      // not mounted yet, or the element was unmounted (e.g. by v-if)
    }
  })
</pre
  >

  <h2>Ref on Component</h2>
  <p><code>ref</code> can also be used on a child component.</p>

  <p>
    If the child component is using Options API or not using <code>&lt;script setup></code>, the
    referenced instance will be identical to the child component's <code>this</code>, which means
    the parent component will have full access to every property and method of the child component.
    This makes it easy to create tightly coupled implementation details between the parent and the
    child, so component refs should be only used when absolutely needed - in most cases, you should
    try to implement parent / child interactions using the standard props and emit interfaces first.
  </p>
  <p>
    An exception here is that components using <code>&lt;script setup></code> are private by
    default: a parent component referencing a child component using
    <code>&lt;script setup></code> won't be able to access anything unless the child component
    chooses to expose a public interface using the <code>defineExpose</code> macro:
  </p>
  <pre>
  &lt;script setup>
  import { ref } from 'vue'

  const a = 1
  const b = ref(2)

  // Compiler macros, such as defineExpose, don't need to be imported
  defineExpose({
    a,
    b
  })
  &lt;/script>
</pre
  >
  <p>
    When a parent gets an instance of this component via template refs, the retrieved instance will
    be of the shape <code>{ a: number, b: number }</code> (refs are automatically unwrapped just
    like on normal instances).
  </p>
  <p>
    Note that <code>defineExpose</code> must be called before any await operation. Otherwise,
    properties and methods exposed after the await operation will not be accessible.
  </p>

  <h2>Refs inside <code>v-for</code></h2>
  <p>
    When <code>ref</code> is used inside <code>v-for</code>, the corresponding ref should contain an
    Array value, which will be populated with the elements after mount:
  </p>
  <pre>
  &lt;script setup>
  import { ref, useTemplateRef, onMounted } from 'vue'

  const list = ref([
    /* ... */
  ])

  const itemRefs = useTemplateRef('items')

  onMounted(() => console.log(itemRefs.value))
  &lt;/script>

  &lt;template>
    &lt;ul>
      &lt;li v-for="item in list" ref="items">
        &lcub;&lcub; item &rcub;&rcub;
      &lt;/li>
    &lt;/ul>
  &lt;/template>
</pre
  >
  <p>
    It should be noted that the ref array does <strong>not</strong> guarantee the same order as the
    source array.
  </p>

  <h2>Function Refs</h2>
  <p>
    Instead of a string key, the <code>ref</code> attribute can also be bound to a function, which
    will be called on each component update and gives you full flexibility on where to store the
    element reference. The function receives the element reference as the first argument:
  </p>
  <pre>
  &lt;input :ref="(el) => { /* assign el to a property or ref */ }">
</pre
  >
  <p>
    Note we are using a dynamic <code>:ref</code> binding so we can pass it a function instead of a
    ref name string. When the element is unmounted, the argument will be <code>null</code>. You can,
    of course, use a method instead of an inline function.
  </p>
</template>
