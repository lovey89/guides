<script setup>
import { ref, reactive } from 'vue'

const count = ref(0)
console.log(count) // { value: 0 }
console.log(count.value) // 0

count.value++
console.log(count.value) // 1

function incrementCount() {
  count.value++
}

const obj = ref({
  nested: { count: 0 },
  arr: ['foo', 'bar'],
})

function mutateDeeply() {
  // these will work as expected.
  obj.value.nested.count++
  obj.value.arr.push('baz')
}

const state = reactive({ count: 0 })

const raw = {}
const proxy = reactive(raw)

// proxy is NOT equal to the original.
console.log(proxy === raw) // false

// Destruct ref test
const fullObj = ref({ a: 1, b: 2 })
const { a, b } = fullObj.value
function incrementFullObj() {
  fullObj.value.a++
  fullObj.value.b++
}
</script>

<template>
  <h1>Reactivity Fundamentals</h1>
  <p>
    In Composition API, the recommended way to declare reactive state is using the ref() function
  </p>
  <p>ref() takes the argument and returns it wrapped within a ref object with a .value property</p>
  <p>
    You do not need to append .value when using the ref in the template. For convenience, refs are
    automatically unwrapped when used inside templates with a few caveats (see below)
  </p>
  <span
    >Count ref: {{ count }}. Appending .value will not work it looks like: {{ count.value }}</span
  >

  <p>You can also mutate a ref directly in event handlers:</p>
  <button @click="count++">Increment count: {{ count }}</button>

  <p>
    For more complex logic, we can declare functions that mutate refs in the same scope and expose
    them as methods alongside the state.
  </p>
  <button @click="incrementCount">
    <!-- Note that it's a reference to the function and not a call with ()-->
    Increment count with function: {{ count }}
  </button>

  <h2>Why refs?</h2>
  <p>
    When you use a ref in a template, and change the ref's value later, Vue automatically detects
    the change and updates the DOM accordingly. This is made possible with a dependency-tracking
    based reactivity system. When a component is rendered for the first time, Vue tracks every ref
    that was used during the render. Later on, when a ref is mutated, it will trigger a re-render
    for components that are tracking it.
  </p>
  <p>
    In standard JavaScript, there is no way to detect the access or mutation of plain variables.
    However, we can intercept the get and set operations of an object's properties using getter and
    setter methods.
  </p>
  <p>
    The .value property gives Vue the opportunity to detect when a ref has been accessed or mutated.
    Under the hood, Vue performs the tracking in its getter, and performs triggering in its setter.
  </p>

  <h2>Deep reactivity</h2>
  <p>
    Refs can hold any value type, including deeply nested objects, arrays, or JavaScript built-in
    data structures like Map.
  </p>
  <p>
    A ref will make its value deeply reactive. This means you can expect changes to be detected even
    when you mutate nested objects or arrays
  </p>

  <button @click="mutateDeeply">Mutate deeply</button>
  <p>{{ obj }}</p>
  <p>
    It is also possible to opt-out of deep reactivity with shallow refs. For shallow refs, only
    .value access is tracked for reactivity. Shallow refs can be used for optimizing performance by
    avoiding the observation cost of large objects, or in cases where the inner state is managed by
    an external library.
  </p>

  <h2>DOM Update Timing</h2>
  <p>
    When you mutate reactive state, the DOM is updated automatically. However, it should be noted
    that the DOM updates are not applied synchronously. Instead, Vue buffers them until the "next
    tick" in the update cycle to ensure that each component updates only once no matter how many
    state changes you have made.
  </p>
  <p>
    To wait for the DOM update to complete after a state change, you can use the nextTick() global
    API calling it like <code>await nextTick()</code>
  </p>

  <h2>reactive()</h2>
  <p>
    There is another way to declare reactive state, with the <code>reactive()</code> API. Unlike a
    ref which wraps the inner value in a special object, <code>reactive()</code> makes an object
    itself reactive
  </p>
  <button @click="state.count++">Increment reactive: {{ state.count }}</button>

  <p>
    <code>reactive()</code> converts the object deeply: nested objects are also wrapped with
    <code>reactive()</code> when accessed. It is also called by <code>ref()</code> internally when
    the ref value is an object. Similar to shallow refs, there is also the
    <code>shallowReactive()</code> API for opting-out of deep reactivity.
  </p>

  <p>
    It is important to note that the returned value from <code>reactive()</code> is a Proxy of the
    original object, which is not equal to the original object (see script section)
  </p>
  <p>
    Only the proxy is reactive - mutating the original object will not trigger updates. Therefore,
    the best practice when working with Vue's reactivity system is to exclusively use the proxied
    versions of your state.
  </p>
  <p>
    To ensure consistent access to the proxy, calling <code>reactive()</code> on the same object
    always returns the same proxy, and calling <code>reactive()</code> on an existing proxy also
    returns that same proxy:
  </p>

  <h3>Limitations of reactive()</h3>
  <p>The <code>reactive()</code> API has a few limitations:</p>
  <ul>
    <li>
      Limited value types: it only works for object types (objects, arrays, and collection types
      such as Map and Set). It cannot hold primitive types such as string, number or boolean.
    </li>
    <li>
      Cannot replace entire object: since Vue's reactivity tracking works over property access, we
      must always keep the same reference to the reactive object. This means we can't easily
      "replace" a reactive object because the reactivity connection to the first reference is lost:
      <pre>
        let state = reactive({ count: 0 })

        // the above reference ({ count: 0 }) is no longer being tracked
        // (reactivity connection is lost!)
        state = reactive({ count: 1 })
      </pre>
    </li>
    <li>
      Not destructure-friendly: when we destructure a reactive object's primitive type property into
      local variables, or when we pass that property into a function, we will lose the reactivity
      connection:
      <pre>
        const state = reactive({ count: 0 })

        // count is disconnected from state.count when destructured.
        let { count } = state
        // does not affect original state
        count++

        // the function receives a plain number and
        // won't be able to track changes to state.count
        // we have to pass the entire object in to retain reactivity
        callSomeFunction(state.count)
      </pre>
    </li>
  </ul>
  <p>
    Due to these limitations, it's recommended to use <code>ref()</code> as the primary API for
    declaring reactive state.
  </p>

  <h2>Additional Ref Unwrapping Details</h2>
  <h3>As Reactive Object Property</h3>
  <p>
    A ref is automatically unwrapped when accessed or mutated as a property of a reactive object. In
    other words, it behaves like a normal property:
  </p>

  <pre>
    const count = ref(0)
    const state = reactive({
      count
    })

    console.log(state.count) // 0

    state.count = 1
    console.log(count.value) // 1
  </pre>

  <p>
    If a new ref is assigned to a property linked to an existing ref, it will replace the old ref:
  </p>

  <pre>
    const otherCount = ref(2)

    state.count = otherCount
    console.log(state.count) // 2
    // original ref is now disconnected from state.count
    console.log(count.value) // 1
  </pre>

  <h3>Caveat in Arrays and Collections</h3>
  <p>
    Unlike reactive objects, there is no unwrapping performed when the ref is accessed as an element
    of a reactive array or a native collection type like Map:
  </p>
  <pre>
    const books = reactive([ref('Vue 3 Guide')])
    // need .value here
    console.log(books[0].value)

    const map = reactive(new Map([['count', ref(0)]]))
    // need .value here
    console.log(map.get('count').value)
  </pre>

  <h3>Caveat when Unwrapping in Templates</h3>
  <p>
    Ref unwrapping in templates only applies if the ref is a top-level property in the template
    render context.
  </p>
  <p>In the example below, count and object are top-level properties, but object.id is not:</p>
  <pre>
    const count = ref(0)
    const object = { id: ref(1) }
  </pre>

  <p>Therefore, this expression works as expected:</p>
  <pre>&lcub;&lcub; count + 1 &rcub;&rcub;</pre>
  <p>...while this one does NOT:</p>
  <pre>&lcub;&lcub; object.id + 1 &rcub;&rcub;</pre>

  <p>
    The rendered result will be <code>[object Object]1</code> because <code>object.id</code> is not
    unwrapped when evaluating the expression and remains a ref object. To fix this, we can
    destructure id into a top-level property:
  </p>
  <pre>
    const { id } = object
    ...

    &lcub;&lcub; id + 1 &rcub;&rcub;
  </pre>

  <p>
    Another thing to note is that a ref does get unwrapped if it is the final evaluated value of a
    text interpolation (i.e. a <code>&lcub;&lcub; &rcub;&rcub;</code> tag), so the following will
    render 1:
  </p>
  <pre>&lcub;&lcub; object.id &rcub;&rcub;</pre>

  <p>
    This is just a convenience feature of text interpolation and is equivalent to
    <code>&lcub;&lcub; object.id.value &rcub;&rcub;</code>.
  </p>

  <h2>Destruct ref test</h2>
  <p>
    a and b seems to lose its reactivity. But click the increment buttons a few time and they will
    be updated when the full object is updated and rerendered.
  </p>
  <p>Full obj: {{ fullObj }}</p>
  <p>a: {{ a }}</p>
  <p>b: {{ b }}</p>
  <button @click="a++">Increment a</button>
  <button @click="b++">Increment b</button>
  <button @click="incrementFullObj">Increment full obj</button>
</template>
