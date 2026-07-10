import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-student-profile',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './student-profile.html',
  styleUrl: './student-profile.css'
})
export class StudentProfile {

  profileForm = new FormGroup({
    name: new FormControl('', [
      Validators.required,
      Validators.minLength(3)
    ]),

    email: new FormControl('', [
      Validators.required,
      Validators.email
    ]),

    age: new FormControl('', [
      Validators.required,
      Validators.min(18),
      Validators.max(60)
    ])
  });

  onSubmit() {
    if (this.profileForm.valid) {
      alert('Profile Submitted Successfully!');
      console.log(this.profileForm.value);
    }
  }
}