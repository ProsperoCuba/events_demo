(function($) {

    var data_lang = document.currentScript.dataset.language;
    if (!data_lang) {
        data_lang = typeof lang !== 'undefined'? lang : "en";
    }

  var data,
    cssClass = ".intl-birthdate-input",
    inputs = $(cssClass);

  inputs.each(function(i, el) {

    var $el;

    $el = $(el);
    data = $el.data();
    if (!data.maxDate){
        data.maxDate = data_lang === 'es' ? "31/12/2000" : "31/12/2000";
    }
    let options = {'alias': 'datetime', "inputFormat": "mm/dd/yyyy", 'min': '01/01/1917', 'max': data.maxDate};
    if (data_lang === 'es') {
        options = {'alias': 'datetime', "inputFormat": "dd/mm/yyyy", 'min': '01/01/1917', 'max': data.maxDate};
    }

      $el.inputmask(options);


  });

})(jQuery);
