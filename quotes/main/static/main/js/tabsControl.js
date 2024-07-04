function tabsControl(index, index1, record) {
    let pages = document.querySelectorAll(".list_of_notes");
    let tabs = document.querySelectorAll(".tab-element");
    pages[index1].classList.add("list_of_notes_no_active");
    pages[index].classList.remove("list_of_notes_no_active");
    tabs.forEach((el, ind) => {
        el.classList.toggle("tab-element-active");
        el.classList.toggle("tab-element-no-active");
    })
    if (index == 1) {
        deletTeb();
        record.innerHTML = "Вы в режиме удаления записей.";
    } else {
        record.innerHTML = "Вы в режиме добавления записей.";
    }
}

function deletTeb() {
    let url = new URL(window.location.href);
    let csrftoken = getCookie('quotes_user');
    let req = new XMLHttpRequest();
    req.open('GET', document.location, true);
    req.send(null);
    req.onload = function() {
        var headers = req.getAllResponseHeaders().toLowerCase();
        console.log(headers);
    };
    console.log(csrftoken);
    // fetch(url, {
    //         method: 'POST',
    //         headers: {
    //             "X-CSRFToken": csrftoken
    //         },
    //     })
    //     .then((response) => {
    //         console.log("url = ", url);
    //         console.log("response.headers = ", response.headers.get("Rafael"));
        
    //     })
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export {tabsControl};

