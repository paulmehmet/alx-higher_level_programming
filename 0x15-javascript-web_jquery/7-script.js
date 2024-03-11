$('document').ready(() => {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        success: (responseText) => {
            $('DIV#character').text(`${responseText.name}`)
        },
    });
})