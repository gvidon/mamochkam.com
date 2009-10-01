Video = {
	//EVENTS HANDLER
	'bindEvents': function(){
		Comments.bindTo($('#comment-form'), $('.tpl-comments ul'));
	},
	
	//INIT VIDEO PLAYER
	'initPlayer': function (videoPath)
	{
		flashembed('video', 
			{
				src   : mediaURL+'/FlowPlayerClassic.swf',
				width : 400,
				height: 290
			},
			
			{config: {
				autoPlay                 : false,
				autoBuffering            : true,
				controlBarBackgroundColor: '0x2e8860',
				initialScale             : 'scale',
				videoFile                : videoPath
			}} 
		);
	},
	
	//INIT PLUGINS
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

