ItemListTest = TestCase("ItemListTest");

var SAMPLE_NAME = "A name";
var SAMPLE_VALUE = "This value";

var SAMPLE_ITEMS = {"a": 1, "b": 2, "c":3};

function obj_size(obj) {
    var size = 0, key;
    for (key in obj) {
        if (obj.hasOwnProperty(key)) size++;
    }
    return size;
}


ItemListTest.prototype.test_add = function(){
	/*:DOC+= <div id="items">
	        <input class="item_name" name="item_name" />
	        <input class="item_value" name="item_value"/>
	        <button class="add_item">Add</button>
	        <ul class="item_list"></ul>
	      </div>*/
	var list = new pwc.ItemList("#items");
	list.setup_events();
	list.root.find("input.item_name").val(SAMPLE_NAME);
	list.root.find("input.item_value").val(SAMPLE_VALUE);
	list.root.find("button.add_item").trigger("click");
	assertEquals(1, obj_size(list.items));
	assertEquals(1, list.item_list.children().length);
};

ItemListTest.prototype.test_delete = function(){
	/*:DOC+= <div id="items">
	        <input class="item_name" name="item_name" />
	        <input class="item_value" name="item_value"/>
	        <button class="add_item">Add</button>
	        <ul class="item_list">
	        <li><span class="name">A name</span><button>Remove</button></li></ul>
	      </div>*/
	var list = new pwc.ItemList("#items");
	list.items[SAMPLE_NAME] = SAMPLE_VALUE;
	list.setup_events();
	list.item_list.find("li button").trigger("click");
	assertEquals(0, obj_size(list.items));
	assertEquals(0, list.item_list.children().length);
};

ItemListTest.prototype.test_render = function(){
	/*:DOC+= <div id="items">
	        <input class="item_name" name="item_name" />
	        <input class="item_value" name="item_value"/>
	        <button class="add_item">Add</button>
	        <ul class="item_list">
	        <li><span class="name">A name</span><button>Remove</button></li></ul>
	      </div>*/
	var list = new pwc.ItemList("#items");
	list.items = SAMPLE_ITEMS;
	list.render();
	assertEquals(3, list.item_list.children().length);
};