let buttonForUser = document.getElementById("addUSer");
let listOfUsers = document.getElementById("usersList");
let userName = document.getElementById("user-name");
let buttonDel = document.getElementById("button-del-user");

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