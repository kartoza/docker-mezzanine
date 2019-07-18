$(document).ready(function () {
    // setupGalleria()
    setupTable()
    $('span[data-action=tag]').click(function () {
        searchTag(this)
    })
    $('span[data-action=technology]').click(function () {
        searchTechnology(this)
    })
    $('span[data-action=clear_technology]').click(function () {
        clearTechnology()
    })
    $('span[data-action=clear_tags]').click(function () {
        clearTag()
    })
    $('button[data-action=export]').click(function () {
        exportDocuments()
    })

})

const sortIds = (dict) => {
// Create items array
    var items = Object.keys(dict).map(function (key) {
        return [key, dict[key]];
    });
// Sort the array based on the second element
    items.sort(function (second, first) {
        return second[1] - first[1];
    });

    return items
}

const exportDocuments = () => {
    let selected_ids = {}
    let selected_rows = $('#table_id tr.selected')
    selected_rows.each(function () {
        let sort_order = $(this).find('input').val()
        selected_ids[($(this).data("pk"))] = sort_order
    })
    let project_ids_container = $('#project_ids')
    let items = sortIds(selected_ids)
    project_ids_container.html(items.toString())
    ajaxRequestExportDocuments(items)
}



const clearTechnology = () => {
    $('#search_technologies').val('')
    $('#search_technologies').trigger('change');
}

const clearTag = () => {
    $('#search_tags').val('')
    $('#search_tags').trigger('change');
}

const setupTable = () => {
    let table = $('#table_id').DataTable({
        select: {
            items: 'row',
            info: true,
            style: 'multi',
        },
    });
    setupTableSearchFields(table);

    $('#table_id tbody').on('click', 'tr', function () {
        $(this).toggleClass('selected');
    });

}

const searchTag = (e) => {
    let tag = e.innerHTML
    let tag_input = $('#search_tags')
    let tag_input_value = tag_input.val()
    if (tag_input_value.indexOf(tag) <= 0) {
        tag_input.val(`${tag_input_value} ${tag}`)
        tag_input.trigger("change")
    }

}


const searchTechnology = (e) => {
    let tag = e.innerHTML
    let tag_input = $('#search_technologies')
    let tag_input_value = tag_input.val()
    if (tag_input_value.indexOf(tag) <= 0) {
        tag_input.val(`${tag_input_value} ${tag}`)
        tag_input.trigger("change")
    }

}


const setupTableSearchFields = (table) => {

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


const ajaxRequestExportDocuments = (projects_to_export) => {
    const json = {projects_to_export}
    const data = JSONToPostData(json)
    const url = getExportProjectsURL()
    const request = new XMLHttpRequest()
    request.open('POST', url, true)
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
    request.setRequestHeader('X-CSRFToken', getCSRFTokenFromCookies())

    request.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            createPopoverWithReference(JSON.parse(request.responseText)[0], target)
        }
    }
    request.send(data)
}

const getCSRFTokenFromCookies = () => {
    let csrfToken
    document.cookie.split(';').forEach((cookie) => {
        const csrfRegex = RegExp('csrftoken')
        if (csrfRegex.test(cookie.trim())) {
            csrfToken = cookie.trim().split('=')[1]
        }
    })
    return csrfToken
}

const getExportProjectsURL = () => {
    return document.getElementById('export-projects').value
}

const JSONToPostData = (event) => {
    let data = []
    Object.keys(event).forEach((key) => {
        data.push(`${key}=${event[key]}`)
    })
    return data.join('&')
}
