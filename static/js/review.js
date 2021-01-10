//Confirm if user wants to delete review - confirmation is hidden on page launch
$("#sure").hide();


$('#delete').on('click', function() {
        $("#sure").show();
    });

$('#no').on('click', function() {
        $("#sure").hide();
    });