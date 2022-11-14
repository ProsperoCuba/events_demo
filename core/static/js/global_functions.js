function fail_response(resp, error_text) {

    var msg = error_text ? error_text : ($("#scripts_translated_labels").data("custom-action-error-msg") || "Lo sentimos, ha ocurrido un error durante la operación. Estamos trabajando en ello.")
    var resp_json = resp.responseJSON;

    if (resp.status === 403) {
        window.location.reload();
    } else if (resp.status === 404) {

        swal.fire({
            title: 'Error!',
            text: $("#scripts_translated_labels").data("custom-action-notfound") || 'No encontrado',
            type: 'error',
        }).then(function () {
            window.location.reload();

        });
    } else {
        if (resp_json) {
            if (resp_json.msg) {
                msg = resp_json.msg
            } else if (resp_json.non_field_errors) {
                msg = resp_json.non_field_errors[0]
            } else {
                msg = resp_json
            }
        }

        swal.fire({
            title: 'Error!',
            text: msg,
            type: 'error',
        });
    }
}

function fail_response_api_client(resp, error_text) {

    var msg = error_text ? error_text : $("#scripts_translated_labels").data("custom-action-error-msg") || "Lo sentimos, ha ocurrido un error durante la operación. Estamos trabajando en ello."

    if (resp.message.includes("403")) {
        window.location.reload();
    } else if (resp.message.includes("404")) {
        swal.fire({
            title: 'Error!',
            text: $("#scripts_translated_labels").data("custom-action-notfound") || 'No encontrado',
            type: 'error',
        })
    } else {
        var resp_json = resp.content;
        if (resp_json) {
            if (resp_json.msg) {
                msg = resp_json.msg
            } else {
                msg = resp_json
            }
        }

        swal.fire({
            title: 'Error!',
            text: msg,
            type: 'error',
        });
    }
}

function fail_response_field_errors(resp, show_swal) {
    const resp_text = resp.responseText;

    let msg = null
    if (resp.status === 403) {
        window.location.reload();
    } else if (resp.status === 404) {
        swal.fire({
            title: 'Error!',
            text: $("#scripts_translated_labels").data("custom-action-notfound") || 'No encontrado.',
            type: 'error',
        })
    } else {
        try {
            const json = JSON.parse(resp_text);
            if (typeof json === 'object') {

                if (json.msg) {
                    msg = json.msg
                } else {
                    for (const k of Object.keys(json)) {
                        const input = $(`#id_${k}`)
                        const form_group = input.closest('.form-group')
                        form_group.addClass('is-invalid')
                        form_group.find('.error_msg').append(`<div class='error invalid-feedback'>${json[k]}</div>`)

                    }
                    if (json['non_field_errors']) {

                        if (show_swal){
                            swal.fire({
                                title: 'Error!',
                                text: json['non_field_errors'][0],
                                type: 'error',
                            });

                        }else{
                            const errorElement = document.getElementById('modal_none_field_errors')
                            if (errorElement) {
                                $(errorElement).show().find('.alert-text').html(json['non_field_errors'][0])
                            }
                        }

                    }else if (json[0]){
                        msg = json[0]
                    }
                }

            } else if (typeof json === 'string') {
                msg = json
            }

            if (msg) {
                swal.fire({
                    title: 'Error!',
                    text: msg,
                    type: 'error',
                });
            }
        } catch (e) {
            return false;
        }


    }

}

function clear_form_errors() {
    $(".error.invalid-feedback").remove()
    $("#modal_none_field_errors").css('display', 'none')
    $("#modal_none_field_errors").find('.alert-text').html("")
}

function processing() {
    if(typeof KTApp !== 'undefined'){
        KTApp.blockPage({
            overlayColor: '#000000',
            type: 'v2',
            state: 'brand',
            message: $("#scripts_translated_labels").data("custom-action-processing") || 'Procesando...',
            size: 'lg',
            opacity: 0.15,

        });
    }

}

function completed() {
    if(typeof KTApp !== 'undefined'){
        KTApp.unblockPage();
    }
}

function closePrint() {
    document.body.removeChild(this.__container__);
}

function setPrint() {
    this.contentWindow.__container__ = this;
    this.contentWindow.onbeforeunload = closePrint;
    this.contentWindow.onafterprint = closePrint;
    this.contentWindow.document.write(this.__url__);
    this.contentWindow.document.close();
    this.contentWindow.focus(); // Required for IE
    this.contentWindow.print();
}

function printPage(sURL) {
    var oHideFrame = document.createElement("iframe");
    oHideFrame.onload = setPrint;
    oHideFrame.__url__ = sURL;
    oHideFrame.style.position = "fixed";
    oHideFrame.style.right = "0";
    oHideFrame.style.bottom = "0";
    oHideFrame.style.width = "0";
    oHideFrame.style.height = "0";
    oHideFrame.style.border = "0";
    //oHideFrame.src = sURL;
    document.body.appendChild(oHideFrame);

}

navigator.sayswho= (function(){
    var N= navigator.appName, ua= navigator.userAgent, tem,
    M= ua.match(/(opera|chrome|safari|firefox|msie)\/?\s*([\d\.]+)/i);
    if(M && (tem= ua.match(/version\/([\.\d]+)/i))!= null) M[2]= tem[1];
    M= M? [M[1], M[2]]:[N, navigator.appVersion, '-?'];
    return M.join(' ').toLowerCase();
})();


function addProcessingListenerToForms(){
    // Add processing listener to all forms
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', event => {
            processing();
        });
    });
}

function downloadWithProgress(url, filename) {
  const startTime = new Date().getTime();

  request = new XMLHttpRequest();

  request.responseType = "blob";
  request.open("get", url, true);
  request.send();

  processing()

  request.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
          const imageURL = window.URL.createObjectURL(this.response);
          const anchor = document.createElement("a");
          anchor.href = imageURL;
          anchor.download = filename;
          document.body.appendChild(anchor);
          anchor.click();
          completed()
      }
  };

  request.onprogress = function (e) {
    const percent_complete = Math.floor((e.loaded / e.total) * 100);

    const duration = (new Date().getTime() - startTime) / 1000;
    const bps = e.loaded / duration;

    const kbps = Math.floor(bps / 1024);

    const time = (e.total - e.loaded) / bps;
    const seconds = Math.floor(time % 60);
    const minutes = Math.floor(time / 60);

    // console.log(
    //   `${percent_complete}% - ${kbps} Kbps - ${minutes} min ${seconds} sec remaining`
    // );
  };
}

/* == Force translation for dynamic collapse and expand advanced filters ==*/
function translateCollapseTooltip(item){
    let label = $(item).parent().find(".tooltip .tooltip-inner");
    if (label.length){
        if(label.html() == "Expand"){
            label.html("Expandir");
        }else if(label.html() == "Collapse"){
            label.html("Contraer");
        }
    }
}

function addListenerForCollapseLabelTranslate(){
    let toggle = $("#advanced_filter_toggle_btn");
    if(toggle.length){
        $(toggle).on("mouseenter", function () {
            setTimeout(()=>{translateCollapseTooltip(this);}, 100);
        });
        $(toggle).on("click", function(){ translateCollapseTooltip(this);});
    }
}