var country_endpoint = document.currentScript.dataset.url;

(function($) {
  var options,
    data,
    cssClass = ".intl-tel-input",
    inputs = $(cssClass);

  var codes = [];

  $.ajax({
      url: country_endpoint,
      success: function (result) {
        $.each(result.results, function(i, obj){
          codes.push(obj.code);
        });
      },
      async: false
  });

  inputs.each(function(i, el) {

    var $el;

    $el = $(el);
    data = $el.data();
    options = {
      onlyCountries: codes,
      preferredCountries: ["US"],
      separateDialCode: true,
      initialCountry: "auto",
      geoIpLookup: function(callback) {
        $.get('https://ipinfo.io?token=b40d745e539ae9', function() {}, "jsonp").always(function(resp) {
          var countryCode = (resp && resp.country) ? resp.country : "us";
          callback(countryCode);
        });
      },
      allowDropdown: data.allowDropdown !== undefined ? true : false,
      hiddenInput: data.hiddenName
    };

    $el.intlTelInput(options);


  });



})(jQuery);
