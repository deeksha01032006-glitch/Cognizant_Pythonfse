<template>
  <div class="profile">

    <h1>Student Profile</h1>

    <h2>Total Enrolled Courses: {{ total }}</h2>

    <button @click="clearEnrollments">
      Reset Enrollment
    </button>

    <div
      v-for="course in enrolledCourses"
      :key="course.id"
      class="card"
    >
      <h3>{{ course.name }}</h3>

      <p>Code : {{ course.code }}</p>

      <p>Credits : {{ course.credits }}</p>

      <p>Grade : {{ course.grade }}</p>

    </div>

  </div>
</template>

<script setup>
import { storeToRefs } from "pinia";
import { useEnrollmentStore } from "../stores/enrollment";

const store = useEnrollmentStore();

const { enrolledCourses, total } = storeToRefs(store);

function clearEnrollments() {
  store.$reset();
}
</script>

<style scoped>

.profile{
    width:90%;
    margin:auto;
    padding:40px;
}

.card{

    margin-top:20px;
    padding:20px;

    border-radius:10px;

    background:white;

    box-shadow:0 5px 10px rgba(0,0,0,.2);
}

button{

    margin:20px 0;

    padding:12px 20px;

    background:#2563eb;

    color:white;

    border:none;

    border-radius:8px;

    cursor:pointer;
}

</style>