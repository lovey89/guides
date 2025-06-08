<script setup>
import { reactive, ref, computed } from 'vue'

let isActive = ref(true)
let hasError = ref(false)
const error = ref(null) // ref("fatal");

const classObject = reactive({
  active: false,
  'text-danger': true,
})

const computedClassObject = computed(() => ({
  active: isActive.value && !error.value,
  'text-danger': error.value && error.value.type === 'fatal',
}))

const activeColor = ref('red')
const fontSize = ref(18)

const styleObject = reactive({
  color: 'blue',
  fontSize: '1.4em',
})
</script>

<template>
  <h1>Class and Style Bindings</h1>
  <h2>Dynamically toggle classes</h2>
  <p>We can pass an object to :class to dynamically toggle classes:</p>
  <div class="static" :class="{ active: isActive, 'text-danger': hasError }">
    The active class here depends on the truthiness of the isActive and hasError variable.
  </div>
  <div>
    As seen in the code above <code>class</code> and <code>:class</code> can be used together if you
    have static classes as well
  </div>

  <div :class="classObject">
    The bound object doesn't have to be inline but can be written as an object and then you add the
    whole object as an argument to <code>:class</code>
  </div>
  <div :class="computedClassObject"><code>computed</code> values can also be used</div>

  <h2>Binding to arrays</h2>
  <p>You can provide an array of dynamic classes as well:</p>
  <pre>
  const activeClass = ref('active')
  const errorClass = ref('text-danger')
  ...
  &lt;div :class="[activeClass, errorClass]"&gt;&lt;/div&gt;
</pre
  >

  You can also add classes conditionally;
  <pre>
  const activeClass = ref('active')
  const errorClass = ref('text-danger')
  ...
  &lt;div :class="[{ [activeClass]: isActive }, errorClass]"&gt;&lt;/div&gt;
</pre
  >

  <h2>With components</h2>
  <p>
    When you use the <code>class</code> attribute on a component with a single root element, those
    classes will be added to the component's root element and merged with any existing class already
    on it.
  </p>

  <p>
    If your component has multiple root elements, you would need to define which element will
    receive this class. You can do this using the <code>$attrs</code> component property:
  </p>
  <pre>
  &lt;!-- MyComponent template using $attrs --&gt;
  &lt;p :class="$attrs.class"&gt;Hi!&lt;/p&gt;
  &lt;span&gt;This is a child component&lt;/span&gt;
</pre
  >
  More about that later

  <h2>Binding inline styles</h2>
  <p :style="{ color: activeColor, fontSize: fontSize + 'px' }">
    <code>:style</code> supports binding to JavaScript object values - it corresponds to an HTML
    element's style property.
  </p>
  <p>
    Although camelCase keys are recommended, :style also supports kebab-cased CSS property keys
    (corresponds to how they are used in actual CSS)
  </p>
  <p :style="styleObject">
    It is often a good idea to bind to a style object directly so that the template is cleaner
  </p>
  <p style="color: red" :style="'font-size: 0.8em'">
    :style directives can also coexist with regular style attributes, just like :class.
  </p>

  <h2>Binding to Arrays</h2>
  We can bind :style to an array of multiple style objects. These objects will be merged and applied
  to the same element:
  <pre>
  &lt;div :style="[baseStyles, overridingStyles]"&gt;&lt;/div&gt;
</pre
  >
</template>

<style>
.static {
  border: dotted;
}
.active {
  color: green;
}
.text-danger {
  background-color: crimson;
}
</style>
