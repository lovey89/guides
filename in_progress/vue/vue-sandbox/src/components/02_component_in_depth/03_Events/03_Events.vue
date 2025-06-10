<script setup>
import MyComponent from './MyComponent.vue'
import EmitWithArg from './EmitWithArg.vue'
import WithValidation from './WithValidation.vue'
import { ref } from 'vue'

const count = ref(0)
const count2 = ref(0)
const count3 = ref(0)
const count4 = ref(0)
const count5 = ref(0)

function increaseCount4(n) {
  count4.value += n
}
</script>

<template>
  <h1>Component Events</h1>
  <h2>Emitting and Listening to Events</h2>
  <p>
    A component can emit custom events directly in template expressions (e.g. in a
    <code>v-on</code> handler) using the built-in <code>$emit</code> method. The button component
    below emits a <code>someEvent</code> event.
  </p>
  <div style="background-color: gainsboro">
    <p>Counter: {{ count }}</p>
    <MyComponent @some-event="count++" />
  </div>

  <p>The <code>.once</code> modifier is also supported on component event listeners:</p>
  <div style="background-color: gainsboro">
    <p>Counter: {{ count2 }}</p>
    <MyComponent @some-event.once="count2++" />
  </div>
  <p>
    Like components and props, event names provide an automatic case transformation. Notice we
    emitted a camelCase event, but can listen for it using a kebab-cased listener in the parent.
  </p>
  <p>
    <strong>Note:</strong> Unlike native DOM events, component emitted events do not bubble. You can
    only listen to the events emitted by a direct child component.
  </p>

  <h2>Event arguments</h2>
  <p>
    It's sometimes useful to emit a specific value with an event. In those cases, we can pass extra
    arguments to <code>$emit</code> to provide this value.
  </p>
  <div style="background-color: gainsboro">
    <p>Counter: {{ count3 }}</p>
    <EmitWithArg @some-event="(n) => (count3 += n)" />
  </div>
  <p>Or, if the event handler is a method:</p>
  <div style="background-color: gainsboro">
    <p>Counter: {{ count4 }}</p>
    <EmitWithArg @some-event="increaseCount4" />
  </div>
  <p>
    <strong>Note:</strong> All extra arguments passed to <code>$emit()</code> after the event name
    will be forwarded to the listener. For example, with <code>$emit('foo', 1, 2, 3)</code> the
    listener function will receive three arguments.
  </p>

  <h2>Declaring Emitted Events</h2>
  <p>
    A component can explicitly declare the events it will emit using the
    <a href="/api/sfc-script-setup.html#defineprops-defineemits"><code>defineEmits()</code></a>
    macro.
  </p>
  <p>
    The <code>$emit</code> method that we used in the <code>&lt;template&gt;</code> isn't accessible
    within the <code>&lt;script setup&gt;</code> section of a component, but
    <code>defineEmits()</code> returns an equivalent function that we can use instead:
  </p>
  <pre>
  &lt;script setup>
  const emit = defineEmits(['inFocus', 'submit'])

  function buttonClick() {
    emit('submit')
  }
  &lt;/script>
</pre
  >
  <p>
    The <code>defineEmits()</code> macro <strong>cannot</strong> be used inside a function, it must
    be placed directly within <code>&lt;script setup&gt;</code>, as in the example above.
  </p>
  <p>
    Although optional, it is recommended to define all emitted events in order to better document
    how a component should work. It also allows Vue to exclude known listeners from fallthrough
    attributes (see later), avoiding edge cases caused by DOM events manually dispatched by 3rd
    party code.
  </p>
  <p>
    <strong>Note:</strong> If a native event (e.g., <code>click</code>) is defined in the
    <code>emits</code> option, the listener will now only listen to component-emitted
    <code>click</code> events and no longer respond to native <code>click</code> events.
  </p>

  <h2>Events Validation</h2>
  <p>
    The <code>emits</code> option and <code>defineEmits()</code> macro also support an object
    syntax.
  </p>
  <p>
    Similar to prop type validation, an emitted event can be validated if it is defined with the
    object syntax instead of the array syntax.
  </p>
  <p>
    To add validation, the event is assigned a function that receives the arguments passed to the
    <code>emit</code> call and returns a boolean to indicate whether the event is valid or not.
  </p>
  <div style="background-color: gainsboro">
    <p>Counter: {{ count5 }}</p>
    <WithValidation @submit="(n) => (count5 += n)" />
  </div>
  <p>It looks like as if the validation fails, a warning is printed in the console log.</p>
</template>
