$(document).ready(function () {
    setupGalleria()
    setupIsotope()
    $('span[data-action=tag]').click(function () {
        search_tag(this)
    })
    $('span[data-action=technology]').click(function () {
        search_tag(this)
    })
    $('span[data-action=sort]').click(function () {
        sort_tag(this)
    })
    $('span[data-action=clear-filters]').click(function () {
        clear_filter(this)
    })
})


const setupGalleria = () => {
    Galleria.loadTheme('https://cdnjs.cloudflare.com/ajax/libs/galleria/1.5.7/themes/classic/galleria.classic.min.js');
    Galleria.run('.galleria', {showInfo: true, _toggleInfo: false});
}

const setupIsotope = () => {
    var $grid = $('.grid').isotope({
        // options
        itemSelector: '.grid-item',
            layoutMode: 'fitRows',

    });

}

const search_tag = (e) => {
    let tag = e.innerHTML
    $('#tag-filter').text(tag);
    $('.grid').isotope({filter: '.' + tag})
}

const sort_tag = (e) => {

    let tag = e.innerHTML.toLowerCase().replace(' ', '_')
    // $('.grid').isotope({sortBy: tag})
    $('#tag-filter').text(tag);
    $('.grid').isotope({ sortBy : tag });

}

const clear_filter = (e) => {
    $('#tag-filter').text('')
    $('.grid').isotope({filter: ''})
}

