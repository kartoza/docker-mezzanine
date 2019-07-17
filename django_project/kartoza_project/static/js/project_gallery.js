$(document).ready(function () {
    // setupGalleria()
    setupTable()
    $('span[data-action=tag]').click(function () {
        search_tag(this)
    })
    $('span[data-action=technology]').click(function () {
        search_technology(this)
    })

})


const setupTable = () => {

    let table = $('#table_id').DataTable({
        select: {
            items: 'row',
            info: true,
            style: 'multi',
        }
    });
    setup_table_footers(table);

    $('#table_id tbody').on('click', 'tr', function () {
        $(this).toggleClass('selected');
    });

}

const search_tag = (e) => {
    let tag = e.innerHTML
    let tag_input = $('#search_tags')
    let tag_input_value = tag_input.val()
    if (tag_input_value.indexOf(tag) <= 0) {
        tag_input.val(`${tag_input_value} ${tag}`)
        tag_input.trigger("change")
    }

}


const search_technology = (e) => {
    let tag = e.innerHTML
    let tag_input = $('#search_technologies')
    let tag_input_value = tag_input.val()
    if (tag_input_value.indexOf(tag) <= 0) {
        tag_input.val(`${tag_input_value} ${tag}`)
        tag_input.trigger("change")
    }

}



const setup_table_footers = (table) => {

    $('.search-bar').each(function () {
        var title = $(this).text();
        $(this).html('<input class="form-control" id="search_' + title.toLowerCase().replace(' ', '_') + '" type="text" placeholder="' + title + '..." />');
    });

    // Apply the search
    table.columns().every(function () {
        var that = this;
        let search_column = this.header().innerHTML.toLowerCase().replace(' ', '_')
        let search_element = $(`#search_${search_column}`)
        if (search_element.length) {
            $(search_element).on('keyup change', function () {
                    if (that.search() !== this.value) {
                        that
                            .search(this.value)
                            .draw();
                    }
                })
        }
    });
}
