Comments = {
	'bindTo': function(form, comments) {
		var date = new Date();
		this.requestDateTime = date.format('yyyy-mm-dd HH:MM:ss');
		
		form.submit(function() {
			// send comment and recieve all comments since requestDateTime
			Comments.update(form, comments);
				
			return false;
		})	
	},
	
	'update': function(form, comments) {
		comment = form.find('.text')
		error   = form.find('.error')
		
		$('.ajax-load, input[type="submit"]').toggle();
		
		$.ajax({
			'url'        : form.attr('action'),
			'type'       : 'post',
			'contentType': 'text/x-json',
			'dataType'   : 'json',
			'data'       : { 'comment': comment.val(), 'since': Comments.requestDateTime },
			
			'error'      : function () {
				$('.ajax-load, input[type="submit"]').toggle();
				error.html('<strong>Ошибка</strong> соединения с сервером');
			},
			
			'success': function (data) {
				error.html('');
				$('.ajax-load, input[type="submit"]').toggle();
				
				if( ! data.success)
					error.html(data.error);
				else {
					date = new Date();
					Comments.requestDateTime = date.format('yyyy-mm-dd HH:MM:ss');
					
					comments.children('.empty-msg').hide();
					
					comment.val('');
					$(data.fresh).appendTo(comments);
				}
			}
		});
	}
};
