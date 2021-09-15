  
$(document).ready(function() {

	$('form').on('submit', function(event) {
        
        var question_id = $(this).attr('question_id');
        var RadioButtonStatusCheck = $('form input[type=radio]:checked').val()

		$.ajax({
			data : {
				choice : RadioButtonStatusCheck,
                question_id : question_id
			},
			type : 'POST',
			url : '/guest/update',    
		})
        .done(function(data) {
			
            $('form input[type=radio]:checked').prop('checked', false);

            if (data.error) {
				$('input[id="'+data.choice_id+'"][value="'+data.choice+'"]').attr('disabled', 'disabled');
				$('label[for="'+data.choice_id+'"]').css('color', '#b80b00');
				
			}
			else {
				$('label[for="'+data.choice_id+'"]').css('color', '#009423');
				$('input[name="choicesFor'+question_id+'"]:radio').attr('disabled', 'disabled');
				$('#submitButton'+question_id).fadeOut(500)

			}

        });
        event.preventDefault();
        event.stopImmediatePropagation();
	});
    
});