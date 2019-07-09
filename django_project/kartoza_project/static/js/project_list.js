$(document).ready(function () {
    setupGalleria()
})


const setupGalleria = () => {
    Galleria.loadTheme('https://cdnjs.cloudflare.com/ajax/libs/galleria/1.5.7/themes/classic/galleria.classic.min.js');
    Galleria.run('.galleria', {showInfo: true, _toggleInfo: false});
}

