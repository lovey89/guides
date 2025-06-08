<script setup>
import { ref, reactive } from 'vue'

const parentMessage = ref('Parent')
const items = ref([
  { message: 'Foo', myKey: 1 },
  { message: 'Bar', myKey: 2 },
])

const myObject = reactive({
  title: 'How to do lists in Vue',
  author: 'Jane Doe',
  publishedAt: '2016-04-10',
})
</script>

<template>
  <h1>List Rendering</h1>
  <h2>v-for</h2>
  <p>
    We can use the v-for directive to render a list of items based on an array. The v-for directive
    requires a special syntax in the form of <code>item in items</code>, where <code>items</code> is
    the source data array and <code>item</code> is an alias for the array element being iterated on:
  </p>
  <p>Example:</p>
  <ul>
    <li v-for="item in items">
      {{ item.message }}
    </li>
  </ul>

  <p>
    Inside the v-for scope, template expressions have access to all parent scope properties. In
    addition, v-for also supports an optional second alias for the index of the current item:
  </p>
  <ul>
    <li v-for="(item, index) in items">{{ parentMessage }} - {{ index }} - {{ item.message }}</li>
  </ul>

  <p>
    You can use destructuring on the v-for item alias similar to destructuring function arguments:
  </p>
  <ul>
    <li v-for="{ message } in items">
      {{ message }}
    </li>
  </ul>
  <p>with index alias</p>
  <ul>
    <li v-for="({ message }, index) in items">{{ message }} {{ index }}</li>
  </ul>

  <p>
    For nested v-for, scoping also works similar to nested functions. Each v-for scope has access to
    parent scopes:
  </p>
  <p>
    You can also use <code>of</code> as the delimiter instead of <code>in</code>, so that it is
    closer to JavaScript's syntax for iterators
  </p>

  <h2>v-for with an Object</h2>
  <p>
    You can also use v-for to iterate through the properties of an object. The iteration order will
    be based on the result of calling <code>Object.values()</code> on the object:
  </p>
  <p>Example</p>
  <ul>
    <li v-for="value in myObject">
      {{ value }}
    </li>
  </ul>
  <p>With keys included:</p>
  <ul>
    <li v-for="(value, key) in myObject">{{ key }}: {{ value }}</li>
  </ul>
  <p>With keys and index:</p>
  <ul>
    <li v-for="(value, key, index) in myObject">{{ index }}. {{ key }}: {{ value }}</li>
  </ul>

  <h2>v-for with a Range</h2>
  <p>
    v-for can also take an integer. In this case it will repeat the template that many times, based
    on a range of 1...n.
  </p>
  <span v-for="n in 10">{{ n }}, </span>
  <p>Note here n starts with an initial value of 1 instead of 0.</p>

  <h2>v-for on &lt;template&gt;</h2>
  <p>
    Similar to template v-if, you can also use a &lt;template&gt; tag with v-for to render a block
    of multiple elements.
  </p>
  <ul>
    <template v-for="(item, index) in items">
      <li>{{ index }}</li>
      <li>{{ item.message }}</li>
    </template>
  </ul>

  <h2>v-for with v-if</h2>
  <p>
    When they exist on the same node, v-if has a higher priority than v-for. That means the v-if
    condition will not have access to variables from the scope of the v-for
  </p>
  <pre>
  &lt;!--
  This will throw an error because property "todo"
  is not defined on instance.
  --&gt;
  &lt;li v-for="todo in todos" v-if="!todo.isComplete"&gt;
    &lcub;&lcub; todo.name &rcub;&rcub;
  &lt;/li&gt;
</pre
  >
  <p>
    This can be fixed by moving v-for to a wrapping &lt;template&gt; tag (which is also more
    explicit):
  </p>
  <pre>
  &lt;template v-for="todo in todos"&gt;
    &lt;li v-if="!todo.isComplete"&gt;
      &lcub;&lcub; todo.name &rcub;&rcub;
    &lt;/li&gt;
  &lt;/template&gt;
