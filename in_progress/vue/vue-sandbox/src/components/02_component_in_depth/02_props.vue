<template>
  <h1>Props</h1>
  <h2>Props Declaration</h2>
  <p>
    Vue components require explicit props declaration so that Vue knows what external props passed
    to the component should be treated as fallthrough attributes (which will be discussed in its
    dedicated section).
  </p>
  <p>
    In SFCs using <code>&lt;script setup&gt;</code>, props can be declared using the
    <code>defineProps()</code> macro:
  </p>
  <pre>
    &lt;script setup>
    const props = defineProps(['foo'])

    console.log(props.foo)
    &lt;/script>
  </pre>
  <p>
    In addition to declaring props using an array of strings, we can also use the object syntax:
  </p>
  <pre>
    defineProps({
      title: String,
      likes: Number
    })
  </pre>
  <p>
    For each property in the object declaration syntax, the key is the name of the prop, while the
    value should be the constructor function of the expected type.
  </p>
  <p>
    This not only documents your component, but will also warn other developers using your component
    in the browser console if they pass the wrong type.
  </p>

  <h2>Reactive Props Destructure</h2>
  <p>
    Vue's reactivity system tracks state usage based on property access. E.g. when you access
    <code>props.foo</code> in a computed getter or a watcher, the <code>foo</code> prop gets tracked
    as a dependency.
  </p>
  <p>So, given the following code:</p>
  <pre>
    const { foo } = defineProps(['foo'])

    watchEffect(() => {
      // runs only once before 3.5
      // re-runs when the "foo" prop changes in 3.5+
      console.log(foo)
    })
  </pre>
  <p>
    In version 3.4 and below, <code>foo</code> is an actual constant and will never change. In
    version 3.5 and above, Vue's compiler automatically prepends <code>props.</code> when code in
    the same <code>&lt;script setup&gt;</code> block accesses variables destructured from
    <code>defineProps</code>. Therefore the code above becomes equivalent to the following:
  </p>
  <pre>
    const props = defineProps(['foo'])

    watchEffect(() => {
      // `foo` transformed to `props.foo` by the compiler
      console.log(props.foo)
    })
  </pre>
  <p>
    In addition, you can use JavaScript's native default value syntax to declare default values for
    the props.
  </p>
  <pre>
    const { foo = 'default value' } = defineProps(['foo'])
  </pre>

  <h3>Passing Destructured Props into Functions</h3>
  <p>When we pass a destructured prop into a function, e.g.:</p>
  <pre>
    const { foo } = defineProps(['foo'])

    watch(foo, /* ... */)
  </pre>
  <p>
    This will not work as expected because it is equivalent to <code>watch(props.foo, ...)</code> -
    we are passing a value instead of a reactive data source to <code>watch</code>. In fact, Vue's
    compiler will catch such cases and throw a warning.
  </p>
  <p>
    Similar to how we can watch a normal prop with <code>watch(() =&gt; props.foo, ...)</code>, we
    can watch a destructured prop also by wrapping it in a getter:
  </p>
  <pre>
    watch(() => foo, /* ... */)
  </pre>
  <p>
    In addition, this is the recommended approach when we need to pass a destructured prop into an
    external function while retaining reactivity:
  </p>
  <pre>
    useComposable(() => foo)
  </pre>

  <h2>Prop Passing Details</h2>
  <h3>Prop Name Casing</h3>
  <p>
    We declare long prop names using camelCase because this avoids having to use quotes when using
    them as property keys, and allows us to reference them directly in template expressions because
    they are valid JavaScript identifiers.
  </p>
  <pre>
    defineProps({
      greetingMessage: String
    })
  </pre>
  <p>However, the convention is using kebab-case in all cases to align with HTML attributes.</p>
  <pre>
    &lt;MyComponent greeting-message="hello" />
  </pre>

  <h3>Static vs. Dynamic Props</h3>
  <p>You can pass props with <code>v-bind</code> or its <code>:</code> shortcut, such as in:</p>
  <pre>
    &lt;!-- Dynamically assign the value of a complex expression -->
    &lt;BlogPost :title="post.title + ' by ' + post.author.name" />
  </pre>

  <h3>Passing Different Value Types</h3>
  <p>
    In the example above, we happen to pass a string value, but <em>any</em> type of value can be
    passed to a prop.
  </p>
  <h4>Number</h4>
  <pre>
    &lt;!-- Even though `42` is static, we need v-bind to tell Vue that -->
    &lt;!-- this is a JavaScript expression rather than a string.       -->
    &lt;BlogPost :likes="42" />

    &lt;!-- Dynamically assign to the value of a variable. -->
    &lt;BlogPost :likes="post.likes" />
  </pre>

  <h4>Boolean</h4>
  <pre>
    &lt;!-- Including the prop with no value will imply `true`. -->
    &lt;BlogPost is-published />

    &lt;!-- Even though `false` is static, we need v-bind to tell Vue that -->
    &lt;!-- this is a JavaScript expression rather than a string.          -->
    &lt;BlogPost :is-published="false" />

    &lt;!-- Dynamically assign to the value of a variable. -->
    &lt;BlogPost :is-published="post.isPublished" />
  </pre>

  <h4>Array</h4>
  <pre>
    &lt;!-- Even though the array is static, we need v-bind to tell Vue that -->
    &lt;!-- this is a JavaScript expression rather than a string.            -->
    &lt;BlogPost :comment-ids="[234, 266, 273]" />

    &lt;!-- Dynamically assign to the value of a variable. -->
    &lt;BlogPost :comment-ids="post.commentIds" />
  </pre>

  <h4>Object</h4>
  <pre>
    &lt;!-- Even though the object is static, we need v-bind to tell Vue that -->
    &lt;!-- this is a JavaScript expression rather than a string.             -->
    &lt;BlogPost
      :author="{
        name: 'Veronica',
        company: 'Veridian Dynamics'
      }"
    />

    &lt;!-- Dynamically assign to the value of a variable. -->
    &lt;BlogPost :author="post.author" />
  </pre>

  <h3>Binding Multiple Properties Using an Object</h3>
  <p>
    If you want to pass all the properties of an object as props, you can use
    <code>v-bind</code> without an argument (<code>v-bind</code> instead of
    <code>:prop-name</code>). For example, given a <code>post</code> object:
  </p>
  <pre>
    const post = {
      id: 1,
      title: 'My Journey with Vue'
    }
    ...
    &lt;BlogPost v-bind="post" />
    &lt;!-- Equivalent to -->
    &lt;BlogPost :id="post.id" :title="post.title" />
  </pre>

  <h2>One-Way Data Flow</h2>
  <p>
    All props form a <strong>one-way-down binding</strong> between the child property and the parent
    one: when the parent property updates, it will flow down to the child, but not the other way
    around. This prevents child components from accidentally mutating the parent's state, which can
    make your app's data flow harder to understand.
  </p>
  <p>
    In addition, every time the parent component is updated, all props in the child component will
    be refreshed with the latest value. This means you should <strong>not</strong> attempt to mutate
    a prop inside a child component. If you do, Vue will warn you in the console:
  </p>

  <p>To convert the prop to a local variable owned by the component itself:</p>
  <pre>
    const props = defineProps(['initialCounter'])

    // counter only uses props.initialCounter as the initial value;
    // it is disconnected from future prop updates.
    const counter = ref(props.initialCounter)
  </pre>
  <p>Or if the value needs to be transformed when the data changes:</p>
  <pre>
    const props = defineProps(['size'])

    // computed property that auto-updates when the prop changes
    const normalizedSize = computed(() => props.size.trim().toLowerCase())
  </pre>

  <h3>Mutating Object / Array Props</h3>
  <p>
    When objects and arrays are passed as props, while the child component cannot mutate the prop
    binding, it will be able to mutate the object or array's nested properties. This is because in
    JavaScript objects and arrays are passed by reference. Avoid modifying them anyways.
  </p>

  <h2>Prop Validation</h2>
  <p>
    Components can specify requirements for their props, such as the types you've already seen. If a
    requirement is not met, Vue will warn you in the browser's JavaScript console. This is
    especially useful when developing a component that is intended to be used by others.
  </p>
  <p>
    To specify prop validations, you can provide an object with validation requirements to the
    <span class="composition-api"><code>defineProps()</code> macro</span
    ><span class="options-api"><code>props</code> option</span>, instead of an array of strings. For
    example:
  </p>
  <pre>
    defineProps({
      // Basic type check
      //  (`null` and `undefined` values will allow any type)
      propA: Number,
      // Multiple possible types
      propB: [String, Number],
      // Required string
      propC: {
        type: String,
        required: true
      },
      // Required but nullable string
      propD: {
        type: [String, null],
        required: true
      },
      // Number with a default value
      propE: {
        type: Number,
        default: 100
      },
      // Object with a default value
      propF: {
        type: Object,
        // Object or array defaults must be returned from
        // a factory function. The function receives the raw
        // props received by the component as the argument.
        default(rawProps) {
          return { message: 'hello' }
        }
      },
      // Custom validator function
      // full props passed as 2nd argument in 3.4+
      propG: {
        validator(value, props) {
          // The value must match one of these strings
          return ['success', 'warning', 'danger'].includes(value)
        }
      },
      // Function with a default value
      propH: {
        type: Function,
        // Unlike object or array default, this is not a factory
        // function - this is a function to serve as a default value
        default() {
          return 'Default function'
        }
      }
    })
  </pre>
  <p>
    <strong>Note:</strong> Code inside the <code>defineProps()</code> argument
    <strong>cannot access other variables declared in <code>&lt;script setup&gt;</code></strong
    >, because the entire expression is moved to an outer function scope when compiled.
  </p>
  <p>
    When prop validation fails, Vue will produce a console warning (if using the development build).
  </p>

  <h3>Runtime Type Checks</h3>
  <p>The <code>type</code> can be one of the following native constructors:</p>
  <ul>
    <li><code>String</code></li>
    <li><code>Number</code></li>
    <li><code>Boolean</code></li>
    <li><code>Array</code></li>
    <li><code>Object</code></li>
    <li><code>Date</code></li>
    <li><code>Function</code></li>
    <li><code>Symbol</code></li>
    <li><code>Error</code></li>
  </ul>
  <p>
    In addition, <code>type</code> can also be a custom class or constructor function and the
    assertion will be made with an <code>instanceof</code> check.
  </p>

  <h2>Boolean Casting</h2>
  <p>
    Props with <code>Boolean</code> type have special casting rules to mimic the behavior of native
    boolean attributes. Given a <code>&lt;MyComponent&gt;</code> with the following declaration:
  </p>
  <pre>
    defineProps({
      disabled: Boolean
    })
  </pre>
  <p>The component can be used like this:</p>
  <pre>
    &lt;!-- equivalent of passing :disabled="true" -->
    &lt;MyComponent disabled />

    &lt;!-- equivalent of passing :disabled="false" -->
    &lt;MyComponent />
  </pre>
</template>
