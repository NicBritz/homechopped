// On DOM Loaded
document.addEventListener('DOMContentLoaded', function () {
    // Nav-bar for mobile Init
    let sidenavElems = document.querySelectorAll('.sidenav');
    let sidenavInstances = M.Sidenav.init(sidenavElems);

    // Slider init
    let sliderElems = document.querySelectorAll('.slider');
    let instances = M.Slider.init(sliderElems);

});