if (typeof pwc == 'undefined'){
  pwc = {};
};

var DELETE_SELECTOR = "li button";

pwc.ItemList = function(root_selector){
	this.root_selector = root_selector;
	this.root = $(root_selector);
	this.items = {};
	this.item_list = this.root.find("ul.item_list");
};

pwc.ItemList.prototype.setup_events = function(){
	var _this = this;
	
	$(this.root_selector + " button.add_item").live("click", function(){
		var par_name = _this.root.find("input.item_name").val();
		var par_value = _this.root.find("input.item_value").val();
		_this.items[par_name] = par_value;
		_this.render();
	});
	$(this.root_selector + " ul.item_list " + DELETE_SELECTOR).live("click", function(){
		delete _this.items[$(this).parent().find("span.name").text()];
		_this.render();
	});
};

pwc.ItemList.prototype.render = function(){
	this.item_list.empty();
	for (var name in this.items){
		this.item_list.append("<li><span class='name'>" + name + "</span>="
				+ this.items[name]
		        + "<button>Remove</button></li>");
	}
};