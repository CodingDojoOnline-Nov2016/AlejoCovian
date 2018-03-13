$(function() {

    $('#post-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted.")  
        create_post();
    });

});