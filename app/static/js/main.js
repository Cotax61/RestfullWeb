$(document).ready(function() {
    console.log("ready!");
    $("#signin").click(function() {
        $("#signin").hide();
        console.log("Clicked");
        $.ajax({
            method: "POST",
            url: "/test",
            success: function(resp) {
                $('div#log_resp') = resp.data;
            }
        });
    });
});