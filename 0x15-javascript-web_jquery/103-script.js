$('document').ready(() => {

    function translate() {
        const lang = $('INPUT#language_code').val();

        $.ajax({
            url: `https://stefanbohacek.com/hellosalut/?lang=${lang}`,
            success: (res) => {
                $('DIV#hello').html(`<span>${res.hello}</span>`);
            }
        });
    }

    $('INPUT#btn_translate').click(() => {
        translate();
    });

    $('INPUT#language_code').keypress(function (e) {
        const key = e.which;
        if (key === 13) {
          translate();
        }
      });
});
