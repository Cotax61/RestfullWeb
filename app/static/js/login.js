$(document).ready(function() {
    $("button#valid_sigin").click(function() {
        var username = $('text#user').val();
        var password = $('password#password').val();
        $.ajax({
            method: "POST",
            url: "signinded",
            data: {username, password},
            dataType: "dataType",
            success: function(resp) {
                $('div#log_resp').append(resp.data);
            }
        });
    });
});