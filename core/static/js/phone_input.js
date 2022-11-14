(function($) {
  var options,
    data,
    cssClass = ".intl-tel-input",
    inputs = $(cssClass);

  inputs.each(function(i, el) {

    var $el;

    $el = $(el);
    data = $el.data();
    options = {
      // onlyCountries: ["CR", "DO", "GT", "MX", "PA", "US", "VE"],
      preferredCountries: ["US"],
      // initialCountry: data.defaultCode,
      initialCountry: "auto",
      geoIpLookup: function(callback) {
        $.get('https://ipinfo.io?token=b40d745e539ae9', function() {}, "jsonp").always(function(resp) {
          var countryCode = (resp && resp.country) ? resp.country : "us";
          callback(countryCode);
        });
      },
      allowDropdown: data.allowDropdown !== undefined ? true : false,
      hiddenInput: data.hiddenName,
    };

    // options.preferredCountries = data.preferredCountries;


    $el.intlTelInput(options);

    /*$el.inputmask("mask", {
      mask: "(999) 999-9999"
    });*/
  });
})(jQuery);
