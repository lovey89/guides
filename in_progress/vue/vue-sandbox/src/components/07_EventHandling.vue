<script setup>
import { ref } from 'vue'
const count = ref(0)

const name = ref('Vue.js')

function greet(event) {
  alert(`Hello ${name.value}!`)
  // `event` is the native DOM event
  if (event) {
    alert(event.target.tagName)
  }
}

function say(message) {
  alert(message)
}

function dummyEventHandler(event) {
  alert(JSON.stringify(event))
}

const buttonCounter = ref(0)
</script>

<template>
  <h1>Event Handling</h1>
  <h2>Listening to Events</h2>
  <p>
    We can use the v-on directive, which we typically shorten to the @ symbol, to listen to DOM
    events and run some JavaScript when they're triggered. The usage would be v-on:click="handler"
    or with the shortcut, @click="handler".
  </p>
  <p>The handler value can be one of the following:</p>
  <ul>
    <li>
      Inline handlers: Inline JavaScript to be executed when the event is triggered (similar to the
      native onclick attribute).
    </li>
    <li>
      Method handlers: A property name or path that points to a method defined on the component.
    </li>
  </ul>

  <h3>Inline Handlers</h3>
  <button @click="count++">Add 1</button>
  <p>Count is: {{ count }}</p>

  <h3>Method Handlers</h3>
  <p>
    The logic for many event handlers will be more complex though, and likely isn't feasible with
    inline handlers.
  </p>
  <!-- `greet` is the name of the method defined above -->
  <button @click="greet">Greet</button>

  <p>
    A method handler automatically receives the native DOM Event object that triggers it - in the
    example above, we are able to access the element dispatching the event via event.target.
  </p>
  <p>
    The template compiler detects method handlers by checking whether the v-on value string is a
    valid JavaScript identifier or property access path. For example, foo, foo.bar and foo['bar']
    are treated as method handlers, while foo() and count++ are treated as inline handlers.
  </p>

  <h3>Calling Methods in Inline Handlers</h3>
  <p>
    Instead of binding directly to a method name, we can also call methods in an inline handler.
    This allows us to pass the method custom arguments instead of the native event:
  </p>
  <button @click="say('hello')">Say hello</button>
  <button @click="say('bye')">Say bye</button>

  <h3>Accessing Event Argument in Inline Handlers</h3>
  <p>
    Sometimes we also need to access the original DOM event in an inline handler. You can pass it
    into a method using the special $event variable, or use an inline arrow function:
  </p>
  <!-- using $event special variable -->
  <button @click="dummyEventHandler($event)">Submit</button>

  <!-- using inline arrow function -->
  <button @click="(event) => dummyEventHandler(event)">Submit</button>

  <h2>Modifiers</h2>
  <h3>Event modifiers</h3>
  <p>
    It is a very common need to call <code>event.preventDefault()</code> or
    <code>event.stopPropagation()</code> inside event handlers. Although we can do this easily
    inside methods, it would be better if the methods can be purely about data logic rather than
    having to deal with DOM event details.
  </p>
  <p style="color: red">TODO: What are those functions?</p>
  <p>
    To address this problem, Vue provides event modifiers for v-on. Recall that modifiers are
    directive postfixes denoted by a dot.
  </p>
  <ul>
    <li>.stop</li>
    <li>.prevent</li>
    <li>.self</li>
    <li>.capture</li>
    <li>.once</li>
    <li>.passive</li>
  </ul>
  <p style="color: red">TODO: Figure out what these are doing in practice?</p>

  <h3>Key Modifiers</h3>
  <p>
    When listening for keyboard events, we often need to check for specific keys. Vue allows adding
    key modifiers for v-on or @ when listening for key events.
  </p>
  <pre>
  &lt;!-- only call `onPageDown` when the `key` is `PageDown` --&gt;
  &lt;input @keyup.page-down="onPageDown" /&gt;
</pre
  >
  <p>In the above example, the handler will only be called if $event.key is equal to 'PageDown'.</p>
  <p>
    You can directly use any valid key names exposed via
    <a href="https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values"
      >KeyboardEvent.key</a
    >
    as modifiers by converting them to kebab-case.
  </p>
  <h4>Key Aliases</h4>
  <p>Vue provides aliases for the most commonly used keys:</p>
  <ul>
    <li>.enter</li>
    <li>.tab</li>
    <li>.delete (captures both "Delete" and "Backspace" keys)</li>
    <li>.esc</li>
    <li>.space</li>
    <li>.up</li>
    <li>.down</li>
    <li>.left</li>
    <li>.right</li>
  </ul>

  <h4>System Modifier Keys</h4>
  <p>
    You can use the following modifiers to trigger mouse or keyboard event listeners only when the
    corresponding modifier key is pressed:
  </p>
  <ul>
    <li>.ctrl</li>
    <li>.alt</li>
    <li>.shift</li>
    <li>.meta</li>
  </ul>
  <button @click.ctrl="buttonCounter++">Ctrl-click to increment: {{ buttonCounter }}</button>

  <p>
    The <code>.exact</code> modifier allows control of the exact combination of system modifiers
    needed to trigger an event.
  </p>
  <!-- this will fire even if Alt or Shift is also pressed -->
  <button @click.ctrl="buttonCounter++">
    Ctrl-click with e.g. shift will work: {{ buttonCounter }}
  </button>
  <br />
  <!-- this will only fire when Ctrl and no other keys are pressed -->
  <button @click.ctrl.exact="buttonCounter++">
    Ctrl-click with with no other modifying keys will work: {{ buttonCounter }}
  </button>
  <br />
  <!-- this will only fire when no system modifiers are pressed -->
  <button @click.exact="buttonCounter++">
    No modifier buttons are allowed to be pressed: {{ buttonCounter }}
  </button>

  <h3>Mouse Button Modifiers</h3>
  <ul>
    <li>.left</li>
    <li>.right</li>
    <li>.middle</li>
  </ul>
  <p>These modifiers restrict the handler to events triggered by a specific mouse button.</p>
  <p>
    Note, however, that .left, .right, and .middle modifier names are based on the typical
    right-handed mouse layout, but in fact represent "main", "secondary", and "auxiliary" pointing
    device event triggers, respectively, and not the actual physical buttons. So that for a
    left-handed mouse layout the "main" button might physically be the right one but would trigger
    the .left modifier handler. Or a trackpad might trigger the .left handler with a one-finger tap,
    the .right handler with a two-finger tap, and the .middle handler with a three-finger tap.
    Similarly, other devices and event sources generating "mouse" events might have trigger modes
    that are not related to "left" and "right" whatsoever.
  </p>
</template>
