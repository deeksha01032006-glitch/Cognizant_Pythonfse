import { Routes } from '@angular/router';
import { StudentProfile } from './student-profile/student-profile';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'profile',
    pathMatch: 'full'
  },
  {
    path: 'profile',
    component: StudentProfile
  }
];