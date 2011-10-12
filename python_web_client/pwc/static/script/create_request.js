if (typeof pwc == 'undefined'){
  pwc = {};
};

pwc.CreateRequest = function(root_selector, get_callback){
	this.root_selector = root_selector;
	this.root = $(root_selector);
	this.get_callback = get_callback;
	this.parameter_list = new pwc.ItemList(root_selector + " #parameters");
	this.header_list = new pwc.ItemList(root_selector + " #headers");
};

pwc.CreateRequest.prototype.setup_events = function(){
	var _this = this;
	$(this.root_selector + " #submit_request").live("click", function(){
		var url = _this.root.find("#url").val();
		var method = _this.root.find("#method").val();
		var parameters = $.toJSON(_this.parameter_list.parameters);
		var headers = $.toJSON(_this.parameter_list.headers);
		var response_get = $.post("/request", {"url": url, "method": method,
			"parameters": parameters, "headers": headers});
		_this.get_callback(response_get);
	});
	this.parameter_list.setup_events();
	this.header_list.setup_events();
};