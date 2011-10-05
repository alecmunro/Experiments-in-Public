<html>
  <head>
    <title>Welcome to the ${project}!</title>
    <link rel="stylesheet" href="static/pwc.css" />
    <script src="static/script/jquery-1.6.4.min.js"></script>
    <script src="static/script/display_response.js"></script>
    <script src="static/script/create_request.js"></script>
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
	      <input id="url"/>
	      <button id="submit_request">Submit Request</button>
	    </div>
	    <div class="widget" id="display_response">
	      <h3>Response</h3>
	      <strong>Status</strong>:<em class="status"></em><br/>
	      <ul class="headers"></ul>
	      <textarea class="body"></textarea>
	    </div>
	  </div>
	  <div style="clear:both;">&nbsp;</div>
    </div>
  </body>
</html>