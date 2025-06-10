<template>
  <h1>Fallthrough Attributes</h1>

  <h2>Attribute Inheritance</h2>
  <p>
    A "fallthrough attribute" is an attribute or <code>v-on</code> event listener that is passed to
    a component, but is not explicitly declared in the receiving component's props or emits. Common
    examples of this include <code>class</code>, <code>style</code>, and <code>id</code> attributes.
  </p>
  <p>
    When a component renders a single root element, fallthrough attributes will be automatically
    added to the root element's attributes.
  </p>

  <h3><code>class</code> and <code>style</code> Merging</h3>
  <p>
    If the child component's root element already has existing <code>class</code> or
    <code>style</code> attributes, it will be merged with the <code>class</code> and
    <code>style</code> values that are inherited from the parent. Suppose we have:
  </p>
  <pre>
    &lt;!-- template of &lt;MyButton> -->
    &lt;button class="btn">Click Me&gt;/button>
  </pre>
  And we create it with:
  <pre>
    &lt;MyButton class="large" />
  </pre>
  <p>The final rendered DOM would be:</p>
  <pre>
    &lt;button class="btn large">Click Me&lt;/button>
  </pre>

  <h3><code>v-on</code> Listener Inheritance</h3>
  <p>
    The same rule applies to <code>v-on</code> event listeners. If the native root element object
    already has a <code>click</code> listener bound with <code>v-on</code>, then both listeners will
    trigger.
  </p>

  <h3>Nested Component Inheritance</h3>
  <p>
    If a component renders another component as its root node, for example, we refactored
    <code>&lt;MyButton&gt;</code> to render a <code>&lt;BaseButton&gt;</code> as its root. Then the
    fallthrough attributes received by <code>&lt;MyButton&gt;</code> will be automatically forwarded
    to <code>&lt;BaseButton&gt;</code>.
  </p>
  <p>Note that:</p>
  <ol>
    <li>
      <p>
        Forwarded attributes do not include any attributes that are declared as props, or
        <code>v-on</code> listeners of declared events by <code>&lt;MyButton&gt;</code> - in other
        words, the declared props and listeners have been "consumed" by
        <code>&lt;MyButton&gt;</code>.
      </p>
    </li>
    <li>
      <p>
        Forwarded attributes may be accepted as props by <code>&lt;BaseButton&gt;</code>, if
        declared by it.
      </p>
    </li>
  </ol>

  <h2>Disabling Attribute Inheritance</h2>
  <p>
    If you do <strong>not</strong> want a component to automatically inherit attributes, you can set
    <code>inheritAttrs: false</code> in the component's options.
  </p>
  <pre>
    &lt;script setup>
    defineOptions({
      inheritAttrs: false
    })
    // ...setup logic
    &lt;/script>
  </pre>
  <p>
    The common scenario for disabling attribute inheritance is when attributes need to be applied to
    other elements besides the root node. By setting the <code>inheritAttrs</code> option to
    <code>false</code>, you can take full control over where the fallthrough attributes should be
    applied.
  </p>
  <p>
    These fallthrough attributes can be accessed directly in template expressions as
    <code>$attrs</code>.
  </p>
  <p>
    The <code>$attrs</code> object includes all attributes that are not declared by the component's
    <code>props</code> or <code>emits</code> options (e.g., <code>class</code>, <code>style</code>,
    <code>v-on</code> listeners, etc.).
  </p>
  <p>Some notes:</p>
  <ul>
    <li>
      <p>
        Unlike props, fallthrough attributes preserve their original casing in JavaScript (not
        converted to camelCase), so an attribute like <code>foo-bar</code> needs to be accessed as
        <code>$attrs['foo-bar']</code>.
      </p>
    </li>
    <li>
      <p>
        A <code>v-on</code> event listener like <code>@click</code> will be exposed on the object as
        a function under <code>$attrs.onClick</code>.
      </p>
    </li>
  </ul>

  <p>
    To make all fallthrough attributes like <code>class</code> and <code>v-on</code> listeners to be
    applied to an inner element, we can achieve this with <code>inheritAttrs: false</code> and
    <code>v-bind="$attrs"</code>:
  </p>
  <pre>
    &lt;div class="btn-wrapper">
      &lt;button class="btn" v-bind="$attrs">Click Me&lt;/button>
    &lt;/div>
  </pre>
  <p>
    Remember that <code>v-bind</code> without an argument binds all the properties of an object as
    attributes of the target element.
  </p>

  <h2>Attribute Inheritance on Multiple Root Nodes</h2>
  <p>
    Unlike components with a single root node, components with multiple root nodes do not have an
    automatic attribute fallthrough behavior. If <code>$attrs</code> are not bound explicitly, a
    runtime warning will be issued.
  </p>
  <p>
    If <code>&lt;CustomLayout&gt;</code> has the following multi-root template, there will be a
    warning because Vue cannot be sure where to apply the fallthrough attributes:
  </p>
  <pre>
    &lt;header>...&lt;/header>
    &lt;main>...&lt;/main>
    &lt;footer>...&lt;/footer>
  </pre>
  <p>The warning will be suppressed if <code>$attrs</code> is explicitly bound:</p>
  <pre>
    &lt;header>...&lt;/header>
    &lt;main v-bind="$attrs">...&lt;/main>
    &lt;footer>...&lt;/footer>
  </pre>

  <h2>Accessing Fallthrough Attributes in JavaScript</h2>
  <p>
    If needed, you can access a component's fallthrough attributes in
    <code>&lt;script setup&gt;</code> using the <code>useAttrs()</code> API:
  </p>
  <pre>
    &lt;script setup>
    import { useAttrs } from 'vue'

    const attrs = useAttrs()
    &lt;/script>
  </pre>
  <p>
    Note that although the <code>attrs</code> object here always reflects the latest fallthrough
    attributes, it isn't reactive (for performance reasons). You cannot use watchers to observe its
    changes. If you need reactivity, use a prop. Alternatively, you can use
    <code>onUpdated()</code> to perform side effects with the latest <code>attrs</code> on each
    update.
  </p>
</template>
