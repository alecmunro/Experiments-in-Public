if (typeof pwc == 'undefined'){
  pwc = {};
};

pwc.DisplayResponse = function(root_selector){
	this.root_selector = root_selector;
	this.root = $(root_selector);
};

pwc.DisplayResponse.prototype.process_response = function(response){
	this.root.find("em.status").text(response.status);
	var headers = this.root.find("ul.headers").empty();
	for (var name in response.headers){
		headers.append("<li><strong>" + name + "</strong>: <span name='" + name + "'>" + response.headers[name] + "</span></li>");
	}
	this.root.show();
};