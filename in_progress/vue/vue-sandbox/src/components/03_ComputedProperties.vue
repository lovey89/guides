<script setup>
import { ref, reactive, computed } from 'vue'

const author = ref({
  name: 'John Doe',
  books: ['Vue 2 - Advanced Guide', 'Vue 3 - Basic Guide', 'Vue 4 - The Mystery'],
})

// a computed ref
const publishedBooksMessage = computed(() => {
  const noOfBooks = author.value.books.length
  return noOfBooks > 0 ? 'Yes, ' + noOfBooks + ' books' : 'No'
})

function calculateBooksMessage() {
  const noOfBooks = author.value.books.length
  return noOfBooks > 0 ? 'Yes, ' + noOfBooks + ' books' : 'No'
}

function addBook() {
  console.log('addBook() called')
  author.value.books.push('foo')
}

const firstName = ref('John')
const lastName = ref('Doe')

const fullName = computed({
  // getter
  get() {
    return firstName.value + ' ' + lastName.value
  },
  // setter
  set(newValue) {
    // Note: we are using destructuring assignment syntax here.
    ;[firstName.value, lastName.value] = newValue.split(' ')
  },
})

const count = ref(2)

// This computed will return the value of count if even otherwise it will keep the last value
const onlyEven = computed((previous) => {
  if (count.value % 2 == 0) {
    return count.value
  }

  return previous
})

const count2 = ref(3)

const onlyOdd = computed({
  get(previous) {
    if (count2.value % 2 == 1) {
      return count2.value
    }

    return previous
  },
  set(newValue) {
    count2.value = newValue
  },
})
</script>

<template>
  <h1>Computed Properties</h1>
  <h2>Basic Example</h2>
  <p>
    In-template expressions are very convenient, but they are meant for simple operations. Putting
    too much logic in your templates can make them bloated and hard to maintain. For example, if we
    have an object with a nested array:
  </p>
  <pre>
    const author = reactive({
      name: 'John Doe',
      books: [
        'Vue 2 - Advanced Guide',
        'Vue 3 - Basic Guide',
        'Vue 4 - The Mystery'
      ]
    })
  </pre>

  <p>
    And we want to display different messages depending on if author already has some books or not:
  </p>

  <pre>
    &lt;p&gt;Has published books:&lt;/p&gt;
    &lt;span&gt;&lcub;&lcub; author.books.length > 0 ? 'Yes' : 'No' &rcub;&rcub;&lt;/span&gt;
  </pre>

  <p>
    We probably don't want to repeat ourselves if we need to include this calculation in the
    template more than once.
  </p>
  <p>
    For complex logic that includes reactive data, it is recommended to use a bcomputed property.
    Here's the same example, refactored:
  </p>

  <pre>
    &lt;script setup&gt;
      import { reactive, computed } from 'vue'

      const author = reactive({
        name: 'John Doe',
        books: [
          'Vue 2 - Advanced Guide',
          'Vue 3 - Basic Guide',
          'Vue 4 - The Mystery'
        ]
      })

      // a computed ref
      const publishedBooksMessage = computed(() => {
        return author.books.length > 0 ? 'Yes' : 'No'
      })
      &lt;/script&gt;

      &lt;template&gt;
        &lt;p>Has published books:&lt;/p&gt;
        &lt;span>&lcub;&lcub; publishedBooksMessage &rcub;&rcub;&lt;/span&gt;
      &lt;/template&gt;
  </pre>

  <p>Example but with ref instead and a add book addition:</p>
  <p>Has published books:</p>

  <span>{{ publishedBooksMessage }}</span>
  <button @click="addBook">Add book</button>

  <p>
    The <code>computed()</code> function expects to be passed a
    <a
      href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#description"
      >getter function</a
    >, and the returned value is a computed ref. Similar to normal refs, you can access the computed
    result as publishedBooksMessage.value. Computed refs are also auto-unwrapped in templates so you
    can reference them without .value in template expressions.
  </p>

  <p>
    Instead of a computed property, we can define the same function as a method. For the end result,
    the two approaches are indeed exactly the same. However, the difference is that computed
    properties are cached based on their reactive dependencies. A computed property will only
    re-evaluate when some of its reactive dependencies have changed. This means as long as
    author.books has not changed, multiple access to publishedBooksMessage will immediately return
    the previously computed result without having to run the getter function again.
  </p>

  <p>
    It looks like even if we do use a function it will react immediately when something is updated.
    Does that mean that it is rerendered all the time? It only prints a console message when the
    button is clicked so I guess not...
  </p>

  <p>Has published books (add books by the same button above):</p>
  <span>{{ calculateBooksMessage() }}</span>

  <h2>Writable Computed</h2>
  <p>
    Computed properties are by default getter-only. If you attempt to assign a new value to a
    computed property, you will receive a runtime warning. In the rare cases where you need a
    "writable" computed property, you can create one by providing both a getter and a setter. See
    the <code>fullName</code> value in the <code>script</code> section.
  </p>

  <p>
    Now when you run <code>fullName.value = 'John Doe'</code>, the setter will be invoked and
    firstName and lastName will be updated accordingly.
  </p>
  <p>First name: {{ firstName }}</p>
  <p>Last name: {{ lastName }}</p>
  <p>Full name: {{ fullName }}</p>
  <!-- Experimenting with arrow function -->
  <button
    @click="
      () => {
        fullName = 'Dimp Domp'
      }
    "
  >
    Set name to Dimp Domp
  </button>
  <button @click="fullName = 'Herp Derp'">Set name to Herp Derp</button>

  <h2>Getting the Previous Value</h2>
  <p>
    In case you need it, you can get the previous value returned by the computed property accessing
    the first argument of the getter. See example in <code>script</code> section.
  </p>
  <p>Count: {{ count }}</p>
  <p>Computed even: {{ onlyEven }}</p>
  <button @click="count = Math.floor(Math.random() * 1000)">Generate random number</button>

  <p>In case you're using a writable computed. Again see example in <code>script</code> section.</p>
  <p>Count: {{ count2 }}</p>
  <p>Computed odd: {{ onlyOdd }}</p>
  <button @click="onlyOdd = Math.floor(Math.random() * 1000)">Generate random number</button>

  <h2>Best Practices</h2>
  <p>
    Getters should be side-effect free. Later we will discuss how we can perform side effects in
    reaction to state changes with watchers.
  </p>
  <p>
    Avoid mutating computed value. The returned value from a computed property is derived state.
    Think of it as a temporary snapshot - every time the source state changes, a new snapshot is
    created. It does not make sense to mutate a snapshot, so a computed return value should be
    treated as read-only and never be mutated - instead, update the source state it depends on to
    trigger new computations.
  </p>
</template>
