"use strict";

var KTFormsInputmaskDemos={

    init:function(a){
        let data_lang = document.langCode;
        if (!data_lang) {
            data_lang = typeof lang !== 'undefined'? lang : "en";
        }

        let data = $("#id_birthdate").data();
        if (!data.maxDate){
            data.maxDate = data_lang === 'es' ? "31/12/2000" : "31/12/2000";
        }
        let options = {'alias': 'datetime', "inputFormat": "mm/dd/yyyy", 'min': '01/01/1917', 'max': data.maxDate};
        if (data_lang === 'es') {
            options = {'alias': 'datetime', "inputFormat": "dd/mm/yyyy", 'min': '01/01/1917', 'max': data.maxDate};
        }

        Inputmask(options).mask("#id_birthdate");
    }
};

KTUtil.onDOMContentLoaded((
    function(){
        KTFormsInputmaskDemos.init();
    }
));