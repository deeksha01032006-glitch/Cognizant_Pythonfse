<template>
  <header>
    <h1>🎓 Student Portal</h1>

    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/courses">Courses</RouterLink>
      <RouterLink to="/profile">
        Profile ({{ enrolledCourses.length }})
      </RouterLink>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'
import { storeToRefs } from 'pinia'

const store = useEnrollmentStore()
const { enrolledCourses } = storeToRefs(store)
</script>

<style scoped>
header{
display:flex;
justify-content:space-between;
align-items:center;
padding:20px 50px;
background:#2563eb;
color:white;
}

nav{
display:flex;
gap:25px;
}

a{
color:white;
font-weight:bold;
text-decoration:none;
}

.router-link-active{
color:yellow;
}
</style>