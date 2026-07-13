import apiClient from "./apiClient";

const courses = [
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
];

export async function getAllCourses() {
  return Promise.resolve(courses);
}

export async function getCourseById(id) {
  return Promise.resolve(
    courses.find(course => course.id == id)
  );
}

export async function enrollStudent(studentId, courseId) {
  return Promise.resolve({
    success: true,
    studentId,
    courseId
  });
}