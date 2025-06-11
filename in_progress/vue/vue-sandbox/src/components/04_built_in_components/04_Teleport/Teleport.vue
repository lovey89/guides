<script setup>
import MySimpleModal from './MySimpleModal.vue'
import MyTeleportModal from './MyTeleportModal.vue'
</script>

<template>
  <h1>Teleport</h1>
  <p>
    <code>&lt;Teleport&gt;</code> is a built-in component that allows us to "teleport" a part of a
    component's template into a DOM node that exists outside the DOM hierarchy of that component.
  </p>

  <h2>Basic Usage</h2>
  <p>
    Sometimes a part of a component's template belongs to it logically, but from a visual
    standpoint, it should be displayed somewhere else in the DOM, perhaps even outside of the Vue
    application.
  </p>
  <p>
    The most common example of this is when building a full-screen modal. Ideally, we want the code
    for the modal's button and the modal itself to be written within the same single-file component,
    since they are both related to the open / close state of the modal. But that means the modal
    will be rendered alongside the button, deeply nested in the application's DOM hierarchy. This
    can create some tricky issues when positioning the modal via CSS.
  </p>
  <p>Consider the <code>&lt;MySimpleModal&gt;</code> below:</p>
  <div style="background-color: gainsboro" class="outer">
    <h3>Vue Modal without Teleport Example</h3>
    <div>
      <MySimpleModal />
    </div>
  </div>

  <p>
    The component contains a <code>&lt;button&gt;</code> to trigger the opening of the modal, and a
    <code>&lt;div&gt;</code> with a class of <code>.modal</code>, which will contain the modal's
    content and a button to self-close.
  </p>
  <p>
    When using this component inside the initial HTML structure, there are a number of potential
    issues:
  </p>
  <ul>
    <li>
      <p>
        <code>position: fixed</code> only places the element relative to the viewport when no
        ancestor element has <code>transform</code>, <code>perspective</code> or
        <code>filter</code> property set. If, for example, we intend to animate the ancestor
        <code>&lt;div class="outer"&gt;</code> with a CSS transform, it would break the modal
        layout!
      </p>
    </li>
    <li>
      <p>
        The modal's <code>z-index</code> is constrained by its containing elements. If there is
        another element that overlaps with <code>&lt;div class="outer"&gt;</code> and has a higher
        <code>z-index</code>, it would cover our modal.
      </p>
    </li>
  </ul>

  <p>
    <code>&lt;Teleport&gt;</code> provides a clean way to work around these, by allowing us to break
    out of the nested DOM structure. Let's create a new version of
    <code>&lt;MySimpleModal&gt;</code> called <code>&lt;MyTeleportModal&gt;</code> which is using
    <code>&lt;Teleport&gt;</code>:
  </p>
  <pre>
    &lt;button @click="open = true">Open Modal&lt;/button>

    &lt;Teleport to="body">
      &lt;div v-if="open" class="modal">
        &lt;p>Hello from the modal!&lt;/p>
        &lt;button @click="open = false">Close&lt;/button>
      &lt;/div>
    &lt;/Teleport>
  </pre>
  <p>
    The <code>to</code> target of <code>&lt;Teleport&gt;</code> expects a CSS selector string or an
    actual DOM node. Here, we are essentially telling Vue to "<strong>teleport</strong> this
    template fragment <strong>to</strong> the <strong><code>body</code></strong> tag".
  </p>
  <div style="background-color: gainsboro" class="outer">
    <h3>Vue Modal with Teleport Example</h3>
    <div>
      <MyTeleportModal />
    </div>
  </div>
  <p>
    You can click the button below and inspect the <code>&lt;body&gt;</code> tag via your browser's
    devtools.
  </p>
  <p>
    You can combine <code>&lt;Teleport&gt;</code> with
    <a href="https://vuejs.org/guide/built-ins/transition.html"><code>&lt;Transition&gt;</code></a>
    to create animated modals - see <a href="https://vuejs.org/examples/#modal">Example here</a>.
  </p>
  <p>
    <strong>Note:</strong> The teleport <code>to</code> target must be already in the DOM when the
    <code>&lt;Teleport&gt;</code> component is mounted. Ideally, this should be an element outside
    the entire Vue application. If targeting another element rendered by Vue, you need to make sure
    that element is mounted before the <code>&lt;Teleport&gt;</code>.
  </p>

  <h2>Using with Components</h2>
  <p>
    <code>&lt;Teleport&gt;</code> only alters the rendered DOM structure - it does not affect the
    logical hierarchy of the components. That is to say, if <code>&lt;Teleport&gt;</code> contains a
    component, that component will remain a logical child of the parent component containing the
    <code>&lt;Teleport&gt;</code>. Props passing and event emitting will continue to work the same
    way.
  </p>
  <p>
    This also means that injections from a parent component work as expected, and that the child
    component will be nested below the parent component in the Vue Devtools, instead of being placed
    where the actual content moved to.
  </p>

  <h2>Disabling Teleport</h2>
  <p>
    In some cases, we may want to conditionally disable <code>&lt;Teleport&gt;</code>. For example,
    we may want to render a component as an overlay for desktop, but inline on mobile.
    <code>&lt;Teleport&gt;</code> supports the <code>disabled</code> prop which can be dynamically
    toggled:
  </p>
  <pre>
    &lt;Teleport :disabled="isMobile">
      ...
    &lt;/Teleport>
  </pre>

  <h2>Multiple Teleports on the Same Target</h2>
  <p>
    A common use case would be a reusable <code>&lt;Modal&gt;</code> component, with the potential
    for multiple instances to be active at the same time. For this kind of scenario, multiple
    <code>&lt;Teleport&gt;</code> components can mount their content to the same target element. The
    order will be a simple append, with later mounts located after earlier ones, but all within the
    target element.
  </p>
</template>
