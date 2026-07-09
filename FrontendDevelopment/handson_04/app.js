import { courses } from "./data.js";

const courseGrid=document.querySelector(".course-grid");
const loading=document.getElementById("loading");

function renderCourses(data){

courseGrid.innerHTML="";

data.forEach(course=>{

const card=document.createElement("article");

card.className="course-card";

card.innerHTML=`

<h3>${course.name}</h3>

<p>${course.code}</p>

<p>${course.credits} Credits</p>

`;

courseGrid.appendChild(card);

});

}

// --------------------
// Task 1
// --------------------

function fetchUser(id){

return fetch("https://jsonplaceholder.typicode.com/users/"+id)

.then(response=>response.json())

.then(user=>console.log(user.name));

}

fetchUser(1);

// Async Await

async function fetchUserAsync(id){

try{

const response=await fetch(

"https://jsonplaceholder.typicode.com/users/"+id

);

const user=await response.json();

console.log(user.name);

}

catch(error){

console.log(error);

}

}

fetchUserAsync(2);

// Simulated delay

function fetchAllCourses(){

return new Promise(resolve=>{

setTimeout(()=>{

resolve(courses);

},1000);

});

}

loading.style.display="block";

fetchAllCourses().then(data=>{

loading.style.display="none";

renderCourses(data);

});

// Promise.all

Promise.all([

fetch("https://jsonplaceholder.typicode.com/users/1").then(r=>r.json()),

fetch("https://jsonplaceholder.typicode.com/users/2").then(r=>r.json())

]).then(users=>{

console.log(users[0].name);

console.log(users[1].name);

});

// --------------------
// Task 2
// --------------------

const spinner=document.getElementById("spinner");

const posts=document.getElementById("posts");

const errorDiv=document.getElementById("error-message");

const retry=document.getElementById("retry-btn");

async function apiFetch(url){

const response=await fetch(url);

if(!response.ok){

throw new Error("Unable to load data.");

}

return response.json();

}

async function loadPosts(){

spinner.style.display="block";

posts.innerHTML="";

errorDiv.innerHTML="";

retry.style.display="none";

try{

const data=await apiFetch(

"https://jsonplaceholder.typicode.com/posts?_limit=5"

);

spinner.style.display="none";

data.forEach(post=>{

posts.innerHTML+=`

<div class="post">

<h3>${post.title}</h3>

<p>${post.body}</p>

</div>

`;

});

}

catch(error){

spinner.style.display="none";

errorDiv.innerHTML=

"Something went wrong.";

retry.style.display="inline";

}

}

loadPosts();

retry.addEventListener("click",loadPosts);

// 404 Example

apiFetch("https://jsonplaceholder.typicode.com/nonexistent")

.catch(()=>{

console.log("404 Example");

});

// --------------------
// Task 3
// --------------------

axios.interceptors.request.use(config=>{

console.log("API call started:",config.url);

return config;

});

async function axiosPosts(){

const response=await axios.get(

"https://jsonplaceholder.typicode.com/posts",

{

params:{

userId:1

}

}

);

console.log(response.data);

}

axiosPosts();

/*

FETCH

1. Built into Browser

2. Need response.ok

3. Manual JSON parsing

AXIOS

1. External Library

2. Throws HTTP errors automatically

3. Converts JSON automatically

*/