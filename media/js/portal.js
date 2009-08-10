Portal = {
	'bindEvents': function () {
		for(var type in {'photos': 1, 'video': 1, 'forum': 1})
			$('#show-'+type).click(function () {
				type = $(this).attr('id').replace('show-', '');
				
				if($('#'+type+':visible').size())
					return false;
				
				$(this)
					.siblings().removeClass('selected-link').end()
					.addClass('selected-link');
				
				$('.digest').fadeTo('fast', 0, function () {
					$('#'+type).show().fadeTo('fast', 1);
				}).hide();
				
				return false;
			});
	}
};
