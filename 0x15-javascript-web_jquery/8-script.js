$('document').ready(() => {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: (res) => {
            const { results } = res;
            results.map((data) => {
                $('UL#list_movies').append(`<li>${data.title}</li>`)
            })
        }}
    );
});
