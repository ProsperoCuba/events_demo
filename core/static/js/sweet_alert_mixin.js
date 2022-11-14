function init_swal(title, content, confirm_text, confirm_button_color) {

    return {

        customClass: {
            confirmButton: confirm_button_color ? "btn btn-" + confirm_button_color : "btn btn-danger",
            cancelButton: 'btn btn-default'
        },
        buttonsStyling: false,
        title: title ? title : ($("#scripts_translated_labels").data("custom-action-confirm-title") || "Estás seguro?"),
        text: content || content==="" ? content : ($("#scripts_translated_labels").data("custom-action-confirm-msg") || "No serás capaz de revertir esta acción!"),
        type: "warning",
        showCancelButton: true,
        cancelButtonText: ($("#scripts_translated_labels").data("custom-action-cancel-button") ||"Cancelar"),
        confirmButtonText: confirm_text ? confirm_text : ($("#scripts_translated_labels").data("custom-action-confirm-button") ||"Sí, eliminar!"),
        backdrop: true,
        showCloseButton: true

    }
}