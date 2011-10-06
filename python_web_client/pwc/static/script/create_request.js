if (typeof pwc == 'undefined'){
  pwc = {};
};

pwc.CreateRequest = function(root_selector, get_callback){
	this.root_selector = root_selector;
	this.root = $(root_selector);
	this.get_callback = get_callback;
};

pwc.CreateRequest.prototype.setup_events = function(){
	var _this = this;
	$(this.root_selector + " #submit_request").live("click", function(){
		var url = _this.root.find("#url").val();
		var method = _this.root.find("#method").val()
		var response_get = $.getJSON("/request", {"url": url, "method": method});
		_this.get_callback(response_get);
	});
};