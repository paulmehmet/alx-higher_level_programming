$('document').ready(() => {
    $('INPUT#btn_translate').click(() => {
        const lang = $('INPUT#language_code').val();

        $.ajax({
            url: `https://stefanbohacek.com/hellosalut/?lang=${lang}`,
            success: (res) => {
                $('DIV#hello').html(`<span>${res.hello}</span>`);
            }
        });
    });
});
