<template>
  <h1>Provide / Inject</h1>
  <p>
    Usually, when we need to pass data from the parent to a child component, we use props. However,
    imagine the case where we have a large component tree, and a deeply nested component needs
    something from a distant ancestor component. With only props, we would have to pass the same
    prop across the entire parent chain (even if the components in the middle don't care about the
    prop). This is called "props drilling" and definitely isn't fun to deal with.
  </p>
  <p>
    We can solve props drilling with <code>provide</code> and <code>inject</code>. A parent
    component can serve as a <strong>dependency provider</strong> for all its descendants. Any
    component in the descendant tree, regardless of how deep it is, can
    <strong>inject</strong> dependencies provided by components up in its parent chain.
  </p>

  <h2>Provide</h2>
  <p>
    To provide data to a component's descendants, use the
    <a href="https://vuejs.org/api/composition-api-dependency-injection.html#provide"
      ><code>provide()</code></a
    >
    function:
  </p>
  <pre>
    &lt;script setup>
    import { provide } from 'vue'

    provide(/* key */ 'message', /* value */ 'hello!')
    &lt;/script>
  </pre>
  <p>
    The <code>provide()</code> function accepts two arguments. The first argument is called the
    <strong>injection key</strong>, which can be a string or a <code>Symbol</code>. The injection
    key is used by descendant components to lookup the desired value to inject. A single component
    can call <code>provide()</code> multiple times with different injection keys to provide
    different values.
  </p>
  <p>
    The second argument is the provided value. The value can be of any type, including reactive
    state such as refs. Providing reactive values allows the descendant components using the
    provided value to establish a reactive connection to the provider component.
  </p>

  <h2>App-level Provide</h2>
  <p>In addition to providing data in a component, we can also provide at the app level:</p>
  <pre>
    import { createApp } from 'vue'

    const app = createApp({})

    app.provide(/* key */ 'message', /* value */ 'hello!')
  </pre>
  <p>
    App-level provides are available to all components rendered in the app. This is especially
    useful when writing <a href="https://vuejs.org/guide/reusability/plugins.html">plugins</a>, as
    plugins typically wouldn't be able to provide values using components.
  </p>

  <h2>Inject</h2>
  <p>
    To inject data provided by an ancestor component, use the
    <a href="https://vuejs.org/api/composition-api-dependency-injection.html#inject"
      ><code>inject()</code></a
    >
    function:
  </p>
  <pre>
    &lt;script setup>
    import { inject } from 'vue'

    const message = inject('message')
    &lt;/script>
  </pre>
  <p>
    If multiple parents provide data with the same key, inject will resolve to the value from the
    closest parent in component's parent chain.
  </p>
  <p>
    If the provided value is a ref, it will be injected as-is and will <strong>not</strong> be
    automatically unwrapped. This allows the injector component to retain the reactivity connection
    to the provider component.
  </p>

  <h3>Injection Default Values</h3>
  <p>
    By default, <code>inject</code> assumes that the injected key is provided somewhere in the
    parent chain. In the case where the key is not provided, there will be a runtime warning.
  </p>
  <p>
    If we want to make an injected property work with optional providers, we need to declare a
    default value, similar to props:
  </p>
  <pre>
    // `value` will be "default value"
    // if no data matching "message" was provided
    const value = inject('message', 'default value')
  </pre>
  <p>
    To avoid unnecessary computation or side effects in case the optional value is not used, we can
    use a factory function for creating the default value:
  </p>
  <pre>
    const value = inject('key', () => new ExpensiveClass(), true)
  </pre>
  <p>The third parameter indicates the default value should be treated as a factory function.</p>

  <h2>Working with Reactivity</h2>
  <p>
    When using reactive provide / inject values,
    <strong
      >it is recommended to keep any mutations to reactive state inside of the
      <em>provider</em> whenever possible</strong
    >. This ensures that the provided state and its possible mutations are co-located in the same
    component, making it easier to maintain in the future.
  </p>
  <p>
    There may be times when we need to update the data from an injector component. In such cases, we
    recommend providing a function that is responsible for mutating the state:
  </p>
  <pre>
    &lt;!-- inside provider component -->
    &lt;script setup>
    import { provide, ref } from 'vue'

    const location = ref('North Pole')

    function updateLocation() {
      location.value = 'South Pole'
    }

    provide('location', {
      location,
      updateLocation
    })
    &lt;/script>
  </pre>
  <pre>
    &lt;!-- in injector component -->
    &lt;script setup>
    import { inject } from 'vue'

    const { location, updateLocation } = inject('location')
    &lt;/script>

    &lt;template>
      &lt;button @click="updateLocation">&lcub;&lcub; location &rcub;&rcub;&lt;/button>
    &lt;/template>
  </pre>
  <p>
    Finally, you can wrap the provided value with <code>readonly()</code> if you want to ensure that
    the data passed through <code>provide</code> cannot be mutated by the injector component.
  </p>
  <pre>
    &lt;script setup>
    import { ref, provide, readonly } from 'vue'

    const count = ref(0)
    provide('read-only-count', readonly(count))
    &lt;/script>
  </pre>

  <h2>Working with Symbol Keys</h2>
  <p>
    So far, we have been using string injection keys in the examples. If you are working in a large
    application with many dependency providers, or you are authoring components that are going to be
    used by other developers, it is best to use Symbol injection keys to avoid potential collisions.
  </p>
  <pre>
    // keys.js
    export const myInjectionKey = Symbol()
  </pre>
  <pre>
    // in provider component
    import { provide } from 'vue'
    import { myInjectionKey } from './keys.js'

    provide(myInjectionKey, {
      /* data to provide */
    })
  </pre>
  <pre>
    // in injector component
    import { inject } from 'vue'
    import { myInjectionKey } from './keys.js'

    const injected = inject(myInjectionKey)
  </pre>
</template>
