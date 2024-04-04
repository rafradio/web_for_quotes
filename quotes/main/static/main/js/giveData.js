import {fieldLink} from "./input.js";
import {listOfUsers} from "./userListAdd.js";

let dataButton = document.getElementById("new-project");
let gizmoHTML = document.getElementById("gizmo");
let newProjectData = document.querySelectorAll(".new-project");
let record = document.getElementById("stateMessage");

dataButton.onclick = function() {
    dataButton.classList.add("disabledbutton");
    // this.onclick = false;
    let messageFirst = "Начало работы с бд ";
    record.style.color = "red";
    record.innerHTML = messageFirst;
    let getChoosenProject = document.querySelector('input[name="choose-project"]:checked'); 
    console.log("Выбранный проект - ", getChoosenProject.value, gizmoHTML.value);
    let dataToSend = {}

    let userNames = [...listOfUsers.options].map(o => o.text);

    if (getChoosenProject == null) {return;}

    if (getChoosenProject.value == "old") { 
        dataToSend = {
            link: fieldLink[0].value,
            title: fieldLink[1].value,
            gizmo: gizmoHTML.value,
            userList: userNames
        };
    } else {
        dataToSend = {
            link: newProjectData[0].value,
            title: newProjectData[1].value,
            gizmo: gizmoHTML.value,
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
                console.log(dataString.records, dataString.fetched);
                let message = "Вставлено записей в БД - " + dataString.records + "; Записей на alchemy - " + dataString.fetched;
                record.innerHTML = message;
                record.style.color = "black";
                dataButton.classList.remove("disabledbutton");
                // dataButton.onclick = true;
            });
    
    
}

