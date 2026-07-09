import { courses } from "./data.js";

const courseGrid = document.querySelector(".course-grid");

const totalCredits =
document.querySelector("#total-credits");

const searchInput =
document.querySelector("#search-courses");

const sortButton =
document.querySelector("#sort-btn");

const selectedCourse =
document.querySelector("#selected-course");



// --------------------------
// ES6 Features
// --------------------------

courses.forEach(course => {

const {name,credits}=course;

console.log(`${name} - ${credits} credits`);

});


const formattedCourses = courses.map(course =>

`${course.code} — ${course.name} (${course.credits} credits)`

);

console.log(formattedCourses);


const filteredCourses = courses.filter(

course => course.credits>=4

);

console.log(filteredCourses);

console.log(
"Count :",
filteredCourses.length
);


const total = courses.reduce(

(sum,course)=>sum+course.credits,

0

);

console.log(
"Total Credits :",
total
);


// --------------------------
// Rendering
// --------------------------

function renderCourses(courseList){

courseGrid.innerHTML="";

courseList.forEach(course=>{

const article=document.createElement("article");

article.className="course-card";

article.dataset.id=course.id;

article.innerHTML=`

<h3>${course.name}</h3>

<p><strong>Code :</strong> ${course.code}</p>

<p><strong>Credits :</strong> ${course.credits}</p>

`;

courseGrid.appendChild(article);

});

const credits=courseList.reduce(

(sum,course)=>sum+course.credits,

0

);

totalCredits.textContent=
`Total Credits : ${credits}`;

}

renderCourses(courses);


// --------------------------
// Search
// --------------------------

searchInput.addEventListener(

"input",

()=>{

const keyword=
searchInput.value.toLowerCase();

const result=courses.filter(course=>

course.name.toLowerCase().includes(keyword)

);

renderCourses(result);

}

);


// --------------------------
// Sort
// --------------------------

sortButton.addEventListener(

"click",

()=>{

const sorted=[...courses].sort(

(a,b)=>b.credits-a.credits

);

renderCourses(sorted);

}

);


// --------------------------
// Event Delegation
// --------------------------

courseGrid.addEventListener(

"click",

(event)=>{

const card=
event.target.closest(".course-card");

if(!card) return;

const id=parseInt(card.dataset.id);

const course=

courses.find(c=>c.id===id);

selectedCourse.innerHTML=`

<h3>Selected Course</h3>

<p>${course.name}</p>

<p>Grade : ${course.grade}</p>

`;

}

);