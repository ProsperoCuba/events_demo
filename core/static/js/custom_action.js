$(document).ready(function () {

    function ajax_call(url, method, success_text, error_text, redirecturl) {

        $.ajax({
            url: url,
            type: method ? method : 'POST',
        })
        .done(function (resp, status_msg, resp_obj) {
            let msg = success_text ? success_text : $("#scripts_translated_labels").data("custom-action-success-msg") || 'La operación se ha completado con éxito.'
            let redirect_to;
            const resp_json = resp_obj.responseJSON;
            if (resp_json) {
                msg = resp_json.msg ? resp_json.msg : msg;
                redirect_to = resp_json.redirect_to;
            }
            swal.fire({
                title: $("#scripts_translated_labels").data("custom-action-success") || 'Éxito!',
                text: msg,
                type: 'success',
            }).then((resp) => {
                if(redirect_to!==undefined && redirect_to !==""){
                    window.location=redirect_to;
                } else if (redirecturl && redirecturl !== "") {
                    window.location = redirecturl;
                }else{
                    window.location.reload()
                }

            });
        })
        .fail(function (resp) {
            fail_response(resp, error_text)
        });

    }


    // Generic action button
    $(document).on('click', 'a.custom-button', function (e) {
        e.preventDefault();
        e.stopPropagation();

        $button = $(this);
        let url = $button.attr('data-href') || $button.attr('href');
        if (!url) {
            return false
        }

        var object_id = $button.data('id');
        var title = $button.data('title');
        var content = $button.data('content');
        var confirm_text = $button.data('confirm_text');
        var success_text = $button.data('success_text');
        var error_text = $button.data('error_text');
        var method = $button.data('method');
        var skip_confirm = $button.data('skip_confirm');
        var confirm_button_color = $button.data('confirm_button_color');
        var redirecturl = $button.data('redirecturl');

        // skip confirmation and make ajax_call immediately
        if (typeof (skip_confirm) !== "undefined") {
            ajax_call(url, method, success_text, error_text)
        } else {
            const options = init_swal(title, content, confirm_text, confirm_button_color);

            swal.fire(options).then(function (e) {
                if (e.value) {
                    ajax_call(url, method, success_text, error_text, redirecturl)
                }
            });

        }


    })
});
