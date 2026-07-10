<template>
  <div class="container">

    <div class="hero">
      <h1>Available Courses</h1>
      <p>Explore and enroll in your favorite courses.</p>

      <input
        type="text"
        v-model="searchTerm"
        placeholder="🔍 Search Course"
        class="search"
      />
    </div>

    <div class="course-grid">
      <div
        class="course-card"
        v-for="course in filteredCourses"
        :key="course.id"
      >
        <h2>{{ course.name }}</h2>

        <p><strong>Code:</strong> {{ course.code }}</p>

        <p><strong>Credits:</strong> {{ course.credits }}</p>

        <p><strong>Grade:</strong> {{ course.grade }}</p>

        <button @click="enroll(course)">
          Enroll
        </button>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

const searchTerm = ref('')

const courses = ref([])

onMounted(() => {

  courses.value = [

    {
      id:1,
      name:'Java Programming',
      code:'CS101',
      credits:4,
      grade:'A'
    },

    {
      id:2,
      name:'Python Programming',
      code:'CS102',
      credits:4,
      grade:'A'
    },

    {
      id:3,
      name:'Web Development',
      code:'CS103',
      credits:3,
      grade:'A'
    },

    {
      id:4,
      name:'Database Management',
      code:'CS104',
      credits:4,
      grade:'B+'
    },

    {
      id:5,
      name:'Software Engineering',
      code:'CS105',
      credits:4,
      grade:'A+'
    }

  ]

})

const filteredCourses = computed(() =>
  courses.value.filter(course =>
    course.name
      .toLowerCase()
      .includes(searchTerm.value.toLowerCase())
  )
)

function enroll(course){

  store.enroll(course)

}
</script>

<style scoped>

.container{

padding:40px;

background:#eef5ff;

min-height:100vh;

}

.hero{

background:linear-gradient(135deg,#2563eb,#7c3aed);

padding:50px;

border-radius:20px;

color:white;

margin-bottom:40px;

}

.hero h1{

font-size:48px;

margin-bottom:10px;

}

.hero p{

font-size:20px;

margin-bottom:20px;

}

.search{

width:420px;

padding:15px;

border:none;

border-radius:40px;

font-size:18px;

}

.course-grid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(280px,1fr));

gap:25px;

margin-top:40px;

}

.course-card{

background:white;

padding:25px;

border-radius:15px;

box-shadow:0 10px 20px rgba(0,0,0,.15);

transition:.3s;

}

.course-card:hover{

transform:translateY(-8px);

}

.course-card h2{

color:#2563eb;

margin-bottom:15px;

}

.course-card p{

margin:10px 0;

color:#222;

font-size:17px;

}

button{

width:100%;

margin-top:15px;

padding:12px;

background:#2563eb;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

font-size:17px;

}

button:hover{

background:#1d4ed8;

}

</style>