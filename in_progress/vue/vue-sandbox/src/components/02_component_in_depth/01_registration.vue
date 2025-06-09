<template>
  <h1>Component Registration</h1>
  <p>
    A Vue component needs to be "registered" so that Vue knows where to locate its implementation
    when it is encountered in a template. There are two ways to register components: global and
    local.
  </p>

  <h2>Global Registration</h2>
  <p>
    We can make components available globally in the current Vue application using the
    <code>.component()</code> method:
  </p>
  <pre>
  import { createApp } from 'vue'

  const app = createApp({})

  app.component(
    // the registered name
    'MyComponent',
    // the implementation
    {
      /* ... */
    }
  )
</pre
  >
  <p>If using SFCs, you will be registering the imported <code>.vue</code> files:</p>
  <pre>
  import MyComponent from './App.vue'

  app.component('MyComponent', MyComponent)
</pre
  >
  <p>The <code>.component()</code> method can be chained:</p>
  <pre>
  app
    .component('ComponentA', ComponentA)
    .component('ComponentB', ComponentB)
    .component('ComponentC', ComponentC)
</pre
  >
  <p>
    Globally registered components can be used in the template of any component within this
    application:
  </p>
  <pre>
  &lt;!-- this will work in any component inside the app -->
  &lt;ComponentA/>
  &lt;ComponentB/>
  &lt;ComponentC/>
</pre
  >
  <p>
    This even applies to all subcomponents, meaning all three of these components will also be
    available <em>inside each other</em>.
  </p>

  <h2>Local Registration</h2>
  <p>
    Global registration prevents build systems from removing unused components (a.k.a
    "tree-shaking"). If you globally register a component but end up not using it anywhere in your
    app, it will still be included in the final bundle.
  </p>
  <p>Global registrations are also less explicit.</p>
  <p>
    Local registration scopes the availability of the registered components to the current component
    only. It makes the dependency relationship more explicit, and is more tree-shaking friendly.
  </p>
  <p>
    When using SFC with <code>&lt;script setup&gt;</code>, imported components can be locally used
    without registration:
  </p>
  <pre>
  &lt;script setup>
  import ComponentA from './ComponentA.vue'
  &lt;/script>

  &lt;template>
    &lt;ComponentA />
  &lt;/template>
</pre
  >
  <p>
    In non-<code>&lt;script setup&gt;</code>, you will need to use the
    <code>components</code> option:
  </p>
  <pre>
  import ComponentA from './ComponentA.js'

  export default {
    components: {
      ComponentA
    },
    setup() {
      // ...
    }
  }
</pre
  >
</template>
