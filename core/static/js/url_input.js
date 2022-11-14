(function($) {
  var data,
    cssClass = ".url-input",
    inputs = $(cssClass);

  inputs.each(function(i, el) {

    var $el;

    $el = $(el);
    data = $el.data();
    let options = {'regex': 'https://.*', "clearIncomplete": false};
    // $el.inputmask({
    //   regex: "https://.*",
    //   clearIncomplete: false
    // });
    $el.inputmask(options);
  });
})(jQuery);

function validURL(str) {
  var pattern = new RegExp('^(https?:\\/\\/)?'+
      '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+
      '((\\d{1,3}\\.){3}\\d{1,3}))'+
      '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+
      '(\\?[;&a-z\\d%_.~+=-]*)?'+
      '(\\#[-a-z\\d_]*)?$','i');
  return !!pattern.test(str);
}

$('.url-input').on('change', function () {
  if (validURL($(this).val()) === false){
    $('.url-input').addClass("is-invalid");
    $('.url-input').parent().find('span.error').remove();
    var errorMessage = $(this).closest('.url-input-container').attr('data-error-message')||"Please enter a valid URL.";
    var  spanError = '<span id="'+ $(this).attr('id')+'-error" class="error invalid-feedback">'+ errorMessage+ '</span>';
    $('.url-input').parent().append(spanError);
  }else{
    $('.url-input').removeClass("is-invalid");
    $('.url-input').parent().find('span.error').remove();

  }
});
