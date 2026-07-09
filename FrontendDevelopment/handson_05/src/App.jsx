import { useState, useEffect } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

function App() {
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchCourses() {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts"
        );

        if (!response.ok) {
          throw new Error("Failed to fetch courses");
        }

        const data = await response.json();

        const courseNames = [
          "Data Structures",
          "Database Systems",
          "Operating Systems",
          "Computer Networks",
          "Web Development",
        ];

        const courseCodes = [
          "CS101",
          "CS102",
          "CS103",
          "CS104",
          "CS105",
        ];

        const courseCredits = [4, 3, 4, 3, 5];

        const courseGrades = [
          "A",
          "A+",
          "B+",
          "A",
          "A+",
        ];

        const apiCourses = data.slice(0, 5).map((post, index) => ({
          id: post.id,
          name: courseNames[index],
          code: courseCodes[index],
          credits: courseCredits[index],
          grade: courseGrades[index],
        }));

        setCourses(apiCourses);
      } catch (err) {
        setError("Unable to load courses.");
      } finally {
        setLoading(false);
      }
    }

    fetchCourses();
  }, []);

  useEffect(() => {
    console.log("Courses updated");
  }, [courses]);

  function handleEnroll(course) {
    const alreadyEnrolled = enrolledCourses.find(
      (item) => item.id === course.id
    );

    if (!alreadyEnrolled) {
      setEnrolledCourses([...enrolledCourses, course]);
    }
  }

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <>
      <Header
        siteName="Student Portal"
        enrolledCount={enrolledCourses.length}
      />

      <main className="container">
        <h2>Available Courses</h2>

        <input
          type="text"
          placeholder="Search Courses..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />

        {loading && <h2>Loading...</h2>}

        {error && <h2>{error}</h2>}

        {!loading && !error && (
          <div className="grid">
            {filteredCourses.length > 0 ? (
              filteredCourses.map((course) => (
                <CourseCard
                  key={course.id}
                  {...course}
                  onEnroll={() => handleEnroll(course)}
                />
              ))
            ) : (
              <h3>No courses found.</h3>
            )}
          </div>
        )}

        <StudentProfile />
      </main>

      <Footer />
    </>
  );
}

export default App;