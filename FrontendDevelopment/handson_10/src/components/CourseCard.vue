<template>
  <div class="card">

    <h2>{{ course.name }}</h2>

    <p><strong>Code:</strong> {{ course.code }}</p>

    <p><strong>Credits:</strong> {{ course.credits }}</p>

    <p><strong>Grade:</strong> {{ course.grade }}</p>

    <button @click="enroll">
      Enroll
    </button>

  </div>
</template>

<script setup>
import { useEnrollmentStore } from "../stores/enrollment";

const props = defineProps({
  course: Object
});

const store = useEnrollmentStore();

function enroll() {
  store.fetchAndEnroll(props.course.id);
}
</script>

<style scoped>
.card{
  background:white;
  padding:20px;
  border-radius:10px;
  box-shadow:0 5px 10px rgba(0,0,0,.2);
}

button{
  margin-top:15px;
  width:100%;
  padding:10px;
  background:#2563eb;
  color:white;
  border:none;
  border-radius:6px;
  cursor:pointer;
}
</style>