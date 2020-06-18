// On DOM Loaded
document.addEventListener('DOMContentLoaded', function () {

    // Nav-bar for mobile Init
    let sidenavElems = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenavElems);

    // Slider init
    let sliderElems = document.querySelectorAll('.slider');
    M.Slider.init(sliderElems);

    // Modal Init
    let modalElems = document.querySelectorAll('.modal');
    M.Modal.init(modalElems);

    // Dropdown Init
    let dropdownElems = document.querySelectorAll('select');
    M.FormSelect.init(dropdownElems);

    //Character count
    let textNeedCount = document.querySelectorAll('.t-counter');
    M.CharacterCounter.init(textNeedCount);

    // Tool Tips
    let toolElems = document.querySelectorAll('.tooltipped');
    M.Tooltip.init(toolElems);

    // Tabs
    let tabElms = document.querySelectorAll('.tabs');
    M.Tabs.init(tabElms);

    // Dropdown Menu
    let menuDropElems = document.querySelectorAll('.dropdown-trigger');
    M.Dropdown.init(menuDropElems);

});
