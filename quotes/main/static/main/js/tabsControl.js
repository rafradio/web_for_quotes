function tabsControl(index, index1) {
    let pages = document.querySelectorAll(".list_of_notes");
    let tabs = document.querySelectorAll(".tab-element");
    pages[index1].classList.add("list_of_notes_no_active");
    pages[index].classList.remove("list_of_notes_no_active");
    tabs.forEach((el, ind) => {
        el.classList.toggle("tab-element-active");
        el.classList.toggle("tab-element-no-active");
    })
    // tabs[index].classList.toggle("tab-element-active");
}

export {tabsControl};

