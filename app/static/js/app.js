// On DOM Loaded
document.addEventListener('DOMContentLoaded', function () {
    // Nav-bar for mobile Init
    let sidenavElems = document.querySelectorAll('.sidenav');
    let sidenavInstances = M.Sidenav.init(sidenavElems);

    // Slider init
    let sliderElems = document.querySelectorAll('.slider');
    let sliderInstances = M.Slider.init(sliderElems);

    // Modal Init
    let modalElems = document.querySelectorAll('.modal');
    let modalInstances = M.Modal.init(modalElems);

    // Dropdown Init
    let dropdownElems = document.querySelectorAll('select');
    let dropdownInstances = M.FormSelect.init(dropdownElems);

    //Character count
    let textNeedCount = document.querySelectorAll('.t-counter');
    let textNeedCountInstances = M.CharacterCounter.init(textNeedCount);

    // Tool Tips
    let toolElems = document.querySelectorAll('.tooltipped');
    let toolInstances = M.Tooltip.init(toolElems);

    // Tabs
    let tabElms = document.querySelectorAll('.tabs')
    let tabInstance = M.Tabs.init(tabElms);

    // Dropdown Menu
    let menuDropElems = document.querySelectorAll('.dropdown-trigger');
    let menuDropInstances = M.Dropdown.init(menuDropElems)



});
