let fieldLink = document.querySelectorAll(".db");
let dataLink = document.querySelectorAll(".db-datalist");
let dataAllLinks = [];
dataLink.forEach((el, index) => {
    dataAllLinks.push(Array.from(el.options, (option) => option.value));
});

fieldLink.forEach((el, index) => {
    el.onfocus = function () {
        dataLink[index].style.display = 'block';
        el.style.borderRadius = "5px 5px 0 0";  
    };

    for (let option of dataLink[index].options) {
        option.onmousedown = function () {
            event.preventDefault();
        }
        option.onclick = function () {
            el.value = option.value;
            dataLink[index].style.display = 'none';
            el.style.borderRadius = "5px";
            let anotherInput = index & 1 == 1 ? index - 1 : index + 1;
            console.log("Check tab - ", fieldLink.length, index, anotherInput);
            let valueForNotherInput = dataAllLinks[anotherInput][dataAllLinks[index].indexOf(option.value)];
            fieldLink[anotherInput].value = valueForNotherInput;
            console.log("Hello - ", dataAllLinks[index].indexOf(option.value));
            el.blur();
        }
    }

    el.oninput = function() {
        let currentFocus = -1;
        let text = el.value.toUpperCase();
        for (let option of dataLink[index].options) {
            if(option.value.toUpperCase().indexOf(text) > -1) {
                option.style.display = "block";
            } else {
                option.style.display = "none";
            }
        };
    }

});

fieldLink.forEach((el, index) => {
    el.onblur = function (event) {
        dataLink[index].style.display = 'none';
        el.style.borderRadius = "0px";  
        
    };
});

export {fieldLink, dataAllLinks};