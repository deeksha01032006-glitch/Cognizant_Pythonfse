import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CourseCard } from '../course-card/course-card';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [CommonModule, FormsModule, CourseCard],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseList {

  searchTerm = '';

  courses = [
    {
      name: 'Java Programming',
      code: 'CS101',
      credits: 4,
      grade: 'A'
    },
    {
      name: 'Python Programming',
      code: 'CS102',
      credits: 4,
      grade: 'A'
    },
    {
      name: 'Web Development',
      code: 'CS103',
      credits: 3,
      grade: 'A'
    },
    {
      name: 'Database Management',
      code: 'CS104',
      credits: 4,
      grade: 'B+'
    },
    {
      name: 'Software Engineering',
      code: 'CS105',
      credits: 4,
      grade: 'A+'
    }
  ];

  filteredCourses() {
    return this.courses.filter(course =>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }

}