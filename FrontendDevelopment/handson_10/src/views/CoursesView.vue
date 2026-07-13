<template>
  <div class="container">
    <h1>Available Courses</h1>

    <input
      type="text"
      v-model="search"
      placeholder="Search course..."
      class="search"
    />

    <div class="courses">
      <CourseCard
        v-for="course in filteredCourses"
        :key="course.id"
        :course="course"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import CourseCard from "../components/CourseCard.vue";

const search = ref("");

const courses = ref([
  {
    id: 1,
    name: "Java Programming",
    code: "CS101",
    credits: 4,
    grade: "A"
  },
  {
    id: 2,
    name: "Python Programming",
    code: "CS102",
    credits: 4,
    grade: "A+"
  },
  {
    id: 3,
    name: "Web Development",
    code: "CS103",
    credits: 3,
    grade: "A"
  },
  {
    id: 4,
    name: "Database Management",
    code: "CS104",
    credits: 4,
    grade: "B+"
  },
  {
    id: 5,
    name: "Software Engineering",
    code: "CS105",
    credits: 4,
    grade: "A+"
  }
]);

const filteredCourses = computed(() =>
  courses.value.filter(course =>
    course.name.toLowerCase().includes(search.value.toLowerCase())
  )
);
</script>

<style scoped>
.container {
  padding: 40px;
}

h1 {
  text-align: center;
  color: #2563eb;
  margin-bottom: 20px;
}

.search {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  margin-bottom: 30px;
  border-radius: 8px;
  border: 1px solid #ccc;
}

.courses {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
}
</style>