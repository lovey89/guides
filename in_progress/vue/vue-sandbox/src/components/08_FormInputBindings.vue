<script setup>
import { ref } from 'vue'

const message = ref('Initial value')
const textBoxMessage = ref('')
const checked = ref(true)

const checkedNames = ref([])
const picked = ref('')
const selected = ref(null)

const lazyMessage = ref('')
const trimMessage = ref('')
</script>

<template>
  <h1>Form Input Bindings</h1>
  <p>
    When dealing with forms on the frontend, we often need to sync the state of form input elements
    with corresponding state in JavaScript. It can be cumbersome to manually wire up value bindings
    and change event listeners:
  </p>

  <pre>
  &lt;input
    :value="text"
    @input="event => text = event.target.value"&gt;
</pre
  >

  The v-model directive helps us simplify the above to:

  <pre>
  &lt;input v-model="text"&gt;
</pre
  >

  <p>
    In addition, v-model can be used on inputs of different types, &lt;textarea>, and &lt;select>
    elements. It automatically expands to different DOM property and event pairs based on the
    element it is used on:
  </p>

  <ul>
    <li>
      &lt;input> with text types and &lt;textarea> elements use <code>value</code> property and
      <code>input</code> event;
    </li>
    <li>
      &lt;input type="checkbox"> and &lt;input type="radio"> use <code>checked</code> property and
      <code>change</code> event;
    </li>
    <li>&lt;select> uses <code>value</code> as a <code>prop</code> and change as an event.</li>
  </ul>

  <p>
    <strong>Note:</strong> v-model will ignore the initial value, checked or selected attributes
    found on any form elements. It will always treat the current bound JavaScript state as the
    source of truth. You should declare the initial value on the JavaScript side, using reactivity
    APIs.
  </p>

  <h2>Basic Usage</h2>
  <h3>Text</h3>
  <p>Message is: {{ message }}</p>
  <input v-model="message" placeholder="edit me" value="this is ignored when v-model is in use" />

  <h3>Multiline text</h3>
  <span>Multiline message is:</span>
  <p style="white-space: pre-line">{{ textBoxMessage }}</p>
  <textarea v-model="textBoxMessage" placeholder="add multiple lines"></textarea>

  <h3>Checkbox</h3>
  <input type="checkbox" id="checkbox" v-model="checked" />
  <label for="checkbox">{{ checked }}</label>

  <p>We can also bind multiple checkboxes to the same array or Set value:</p>

  <div>Checked names: {{ checkedNames }}</div>
  <input type="checkbox" id="jack" value="Jack" v-model="checkedNames" />
  <label for="jack">Jack</label>

  <input type="checkbox" id="john" value="John" v-model="checkedNames" />
  <label for="john">John</label>

  <input type="checkbox" id="mike" value="Mike" v-model="checkedNames" />
  <label for="mike">Mike</label>

  <h3>Radio</h3>
  <div>Picked: {{ picked }}</div>

  <input type="radio" id="one" value="One" v-model="picked" name="radioButtonGroup" />
  <label for="one">One</label>

  <input type="radio" id="two" value="Two" v-model="picked" name="radioButtonGroup" />
  <label for="two">Two</label>

  <h3>Select Options</h3>
  <p>Selected: {{ selected }}</p>
  <select v-model="selected">
    <!-- inline object literal -->
    <option :value="{ number: 123 }">123</option>
    <option :value="{ number: 456, otherValue: 'Hello' }">456</option>
  </select>
  <p>
    v-model supports value bindings of non-string values as well! In the above example, when the
    option is selected, <code>selected</code> will be set to the object literal value of
    <code>{ number: 123 }</code>.
  </p>

  <h2>Modifiers</h2>

  <h3>.lazy</h3>
  <p>
    By default, v-model syncs the input with the data after each input event (with the exception of
    IME composition as stated above). You can add the lazy modifier to instead
    <code>sync</code> after <code>change</code> events:
  </p>
  <p>Message is: {{ lazyMessage }}</p>
  <input v-model.lazy="lazyMessage" placeholder="edit me" />

  <h3>.trim</h3>
  <p>
    If you want whitespace from user input to be trimmed automatically, you can add the trim
    modifier to your v-model-managed inputs:
  </p>
  <p style="white-space: pre">Trimmed message is: "{{ trimMessage }}"</p>
  <input v-model.trim="trimMessage" placeholder="edit me" />
</template>
