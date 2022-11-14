$(document).ready(function () {
    $("input[type=file].snippet-file").each(function(){
        $(this).change(function () {
            let field_id = $(this).attr('id');
            let filename = this.files[0].name;
            $("#file_name_" + field_id).html(filename);
            $("#box_file_" + field_id).show();
        });
    });
});
