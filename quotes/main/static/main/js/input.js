let fieldLink = document.querySelectorAll(".db");
let dataLink = document.querySelectorAll(".db-datalist")
let dataAllLinks = [Array.from(dataLink[0].options, (option) => option.value), Array.from(dataLink[1].options, (option) => option.value)];
dataAllLinks.push(Array.from(dataLink[2].options, (option) => option.value));
dataAllLinks.push(Array.from(dataLink[3].options, (option) => option.value));


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
            let anotherInput;
            if (Array(0, 1).includes(index)) {
                anotherInput = index == 0 ? 1: 0;
            } else {
                if (Array(2, 3).includes(index)) {
                    anotherInput = index == 2 ? 3: 2;
                }
            }
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