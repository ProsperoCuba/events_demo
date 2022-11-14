$(document).ready(function () {
    let file_input_image = document.getElementById('scripts_translated_labels').getAttribute('data-file-input-image') || 'No file has been selected';
    var flag = false;
    $("input[type=file].snippet-file-image").each(function(){
        $(this).change(function () {
            let field_id = $(this).attr('id');
            let filename = this.files[0].name;
            flag = true;
            $("#file_name_" + field_id).html(filename);
            $("#box_file_" + field_id).show();
        });
    });

    $("button[type=submit]").click(function() {
        if (flag == false){
            $("#file_name_id_signature").html('<span style="color: #fd27eb">' + file_input_image + '</span>');
            $("#box_file_id_signature").show();
        }
    });
});
