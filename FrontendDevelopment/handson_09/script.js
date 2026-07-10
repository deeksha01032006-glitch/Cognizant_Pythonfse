function enroll(course){

    alert("Successfully enrolled in " + course);

}

function cardKey(event,course){

    if(event.key==="Enter"){

        enroll(course);

    }

}

function searchCourse(){

    let input=document.getElementById("search").value.toLowerCase();

    let cards=document.querySelectorAll(".card");

    let count=0;

    cards.forEach(function(card){

        let text=card.innerText.toLowerCase();

        if(text.includes(input)){

            card.style.display="block";
            count++;

        }
        else{

            card.style.display="none";

        }

    });

    document.getElementById("resultCount").innerHTML=count+" Courses Found";

}