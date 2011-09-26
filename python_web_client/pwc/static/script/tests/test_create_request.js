CreateRequestTest = TestCase("CreateRequestTest");

var SAMPLE_URL = "http://123.456.789.0";

CreateRequestTest.prototype.test_constructor = function(){
	/*:DOC += <div id='test_create_request'></div> */
	var creater = new pwc.CreateRequest("#test_create_request");
	assertEquals("DIV", creater.root[0].nodeName);
};

CreateRequestTest.prototype.test_make_request = function(){
	/*:DOC += 
<div id='test_create_request'>
  <input id="url" />
  <button id="submit_request">Submit</button>
</div> */
	expectAsserts(1);
	var creater = new pwc.CreateRequest("#test_create_request", 
			function(deferred){
		//Be nice if we could test what the deferred is waiting to complete...
		assertTrue(true);
	});
	creater.setup_events();
	creater.root.find("#url").val(SAMPLE_URL);
	creater.root.find("#submit_request").trigger("click");
};
