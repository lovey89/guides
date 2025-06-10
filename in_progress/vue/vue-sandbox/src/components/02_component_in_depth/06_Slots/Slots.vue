<script setup>
import FancyButton from './FancyButton.vue'
import WithScopedSlot from './WithScopedSlot.vue'
</script>

<template>
  <h1>Slots</h1>
  <h2>Slot Content and Outlet</h2>
  <p>
    The <code>&lt;slot&gt;</code> element is a <strong>slot outlet</strong> that indicates where the
    parent-provided <strong>slot content</strong> should be rendered.
  </p>
  <FancyButton>
    Click me (nothing will actually happen)!
    <!-- slot content -->
  </FancyButton>

  <p>
    With slots, the <code>&lt;FancyButton&gt;</code> is responsible for rendering the outer
    <code>&lt;button&gt;</code> (and its fancy styling), while the inner content is provided by the
    parent component.
  </p>
  <p>
    Slot content is not just limited to text. It can be any valid template content. For example, we
    can pass in multiple elements, or even other components:
  </p>

  <h2>Render Scope</h2>
  <p>
    Slot content has access to the data scope of the parent component, because it is defined in the
    parent. For example:
  </p>
  <pre>
  &lt;span>&lcub;&lcub; message &rcub;&rcub;&lt;/span>
  &lt;FancyButton>&lcub;&lcub; message &rcub;&rcub;&lt;/FancyButton>
</pre
  >
  <p>
    Here both <span><code>&lcub;&lcub; message &rcub;&rcub;</code></span> interpolations will render
    the same content.
  </p>
  <p>
    Slot content does <strong>not</strong> have access to the child component's data. Expressions in
    Vue templates can only access the scope it is defined in, consistent with JavaScript's lexical
    scoping. In other words:
  </p>

  <h2>Fallback Content</h2>
  <p>
    There are cases when it's useful to specify fallback (i.e. default) content for a slot, to be
    rendered only when no content is provided. For example, in a
    <code>&lt;SubmitButton&gt;</code> component, we might want the text "Submit" to be rendered
    inside the <code>&lt;button&gt;</code> if the parent didn't provide any slot content. To make
    "Submit" the fallback content, we can place it in between the <code>&lt;slot&gt;</code> tags:
  </p>
  <pre>
  &lt;button type="submit">
    &lt;slot>
      Submit &lt;!-- fallback content -->
    &lt;/slot>
  &lt;/button>
</pre
  >
  <p>
    Now when we use <code>&lt;SubmitButton&gt;</code> in a parent component, providing no content
    for the slot and "Submit" will be rendered.
  </p>
  <pre>
  &lt;SubmitButton /> &lt;!-- Will render "Submit" -->

  &lt;SubmitButton>Save&lt;/SubmitButton> &lt;!-- Will render "Save" -->
</pre
  >

  <h2>Named Slots</h2>
  <p>
    There are times when it's useful to have multiple slot outlets in a single component. For
    example, in a <code>&lt;BaseLayout&gt;</code> component. For these cases, the
    <code>&lt;slot&gt;</code> element has a special attribute, <code>name</code>, which can be used
    to assign a unique ID to different slots so you can determine where content should be rendered:
  </p>
  <pre>
  &lt;div class="container">
    &lt;header>
      &lt;slot name="header">&lt;/slot>
    &lt;/header>
    &lt;main>
      &lt;slot>&lt;/slot>
    &lt;/main>
    &lt;footer>
      &lt;slot name="footer">&lt;/slot>
    &lt;/footer>
  &lt;/div>
</pre
  >
  <p>
    A <code>&lt;slot&gt;</code> outlet without <code>name</code> implicitly has the name "default".
  </p>
  <p>
    To pass a named slot, we need to use a <code>&lt;template&gt;</code> element with the
    <code>v-slot</code> directive, and then pass the name of the slot as an argument to
    <code>v-slot</code>:
  </p>
  <pre>
  &lt;BaseLayout>
    &lt;template v-slot:header>
      &lt;!-- content for the header slot -->
    &lt;/template>
  &lt;/BaseLayout>
</pre
  >

  <p>
    <code>v-slot</code> has a dedicated shorthand <code>#</code>, so
    <code>&lt;template v-slot:header&gt;</code> can be shortened to just
    <code>&lt;template #header&gt;</code>. Think of it as "render this template fragment in the
    child component's 'header' slot".
  </p>
  <p>
    Here's the code passing content for all three slots to <code>&lt;BaseLayout&gt;</code> using the
    shorthand syntax:
  </p>
  <pre>
  &lt;BaseLayout>
    &lt;template #header>
      &lt;h1>Here might be a page title&lt;/h1>
    &lt;/template>

    &lt;template #default>
      &lt;p>A paragraph for the main content.&lt;/p>
      &lt;p>And another one.&lt;/p>
    &lt;/template>

    &lt;template #footer>
      &lt;p>Here's some contact info&lt;/p>
    &lt;/template>
  &lt;/BaseLayout>
