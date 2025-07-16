<script setup>
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import { NButton, NModal, NCard } from 'naive-ui'

const router = useRouter()
const route = useRoute()

const search = computed({
  get() {
    return route.query.search ?? ''
  },
  set(search) {
    router.replace({ query: { search } })
  }
})

const showModal = ref(false);
</script>

<template>
  <h2>AboutView</h2>
  <label>
    Search: <input v-model.trim="search" maxlength="20">
  </label>
  <NButton @click="showModal = true">
    Start me up
  </NButton>
  <NModal v-model:show="showModal">
    <NCard

      title="Modal"
      :bordered="false"
      size="huge"
      role="dialog"
      aria-modal="false"
      closable="true"
    >
      <template #header-extra>
        Oops!
      </template>
      <div style="width: 1000px;">
        Content
      </div>
      <template #footer>
        Footer
      </template>
    </NCard>
  </NModal>
</template>

<style scoped>
  .n-card {
    width: 70%;
  }
</style>
