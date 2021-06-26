$(document).ready(function () {

    let waves = {
        init: () => {
            Waves.attach('.btn-close, .btn, .dropdown-item, .nav-item', ['waves-button']); // Put class names of elements that you want to have comma ',' seperated in between the first quotes.
            Waves.init();
        }
    }

    waves.init();

});