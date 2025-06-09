<script setup>
import { ref, reactive, watch, watchEffect } from 'vue'

const question = ref('')
const answer = ref('Questions usually contain a question mark. ;-)')
const loading = ref(false)

// watch works directly on a ref
watch(question, async (newQuestion, oldQuestion) => {
  if (newQuestion.includes('?')) {
    loading.value = true
    answer.value = 'Thinking...'
    try {
      const res = await fetch('https://yesno.wtf/api')
      answer.value = (await res.json()).answer
    } catch (error) {
      answer.value = 'Error! Could not reach the API. ' + error
    } finally {
      loading.value = false
    }
  }
})

const x = ref(0)
const y = ref(0)
// single ref
watch(x, (newX) => {
  console.log(`x is ${newX}`)
})

// getter
watch(
  () => x.value + y.value,
  (sum) => {
    console.log(`sum of x + y is: ${sum}`)
  },
)

// array of multiple sources
watch([x, () => y.value], ([newX, newY]) => {
  console.log(`x is ${newX} and y is ${newY}`)
})

// Doens't work with ref it looks like
const countObj = reactive({ count: 0 })
watch(countObj, (newValue, oldValue) => {
  // fires on nested property mutations
  // Note: `newValue` will be equal to `oldValue` here
  // because they both point to the same object!
  console.log(`countObj is now ${JSON.stringify(newValue)}`)
})

const count = ref(0)
watch(
  count,
  (newValue, oldValue) => {
    console.log(`count is now ${newValue}`)
  },
  { once: true },
)

const todoId = ref(1)
const data = ref(null)

watch(
  todoId,
  async () => {
    data.value = 'Fetching, please wait'
    const response = await fetch(`https://jsonplaceholder.typicode.com/todos/${todoId.value}`)
    data.value = await response.json()
  },
  { immediate: true },
)

const todoId2 = ref(1)
const data2 = ref(null)

watchEffect(async () => {
  data2.value = 'Fetching, please wait'
  const response = await fetch(`https://jsonplaceholder.typicode.com/todos/${todoId2.value}`)
  data2.value = await response.json()
})
</script>

<template>
  <h1>Watchers</h1>
  <h2>Basic Example</h2>
  <p>
    Computed properties allow us to declaratively compute derived values. However, there are cases
    where we need to perform "side effects" in reaction to state changes - for example, mutating the
    DOM, or changing another piece of state based on the result of an async operation.
  </p>
  <p>
    With Composition API, we can use the watch function to trigger a callback whenever a piece of
    reactive state changes:
  </p>

  <div style="background-color: gainsboro">
    <p>
      Ask a yes/no question:
      <input v-model="question" :disabled="loading" />
    </p>
    <p>{{ answer }}</p>
  </div>

  <h2>Watch Source Types</h2>
  <p>
    watch's first argument can be different types of reactive "sources": it can be a ref (including
    computed refs), a reactive object, a getter function, or an array of multiple sources.
  </p>
  <p>Examples (check the console as you update these values):</p>
  <span>x:</span>
  <input type="number" min="0" max="100" v-model="x" />
  <span>y:</span>
  <input type="number" min="0" max="100" v-model="y" />

  <p>Do note that you can't watch a property of a reactive object like this:</p>
  <pre>
  const obj = reactive({ count: 0 })

  // this won't work because we are passing a number to watch()
  watch(obj.count, (count) => {
    console.log(`Count is: ${count}`)
  })
</pre
  >
  <p>Instead, use a getter:</p>
  <pre>
  // instead, use a getter:
  watch(
    () => obj.count,
    (count) => {
      console.log(`Count is: ${count}`)
    }
  )
</pre
  >

  <h2>Deep Watchers</h2>
  <p>
    When you call watch() directly on a reactive object, it will implicitly create a deep watcher -
    the callback will be triggered on all nested mutations:
  </p>
  <button @click="countObj.count++">
    Increment countObj.count and check console: {{ countObj }}
  </button>

  <p>
    This should be differentiated with a getter that returns a reactive object - in the latter case,
    the callback will only fire if the getter returns a different object:
  </p>
  <pre>
  watch(
    () => state.someObject,
    () => {
      // fires only when state.someObject is replaced
    }
  )
