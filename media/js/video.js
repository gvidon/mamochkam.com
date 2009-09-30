Video = {
	'bindEvents': function(){
		Comments.bindTo($('#comment-form'), $('.tpl-comments ul'));
	},
	
	'plugins': function(){	
		$('.tpl-full-archive').jqm();
	
		$('.video img').tooltip({
		  track  : true,
		  delay  : 0,
		  showURL: false,
		  fixPNG : true
		});
	}
};

