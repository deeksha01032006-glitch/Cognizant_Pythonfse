<template>
  <div class="courses-page">

    <div class="hero">
      <h1>Available Courses</h1>
      <p>Explore and enroll in the courses that shape your future.</p>

      <input
        v-model="searchTerm"
        type="text"
        placeholder="🔍 Search Course"
      />
    </div>

    <div class="course-grid">
      <CourseCard
        v-for="course in filteredCourses"
        :key="course.id"
        :course="course"
      />
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import CourseCard from '../components/CourseCard.vue'

const searchTerm = ref('')

const courses = ref([])

onMounted(() => {
  courses.value = [
    {
      id: 1,
      name: 'Java Programming',
      code: 'CS101',
      credits: 4,
      grade: 'A'
    },
    {
      id: 2,
      name: 'Python Programming',
      code: 'CS102',
      credits: 4,
      grade: 'A'
    },
    {
      id: 3,
      name: 'Web Development',
      code: 'CS103',
      credits: 3,
      grade: 'A'
    },
    {
      id: 4,
      name: 'Database Management',
      code: 'CS104',
      credits: 4,
      grade: 'B+'
    },
    {
      id: 5,
      name: 'Software Engineering',
      code: 'CS105',
      credits: 4,
      grade: 'A+'
    }
  ]
})

const filteredCourses = computed(() =>
  courses.value.filter(course =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
)
</script>

<style scoped>
.courses-page{
    width:100%;
    min-height:100vh;
    background:#eef3ff;
    padding:40px;
    box-sizing:border-box;
}

.hero{
    max-width:1400px;
    margin:auto;
    background:linear-gradient(135deg,#3b82f6,#6d28d9);
    color:white;
    padding:50px;
    border-radius:20px;
    margin-bottom:50px;
}

.hero h1{
    font-size:48px;
    margin-bottom:10px;
}

.hero p{
    font-size:22px;
    margin-bottom:25px;
}

.hero input{
    width:400px;
    padding:18px;
    border:none;
    border-radius:50px;
    font-size:18px;
}

.course-grid{
    max-width:1500px;
    margin:auto;
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:30px;
}
</style>