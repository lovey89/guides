<script setup>
import { capitalize, ref } from 'vue'
import MultipleBindings from './MultipleBindings.vue'
import BindingWithModifier from './BindingWithModifier.vue'

const first = ref('Herp')
const last = ref('Derp')

const myVar = ref('test')
</script>

<template>
  <h1>Component v-model</h1>
  <h2>Basic Usage</h2>
  <p><code>v-model</code> can be used on a component to implement a two-way binding.</p>
  <p>The recommended approach to achieve this is using the <code>defineModel()</code> macro:</p>
  <pre>
  &lt;script setup>
  const model = defineModel()

  function update() {
    model.value++
  }
  &lt;/script>

  &lt;template>
    &lt;div>Parent bound v-model is: &lcub;&lcub; model &rcub;&rcub;&lt;/div>
    &lt;button @click="update">Increment&lt;/button>
  &lt;/template>
</pre
  >
  <p>The parent can then bind a value with <code>v-model</code>:</p>
  <pre>
  &lt;Child v-model="countModel" />
</pre
  >
  <p>
    The value returned by <code>defineModel()</code> is a ref. It can be accessed and mutated like
    any other ref, except that it acts as a two-way binding between a parent value and a local one.
  </p>
  <p>
    This means you can also bind this ref to a native input element with <code>v-model</code>,
    making it straightforward to wrap native input elements while providing the same
    <code>v-model</code> usage:
  </p>
  <pre>
  &lt;script setup>
  const model = defineModel()
  &lt;/script>

  &lt;template>
    &lt;input v-model="model" />
  &lt;/template>
</pre
  >

  <h3>Under the hood</h3>
  <p>
    Under the hood <code>defineModel</code> declares a prop, and therefore you can declare the
    underlying prop's options by passing it to <code>defineModel</code>:
  </p>
  <pre>
  // making the v-model required
  const model = defineModel({ required: true })

  // providing a default value
  const model = defineModel({ default: 0 })
</pre
  >

  <h2>Multiple <code>v-model</code> Bindings</h2>
  <p><code>v-model</code> on a component can also accept an argument:</p>
  <pre>
  &lt;MyComponent v-model:title="bookTitle" />
</pre
  >
  <p>This can be used multiple times to have multiple bindings:</p>
  <pre>
  &lt;UserName
    v-model:first-name="first"
    v-model:last-name="last"
  />
</pre
  >
  <p>
    In the child component, we can support the corresponding argument by passing a string to
    <code>defineModel()</code> as its first argument:
  </p>
  <pre>
  &lt;script setup>
  const firstName = defineModel('firstName')
  const lastName = defineModel('lastName')
  &lt;/script>

  &lt;template>
    &lt;input type="text" v-model="firstName" />
    &lt;input type="text" v-model="lastName" />
  &lt;/template>
</pre
  >
  <div style="background-color: gainsboro">
    <p>Firstname: {{ first }}</p>
    <p>Lastname: {{ last }}</p>
    <MultipleBindings v-model:first-name="first" v-model:last-name="last" />
  </div>

  <h2>Handling <code>v-model</code> Modifiers</h2>
  <p>
    When we were learning about form input bindings, we saw that <code>v-model</code> has built-in
    modifiers - <code>.trim</code>, <code>.number</code> and <code>.lazy</code>. In some cases, you
    might also want the <code>v-model</code> on your custom input component to support custom
    modifiers.
  </p>
  <p>
    Let's create an example custom modifier, <code>capitalize</code>, that capitalizes the first
    letter of the string provided by the <code>v-model</code> binding:
  </p>
  <pre>
  &lt;MyComponent v-model.capitalize="myText" />
</pre
  >
  <p>
    Modifiers added to a component <code>v-model</code> can be accessed in the child component by
    destructuring the <code>defineModel()</code> return value like this:
  </p>
  <pre>
  &lt;script setup>
  const [model, modifiers] = defineModel()

  console.log(modifiers) // { capitalize: true }
  &lt;/script>

  &lt;template>
    &lt;input type="text" v-model="model" />
  &lt;/template>
</pre
  >

  <p>
    To conditionally adjust how the value should be read / written based on modifiers, we can pass
    <code>get</code> and <code>set</code> options to <code>defineModel()</code>. These two options
    receive the value on get / set of the model ref and should return a transformed value. This is
    how we can use the <code>set</code> option to implement the <code>capitalize</code> modifier:
  </p>
  <pre>
  &lt;script setup>
  const [model, modifiers] = defineModel({
    set(value) {
      if (modifiers.capitalize) {
        return value.charAt(0).toUpperCase() + value.slice(1)
      }
      return value
    }
  })
  &lt;/script>

  &lt;template>
    &lt;input type="text" v-model="model" />
  &lt;/template>
</pre
  >
  <div style="background-color: gainsboro">
    <p>Example: This example uses both <code>get</code> and <code>set</code></p>
    <p>Variable: {{ myVar }}</p>
    <BindingWithModifier v-model.capitalize="myVar" />
  </div>
  <p>The same logic can be used when using multiple bindings.</p>
</template>
