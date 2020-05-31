// On DOM Loaded
document.addEventListener('DOMContentLoaded', function () {
    // Nav-bar for mobile Init
    let sidenavElems = document.querySelectorAll('.sidenav');
    let sidenavInstances = M.Sidenav.init(sidenavElems);

    // Carousel init
    let carouselElems = document.querySelectorAll('.carousel');
    let carouselInstances = M.Carousel.init(carouselElems);
    let carouselInstance = M.Carousel.init({
        fullWidth: true,
        indicators: true
    });

    // Slider init
    let sliderElems = document.querySelectorAll('.slider');
    let instances = M.Slider.init(sliderElems);
});