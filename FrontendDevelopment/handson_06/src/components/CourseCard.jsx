import { useNavigate } from "react-router-dom";

function CourseCard({ course }) {
  const navigate = useNavigate();

  return (
    <div className="course-card">
      <h2>{course.name}</h2>

      <p><strong>Code:</strong> {course.code}</p>

      <p><strong>Credits:</strong> {course.credits}</p>

      <p><strong>Grade:</strong> {course.grade}</p>

      <button onClick={() => navigate(`/courses/${course.id}`)}>
        View Details
      </button>
    </div>
  );
}

export default CourseCard;