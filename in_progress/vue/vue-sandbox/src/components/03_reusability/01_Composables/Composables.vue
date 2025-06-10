<script setup>
import MouseTrackingComponent from './MouseTrackingComponent.vue'
import { useMouse } from './mouse.js'
import { trackMouse } from './trackmouse'

// Use composable logic
const { x, y } = useMouse()

const { x: x0, y: y0 } = trackMouse()
</script>

<template>
  <h1>Composables</h1>
  <h2>What is a "Composable"?</h2>
  <p>
    In the context of Vue applications, a "composable" is a function that leverages Vue's
    Composition API to encapsulate and reuse <strong>stateful logic</strong>.
  </p>
  <p>
    When building frontend applications, we often need to reuse logic for common tasks. For example,
    we may need to format dates in many places, so we extract a reusable function for that. This
    formatter function encapsulates <strong>stateless logic</strong>: it takes some input and
    immediately returns expected output. There are many libraries out there for reusing stateless
    logic - for example
    <a href="https://lodash.com/" target="_blank" rel="noreferrer">lodash</a> and
    <a href="https://date-fns.org/" target="_blank" rel="noreferrer">date-fns</a>, which you may
    have heard of.
  </p>
  <p>
    By contrast, stateful logic involves managing state that changes over time. A simple example
    would be tracking the current position of the mouse on a page. In real-world scenarios, it could
    also be more complex logic such as touch gestures or connection status to a database.
  </p>

  <h2>Mouse Tracker Example</h2>
  <p>
    If we were to implement the mouse tracking functionality using the Composition API directly
    inside a component,you can look inside the <code>MouseTrackingComponent.vue</code> file.
  </p>
  <div style="background-color: gainsboro">
    <MouseTrackingComponent />
  </div>
  <p>
    But what if we want to reuse the same logic in multiple components? We can extract the logic
    into an external file, as a composable function. Check the <code>mouse.js</code> file.
  </p>
  <div style="background-color: gainsboro">
    <p>Mouse position is at: {{ x }}, {{ y }}</p>
  </div>
  <p>
    Just like inside a component, you can use the full range of
    <a href="https://vuejs.org/api/#composition-api">Composition API functions</a> in composables.
    The same <code>useMouse()</code> functionality can now be used in any component.
  </p>
  <p>
    Composables can also nest them: one composable function can call one or more other composable
    functions. This enables us to compose complex logic using small, isolated units, similar to how
    we compose an entire application using components. In fact, this is why we decided to call the
    collection of APIs that make this pattern possible Composition API.
  </p>
  <p>
    For example, we can extract the logic of adding and removing a DOM event listener into its own
    composable. Check the <code>event.js</code> and <code>trackmouse.js</code> files.
  </p>
  <div style="background-color: gainsboro">
    <p>Mouse position is at: {{ x0 }}, {{ y0 }}</p>
  </div>

  <h2>Async State Example</h2>
  <p>
    The <code>useMouse()</code> composable doesn't take any arguments, so let's take a look at
    another example that makes use of one. When doing async data fetching, we often need to handle
    different states: loading, success, and error:
  </p>
  <pre>
    &lt;script setup>
    import { ref } from 'vue'

    const data = ref(null)
    const error = ref(null)

    fetch('...')
      .then((res) => res.json())
      .then((json) => (data.value = json))
      .catch((err) => (error.value = err))
    &lt;/script>

    &lt;template>
      &lt;div v-if="error">Oops! Error encountered: &lcub;&lcub; error.message &rcub;&rcub;&lt;/div>
      &lt;div v-else-if="data">
        Data loaded:
        &lt;pre>&lcub;&lcub; data &rcub;&rcub;&lt;/pre>
      &lt;/div>
      &lt;div v-else>Loading...&lt;/div>
    &lt;/template>
  </pre>
  <p>
    It would be tedious to have to repeat this pattern in every component that needs to fetch data.
    Let's extract it into a composable:
  </p>
  <pre>
    export function useFetch(url) {
      const data = ref(null)
      const error = ref(null)

      fetch(url)
        .then((res) => res.json())
        .then((json) => (data.value = json))
        .catch((err) => (error.value = err))

      return { data, error }
    }
  </pre>
  <p>Now in our component we can just do:</p>
  <pre>
    &lt;script setup>
    import { useFetch } from './fetch.js'

    const { data, error } = useFetch('...')
    &lt;/script>
  </pre>

  <h3>Accepting Reactive State</h3>
  <p>
    <code>useFetch()</code> takes a static URL string as input - so it performs the fetch only once
    and is then done. What if we want it to re-fetch whenever the URL changes? In order to achieve
    this, we need to pass reactive state into the composable function, and let the composable create
    watchers that perform actions using the passed state.
  </p>
  <p>For example, <code>useFetch()</code> should be able to accept a ref:</p>
  <pre>
    const url = ref('/initial-url')

    const { data, error } = useFetch(url)

    // this should trigger a re-fetch
    url.value = '/new-url'
  </pre>
  <p>Or, accept a getter function:</p>
  <pre>
    // re-fetch when props.id changes
    const { data, error } = useFetch(() => `/posts/${props.id}`)
  </pre>

  <p>
    We can refactor our existing implementation with the
    <a href="https://vuejs.org/api/reactivity-core.html#watcheffect"><code>watchEffect()</code></a>
    and
    <a href="https://vuejs.org/api/reactivity-utilities.html#tovalue"><code>toValue()</code></a>
    APIs:
  </p>
  <pre>
    // fetch.js
    import { ref, watchEffect, toValue } from 'vue'

    export function useFetch(url) {
      const data = ref(null)
      const error = ref(null)

      const fetchData = () => {
        // reset state before fetching..
        data.value = null
        error.value = null

        fetch(toValue(url))
          .then((res) => res.json())
          .then((json) => (data.value = json))
          .catch((err) => (error.value = err))
      }

      watchEffect(() => {
        fetchData()
      })

      return { data, error }
    }
  </pre>
  <p>
    <code>toValue()</code> is an API added in 3.3. It is designed to normalize refs or getters into
    values. If the argument is a ref, it returns the ref's value; if the argument is a function, it
    will call the function and return its return value. Otherwise, it returns the argument as-is. It
    works similarly to <a href="/api/reactivity-utilities.html#unref"><code>unref()</code></a
    >, but with special treatment for functions.
  </p>
  <p>
    Notice that <code>toValue(url)</code> is called <strong>inside</strong> the
    <code>watchEffect</code> callback. This ensures that any reactive dependencies accessed during
    the <code>toValue()</code> normalization are tracked by the watcher.
  </p>
  <p>
    This version of <code>useFetch()</code> now accepts static URL strings, refs, and getters,
    making it much more flexible.
  </p>

  <h2>Conventions and Best Practices</h2>
  <h3>Naming</h3>
  <p>
    It is a convention to name composable functions with camelCase names that start with
    "<code>use</code>".
  </p>

  <h3>Input Arguments</h3>
  <p>
    A composable can accept ref or getter arguments even if it doesn't rely on them for reactivity.
    If you are writing a composable that may be used by other developers, it's a good idea to handle
    the case of input arguments being refs or getters instead of raw values. The
    <a href="https://vuejs.org/api/reactivity-utilities.html#tovalue"><code>toValue()</code></a>
    utility function will come in handy for this purpose. See above.
  </p>
  <p>
    If your composable creates reactive effects when the input is a ref or a getter, make sure to
    either explicitly watch the ref / getter with <code>watch()</code>, or call
    <code>toValue()</code> inside a <code>watchEffect()</code> so that it is properly tracked.
  </p>

  <h3>Return values</h3>
  <p>
    You have probably noticed that we have been exclusively using <code>ref()</code> instead of
    <code>reactive()</code> in composables. The recommended convention is for composables to always
    return a plain, non-reactive object containing multiple refs. This allows it to be destructured
    in components while retaining reactivity:
  </p>
  <pre>
    // x and y are refs
    const { x, y } = useMouse()
  </pre>
  <p>
    Returning a reactive object from a composable will cause such destructures to lose the
    reactivity connection to the state inside the composable, while the refs will retain that
    connection.
  </p>
  <p>
    If you prefer to use returned state from composables as object properties, you can wrap the
    returned object with <code>reactive()</code> so that the refs are unwrapped. For example:
  </p>
  <pre>
    const mouse = reactive(useMouse())
    // mouse.x is linked to original ref
    console.log(mouse.x)
  </pre>
  <pre>
