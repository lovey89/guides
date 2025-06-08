<script setup>
let msg = 'Derp'
let rawHtml = '<span style="color: red">This should be red.</span>'

let myIdVar = 'myId'
let id = 'myOtherId'

let isButtonDisabled = true // An empty string will also disable the button even though empty string is usually falsy

const objectOfAttrs = {
  id: 'myId',
  class: 'myClass',
  style: 'border:solid',
}

const aNumber = 2
const aString = 'This is a string'

const partialId = 'Id' // "OtherId";

const attributeName = 'id' //"class";
const aTestVar = 'aTest'
</script>

<template>
  <h1>Template syntax</h1>

  <h2>Text interpolation</h2>
  <p>Text interpolation using the "Mustache" syntax (double curly braces)</p>
  <span>Message: {{ msg }}</span>

  <h3>Using raw html</h3>
  <p>
    The double mustaches interpret the data as plain text, not HTML. In order to output real HTML,
    you will need to use the v-html directive
  </p>
  <p>Using text interpolation: {{ rawHtml }}</p>
  <p>Using v-html directive: <span v-html="rawHtml"></span></p>

  <h1>Attribute binding</h1>
  <p>Mustaches cannot be used inside HTML attributes. Instead, use a v-bind directive</p>
  <p v-bind:id="myIdVar">This string has a variable id</p>
  <p>
    The v-bind directive instructs Vue to keep the element's id attribute in sync with the
    component's dynamicId property. If the bound value is null or undefined, then the attribute will
    be removed from the rendered element.
  </p>

  <p>Because v-bind is so commonly used, it has a dedicated shorthand syntax</p>
  <p :id="myIdVar">This string also has a variable id</p>

  <h2>Same-name Shorthand</h2>
  <p>
    If the attribute has the same name as the variable name of the JavaScript value being bound, the
    syntax can be further shortened to omit the attribute value
  </p>
  <p :id="id">This belongs to the id "myOtherId"</p>
  <p :id>And so does this in short form (I know you should not reuse id's but for now it's ok)</p>

  <h2>Boolean attributes</h2>
  <p>
    Boolean attributes are attributes that can indicate true / false values by their presence on an
    element. For example, disabled is one of the most commonly used boolean attributes.
  </p>
  <p>v-bind works a bit differently in this case</p>
  <button :disabled="isButtonDisabled">Button</button>
  <p>
    The disabled attribute will be included if isButtonDisabled has a truthy value. It will also be
    included if the value is an empty string, maintaining consistency with &lt;button
    disabled=""&gt;. For other falsy values the attribute will be omitted.
  </p>

  <h2>Dynamically Binding Multiple Attributes</h2>
  <p>
    If you have a JavaScript object representing multiple attributes you can bind them to a single
    element by using v-bind without an argument
  </p>
  <p v-bind="objectOfAttrs">String with many things happening</p>

  <h1>Using JavaScript Expressions</h1>
  <p>In Vue templates, JavaScript expressions can be used in the following positions:</p>
  <ul>
    <li>Inside text interpolations (mustaches)</li>
    <li>In the attribute value of any Vue directives (special attributes that start with v-)</li>
  </ul>
  <p>A number: {{ aNumber + 1 }}</p>
  <p>A reversed string: {{ aString.split(' ').reverse().join(' ') }}</p>
  <p :id="`my${partialId}`">A dynamic id</p>
  <p>
    Each binding can only contain one single expression. An expression is a piece of code that can
    be evaluated to a value. A simple check is whether it can be used after return.
  </p>
  <p>It's possible to call a component-exposed method inside a binding expression</p>

  <h1>Directives</h1>
  <p>Directives are special attributes with the v- prefix.</p>

  <h2>Arguments</h2>
  <p>
    Some directives can take an "argument", denoted by a colon after the directive name. E.g.
    "v-bind:href" ("href" is argument). Or "v-on:click" ("click" is argument)
  </p>

  <h3>Dynamic arguments</h3>
  <p>
    It is also possible to use a JavaScript expression in a directive argument by wrapping it with
    square brackets
  </p>
  <p :[attributeName]="aTestVar">Here's a test string that is controlled either by id or class</p>
  <p>
    Dynamic arguments are expected to evaluate to a string, with the exception of null. The special
    value null can be used to explicitly remove the binding. Any other non-string value will trigger
    a warning.
  </p>
  <p>
    If you need to pass a complex dynamic argument, it's probably better to use a computed property,
    which we will cover later.
  </p>

  <h2>Modifiers</h2>
  <p>
    Modifiers are special postfixes denoted by a dot, which indicate that a directive should be
    bound in some special way. For example, the .prevent modifier tells the v-on directive to call
    event.preventDefault() on the triggered event
  </p>
  <p>You'll see other exampes of modifiers later.</p>

  <p>
    The example v-on:submit.prevent="onSubmit", "v-on" is the name, "submit" is the argument,
    "prevent" is the modifier and "onSubmit" the value
  </p>
</template>

<style>
#myId {
  color: green;
}

#myOtherId {
  color: purple;
}

.myClass {
  background-color: black;
}

#aTest {
  color: red;
}

.aTest {
  color: blue;
}
</style>
