let fieldLink = document.querySelectorAll(".db");
let dataLink = document.getElementsByTagName("datalist")

fieldLink.forEach((el, index) => {
    el.onfocus = function () {
        dataLink[index].style.display = 'block';
        el.style.borderRadius = "5px 5px 0 0";  
    };

    // el.onblur = function () {
    //     dataLink[index].style.display = 'none';
    //     el.style.borderRadius = "5px";  
    // };
    
    for (let option of dataLink[index].options) {
        option.onclick = function () {
            el.value = option.value;
            dataLink[index].style.display = 'none';
            el.style.borderRadius = "5px";
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

// fieldLink[0].onfocus = function () {
//     dataLink[0].style.display = 'block';
//     fieldLink[0].style.borderRadius = "5px 5px 0 0";  
// };

// for (let option of dataLink[0].options) {
//     option.onclick = function () {
//         fieldLink[0].value = option.value;
//         dataLink[0].style.display = 'none';
//         fieldLink[0].style.borderRadius = "5px";
//     }
// };