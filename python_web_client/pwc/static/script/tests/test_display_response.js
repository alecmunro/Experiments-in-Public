DisplayResponseTest = TestCase("DisplayResponseTest");

var SAMPLE_STATUS = 456;
var SAMPLE_HEADERS = {
	a: 1,
	b: 2
};
DisplayResponseTest.prototype.test_constructor = function(){
	/*:DOC += <div id='test_response'></div> */
	var display = new pwc.DisplayResponse("#test_response");
	assertEquals("DIV", display.root[0].nodeName);
};

DisplayResponseTest.prototype.test_process_response = function(){
	/*:DOC += 
<div id='test_response' style="display:None">
  <em class='status'></em>
  <ul class='headers'></ul>
</div> */
	var display = new pwc.DisplayResponse("#test_response");
	display.process_response({
		status: SAMPLE_STATUS,
		headers: SAMPLE_HEADERS});
	assertEquals(display.root.find("em.status").text(), SAMPLE_STATUS);
	for (var name in SAMPLE_HEADERS){
		assertEquals(display.root.find("span[name='"+name+"']").text(), 
				SAMPLE_HEADERS[name]);
	}
};