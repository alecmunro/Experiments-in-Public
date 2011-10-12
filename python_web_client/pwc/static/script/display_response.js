if (typeof pwc == 'undefined'){
  pwc = {};
};

pwc.DisplayResponse = function(root_selector){
	this.root_selector = root_selector;
	this.root = $(root_selector);
	this.block_displayer = new pwc.BlockDisplayer(root_selector + " div.response_body")
};

pwc.DisplayResponse.prototype.process_response = function(response){
	this.root.find("em.status").text(response.status);
	this.block_displayer.set_content(response.body);
	var headers = this.root.find("ul.headers").empty();
	for (var name in response.headers){
		headers.append("<li><strong>" + name + "</strong>: <span name='" + name + "'>" + response.headers[name] + "</span></li>");
	}
	this.root.show();
};


var DEFAULT_TAB = "plain"
/*Widget offering different ways to display a block of text.*/
pwc.BlockDisplayer = function(root_selector){
	this.root_selector = root_selector;
	this.root = $(root_selector).tabs();
	this.content = "";
	this.current_tab = DEFAULT_TAB;
};

pwc.BlockDisplayer.prototype.set_content = function(content){
	this.content = content;
	this.render();
};

pwc.BlockDisplayer.prototype.render = function(){
	switch(this.current_tab){
	case "plain":
		this.root.find("textarea.body").val(this.content);
		break;
	case "html":
		break;
	}
};