</pre
  >
  <p>
    It's not recommended to use v-if and v-for on the same element due to implicit precedence. There
    are two common cases where this can be tempting:
  </p>
  <ul>
    <li>
      To filter items in a list. In these cases, use a computed property that returns your filtered
      list
    </li>
    <li>
      To avoid rendering a list if it should be hidden. In these cases, move the v-if to a container
      element.
    </li>
  </ul>

  <h2>Maintaining State with key</h2>
  <p>
    When Vue is updating a list of elements rendered with v-for, by default it uses an "in-place
    patch" strategy. If the order of the data items has changed, instead of moving the DOM elements
    to match the order of the items, Vue will patch each element in-place and make sure it reflects
    what should be rendered at that particular index.
  </p>
  <p>
    This default mode is efficient, but only suitable when your list render output does not rely on
    child component state or temporary DOM state (e.g. form input values).
  </p>
  <p>
    To give Vue a hint so that it can track each node's identity, and thus reuse and reorder
    existing elements, you need to provide a unique key attribute for each item
  </p>
  <ul>
    <li v-for="item in items" :key="item.myKey">{{ item.message }}</li>
  </ul>

  <p>
    It is recommended to provide a key attribute with v-for whenever possible, unless the iterated
    DOM content is simple (i.e. contains no components or stateful DOM elements), or you are
    intentionally relying on the default behavior for performance gains.
  </p>
  <p>
    The key binding expects primitive values - i.e. strings and numbers. Do not use objects as v-for
    keys.
  </p>

  <h2>v-for with a Component</h2>
  <p>
    You can directly use v-for on a component, like any normal element (don't forget to provide a
    key)
  </p>
  <p>
    However, this won't automatically pass any data to the component, because components have
    isolated scopes of their own. In order to pass the iterated data into the component, we should
    also use props:
  </p>
  <pre>
  &lt;MyComponent
    v-for="(item, index) in items"
    :item="item"
    :index="index"
    :key="item.id"
  /&gt;
</pre
  >
  <p>
    The reason for not automatically injecting item into the component is because that makes the
    component tightly coupled to how v-for works. Being explicit about where its data comes from
    makes the component reusable in other situations.
  </p>

  <h2>Array Change Detection</h2>
  <h3>Mutation Methods</h3>
  <p>
    Vue is able to detect when a reactive array's mutation methods are called and trigger necessary
    updates. These mutation methods are:
  </p>
  <ul>
    <li>push()</li>
    <li>pop()</li>
    <li>shift()</li>
    <li>unshift()</li>
    <li>splice()</li>
    <li>sort()</li>
    <li>reverse()</li>
  </ul>

  <h3>Replacing an Array</h3>
  <p>
    Mutation methods, as the name suggests, mutate the original array they are called on. In
    comparison, there are also non-mutating methods, e.g. <code>filter()</code>,
    <code>concat()</code> and <code>slice()</code>, which do not mutate the original array but
    always return a new array. When working with non-mutating methods, we should replace the old
    array with the new one:
  </p>

  <pre>
  // `items` is a ref with array value
  items.value = items.value.filter((item) => item.message.match(/Foo/))
</pre
  >
  <p>
    You might think this will cause Vue to throw away the existing DOM and re-render the entire list
    - luckily, that is not the case. Vue implements some smart heuristics to maximize DOM element
    reuse, so replacing an array with another array containing overlapping objects is a very
    efficient operation.
  </p>

  <h2>Displaying Filtered/Sorted Results</h2>
  <p>
    Sometimes we want to display a filtered or sorted version of an array without actually mutating
    or resetting the original data. In this case, you can create a computed property that returns
    the filtered or sorted array.
  </p>

  <p>
    In situations where computed properties are not feasible (e.g. inside nested v-for loops), you
    can use a method:
  </p>

  <pre>
  const sets = ref([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
  ])

  function even(numbers) {
    return numbers.filter((number) => number % 2 === 0)
  }
</pre
  >

  <pre>
  &lt;ul v-for="numbers in sets"&gt;
    &lt;li v-for="n in even(numbers)">&lcub;&lcub; n &rcub;&rcub;&lt;li&gt;
  &lt;/ul&gt;
</pre
  >
  <p>
    Be careful with reverse() and sort() in a computed property! These two methods will mutate the
    original array, which should be avoided in computed getters. Create a copy of the original array
    before calling these methods
  </p>
</template>
