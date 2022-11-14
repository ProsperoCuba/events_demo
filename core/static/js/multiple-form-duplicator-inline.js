$(document).ready(function () {

    function cloneMoreInline(e) {
        e.preventDefault();
        const $btn = $(this);
        const container = $btn.closest(".formset_container")
        var last_row = container.find('.formset-row:last')

        const form_prefix = container.data('form_prefix')

        // // current total form count
        // var count = parseInt($('#id_form-TOTAL_FORMS').val());
        // console.log("count")
        // console.log(count)
        // // update django Total form count
        // $('#id_form-TOTAL_FORMS').val(count + 1);

        // current total form count
        var count = parseInt($('#id_' + form_prefix + '-TOTAL_FORMS').val());
        // update django Total form count
        $('#id_' + form_prefix + '-TOTAL_FORMS').val(count + 1);

        // gen template with updated prefix

        // empty_form-form-__prefix__
        var template = $(`#empty_form-${form_prefix}-__prefix__`).html().replace(/__prefix__/g, count);
        var newElement = $(template)
        newElement.hide();
        if (last_row.length > 0) {

            newElement.insertAfter(last_row);
            newElement.slideDown(300);
        } else {
            // add as first element
            container.find('table').append(newElement)
            newElement.slideDown(300);

        }

        // // initialize select2 instance
        var select2elements = $(newElement).find('.django-select2');
        $.each(select2elements, function (i, input) {
            $(input).next('span.select2-container').remove()
            $(input).djangoSelect2();

        });
    }

    function updateFormInlineElementIndices(i, el) {

        var curIndex = $(el)
            .attr('id')
            .match(/\d+/)[0];

        // update form row id
        $(el).attr('id', $(el).attr('id').replace(curIndex, i));

        // update delete button
        $(el).find('a.remove-form-inline-row').attr('data-form', $(el).attr('id').replace(curIndex, i));

        // update inputs
        var inputs = $(el).find('input');

        inputs.each(function (j, input) {
            $(input).attr('id', $(input).attr('id').replace(curIndex, i));
            $(input).attr('name', $(input).attr('name').replace(curIndex, i));
        });


        var select2elements = $(el).find('.django-select2');
        select2elements.each(function (j, input) {
            $(input).select2("destroy");
            $(input).attr('id', $(input).attr('id').replace(curIndex, i));
            $(input).djangoSelect2();
            $(input).select2();
        });

        // define all custom inputs may needed

    }

    function deleteFormInline(e) {
        e.preventDefault()
        swal.fire(init_swal()).then((result) => {
            if (result.value) {
                var $btn = $(this)
                const container = $btn.closest(".formset_container");
                var row_prefix = $btn.data('form');
                var $delete_input = $('#id_' + row_prefix + '-DELETE');
                if ($delete_input.length > 0) {
                    $delete_input.prop('checked', true);
                    $('#' + row_prefix).slideUp(300);
                } else {
                    const form_prefix = container.data('form_prefix')
                    var count = parseInt($('#id_' + form_prefix + '-TOTAL_FORMS').val());

                    $("#id_" + form_prefix + "-TOTAL_FORMS").val(count - 1);
                    $('#' + row_prefix).slideUp(300, function () {
                        $(this).remove()
                        var forms = container.find(".formset-row");
                        //
                        $.each(forms, updateFormInlineElementIndices);
                    });
                }
            }
        });
    }


    $(document).on("click", ".add-form-inline-row", cloneMoreInline);


    $(document).on("click", ".remove-form-inline-row", deleteFormInline);


})