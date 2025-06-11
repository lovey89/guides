<template>
  <h1>Plugins</h1>
  <p>Plugins are self-contained code that usually add app-level functionality to Vue.</p>
  <p>
    There is no strictly defined scope for a plugin, but common scenarios where plugins are useful
    include:
  </p>
  <ol>
    <li>
      <p>
        Register one or more global components or custom directives with
        <a href="https://vuejs.org/api/application.html#app-component"
          ><code>app.component()</code></a
        >
        and
        <a href="https://vuejs.org/api/application.html#app-directive"
          ><code>app.directive()</code></a
        >.
      </p>
    </li>
    <li>
      <p>
        Make a resource
        <a href="https://vuejs.org/guide/components/provide-inject.html">injectable</a> throughout
        the app by calling
        <a href="https://vuejs.org/api/application.html#app-provide"><code>app.provide()</code></a
        >.
      </p>
    </li>
    <li>
      <p>
        Add some global instance properties or methods by attaching them to
        <a href="https://vuejs.org/api/application.html#app-config-globalproperties"
          ><code>app.config.globalProperties</code></a
        >.
      </p>
    </li>
    <li>
      <p>
        A library that needs to perform some combination of the above (e.g.
        <a href="https://github.com/vuejs/vue-router-next" target="_blank" rel="noreferrer"
          >vue-router</a
        >).
      </p>
    </li>
  </ol>

  <p style="color: red">
    Read more about plugins in the
    <a href="https://vuejs.org/guide/reusability/plugins.html">official guide</a>
  </p>
</template>
