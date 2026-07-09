import { useParams } from "react-router-dom";
import courses from "../data";

function CourseDetailPage() {
  const { courseId } = useParams();

  const course = courses.find(
    (c) => c.id === Number(courseId)
  );

  if (!course) {
    return <h2>Course Not Found</h2>;
  }

  return (
    <div className="container">
      <h2>{course.name}</h2>

      <p><strong>Course Code:</strong> {course.code}</p>

      <p><strong>Credits:</strong> {course.credits}</p>

      <p><strong>Grade:</strong> {course.grade}</p>

      <button>Enroll</button>
    </div>
  );
}

export default CourseDetailPage;