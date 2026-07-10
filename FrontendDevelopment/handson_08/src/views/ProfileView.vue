<template>

<div class="profile">

<h1>Student Profile</h1>

<h2>Enrolled Courses</h2>

<div
class="card"
v-for="course in store.enrolledCourses"
:key="course.id"
>

<h3>{{ course.name }}</h3>

<p>Code : {{ course.code }}</p>

<p>Credits : {{ course.credits }}</p>

<p>Grade : {{ course.grade }}</p>

<button
class="remove"
@click="store.unenroll(course.id)"
>
Remove
</button>

</div>

<h2 class="credits">

Total Credits :
{{ store.totalCredits }}

</h2>

</div>

</template>

<script setup>

import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

</script>

<style scoped>

.profile{

padding:40px;

background:#eef5ff;

min-height:100vh;

}

.card{

background:white;

padding:20px;

margin-bottom:20px;

border-radius:15px;

box-shadow:0 8px 18px rgba(0,0,0,.15);

}

.card h3{

color:#2563eb;

margin-bottom:10px;

}

.remove{

margin-top:10px;

padding:10px 20px;

background:#ef4444;

border:none;

color:white;

border-radius:8px;

cursor:pointer;

}

.remove:hover{

background:#dc2626;

}

.credits{

margin-top:30px;

color:#0f172a;

}

</style>