<script setup>
import { shallowRef } from 'vue'
import CompA from './CompA.vue'
import CompB from './CompB.vue'

const current = shallowRef(CompA)
const current2 = shallowRef(CompA)
const current3 = shallowRef(CompA)
</script>

<template>
  <h1>KeepAlive</h1>
  <p>
    <code>&lt;KeepAlive&gt;</code> is a built-in component that allows us to conditionally cache
    component instances when dynamically switching between multiple components.
  </p>

  <h2>Basic Usage</h2>
  <p>
    In the Component Basics chapter, we introduced the syntax for Dynamic Components, using the
    <code>&lt;component&gt;</code> special element:
  </p>
  <pre>
    &lt;component :is="activeComponent" />
  </pre>
  <p>
    By default, an active component instance will be unmounted when switching away from it. This
    will cause any changed state it holds to be lost. When this component is displayed again, a new
    instance will be created with only the initial state.
  </p>
  <p>
    In the example below, we have two stateful components - A contains a counter, while B contains a
    message synced with an input via <code>v-model</code>. Try updating the state of one of them,
    switch away, and then switch back to it:
  </p>

  <div class="demo">
    <label><input type="radio" v-model="current" :value="CompA" /> A</label>
    <label><input type="radio" v-model="current" :value="CompB" /> B</label>
    <component :is="current"></component>
  </div>
  <p>You'll notice that when switched back, the previous changed state would have been reset.</p>

  <p>
    If this is not the behaviour we want we can wrap our dynamic component with the
    <code>&lt;KeepAlive&gt;</code> built-in component:
  </p>
  <div class="demo">
    <label><input type="radio" v-model="current2" :value="CompA" /> A</label>
    <label><input type="radio" v-model="current2" :value="CompB" /> B</label>
    <KeepAlive>
      <component :is="current2"></component>
    </KeepAlive>
  </div>

  <h2>Include / Exclude</h2>
  <p>
    By default, <code>&lt;KeepAlive&gt;</code> will cache any component instance inside. We can
    customize this behavior via the <code>include</code> and <code>exclude</code> props. Both props
    can be a comma-delimited string, a <code>RegExp</code>, or an array containing either types.
  </p>
  <p>In the following example only <code>CompA</code> will be kept alive</p>
  <div class="demo">
    <label><input type="radio" v-model="current3" :value="CompA" /> A</label>
    <label><input type="radio" v-model="current3" :value="CompB" /> B</label>
    <KeepAlive :include="'CompA'">
      <component :is="current3"></component>
    </KeepAlive>
  </div>
  <p>
    The match is checked against the component's
    <a href="https://vuejs.org/api/options-misc.html#name"><code>name</code></a> option, so
    components that need to be conditionally cached by <code>KeepAlive</code> must explicitly
    declare a <code>name</code> option.
  </p>
  <p>
    Since version 3.2.34, a single-file component using <code>&lt;script setup&gt;</code> will
    automatically infer its <code>name</code> option based on the filename, removing the need to
    manually declare the name.
  </p>
  <p style="color: red">
    See more examples in the
    <a href="https://vuejs.org/guide/built-ins/keep-alive.html#include-exclude">official guide</a>
  </p>

  <h2>Max Cached Instances</h2>
  <p>
    We can limit the maximum number of component instances that can be cached via the
    <code>max</code> prop. When <code>max</code> is specified,
    <code>&lt;KeepAlive&gt;</code> behaves like an LRU cache: if the number of cached instances is
    about to exceed the specified max count, the least recently accessed cached instance will be
    destroyed to make room for the new one.
  </p>
  <pre>
    &lt;KeepAlive :max="10">
      &lt;component :is="activeComponent" />
    &lt;/KeepAlive>
  </pre>

  <h2>Lifecycle of Cached Instance</h2>
  <p>
    When a component instance is removed from the DOM but is part of a component tree cached by
    <code>&lt;KeepAlive&gt;</code>, it goes into a <strong>deactivated</strong> state instead of
    being unmounted. When a component instance is inserted into the DOM as part of a cached tree, it
    is <strong>activated</strong>.
  </p>
  <p>
    A kept-alive component can register lifecycle hooks for these two states using
    <a href="https://vuejs.org/api/composition-api-lifecycle.html#onactivated"
      ><code>onActivated()</code></a
    >
    and
    <a href="https://vuejs.org/api/composition-api-lifecycle.html#ondeactivated"
      ><code>onDeactivated()</code></a
    >.
  </p>
  <p>Note that:</p>
  <ul>
    <li>
      <p>
        <code>onActivated</code> is also called on mount, and <code>onDeactivated</code> on unmount.
      </p>
    </li>
    <li>
      <p>
        Both hooks work for not only the root component cached by <code>&lt;KeepAlive&gt;</code>,
        but also the descendant components in the cached tree.
      </p>
    </li>
  </ul>
</template>

<style scoped>
.demo {
  background-color: gainsboro;
}
</style>
