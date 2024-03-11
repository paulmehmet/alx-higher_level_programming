$('DIV#toggle_header').click(() => {
    if ($('HEADER').hasClass('red')) {
        $('HEADER').removeClass('red');
        $('HEADER').addClass('green');
    }else {
        $('HEADER').removeClass('green');
        $('HEADER').addClass('red');
    }
});
