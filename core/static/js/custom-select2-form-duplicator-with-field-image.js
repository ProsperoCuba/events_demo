if (typeof form_prefix === 'undefined') {
    var form_prefix = document.currentScript.dataset.form_prefix;
}

if (typeof URL === 'undefined') {
    var URL = document.currentScript.dataset.url;
}
if (typeof MININPUTLENGHT === 'undefined') {
    var MININPUTLENGHT = document.currentScript.dataset.minimumInputLength || 2;
}


$(document).ready(function () {
    if (!URL) {
        return
    }
    function cloneMore(selector) {

        var last_row = $(selector)

        // current total form count
        var count = parseInt($('#id_' + form_prefix + '-TOTAL_FORMS').val());

        // update django Total form count
        $('#id_' + form_prefix + '-TOTAL_FORMS').val(count + 1);

        // gen template with updated prefix
        var template = $('#empty_form').html().replace(/__prefix__/g, count);
        var newElement = $(template)
        newElement.hide()

        if (last_row.length > 0) {
            newElement.insertAfter(last_row);
            newElement.slideDown(300);
        } else {
            // add as first element
            $(".formset_container").append(newElement)
            newElement.slideDown(300);

        }

        // // initialize select2 instance
        $.each(newElement.find('.select2me'), function (i, obj) {
            if (!$(obj).data("select2")) {
                let selectUrl = URL;
                if($(obj).data("select2-url")){
                    selectUrl = $(obj).data("select2-url");
                }
                let options = {
                    ajax: {
                        url: selectUrl,
                        dataType: 'json',
                        type: "GET",
                    }
                }
                if (MININPUTLENGHT || MININPUTLENGHT === 0) {
                    $.extend(options, {'minimumInputLength': MININPUTLENGHT})
                }
                if (typeof DATAFUNCTION !== 'undefined') {
                    $.extend(options.ajax, {'data': DATAFUNCTION})
                }
                if (typeof PROCESSRESULTSFUNCTION !== 'undefined') {
                    $.extend(options.ajax, {'processResults': PROCESSRESULTSFUNCTION})
                }

                $(obj).select2(options)
            }
        })

    }

    function updateFormElementIndices(i, el) {

        var curIndex = $(el)
            .attr('id')
            .match(/\d+/)[0];

        // update form row id
        $(el).attr('id', $(el).attr('id').replace(curIndex, i));
        // update delete button
        $(el).find('a.remove-form-row').attr('data-form', $(el).attr('id').replace(curIndex, i));

        // update inputs
        var inputs = $(el).find('input');

        inputs.each(function (j, input) {
            $(input).attr('id', $(input).attr('id').replace(curIndex, i));
            $(input).attr('name', $(input).attr('name').replace(curIndex, i));
        });

        // select2 inputs
        var select2elements = $(el).find('.select2me');

        select2elements.each(function (j, input) {
            $(input).select2("destroy")
            $(input).attr('id', $(input).attr('id').replace(curIndex, i));
            // not needed since it is recreated on line select2()
            // $(input).attr('data-select2-id', $(input).attr('data-select2-id').replace(curIndex, i))
            $(input).select2()
        });

        // define all custom inputs may needed

    }

    function deleteForm(e) {
        e.preventDefault()
        swal.fire(init_swal()).then((result) => {
            if (result.value) {
                var $btn = $(this);
                var prefix = $btn.data('form');
                var $delete_input = $('#id_' + prefix + '-DELETE');
                if ($delete_input.length > 0) {
                    $delete_input.prop('checked', true);
                    $('#' + prefix).slideUp(300);
                } else {
                    var count = parseInt($('#id_' + form_prefix + '-TOTAL_FORMS').val());
                    $("#id_" + form_prefix + "-TOTAL_FORMS").val(count - 1);

                    $('#' + prefix).slideUp(300, function () {
                        $(this).remove()
                        var forms = $(".formset_container .formset-row");
                        //
                        $.each(forms, updateFormElementIndices);
                    });
                }
            }
        });
    }

    function loadKTAvatar() {
        var list_input = [];
        $('.kt-avatar input[type=file]').each(function() {
            list_input.push($(this).attr("id"));
        });
        list_input.reverse();
        KTUtil.ready(function () {
            for (let id of list_input){
                console.log("declared id:" + id)
                new KTAvatar('kt_' + id);
            }

        });
    }

    $(document).ready(function() {
        loadKTAvatar();
    });

    $(document).on("click", ".add-form-row", function (e) {
        e.preventDefault();
        cloneMore(".formset_container .formset-row:last");
        loadKTAvatar();
        // return false;
    });


    $(document).on("click", ".remove-form-row", deleteForm);


})