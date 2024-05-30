import {fieldLink, dataAllLinks} from "./input.js";
import {listOfUsers} from "./userListAdd.js";
import {tabsControl} from "./tabsControl.js"

let dataButton = document.getElementById("new-project");
let gizmoHTML = document.getElementById("gizmo");
let newProjectData = document.querySelectorAll(".new-project");
let record = document.getElementById("stateMessage");
let programmer = document.querySelectorAll(".select-prog");
let tabs = document.querySelectorAll(".tab-element");

// document.querySelectorAll(".list_of_notes")[1].classList.add("list_of_notes_no_active");
// document.querySelectorAll(".list_of_notes")[0].classList.add("list_of_notes_no_active");
document.querySelectorAll(".tab-element")[1].classList.add("tab-element-active");
document.querySelectorAll(".tab-element")[0].classList.add("tab-element-no-active");
let loader = document.createElement('span');
loader.setAttribute("class", "loader");

gizmoHTML.onchange = function() {
    programmer[0].style.display = 'none';
}


dataButton.onclick = function() {
    let getChoosenProject = document.querySelector('input[name="choose-project"]:checked'); 

    if (getChoosenProject == null) {
        record.style.color = "rgb(159, 22, 129)";
        record.innerHTML = "Вы не выбрали тип проекта."; 
        return;
    }


    // dataButton.classList.add("disabledbutton");
    // // this.onclick = false;
    // let messageFirst = "Начало работы с бд ";
    // record.style.color = "red";
    // record.innerHTML = messageFirst; 
    console.log("Выбранный проект - ", getChoosenProject.value, gizmoHTML.value);
    let dataToSend = {}

    let userNames = [...listOfUsers.options].map(o => o.text);
    let userNamesUnique = [...new Set(userNames)];

    if (getChoosenProject.value == "old") { 
        dataToSend = {
            link: fieldLink[0].value,
            title: fieldLink[1].value,
            gizmo: gizmoHTML.value,
            userList: userNamesUnique,
            typeOfProject: "old"
        };
    } else {
        dataToSend = {
            link: newProjectData[0].value,
            title: newProjectData[1].value,
            gizmo: gizmoHTML.value,
            userList: userNamesUnique,
            typeOfProject: "new"
        };
    }      
    
    let isEmptyValues = false;
    console.log("проверка isEmptyValues", dataToSend.userList.length);
    if (dataToSend.userList.length) {
        isEmptyValues = Object.values(dataToSend).every(x => x != null && x != '');
        console.log("проверка isEmptyValues", isEmptyValues);
        if (dataToSend.typeOfProject == "old") {
            isEmptyValues = ((dataAllLinks[0].indexOf(dataToSend.link) > -1) && (dataAllLinks[1].indexOf(dataToSend.title) > -1)) ? true : false;
        }
        console.log("проверка isEmptyValues", isEmptyValues);
    }
    // if (dataToSend.gizmo == '') {isEmptyValues = false;}
    // if (dataToSend.link == '') {isEmptyValues = false;}

    console.log("Проверка полей - ", isEmptyValues, " массив - ", dataToSend.link);

    let url = new URL(window.location.href);
    url.pathname = "/getdata";

    dataButton.classList.add("disabledbutton");
    // this.onclick = false;
    let messageFirst = "Начало работы с бд ";
    record.style.color = "red";
    record.innerHTML = messageFirst; 
    let theFirstChild = record.firstChild;
    record.insertBefore(loader, theFirstChild);

    if (isEmptyValues) {
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
                let message ="Вы выбрали неправильного исполнителя! "
                console.log(dataString.records, dataString.fetched);
                if (dataString.message != 0) {
                    message = "Вставлено записей в БД - " + dataString.records + "; Записей на alchemy - " + dataString.fetched;
                }
                record.innerHTML = message;
                record.style.color = "black";
                dataButton.classList.remove("disabledbutton");
                programmer[0].style.display = 'block';
            });
    } else {
        record.style.color = "rgb(159, 22, 129)";
        record.innerHTML = "Вы не выбрали все данные."; 

    }
    
    
}

tabsControl(0, 1);

tabs.forEach((el, index) => {
    el.onclick = function() {
        let index1 = index == 1 ? 0: 1;
        tabsControl(index, index1);
    }
});