</pre
  >
  <p>
    You can, however, force the second case into a deep watcher by explicitly using the deep option:
  </p>
  <pre>
  watch(
    () => state.someObject,
    (newValue, oldValue) => {
      // Note: `newValue` will be equal to `oldValue` here
      // *unless* state.someObject has been replaced
    },
    { deep: true }
  )
</pre
  >
  <p>
    In Vue 3.5+, the deep option can also be a number indicating the max traversal depth - i.e. how
    many levels should Vue traverse an object's nested properties.
  </p>
  <p>
    <strong>Use with Caution:</strong> Deep watch requires traversing all nested properties in the
    watched object, and can be expensive when used on large data structures. Use it only when
    necessary and beware of the performance implications.
  </p>

  <h2>Eager Watchers</h2>
  <p>
    watch is lazy by default: the callback won't be called until the watched source has changed. But
    in some cases we may want the same callback logic to be run eagerly - for example, we may want
    to fetch some initial data, and then re-fetch the data whenever relevant state changes.
  </p>
  <p>
    We can force a watcher's callback to be executed immediately by passing the
    <code>immediate: true</code> option:
  </p>
  <pre>
  watch(
    source,
    (newValue, oldValue) => {
      // executed immediately, then again when `source` changes
    },
    { immediate: true }
  )
</pre
  >

  <h2>Once Watchers</h2>
  Watcher's callback will execute whenever the watched source changes. If you want the callback to
  trigger only once when the source changes, use the <code>once: true</code> option.
  <button @click="count++">Increment count and check console: {{ count }}</button>

  <h2>watchEffect()</h2>
  <p>
    It is common for the watcher callback to use exactly the same reactive state as the source. E.g.
  </p>
  <div style="background-color: gainsboro">
    <p>Data: {{ data }}</p>
    <button @click="todoId++">Increment todoId: {{ todoId }}</button>
  </div>
  <p>
    Notice how the watcher uses todoId twice, once as the source and then again inside the callback.
  </p>
  <p>
    This can be simplified with watchEffect(). watchEffect() allows us to track the callback's
    reactive dependencies automatically. Here's the example above again with watchEffect():
  </p>
  <div style="background-color: gainsboro">
    <p>Data: {{ data2 }}</p>
    <button @click="todoId2++">Increment todoId: {{ todoId2 }}</button>
  </div>
  <p>
    Here, the callback will run immediately, there's no need to specify
    <code>immediate: true</code>. During its execution, it will automatically track todoId.value as
    a dependency (similar to computed properties).
  </p>
  <p>
    If you need to watch several properties in a nested data structure, watchEffect() may prove more
    efficient than a deep watcher, as it will only track the properties that are used in the
    callback, rather than recursively tracking all of them.
  </p>
  <p>
    <strong>Tip:</strong> watchEffect only tracks dependencies during its synchronous execution.
    When using it with an async callback, only properties accessed before the first await tick will
    be tracked.
  </p>

  <h3>watch vs. watchEffect</h3>
  <p>
    watch and watchEffect both allow us to reactively perform side effects. Their main difference is
    the way they track their reactive dependencies:
  </p>
  <ul>
    <li>
      watch only tracks the explicitly watched source. It won't track anything accessed inside the
      callback. In addition, the callback only triggers when the source has actually changed. watch
      separates dependency tracking from the side effect, giving us more precise control over when
      the callback should fire.
    </li>
    <li>
      watchEffect, on the other hand, combines dependency tracking and side effect into one phase.
      It automatically tracks every reactive property accessed during its synchronous execution.
      This is more convenient and typically results in terser code, but makes its reactive
      dependencies less explicit.
    </li>
  </ul>

  <h2>Side Effect Cleanup</h2>
  <p>Sometimes we may perform side effects, e.g. asynchronous requests, in a watcher:</p>
  <pre>
  watch(id, (newId) => {
    fetch(`/api/${newId}`).then(() => {
      // callback logic
    })
  })
