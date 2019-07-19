$(document).ready(function () {
    setupReferenceTooltips()
    setupTaggle()
    setupGalleria()
})

const setupReferenceTooltips = () => {

    $('.reference_tooltip').each(function (index) {
        let id = this.getAttribute('data-consultant-id')
        ajaxFetchReferenceDetails(id, this)
    })
}

const setupGalleria = () => {
    Galleria.loadTheme('https://cdnjs.cloudflare.com/ajax/libs/galleria/1.5.7/themes/classic/galleria.classic.min.js');
    Galleria.run('.galleria', {showInfo: true, _toggleInfo: false});
}

const setupTaggle = () => {
    var technology_parts = technologies.split(',');
    var tag_parts = tags.split(',')
    new Taggle('technologies', {tags: technology_parts})
    new Taggle('tags', {tags: tag_parts})
    $('.taggle_input').remove()
    $('.taggle button').remove()
}

const ajaxFetchReferenceDetails = (reference_id, target) => {
    const json = {'reference_id': reference_id.toString()}
    const data = JSONToPostData(json)
    const url = getFetchReferenceURL()
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

const JSONToPostData = (event) => {
    let data = []
    Object.keys(event).forEach((key) => {
        data.push(`${key}=${event[key]}`)
    })
    return data.join('&')
}

const getReferenceDetails = () => {
    let company_id = $('#id_company').children("option:selected").val();
    let title = '-----'
    let person = $('#id_person').children("option:selected").val();
    let first_name = $('#id_first_name').val()
    let last_name = $('#id_last_name').val()
    let role = $('#id_role').val()
    let email = $('#id_email').val()
    let reference = {
        'company_id': company_id.toString(),
        'title': title,
        'person': person.toString(),
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'role': role
    }
    return reference
}


const createPopoverWithReference = (reference, target) => {
    let name = reference['fields']['name']
    let email = reference['fields']['email']
    let description = reference['fields']['description']
    if (!description) {
        description = 'No description provided'
    }
     if (!email) {
        email = 'No email provided'
    }
    let content =  `<div class="row"><div class="col-sm-12"><div>Email</div> - ${email}</div><br>
                    <div class="col-sm-12"><div>Description</div>- ${description}</div></div>`
    let options = {
        'trigger': 'hover',
        'title': name,
        'content': content,
        'html': true
    }
    $(target).popover(options)
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

const getFetchReferenceURL = () => {
    return document.getElementById(
  'get-reference').value
}
