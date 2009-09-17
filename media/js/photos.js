var date = new Date();

requestDateTime = {
	'year': date.getYear()
};

Photos = {
	'bindEvents': function(){
		Comments.bindTo($('#comment-form'), $('.tpl-comments ul'), requestDateTime);
	},
	
	'plugins': function(){	
		$('.tpl-full-archive').jqm();
	
		$('.photo img').tooltip({
		  track     : true,
		  delay     : 0,
		  showURL   : false,
		  fixPNG    : true
		});
	}
};

