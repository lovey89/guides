<script setup>
import { ref } from 'vue'
const showDefault = ref(true)
const showSlideFade = ref(true)
const showBounce = ref(true)
</script>

<template>
  <h1>Transition</h1>
  <p>
    Vue offers two built-in components that can help work with transitions and animations in
    response to changing state:
  </p>
  <ul>
    <li>
      <p>
        <code>&lt;Transition&gt;</code> for applying animations when an element or component is
        entering and leaving the DOM. This is covered on this page.
      </p>
    </li>
    <li>
      <p>
        <code>&lt;TransitionGroup&gt;</code> for applying animations when an element or component is
        inserted into, removed from, or moved within a <code>v-for</code> list..
      </p>
    </li>
  </ul>
  <p>
    Aside from these two components, we can also apply animations in Vue using other techniques such
    as toggling CSS classes or state-driven animations via style bindings.
  </p>

  <h2>The <code>&lt;Transition&gt;</code> Component</h2>
  <p>
    <code>&lt;Transition&gt;</code> is a built-in component: this means it is available in any
    component's template without having to register it. It can be used to apply enter and leave
    animations on elements or components passed to it via its default slot. The enter or leave can
    be triggered by one of the following:
  </p>
  <ul>
    <li>Conditional rendering via <code>v-if</code></li>
    <li>Conditional display via <code>v-show</code></li>
    <li>Dynamic components toggling via the <code>&lt;component&gt;</code> special element</li>
    <li>Changing the special <code>key</code> attribute</li>
  </ul>

  <button @click="showDefault = !showDefault">Toggle</button>
  <Transition>
    <p v-if="showDefault">hello</p>
  </Transition>

  <p>
    <strong>Note:</strong> <code>&lt;Transition&gt;</code> only supports a single element or
    component as its slot content. If the content is a component, the component must also have only
    one single root element.
  </p>
  <p>
    When an element in a <code>&lt;Transition&gt;</code> component is inserted or removed, this is
    what happens:
  </p>
  <ol>
    <li>
      <p>
        Vue will automatically sniff whether the target element has CSS transitions or animations
        applied. If it does, a number of
        <a href="#transition-classes">CSS transition classes</a> will be added / removed at
        appropriate timings.
      </p>
    </li>
    <li>
      <p>
        If there are listeners for <a href="#javascript-hooks">JavaScript hooks</a>, these hooks
        will be called at appropriate timings.
      </p>
    </li>
    <li>
      <p>
        If no CSS transitions / animations are detected and no JavaScript hooks are provided, the
        DOM operations for insertion and/or removal will be executed on the browser's next animation
        frame.
      </p>
    </li>
  </ol>

  <h2>CSS-Based Transitions</h2>
  <h3 id="transition-classes">Transition Classes</h3>
  <p>There are six classes applied for enter / leave transitions.</p>
  <ol>
    <li>
      <p>
        <code>v-enter-from</code>: Starting state for enter. Added before the element is inserted,
        removed one frame after the element is inserted.
      </p>
    </li>
    <li>
      <p>
        <code>v-enter-active</code>: Active state for enter. Applied during the entire entering
        phase. Added before the element is inserted, removed when the transition/animation finishes.
        This class can be used to define the duration, delay and easing curve for the entering
        transition.
      </p>
    </li>
    <li>
      <p>
        <code>v-enter-to</code>: Ending state for enter. Added one frame after the element is
        inserted (at the same time <code>v-enter-from</code> is removed), removed when the
        transition/animation finishes.
      </p>
    </li>
    <li>
      <p>
        <code>v-leave-from</code>: Starting state for leave. Added immediately when a leaving
        transition is triggered, removed after one frame.
      </p>
    </li>
    <li>
      <p>
        <code>v-leave-active</code>: Active state for leave. Applied during the entire leaving
        phase. Added immediately when a leaving transition is triggered, removed when the
        transition/animation finishes. This class can be used to define the duration, delay and
        easing curve for the leaving transition.
      </p>
    </li>
    <li>
      <p>
        <code>v-leave-to</code>: Ending state for leave. Added one frame after a leaving transition
        is triggered (at the same time <code>v-leave-from</code> is removed), removed when the
        transition/animation finishes.
      </p>
    </li>
  </ol>

  <p>
    <code>v-enter-active</code> and <code>v-leave-active</code> give us the ability to specify
    different easing curves for enter / leave transitions, which we'll see an example of in the
    following sections.
  </p>

  <h3>Named Transitions</h3>
  <p>A transition can be named via the <code>name</code> prop:</p>
  <pre>
    &lt;Transition name="fade">
      ...
    &lt;/Transition>
  </pre>
  <p>
    For a named transition, its transition classes will be prefixed with its name instead of
    <code>v</code>. For example, the applied class for the above transition will be
    <code>fade-enter-active</code> instead of <code>v-enter-active</code>. The CSS for the fade
    transition should look like this:
  </p>
  <pre>
    .fade-enter-active,
    .fade-leave-active {
      transition: opacity 0.5s ease;
    }

    .fade-enter-from,
    .fade-leave-to {
      opacity: 0;
    }
  </pre>

  <h3>CSS Transitions</h3>
  <p>
    <code>&lt;Transition&gt;</code> is most commonly used in combination with
    <a
      href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions"
      target="_blank"
      rel="noreferrer"
      >native CSS transitions</a
    >, as seen in the basic example above. The <code>transition</code> CSS property is a shorthand
    that allows us to specify multiple aspects of a transition, including properties that should be
    animated, duration of the transition, and
    <a
      href="https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function"
      target="_blank"
      rel="noreferrer"
      >easing curves</a
    >.
  </p>
  <p>
    Here is a more advanced example that transitions multiple properties, with different durations
    and easing curves for enter and leave:
  </p>
  <button @click="showSlideFade = !showSlideFade">Toggle</button>
  <Transition name="slide-fade">
    <p v-if="showSlideFade">hello</p>
  </Transition>

  <h3>CSS Animations</h3>
  <p>
    <a
      href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations"
      target="_blank"
      rel="noreferrer"
      >Native CSS animations</a
    >
    are applied in the same way as CSS transitions, with the difference being that
    <code>*-enter-from</code> is not removed immediately after the element is inserted, but on an
    <code>animationend</code> event.
  </p>
  <p>
    For most CSS animations, we can simply declare them under the <code>*-enter-active</code> and
    <code>*-leave-active</code> classes. Here's an example:
  </p>
  <button @click="showBounce = !showBounce">Toggle</button>
  <Transition name="bounce">
    <p v-if="showBounce" style="text-align: center">Hello here is some bouncy text!</p>
  </Transition>
  <p style="color: red">
    Read more about <code>&lt;Transition&gt;</code>
    <a href="https://vuejs.org/guide/built-ins/transition.html">here</a>.
  </p>
</template>

<style>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

/*
  Enter and leave animations can use different
  durations and timing functions.
*/
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}

.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.25);
  }
  100% {
    transform: scale(1);
  }
}
</style>
