$(document).ready(function() {
    $("button").click(function() {
        var username = $('text#user').val();
        var password = $('password#password').val();
        $.ajax({
            method: "POST",
            url: "signin",
            data: {username, password},
            dataType: "dataType",
            success: function(resp) {
                $('div#log_resp') = resp.data;
            }
        });
    });
});