</pre
  >
  <p>
    But what if id changes before the request completes? When the previous request completes, it
    will still fire the callback with an ID value that is already stale. Ideally, we want to be able
    to cancel the stale request when id changes to a new value.
  </p>
  <p>
    We can use the <code>onWatcherCleanup()</code> API to register a cleanup function that will be
    called when the watcher is invalidated and is about to re-run:
  </p>

  <pre>
  import { watch, onWatcherCleanup } from 'vue'

  watch(id, (newId) => {
    const controller = new AbortController()

    fetch(`/api/${newId}`, { signal: controller.signal }).then(() => {
      // callback logic
    })

    onWatcherCleanup(() => {
      // abort stale request
      controller.abort()
    })
  })
</pre
  >
  <p>
    Note that <code>onWatcherCleanup</code> must be called during the synchronous execution of a
    watchEffect effect function or watch callback function: you cannot call it after an await
    statement in an async function.
  </p>
  <p>
    Alternatively, an <code>onCleanup</code> function is also passed to watcher callbacks as the 3rd
    argument, and to the watchEffect effect function as the first argument:
  </p>
  <pre>
  watch(id, (newId, oldId, onCleanup) => {
    // ...
    onCleanup(() => {
      // cleanup logic
    })
  })

  watchEffect((onCleanup) => {
    // ...
    onCleanup(() => {
      // cleanup logic
    })
  })
</pre
  >
  <p>
    <code>onCleanup</code> passed via function argument is bound to the watcher instance so it is
    not subject to the synchronously constraint of onWatcherCleanup.
  </p>

  <h2>Callback Flush Timing</h2>
  <p>
    When you mutate reactive state, it may trigger both Vue component updates and watcher callbacks
    created by you.
  </p>
  <p>
    Similar to component updates, user-created watcher callbacks are batched to avoid duplicate
    invocations. For example, we probably don't want a watcher to fire a thousand times if we
    synchronously push a thousand items into an array being watched.
  </p>
  <p>
    By default, a watcher's callback is called after parent component updates (if any), and before
    the owner component's DOM updates. This means if you attempt to access the owner component's own
    DOM inside a watcher callback, the DOM will be in a pre-update state.
    <span style="color: red">TODO: What does this actually mean?</span>
  </p>

  <h3>Post Watchers</h3>
  <p>
    If you want to access the owner component's DOM in a watcher callback after Vue has updated it,
    you need to specify the flush: 'post' option:
  </p>
  <pre>
  watch(source, callback, {
    flush: 'post'
  })

  watchEffect(callback, {
    flush: 'post'
  })
</pre
  >
  <p>Post-flush watchEffect() also has a convenience alias, watchPostEffect():</p>
  <pre>
  import { watchPostEffect } from 'vue'

  watchPostEffect(() => {
    /* executed after Vue updates */
  })
</pre
  >

  <h3>Sync Watchers</h3>
  <p style="color: red">TODO</p>
  <h2>Stopping a Watcher</h2>
  <p>
    Watchers declared synchronously inside setup() or &lt;script setup> are bound to the owner
    component instance, and will be automatically stopped when the owner component is unmounted. In
    most cases, you don't need to worry about stopping the watcher yourself.
  </p>
  <p>
    The key here is that the watcher must be created <strong>synchronously</strong>: if the watcher
    is created in an async callback, it won't be bound to the owner component and must be stopped
    manually to avoid memory leaks. Here's an example:
  </p>

  <pre>
  &lt;script setup>
  import { watchEffect } from 'vue'

  // this one will be automatically stopped
  watchEffect(() => {})

  // ...this one will not!
  setTimeout(() => {
    watchEffect(() => {})
  }, 100)
  &lt;/script>
</pre
  >
  <p>
    To manually stop a watcher, use the returned handle function. This works for both watch and
    watchEffect:
  </p>
  <pre>
  const unwatch = watchEffect(() => {})

  // ...later, when no longer needed
  unwatch()
</pre
  >
  <p>
    Note that there should be very few cases where you need to create watchers asynchronously, and
    synchronous creation should be preferred whenever possible. If you need to wait for some async
    data, you can make your watch logic conditional instead.
  </p>
  <pre>
  // data to be loaded asynchronously
  const data = ref(null)

  watchEffect(() => {
    if (data.value) {
      // do something when data is loaded
    }
  })
</pre
  >
</template>
