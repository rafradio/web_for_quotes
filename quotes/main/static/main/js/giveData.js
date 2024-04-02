import {fieldLink} from "./input.js";
import {listOfUsers} from "./userListAdd.js";

let dataButton = document.getElementById("new-project");


dataButton.onclick = () => {

    let userNames = [...listOfUsers.options].map(o => o.text);

    let dataToSend = {
        link: fieldLink[0].value,
        title: fieldLink[1].value,
        userList: userNames
    };

    

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

