<script setup>
// enables v-highlight in templates
const vHighlight = {
  mounted: (el) => {
    el.classList.add('is-highlight')
  },
}
</script>

<template>
  <h1>Custom Directives</h1>
  <p>
    In addition to the default set of directives shipped in core (like <code>v-model</code> or
    <code>v-show</code>), Vue also allows you to register your own custom directives.
  </p>
  <p>
    We have introduced two forms of code reuse in Vue: components and composables. Components are
    the main building blocks, while composables are focused on reusing stateful logic. Custom
    directives, on the other hand, are mainly intended for reusing logic that involves low-level DOM
    access on plain elements.
  </p>
  <p>
    A custom directive is defined as an object containing lifecycle hooks similar to those of a
    component. The hooks receive the element the directive is bound to. Here is an example of a
    directive that adds a class to an element when it is inserted into the DOM by Vue:
  </p>
  <p>
    The paragraph below is enabled by the <code>vHighlight</code> object which wil add the
    <code>is-highlight</code> class if the <code>v-highlight</code> directive is present.
  </p>
  <p v-highlight>This sentence is important!</p>
  <p>
    In <code>&lt;script setup&gt;</code>, any camelCase variable that starts with the
    <code>v</code> prefix can be used as a custom directive.
  </p>
  <p>It is also common to globally register custom directives at the app level:</p>
  <pre>
    const app = createApp({})

    // make v-highlight usable in all components
    app.directive('highlight', {
      /* ... */
    })
  </pre>

  <h2>When to use custom directives</h2>
  <p>
    Custom directives should only be used when the desired functionality can only be achieved via
    direct DOM manipulation.
  </p>
  <p>
    A common example of this is a <code>v-focus</code> custom directive that brings an element into
    focus.
  </p>
  <pre>
    &lt;script setup>
    // enables v-focus in templates
    const vFocus = {
      mounted: (el) => el.focus()
    }
    &lt;/script>

    &lt;template>
      &lt;input v-focus />
    &lt;/template>
  </pre>
  <p>
    This directive is more useful than the <code>autofocus</code> attribute because it works not
    just on page load - it also works when the element is dynamically inserted by Vue!
  </p>
  <p>
    Declarative templating with built-in directives such as <code>v-bind</code> is recommended when
    possible because they are more efficient and server-rendering friendly.
  </p>

  <h2>Directive Hooks</h2>
  <p>A directive definition object can provide several hook functions (all optional):</p>
  <pre>
    const myDirective = {
      // called before bound element's attributes
      // or event listeners are applied
      created(el, binding, vnode) {
        // see below for details on arguments
      },
      // called right before the element is inserted into the DOM.
      beforeMount(el, binding, vnode) {},
      // called when the bound element's parent component
      // and all its children are mounted.
      mounted(el, binding, vnode) {},
      // called before the parent component is updated
      beforeUpdate(el, binding, vnode, prevVnode) {},
      // called after the parent component and
      // all of its children have updated
      updated(el, binding, vnode, prevVnode) {},
      // called before the parent component is unmounted
      beforeUnmount(el, binding, vnode) {},
      // called when the parent component is unmounted
      unmounted(el, binding, vnode) {}
    }
  </pre>

  <h3>Hook Arguments</h3>
  <p>Directive hooks are passed these arguments:</p>
  <ul>
    <li>
      <p>
        <code>el</code>: the element the directive is bound to. This can be used to directly
        manipulate the DOM.
      </p>
    </li>
    <li>
      <p><code>binding</code>: an object containing the following properties.</p>
      <ul>
        <li>
          <code>value</code>: The value passed to the directive. For example in
          <code>v-my-directive="1 + 1"</code>, the value would be <code>2</code>.
        </li>
        <li>
          <code>oldValue</code>: The previous value, only available in <code>beforeUpdate</code> and
          <code>updated</code>. It is available whether or not the value has changed.
        </li>
        <li>
          <code>arg</code>: The argument passed to the directive, if any. For example in
          <code>v-my-directive:foo</code>, the arg would be <code>"foo"</code>.
        </li>
        <li>
          <code>modifiers</code>: An object containing modifiers, if any. For example in
          <code>v-my-directive.foo.bar</code>, the modifiers object would be
          <code>{ foo: true, bar: true }</code>.
        </li>
        <li><code>instance</code>: The instance of the component where the directive is used.</li>
        <li><code>dir</code>: the directive definition object.</li>
      </ul>
    </li>
    <li>
      <p><code>vnode</code>: the underlying VNode representing the bound element.</p>
    </li>
    <li>
      <p>
        <code>prevVnode</code>: the VNode representing the bound element from the previous render.
        Only available in the <code>beforeUpdate</code> and <code>updated</code> hooks.
      </p>
    </li>
  </ul>

  <h2>Function Shorthand</h2>
  <p>
    It's common for a custom directive to have the same behavior for <code>mounted</code> and
    <code>updated</code>, with no need for the other hooks. In such cases we can define the
    directive as a function:
  </p>
  <pre>
    &lt;div v-color="color">&lt;/div>
  </pre>
  <pre>
    app.directive('color', (el, binding) => {
      // this will be called for both `mounted` and `updated`
      el.style.color = binding.value
    })
  </pre>

  <h2>Object Literals</h2>
  <p>
    If your directive needs multiple values, you can also pass in a JavaScript object literal.
    Remember, directives can take any valid JavaScript expression.
  </p>
  <pre>
    &lt;div v-demo="{ color: 'white', text: 'hello!' }">&lt;/div>
  </pre>
  <pre>
    app.directive('demo', (el, binding) => {
      console.log(binding.value.color) // => "white"
      console.log(binding.value.text) // => "hello!"
    })
  </pre>
</template>

<style scoped>
.is-highlight {
  background-color: yellow;
}
</style>
