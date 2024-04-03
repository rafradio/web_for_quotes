import {fieldLink} from "./input.js";
import {listOfUsers} from "./userListAdd.js";

let dataButton = document.getElementById("new-project");
let gizmoHTML = document.getElementById("gizmo");
let newProjectData = document.querySelectorAll(".new-project");


dataButton.onclick = () => {
    let getChoosenProject = document.querySelector('input[name="choose-project"]:checked'); 
    console.log("Выбранный проект - ", getChoosenProject.value, gizmoHTML.value);
    let dataToSend = {}

    let userNames = [...listOfUsers.options].map(o => o.text);

    if (getChoosenProject == null) {return;}

    if (getChoosenProject.value == "old") { 
        dataToSend = {
            link: fieldLink[0].value,
            title: fieldLink[1].value,
            gizmo: 1,
            userList: userNames
        };
    } else {
        dataToSend = {
            link: newProjectData[0].value,
            title: newProjectData[1].value,
            gizmo: 2,
            userList: userNames
        };
    }       

        console.log(userNames);

        let url = new URL(window.location.href);
        url.pathname = "/getdata";

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                
            },
            body: JSON.stringify(dataToSend)
            })
            .then(response => response.json())
            .then(data => {
                let dataString = data;
                console.log(dataString.name);
            });
    
    
}
