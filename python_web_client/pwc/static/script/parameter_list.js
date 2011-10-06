if (typeof pwc == 'undefined'){
  pwc = {};
};

pwc.ParameterList = function(root_selector){
	this.root_selector = root_selector;
	this.root = $(root_selector);
	this.parameters = {};
	this.parameter_list = this.root.find("ul.parameter_list");
};

pwc.ParameterList.prototype.setup_events = function(){
	var _this = this;
	
	$(this.root_selector + " button.add_parameter").live("click", function(){
		var par_name = _this.root.find("input.parameter_name").val();
		var par_value = _this.root.find("input.parameter_value").val();
		_this.parameters[par_name] = par_value;
		_this.render();
	});
	$(this.root_selector + " ul.parameter_list li button").live("click", function(){
		delete _this.parameters[$(this).parent().find("span.name").text()];
		_this.render();
	});
};

pwc.ParameterList.prototype.render = function(){
	this.parameter_list.empty();
	for (var name in this.parameters){
		this.parameter_list.append("<li><span class='name'>" + name + "</span>="
				+ this.parameters[name]
		        + "<button>Remove</button></li>");
	}
};