let buttonForUser = document.getElementById("addUSer");
let listOfUsers = document.getElementById("usersList");
let userName = document.getElementById("user-name");
let buttonDel = document.getElementById("button-del-user");
let inputRadio = document.querySelectorAll(".radio-button");
let oldProject = document.getElementById("old-project");
let newProject = document.querySelectorAll(".new-project");

buttonForUser.onclick = () => {
    let text = userName.value;
    console.log("users ", text);
    let option = document.createElement("option");
    option.text = userName.value;
    listOfUsers.add(option);
}

buttonDel.onclick = () => {
    listOfUsers.remove(listOfUsers.selectedIndex);
}

inputRadio.forEach((el, index) => {
    el.onclick = () => {
        if (index == 1) {
            oldProject.disabled = false;
        } else {
            newProject.forEach((el, index) => {el.disabled = false;});
        }
    }
});

export {listOfUsers, newProject};