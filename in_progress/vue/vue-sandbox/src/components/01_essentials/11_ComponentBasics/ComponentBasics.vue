<script setup>
import { ref } from 'vue'
import ButtonCounter from './ButtonCounter.vue'
import BlogPost from './BlogPost.vue'
import AdvancedBlogPost from './AdvancedBlogPost.vue'
import AlertBox from './AlertBox.vue'
import Home from './Home.vue'
import Posts from './Posts.vue'
import Archive from './Archive.vue'

const posts = ref([
  { id: 1, title: 'My journey with Vue', postFontSize: ref(1) },
  { id: 2, title: 'Blogging with Vue', postFontSize: ref(1) },
  { id: 3, title: 'Why Vue is so fun', postFontSize: ref(1) },
])

const currentTab = ref('Home')

const tabs = {
  Home,
  Posts,
  Archive,
}
</script>

<template>
  <h1>Components Basics</h1>
  <h2>Defining a Component</h2>
  <p>
    When using a build step, we typically define each Vue component in a dedicated file using the
    <code>.vue</code> extension - known as a Single-File Component (SFC for short). Check the
    <code>ButtonCounter.vue</code> file for an example
  </p>

  <h2>Using a Component</h2>
  <p>
    To use a child component, we need to import it in the parent component. The component will be
    exposed as the file's default export
  </p>
  <p>
    With <code>&lt;script setup></code>, imported components are automatically made available to the
    template.
  </p>
  <p>
    It's also possible to globally register a component, making it available to all components in a
    given app without having to import it. More about that later.
  </p>
  <p>Components can be reused as many times as you want. Here are many child components!</p>
  <div style="background-color: gainsboro">
    <ButtonCounter />
    <ButtonCounter />
    <ButtonCounter />
  </div>
  <p>
    Notice that when clicking on the buttons, each one maintains its own, separate
    <code>count</code>. That's because each time you use a component, a new instance of it is
    created.
  </p>

  <h2>Passing Props (Arguments)</h2>
  <p>
    Props are custom attributes you can register on a component. To pass a title to our blog post
    component, we must declare it in the list of props this component accepts, using the
    <code>defineProps</code> macro (see the <code>BlogPost.vue</code> file).
  </p>
  <p>
    <code>defineProps</code> is a compile-time macro that is only available inside
    <code>&lt;script setup></code> and does not need to be explicitly imported. Declared props are
    automatically exposed to the template. <code>defineProps</code> also returns an object that
    contains all the props passed to the component, so that we can access them in JavaScript if
    needed.
  </p>
  <pre>
    const props = defineProps(['title'])
    console.log(props.title)
  </pre>
  <p>
    A component can have as many props as you like and, by default, any value can be passed to any
    prop.
  </p>
  <p>Once a prop is registered, you can pass data to it as a custom attribute, like this:</p>

  <div style="background-color: gainsboro">
    <!-- v-bind syntax is allowed -->
    <BlogPost v-for="post in posts" :key="post.id" :title="post.title" />
  </div>

  <h2>Emitting events</h2>
  <p>Some features may require communicating back up to the parent.</p>
  <p>
    Components provide a custom events system. The parent can choose to listen to any event on the
    child component instance with <code>v-on</code> or <code>@</code>, just as we would with a
    native DOM event. In the example below we are listening for the <code>enlarge-text</code> event.
  </p>
  <p>
    Then the child component can emit an event on itself by calling the built-in
    <code>$emit</code> method, passing the name of the event. See the
    <code>AdvancedBlogPost.vue</code> file
  </p>

  <div style="background-color: gainsboro">
    <AdvancedBlogPost
      v-for="post in posts"
      :style="{ fontSize: post.postFontSize + 'em' }"
      :key="post.id"
      :title="post.title"
      @enlarge-text="post.postFontSize += 0.1"
    />
  </div>
  <p>We can optionally declare emitted events using the <code>defineEmits</code> macro:</p>
  <pre>
    &lt;script setup>
    defineProps(['title'])
    defineEmits(['enlarge-text'])
    &lt;/script>
  </pre>
  <p>
    This documents all the events that a component emits and optionally validates them. It also
    allows Vue to avoid implicitly applying them as native listeners to the child component's root
    element.
  </p>

  <p>
    Similar to <code>defineProps</code>, <code>defineEmits</code> is only usable in
    <code>&lt;script setup></code> and doesn't need to be imported. It returns an
    <code>emit</code> function that is equivalent to the <code>$emit</code> method. It can be used
    to emit events in the <code>&lt;script setup></code> section of a component, where
    <code>$emit</code> isn't directly accessible:
  </p>
  <pre>
    &lt;script setup>
    const emit = defineEmits(['enlarge-text'])

    emit('enlarge-text')
    &lt;/script>
  </pre>

  <h2>Content Distribution with Slots</h2>
  <p>
    Just like with HTML elements, it's often useful to be able to pass content to a component, like
    this:
  </p>
  <pre>
    &lt;AlertBox>
      Something bad happened.
    &lt;/AlertBox>
  </pre>
  <p>
    This can be achieved using Vue's custom <code>&lt;slot></code> element. See the
    <code>AlertBox.vue</code> file for an example:
  </p>
  <AlertBox> Something bad happened. </AlertBox>
  <p>
    As you'll see above, we use the <code>&lt;slot></code> as a placeholder where we want the
    content to go.
  </p>

  <h2>Dynamic Components</h2>
  <p>
    Sometimes, it's useful to dynamically switch between components, like in a tabbed interface:
  </p>
  <div class="demo">
    <button
      v-for="(_, tab) in tabs"
      :key="tab"
      :class="['tab-button', { selectedTab: currentTab === tab }]"
      @click="currentTab = tab"
    >
      {{ tab }}
    </button>
    <component :is="tabs[currentTab]" class="tab"></component>
  </div>
  <p>
    The above is made possible by Vue's <code>&lt;component></code> element with the special
    <code>:is</code> attribute.
  </p>
  <p>
    The value passed to <code>:is</code> can contain either the name string of a registered
    component, or the actual imported component object
  </p>
  <p>
    When switching between multiple components with <code>&lt;component :is="..."&gt;</code>, a
    component will be unmounted when it is switched away from. We can force the inactive components
    to stay "alive" with the built-in <code>&lt;KeepAlive&gt;</code> component.
  </p>
</template>

<style scoped>
.demo {
  font-family: sans-serif;
  border: 1px solid #eee;
  border-radius: 2px;
  padding: 20px 30px;
  margin-top: 1em;
  margin-bottom: 40px;
  user-select: none;
  overflow-x: auto;
}

.tab-button {
  padding: 6px 10px;
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
  border: 1px solid #ccc;
  cursor: pointer;
  background: #f0f0f0;
  margin-bottom: -1px;
  margin-right: -1px;
}
.tab-button:hover {
  background: #e0e0e0;
}
.tab-button.selectedTab {
  background: #e0e0e0;
}
.tab {
  border: 1px solid #ccc;
  padding: 10px;
}
</style>
