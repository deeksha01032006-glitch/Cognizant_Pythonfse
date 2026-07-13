import { defineStore } from "pinia";
import { ref, computed } from "vue";
import { enrollStudent, getCourseById } from "../api/courseApi";

export const useEnrollmentStore = defineStore("enrollment", () => {

  const enrolledCourses = ref([]);

  const total = computed(() => enrolledCourses.value.length);

  async function fetchAndEnroll(courseId) {

    const course = await getCourseById(courseId);

    await enrollStudent(1, courseId);

    if (
      course &&
      !enrolledCourses.value.find(c => c.id === course.id)
    ) {
      enrolledCourses.value.push(course);
    }
  }

  function $reset() {
    enrolledCourses.value = [];
  }

  return {
    enrolledCourses,
    total,
    fetchAndEnroll,
    $reset
  };
});