$(document).ready(function() {
    $("#signin").click(function() {
        $.ajax({
            method: "POST",
            url: "/test",
            success: function(resp) {
            }
        });
    });
});