Mouse position is at: &lcub;&lcub; mouse.x &rcub;&rcub;, &lcub;&lcub; mouse.y &rcub;&rcub;</pre
  >

  <h3>Side Effects</h3>
  <p>
    It is OK to perform side effects (e.g. adding DOM event listeners or fetching data) in
    composables but remember to clean up side effects in <code>onUnmounted()</code>.
  </p>

  <h3>Usage Restrictions</h3>
  <p>
    Composables should only be called in <code>&lt;script setup&gt;</code> or the
    <code>setup()</code> hook. They should also be called <strong>synchronously</strong> in these
    contexts. In some cases, you can also call them in lifecycle hooks like
    <code>onMounted()</code>.
  </p>
  <p>
    These restrictions are important because these are the contexts where Vue is able to determine
    the current active component instance. Access to an active component instance is necessary so
    that:
  </p>
  <ol>
    <li><p>Lifecycle hooks can be registered to it.</p></li>
    <li>
      <p>
        Computed properties and watchers can be linked to it, so that they can be disposed when the
        instance is unmounted to prevent memory leaks.
      </p>
    </li>
  </ol>

  <h3>Extracting Composables for Code Organization</h3>
  <p>
    Composables can be extracted not only for reuse, but also for code organization. As the
    complexity of your components grows, you may end up with components that are too large to
    navigate and reason about. Composition API gives you the full flexibility to organize your
    component code into smaller functions based on logical concerns:
  </p>
  <p>
    To some extent, you can think of these extracted composables as component-scoped services that
    can talk to one another.
  </p>
</template>
