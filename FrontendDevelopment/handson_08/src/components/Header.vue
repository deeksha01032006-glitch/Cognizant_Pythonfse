<template>
  <header class="header">
    <div class="logo">
      🎓 Student Portal
    </div>

    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/courses">Courses</RouterLink>
      <RouterLink to="/profile">
        Profile ({{ store.enrolledCourses.length }})
      </RouterLink>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<style scoped>
.header{
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:20px 60px;
  background:linear-gradient(90deg,#2563eb,#7c3aed);
  color:white;
  box-shadow:0 4px 15px rgba(0,0,0,.2);
}

.logo{
  font-size:34px;
  font-weight:bold;
}

nav{
  display:flex;
  gap:30px;
}

nav a{
  color:white;
  text-decoration:none;
  font-size:20px;
  font-weight:600;
  transition:.3s;
}

nav a:hover{
  color:#ffd54f;
}
</style>