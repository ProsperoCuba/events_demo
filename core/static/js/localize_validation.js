function translateValidationMessages(currentLang) {
  message = {
    en: {
      required: "Required.",
      remote: "Please fix this field.",
      email: "Wrong email.",
      url: "Please enter a valid URL.",
      date: "Please enter a valid date.",
      dateISO: "Please enter a valid date (ISO).",
      number: "Please enter a valid number.",
      digits: "Please enter only digits.",
      creditcard: "Please enter a valid credit card number.",
      equalTo: "Please enter the same value again.",
      maxlength: $.validator.format("Please enter no more than {0} characters."),
      minlength: $.validator.format("Please enter at least {0} characters."),
      rangelength: $.validator.format("Please enter a value between {0} and {1} characters long."),
      range: $.validator.format("Please enter a value between {0} and {1}."),
      max: $.validator.format("Please enter a value less than or equal to {0}."),
      min: $.validator.format("Please enter a value greater than or equal to {0}.")
    },
    es: {
      required: "Este campo es requerido", // que sea igual a las traducciones en django
      maxlength: "",
      minlength: "",
      rangelength: "",
      email: "",
      url: "",
      date: "",
      dateISO: "",
      number: "",
      digits: "",
      equalTo: "",
      range: "",
      max: "",
      min: "",
      creditcard: ""
    }
  };
    console.log("Translating validation messages to: "+currentLang);

  if (currentLang === "es") {
    $.extend($.validator.messages, message.es);
  } else {
    $.extend($.validator.messages, message.en);
  }
}