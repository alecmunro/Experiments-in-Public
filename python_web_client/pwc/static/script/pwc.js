if (typeof pwc == 'undefined'){
  pwc = {};
};

pwc.Index = function(create_request_root, display_response_root){
	var _this = this;
	this.create_request = new pwc.CreateRequest(create_request_root, 
		function(deferred){_this.process_request_get(deferred)});
	this.display_response = new pwc.DisplayResponse(display_response_root);
};

pwc.Index.prototype.setup_events = function(){
	this.create_request.setup_events();
};

pwc.Index.prototype.process_request_get = function(request_get){
	var _this = this;
	request_get.success(function(data){
		_this.display_response.process_response(data);
	})
	
};