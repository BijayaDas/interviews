//ADD YOUR CODE HERE.

$(function () {
	// initialilisation on page reload
	NEXT_ID = {{step['next']}};
	$("{{step['selector']}}").popover({
        placement : 'top',
        html : true,
        title : '<h4>Hint</h4>',
        content : '<div class="media"><p>{{ step["content"] }}</p></div><a href="#" id="next_tip_please" class="btn btn-info" data-dismiss="alert">Got it! Next</a>'
    });
    $("{{step['selector']}}").popover('show');

    // guided learning from next stage
    $(document).on("click", "#next_tip_please" , function(){
        $(this).parents(".popover").popover('hide');
        if(NEXT_ID == null){
        	alert("You have reached the end of guided learning");
        	return false;
        }

        // calling the server for ajax call
        $.ajax({
        	method: "GET",
            url : '/get_next_step?next_id=' + NEXT_ID,
            dataType: "json",
            success: function(data) {
            	NEXT_ID = data["results"]["next"];
    	    	$(data["results"]["selector"]).popover({
			        placement : 'top',
			        html : true,
			        title : '<h4>Hint</h4>',
			        content : '<div class="media"><p>' + data["results"]["content"] + '</p></div><a href="#" id="next_tip_please" class="btn btn-info" data-dismiss="alert">Got it! Next</a>'
			    });
			    $(data["results"]["selector"]).popover('show');

            }
        });
    });

})