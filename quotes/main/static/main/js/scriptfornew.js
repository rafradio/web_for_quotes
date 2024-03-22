function SaveToJson() {
    this.buttonJson = document.getElementById("json");
    this.returnButton = document.getElementById("return");
    // this.initSettings();
}

SaveToJson.prototype.initSettings = function() {
    this.returnButton.addEventListener('click', () => {
        location.href = "http://localhost:8000";
    });
}

const saveAction = new SaveToJson();

export {saveAction};