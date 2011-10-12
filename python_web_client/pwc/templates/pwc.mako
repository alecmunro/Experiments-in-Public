<html>
  <head>
    <title>Welcome to the ${project}!</title>
    <link rel="stylesheet" href="static/css/pwc.css" />
    <link rel="stylesheet" href="static/css/sunny/jquery-ui-1.8.16.custom.css" />
    <script src="static/script/jquery-1.6.4.min.js"></script>
    <script src="static/script/jquery-ui-1.8.16.custom.min.js"></script>
    <script src="static/script/jquery.json-2.3.min.js"></script>
    <script src="static/script/display_response.js"></script>
    <script src="static/script/create_request.js"></script>
    <script src="static/script/item_list.js"></script>
    <script src="static/script/pwc.js"></script>
    <script>
$(document).ready(function(){
  var index_page = new pwc.Index("#create_request", "#display_response");
  index_page.setup_events();
});
    </script>
  </head>
  <body>
    <div id="pwc">
	  <h1>${project}</h1>
	  <p>The ${project} is a simple web service to assist in debugging and documenting HTTP APIs.</p>
	  <div id="controls">
	  
	    <div class="widget" id="create_request">
	      <h3>Enter Request Details</h3>
	      <select id="method">
	      % for method in methods:
	        <option>${method}</option>
	      % endfor
	      </select>
	      <input id="url" size="60" value="http://" />
	      <button id="submit_request">Submit Request</button><br />
	      <div id="parameters" class="item_list_widget">
	        <h4>Request Parameters</h4>
 	        <ul class="item_list"></ul>
	        <label for="item_name">Name</label>: <input class="item_name" name="item_name" />
	        <label for="item_value">Value</label>: <input class="item_value" name="item_value"/>
	        <button class="add_item">Add</button>
	      </div>
	      <div id="headers" class="item_list_widget">
	        <h4>Request Headers</h4>
	        <ul class="item_list"></ul>
	        <label for="item_name">Name</label>: <input class="item_name" name="item_name" />
	        <label for="item_value">Value</label>: <input class="item_value" name="item_value"/>
	        <button class="add_item">Add</button>
	      </div>
	    </div>
	    <div class="widget" id="display_response">
	      <h3>Response</h3>
	      <strong>Status</strong>:<em class="status"></em><br/>
	      <ul class="headers"></ul>
	      <div class="response_body">
	        <ul>
	          <li><a href="#body_plain">Plain</a></li>
	          <li><a href="#body_html">HTML</a></li>
	        </ul>
	        <div id="body_plain">
	          <textarea class="body"></textarea>
	        </div>
	        <div id="body_html">
	          <p>Not Implemented.</p>
	        <div>
	      </div>
	      
	    </div>
	    
	  </div>
	  <div style="clear:both;">&nbsp;</div>
    </div>
  </body>
</html>