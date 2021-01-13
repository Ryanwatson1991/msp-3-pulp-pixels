//Confirm if user wants to delete review - confirmation is hidden on page launch - on Review page
$("#sure").hide();

$("#review-delete-check").hide();



$('#delete').on('click', function() {
        $("#sure").show();
    });

$('#no').on('click', function() {
        $("#sure").hide();
    });

// Same as above, confirms if user wants to delete review, this time on profile page


$('#delete-2').on('click', function() {
        $("#sure-2").show();
    });

$('#no-2').on('click', function() {
        $("#sure-2").hide();
    });