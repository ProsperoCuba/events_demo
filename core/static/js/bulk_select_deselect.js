var selected = [];

$(document).ready(function () {

    function clearHiddenInputs(form) {
        form.find("input.extra[name='selection[]']").remove()
    }

    function createHiddenInput(form, val) {
        var input = $('<input>')
            .attr('class', 'extra')
            .attr('type', 'hidden')
            .attr('name', 'selection[]').val(val)
        form.append(input)
    }

    function createDeselectedHiddenInput(form, val) {
        var input = $('<input>')
            .attr('class', 'extra')
            .attr('type', 'hidden')
            .attr('name', 'deselected[]').val(val)
        form.append(input)
    }

    function init_checkboxes() {
        $('.table tbody input:checkbox').each(function (_, el) {
            var val = $(el).val();
            if (selected.includes(parseInt(val))) {
                $(this).prop('checked', true);
                $(this).trigger('change')

            }
        });
    }

    init_checkboxes()

    var form = $("#table-head-tools-form")

    $(".table tbody input:checkbox").change(function (e) {
        if (!$(this).is(':checked')) {
            if (selected.indexOf(parseInt($(this).val())) != -1)
                createDeselectedHiddenInput(form, $(this).val())

        } else {
            //remove from deselected
            var val = $(this).val()
            var inputs = form.find("input[name='deselected[]']")

            $.each(inputs, function (i, obj) {

                if ($(obj).val() === val) {
                    $(obj).remove()
                }
            })
        }
    })

    var btn = $("#table-head-tools-save-btn")
    btn.click(function (e) {
        e.preventDefault()
        e.stopPropagation()

        clearHiddenInputs(form);

        $('.table input:checked').each(function (_, el) {
            var val = $(el).val();
            if (val != 'on') {
                createHiddenInput(form, val)
            }
        });

        form.submit()

    })


})