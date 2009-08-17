Bulletins = {
	'bindEvents': function () {
		$('.tpl-full-archive').jqm({ trigger: '.jqModal' });
		
		$('.reply-form').jqm({
			trigger: '#reply-button',
			
			onHide : function (h) {
				h.o.remove();
				h.w.hide();

				$('#error').html('');
			}
		});
		
		$('#reply-form').submit(Bulletins.submitReply);
	},
	
	//AJAX: SUBMIT BULLETIN'S REPLY
	'submitReply': function () {
		form = $(this);
		
		form.children('input[@type="submit"]').fadeTo('fast', 0, function() {
			$(this).hide().siblings('.wait').show();
		});
		
		$.ajax({
			'url'        : '/bulletins/reply',
			'type'       : 'post',
			'contentType': 'text/x-json',
			'dataType'   : 'json',
			'data'       : {
				'id'      : $('#id').val(),
				'contacts': $('#contacts').val(),
				'reply'   : $('#reply').val()
			},
			
			'error'      : function () {
				form.children('input[@type="submit"]').fadeTo('fast', 1, function() {
					$(this).show().siblings('.wait').hide();
				});
				
				$('#error').html('<strong>Ошибка</strong> соединения с сервером');
			},
			
			'success': function (data) {
				$('#error').html('');
				
				form.children('input[@type="submit"]').fadeTo('fast', 1, function() {
					$(this).show().siblings('.wait').hide();
				});
				
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
		
		return false;
	}
}
