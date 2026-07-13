<template>
  <div class="container">
    <h1>Course Details</h1>

    <div class="card">
      <h2>{{ course.name }}</h2>

      <p><strong>Code:</strong> {{ course.code }}</p>

      <p><strong>Credits:</strong> {{ course.credits }}</p>

      <p><strong>Grade:</strong> {{ course.grade }}</p>

      <button @click="enrollCourse">
        Enroll
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { useEnrollmentStore } from "../stores/enrollment";

const route = useRoute();
const router = useRouter();
const store = useEnrollmentStore();

const courses = [
  { id: 1, name: "Java Programming", code: "CS101", credits: 4, grade: "A" },
  { id: 2, name: "Python Programming", code: "CS102", credits: 4, grade: "A+" },
  { id: 3, name: "Web Development", code: "CS103", credits: 3, grade: "A" },
  { id: 4, name: "Database Management", code: "CS104", credits: 4, grade: "B+" },
  { id: 5, name: "Software Engineering", code: "CS105", credits: 4, grade: "A+" }
];

const course =
  courses.find(c => c.id == route.params.id) || courses[0];

function enrollCourse() {
  store.enroll(course);
  alert("Course Enrolled Successfully!");
  router.push("/profile");
}
</script>

<style scoped>
.container{
  padding:40px;
}

.card{
  max-width:500px;
  margin:auto;
  padding:20px;
  background:white;
  border-radius:12px;
  box-shadow:0 5px 15px rgba(0,0,0,0.2);
}

button{
  margin-top:20px;
  padding:10px 20px;
  border:none;
  background:#2563eb;
  color:white;
  border-radius:6px;
  cursor:pointer;
}
</style>