</pre
  >

  <h2>Conditional Slots</h2>
  <p>
    Sometimes you want to render something based on whether or not content has been passed to a
    slot.
  </p>
  <p>
    You can use the <code>$slots</code> property in combination with a <code>v-if</code> to achieve
    this.
  </p>
  <p>
    In the example below we define a Card component with three conditional slots:
    <code>header</code>, <code>footer</code> and the <code>default</code> one. When content for the
    header / footer / default is present, we want to wrap it to provide additional styling:
  </p>
  <pre>
  &lt;template>
    &lt;div class="card">
      &lt;div v-if="$slots.header" class="card-header">
        &lt;slot name="header" />
      &lt;/div>

      &lt;div v-if="$slots.default" class="card-content">
        &lt;slot />
      &lt;/div>

      &lt;div v-if="$slots.footer" class="card-footer">
        &lt;slot name="footer" />
      &lt;/div>
    &lt;/div>
  &lt;/template>
</pre
  >

  <h2>Dynamic Slot Names</h2>
  <p>
    <a href="https://vuejs.org/guide/essentials/template-syntax.html#dynamic-arguments"
      >Dynamic directive arguments</a
    >
    also work on <code>v-slot</code>, allowing the definition of dynamic slot names:
  </p>
  <pre>
  &lt;base-layout>
    &lt;template v-slot:[dynamicSlotName]>
      ...
    &lt;/template>

    &lt;!-- with shorthand -->
    &lt;template #[dynamicSlotName]>
      ...
    &lt;/template>
  &lt;/base-layout>
</pre
  >
  <p>
    Do note the expression is subject to the
    <a
      href="https://vuejs.org/guide/essentials/template-syntax.html#dynamic-argument-syntax-constraints"
      >syntax constraints</a
    >
    of dynamic directive arguments.
  </p>

  <h2>Scoped Slots</h2>
  <p>
    As discussed in Render Scope, slot content does not have access to state in the child component.
  </p>
  <p>
    However, there are cases where it could be useful if a slot's content can make use of data from
    both the parent scope and the child scope. To achieve that, we need a way for the child to pass
    data to a slot when rendering it.
  </p>
  <p>
    In fact, we can do exactly that - we can pass attributes to a slot outlet just like passing
    props to a component:
  </p>
  <pre>
  &lt;!-- &lt;MyComponent> template -->
  &lt;div>
    &lt;slot :text="greetingMessage" :count="1">&lt;/slot>
  &lt;/div>
</pre
  >
  <p>
    Receiving the slot props is a bit different when using a single default slot vs. using named
    slots. We are going to show how to receive props using a single default slot first, by using
    <code>v-slot</code> directly on the child component tag:
  </p>
  <pre>
  &lt;MyComponent v-slot="slotProps">
    &lcub;&lcub; slotProps.text &rcub;&rcub; &lcub;&lcub; slotProps.count &rcub;&rcub;
  &lt;/MyComponent>
</pre
  >
  <p>
    The props passed to the slot by the child are available as the value of the corresponding
    <code>v-slot</code> directive, which can be accessed by expressions inside the slot.
  </p>
  <p>Just like with function arguments, we can use destructuring in <code>v-slot</code>:</p>
  <pre>
  &lt;MyComponent v-slot="{ text, count }">
    &lcub;&lcub; text &rcub;&rcub; &lcub;&lcub; count &rcub;&rcub;
  &lt;/MyComponent>
</pre
  >

  <div style="background-color: gainsboro">
    <WithScopedSlot v-slot="slotProps"> {{ slotProps.text }} {{ slotProps.count }} </WithScopedSlot>
    <p>With destructed <code>v-slot</code></p>
    <WithScopedSlot v-slot="{ text, count }"> {{ count }} {{ text }} </WithScopedSlot>
  </div>

  <h3>Named Scoped Slots</h3>
  <p>
    Named scoped slots work similarly - slot props are accessible as the value of the
    <code>v-slot</code> directive: <code>v-slot:name="slotProps"</code>. When using the shorthand,
    it looks like this:
  </p>
  <pre>
  &lt;MyComponent>
    &lt;template #header="headerProps">
      &lcub;&lcub; headerProps &rcub;&rcub;
    &lt;/template>

    &lt;template #default="defaultProps">
      &lcub;&lcub; defaultProps &rcub;&rcub;
    &lt;/template>

    &lt;template #footer="footerProps">
      &lcub;&lcub; footerProps &rcub;&rcub;
    &lt;/template>
  &lt;/MyComponent>
</pre
  >

  <p>Passing props to a named slot:</p>
  <pre>
  &lt;slot name="header" message="hello">&lt;/slot>
</pre
  >
  <p>
    Note the <code>name</code> of a slot won't be included in the props because it is reserved - so
    the resulting <code>headerProps</code> would be <code>{ message: 'hello' }</code>.
  </p>
  <p>
    If you are mixing named slots with the default scoped slot, you need to use an explicit
    <code>&lt;template&gt;</code> tag for the default slot.
  </p>

  <h3>Renderless Components</h3>
  <p>
    We can come up with components that only encapsulate logic and do not render anything by
    themselves - visual output is fully delegated to the consumer component with scoped slots. We
    call this type of component a <strong>Renderless Component</strong>.
  </p>
  <p>
    An example renderless component could be one that encapsulates the logic of tracking the current
    mouse position:
  </p>
  <pre>
  &lt;MouseTracker v-slot="{ x, y }">
    Mouse is at: &lcub;&lcub; x &rcub;&rcub;, &lcub;&lcub; y &rcub;&rcub;
  &lt;/MouseTracker>
</pre
  >
  <p>
    While an interesting pattern, most of what can be achieved with Renderless Components can be
    achieved in a more efficient fashion with Composition API, without incurring the overhead of
    extra component nesting. Later, we will see how we can implement the same mouse tracking
    functionality as a Composable.
  </p>
</template>
