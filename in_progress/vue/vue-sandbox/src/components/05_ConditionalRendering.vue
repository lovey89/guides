<script setup>
import { ref } from 'vue'
const type = ref('1')

const showBlock = ref(true)
const showShow = ref(true)
</script>

<template>
  <h1>Conditional Rendering</h1>
  <h2>Simple case</h2>
  <p>
    The directive v-if is used to conditionally render a block. The block will only be rendered if
    the directive's expression returns a truthy value.
  </p>
  <p>
    You can use the v-else directive to indicate an "else block" for v-if. A v-else element must
    immediately follow a v-if or a v-else-if element - otherwise it will not be recognized.
  </p>
  <p>
    The v-else-if, as the name suggests, serves as an "else if block" for v-if. It can also be
    chained multiple times. Similar to v-else, a v-else-if element must immediately follow a v-if or
    a v-else-if element.
  </p>
  <p>Example</p>
  <div v-if="type === '1'">One</div>
  <div v-else-if="type === '2'">Two</div>
  <div v-else-if="type === '3'">Three</div>
  <div v-else>It neither one, two or three</div>
  <button @click="type = '1'">1</button>
  <button @click="type = '2'">2</button>
  <button @click="type = '3'">3</button>
  <button @click="type = '4'">4</button>

  <h2>v-if on &lt;template&gt;</h2>
  <p>
    Because v-if is a directive, it has to be attached to a single element. But what if we want to
    toggle more than one element? You could use a &lt;div&gt; but that's not always what you want.
    In this case we can use v-if on a &lt;template&gt; element, which serves as an invisible
    wrapper. The final rendered result will not include the &lt;template&gt; element.
  </p>
  <p>Example</p>
  <button @click="showBlock = !showBlock">Toggle block</button>
  <template v-if="showBlock">
    <h1>Title</h1>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
  </template>

  <h2>v-show</h2>
  <p>
    Another option for conditionally displaying an element is the v-show directive. The usage is
    largely the same.
  </p>
  <p>
    The difference is that an element with v-show will always be rendered and remain in the DOM;
    v-show only toggles the display CSS property of the element.
  </p>
  <p>v-show doesn't support the &lt;template&gt; element, nor does it work with v-else.</p>
  <button @click="showShow = !showShow">Toggle show</button>
  <div v-if="showShow" style="background-color: gainsboro">
    <h1>Title</h1>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
  </div>

  <h2>v-if vs. v-show</h2>
  <p>
    v-if is "real" conditional rendering because it ensures that event listeners and child
    components inside the conditional block are properly destroyed and re-created during toggles.
  </p>
  <p>
    v-if is also lazy: if the condition is false on initial render, it will not do anything - the
    conditional block won't be rendered until the condition becomes true for the first time.
  </p>
  <p>
    In comparison, v-show is much simpler - the element is always rendered regardless of initial
    condition, with CSS-based toggling.
  </p>
  <p>
    Generally speaking, v-if has higher toggle costs while v-show has higher initial render costs.
    So prefer v-show if you need to toggle something very often, and prefer v-if if the condition is
    unlikely to change at runtime.
  </p>

  <h2>v-if with v-for</h2>
  <p>When v-if and v-for are both used on the same element, v-if will be evaluated first.</p>
  <p>
    <strong>Note:</strong> It's not recommended to use v-if and v-for on the same element due to
    implicit precedence.
  </p>
</template>
