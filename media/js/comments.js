Comments = {
	'bindTo': function(form, comments, requestDateTime) {
		form.submit(function() {
			if(comments = Comments.send(form, comments, requestDateTime))
				Comments.updateWith(comments)
				
			return false;
		})	
	},
	
	'send': function(form, comments, requestDateTime) {
		$('.ajax-load, input[type="submit"]').toggle();
		
		$.ajax({
			'url'        : form.attr('action'),
			'type'       : 'post',
			'contentType': 'text/x-json',
			'dataType'   : 'json',
			'data'       : { 'comment': form.children('textarea').val() },
			
			'error'      : function () {
				$('.ajax-load, input[type="submit"]').toggle();
				$('#error').html('<strong>Ошибка</strong> соединения с сервером');
			},
			
			'success': function (data) {
				$('#error').html('');
				$('.ajax-load, input[type="submit"]').toggle();
				
				if( ! data.success) {
					$('#error').html(data.error);
				} else {
					alert('Сообщение отправлено!');
					
					$('.reply-form').jqmHide();
					$('#contacts').val('');
					$('#reply').val('');
				}
			}
		});
	},
	
	'updateWith': function(comments) {
		return true;
	}
};
