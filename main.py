#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('''
		<!DOCTYPE html> 
<html>
	<head>
		<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1" />
		<title>DHS Events</title>
		<link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.css" />
		<script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
		<script src="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.js"></script>
	</head>
	<body>
		<div data-role="page"> 

			<div data-role="header" data-position="inline" data-theme="b"> 
			<a onClick="javascript: history.go(-1)" data-icon="back">Back</a>
				<h1>DHS Events</h1> 
			<a href="index.html" data-icon="home">Home</a>
			</div>
			
			<div data-role="content">   
			<ul data-role="listview" data-inset="true">
			<li><a href="cca.html">View events by CCA</a></li>
			<li><a href="overview.html" class="mainmenu">View events by date</a></li>  
			</ul>
			</div><!-- /content -->
		<div data-role="footer">
		<h6>&copy Samantha Ai</h6>
		</div>
        </div><!-- /page --> 
	</body>
</html>''')

class ccaHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('''<!DOCTYPE html> 
<html>
	<head>
		<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1" />
		<title>DHS Events</title>
		<link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.css" />
		<script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
		<script src="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.js"></script>
	</head>
	<body>
		<div data-role="page"> 

			<div data-role="header" data-position="inline"  data-theme="b"> 
			<a onClick="javascript: history.go(-1)" data-icon="back">Back</a>
				<h1>DHS Events</h1> 
			<a href="index.html"  data-icon="home">Home</a>
			</div>
			<div data-role="content">   
		<!-- show list of CCAs, click on CCA to find out events -->
		
		<div data-role="collapsible" data-collapsed="true">
		<h3>Clubs & Societies</h3>
		<ul data-role="listview" data-inset="true">
		<li><a href="art.html" class="ccalink">Art Club</a><br /></li>
		<li><a href="biz.html" class="ccalink">Biz! Club</a><br /></li>
		<li><a href="csc.html" class="ccalink">Community Service Club</a><br /></li>
		<li><a href="cul.html" class="ccalink">Culinary Club</a><br /></li>
		<li><a href="env.html" class="ccalink">Environmental Club</a><br /></li>
		<li><a href="isac.html" class="ccalink">International Strategic Affairs Council</a><br /></li>
		<li><a href="infocomm.html" class="ccalink">Infocomm Club</a><br /></li>
		<li><a href="lib.html" class="ccalink">Library Society</a><br /></li>
		<li><a href="malay.html" class="ccalink">Malay Cultural Club</a><br /></li>
		<li><a href="masscom.html" class="ccalink">Mass Communication Club</a><br /></li>
		<li><a href="medsoc.html" class="ccalink">Medical Society</a><br /></li>
		<li><a href="msc.html" class="ccalink">Mind Sports Club</a><br /></li>
		<li><a href="ms.html" class="ccalink">Music Society</a><br /></li>
		<li><a href="os.html" class="ccalink">Oratorical Society</a><br /></li>
		<li><a href="photog.html" class="ccalink">Photographic Society</a><br /></li>
		<li><a href="pub.html" class="ccalink">Publications</a><br /></li>
		<li><a href="robotics.html" class="ccalink">Robotics Club</a><br /></li>
		<li><a href="science.html" class="ccalink">Science Society</a><br /></li>
		<li><a href="sc.html" class="ccalink">Student Council</a><br /></li>
		<li><a href="techies.html" class="ccalink">Techies</a><br /></li>
		<li><a href="ugc.html" class="ccalink">Uniformed Group Council</a><br /></li>
		<li><a href="yjcc.html" class="ccalink">Yutaka Japanese Cultural Club</a><br /></li>
		</ul>
		</div>
		
		<div data-role="collapsible" data-collapsed="true">
		<h3>Performing Arts</h3>
		<ul data-role="listview" data-inset="true">
		<li><a href="bjopera.html" class="ccalink">Beijing Opera</a><br /></li>
		<li><a href="co.html" class="ccalink">Chinese Orchestra</a><br /></li>
		<li><a href="cs.html" class="ccalink">Chinese Society</a><br /></li>
		<li><a href="choir.html" class="ccalink">Choir</a><br /></li>
		<li><a href="dance.html" class="ccalink">Dance Society</a><br /></li>
		<li><a href="eds.html" class="ccalink">English Drama Society</a><br /></li>
		<li><a href="ge.html" class="ccalink">Guitar Ensemble</a><br /></li>
		<li><a href="guzheng.html" class="ccalink">Guzheng Ensemble</a><br /></li>
		<li><a href="se.html" class="ccalink">String Ensemble</a><br /></li>
		<li><a href="band.html" class="ccalink">Symphonic Band</a><br /></li>
		</ul>
		</div>

		<div data-role="collapsible" data-collapsed="true">
		<h3>Sports & Games</h3>
		<ul data-role="listview" data-inset="true">
		<li><a href="awc.html" class="ccalink">Air Weapons Club</a><br /></li>
		<li><a href="badminton.html" class="ccalink">Badminton</a><br /></li>
		<li><a href="basketball.html" class="ccalink">Basketball</a><br /></li>
		<li><a href="bowling.html" class="ccalink">Bowling</a><br /></li>
		<li><a href="golf.html" class="ccalink">Golf</a><br /></li>
		<li><a href="netball.html" class="ccalink">Netball</a><br /></li>
		<li><a href="odac.html" class="ccalink">Outdoor Activities Club</a><br /></li>
		<li><a href="sailing.html" class="ccalink">Sailing</a><br /></li>
		<li><a href="syfc.html" class="ccalink">Singapore Youth Flying Club</a><br /></li>
		<li><a href="soccer.html" class="ccalink">Soccer</a><br /></li>
		<li><a href="softball.html" class="ccalink">Softball</a><br /></li>
		<li><a href="tt.html" class="ccalink">Table Tennis</a><br /></li>
		<li><a href="taekwondo.html" class="ccalink">Taekwondo</a><br /></li>
		<li><a href="tennis.html" class="ccalink">Tennis</a><br /></li>
		<li><a href="rugby.html" class="ccalink">Touch Rugby</a><br /></li>
		<li><a href="tnf.html" class="ccalink">Track & Field</a><br /></li>
		<li><a href="volleyball.html" class="ccalink">Volleyball</a><br /></li>
		<li><a href="wushu.html" class="ccalink">Wushu</a><br /></li>
		</ul>
		</div>
		
		<div data-role="collapsible" data-collapsed="true">
		<h3>Uniformed Groups</h3>
		<ul data-role="listview" data-inset="true">
		<li><a href="gg.html" class="ccalink">Girl Guides</a><br /></li>
		<li><a href="npcc.html" class="ccalink">National Police Cadet Corps</a><br /></li>
		<li><a href="scouts.html" class="ccalink">Scouts</a><br /></li>
		<li><a href="sjab.html" class="ccalink">St. John Ambulance Brigade</a><br /></li>
		</ul>
		</div>

		</div><!-- /content -->
		
		<div data-role="footer">
		<h6>&copy Samantha Ai</h6>
		</div>
		

	</body>
</html>				
		''')
		
class overviewHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('''<!DOCTYPE html> 
<html>
	<head>
		<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1" />
		<title>DHS Events</title>
		<script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
		<script>
  //reset type=date inputs to text
  $( document ).bind( "mobileinit", function(){
    $.mobile.page.prototype.options.degradeInputs.date = true;
  });	
		</script>	
		<link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.css" />
		<link rel="stylesheet" href="jquery.ui.datepicker.mobile.css" /> 
		<script src="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.js"></script>
		<script src="jQuery.ui.datepicker.js"></script>
		<script src="jquery.ui.datepicker.mobile.js"></script>

	</head>
	<body>
		<div data-role="page"> 

			<div data-role="header" data-position="inline" data-theme="b"> 
			<a onClick="javascript: history.go(-1)" data-icon="back">Back</a>
				<h1>DHS Events</h1> 
			<a href="index.html" data-icon="home">Home</a>
			</div>
			
			<div data-role="content">   
			<form action="chosendate.html" method="get" accept-charset="utf-8"> 
			<div data-role="fieldcontain">
			<label for="date">Date (MM/DD/YYYY):</label>
			<input type="date" name="date" id="date" value=""  />	
<p><input type="submit" value="See Events"></p> 
			
			</div>
			</form>
			
			</div><!-- /content -->
			
			<div data-role="footer">
		<h6>&copy Samantha Ai</h6>
		</div>
		
        </div><!-- /page --> 
		
	</body>
</html>
	''')		

class eventdateHandler(webapp2.RequestHandler):
	def get(self):
		if self.request.get('date') == '05/12/2012':
			self.response.out.write('''<!DOCTYPE html> 
<html>
	<head>
		<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1" />
		<title>DHS Events</title>
		<script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
		<script>
  $( document ).bind( "mobileinit", function(){
    $.mobile.page.prototype.options.degradeInputs.date = true;
  });	
		</script>	
		<link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.css" />
		<script src="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.js"></script>
		<link rel="stylesheet" href="jquery.ui.datepicker.mobile.css" /> 
		<script src="jQuery.ui.datepicker.js"></script>
		<script src="jquery.ui.datepicker.mobile.js"></script>



	</head>
	<body>
		<div data-role="page"> 

	<div data-role="header" data-position="inline" data-theme="b"> 
			<a onClick="javascript: history.go(-1)" data-icon="back">Back</a>
				<h1>DHS Events - 05/12/2012</h1> 
			<a href="index.html" data-icon="home">Home</a>
			</div>

	<div data-role="content">	
		<p>Guitar Ensemble Concert<br />
		Timepiece III: Journey<br />
		7.30pm - 9.30pm<br />
		DHS Performing Arts Centre</p>		
	</div><!-- /content -->
	
	<div data-role="footer">
		<h6>&copy Samantha Ai</h6>
		</div>
</div><!-- /page -->


	</body>
</html>		
		''')
		else:
			self.response.out.write('''<!DOCTYPE html> 
<html>
	<head>
		<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1" />
		<title>DHS Events</title>
		<script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
		<script>
  //reset type=date inputs to text
  $( document ).bind( "mobileinit", function(){
    $.mobile.page.prototype.options.degradeInputs.date = true;
  });	
		</script>	
		<link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.css" />
		<script src="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.js"></script>
		<link rel="stylesheet" href="jquery.ui.datepicker.mobile.css" /> 
		<script src="jQuery.ui.datepicker.js"></script>
		<script src="jquery.ui.datepicker.mobile.js"></script>


	</head>
	<body>
		<div data-role="page"> 
	<div data-role="header" data-position="inline" data-theme="b"> 
			<a onClick="javascript: history.go(-1)" data-icon="back">Back</a>
				<h1>No Events</h1> 
			<a href="index.html" data-icon="home">Home</a>
			</div>

	<div data-role="content">	
		<p>No events</p>		
	</div><!-- /content -->
	
	<div data-role="footer">
		<h6>&copy Samantha Ai</h6>
		</div>
</div><!-- /page -->
	</body>
</html>		
		''')
		
class geHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('''<!DOCTYPE html> 
<html>
	<head>
		<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1" />
		<title>DHS Events</title>
		<script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
		<script>
  //reset type=date inputs to text
  $( document ).bind( "mobileinit", function(){
    $.mobile.page.prototype.options.degradeInputs.date = true;
  });	
		</script>	
		<link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.css" />
		<link rel="stylesheet" href="jquery.ui.datepicker.mobile.css" /> 
		<script src="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.js"></script>
		<script src="jQuery.ui.datepicker.js"></script>
		<script src="jquery.ui.datepicker.mobile.js"></script>

	</head>
	<body>
		<div data-role="page"> 

			<div data-role="header" data-position="inline" data-theme="b"> 
			<a onClick="javascript: history.go(-1)" data-icon="back">Back</a>
				<h1>Guitar Ensemble Events</h1> 
			<a href="index.html" data-icon="home">Home</a>
			</div>
			
				<div data-role="content">	
		<p>Guitar Ensemble Concert<br />
		12 May 2012<br />
		Timepiece III: Journey<br />
		7.30pm - 9.30pm<br />
		DHS Performing Arts Centre</p>		
	</div><!-- /content -->
		
        </div><!-- /page --> 
		
		<div data-role="footer">
		<h6>&copy Samantha Ai</h6>
		</div>
		
	</body>
</html>
	''')	
		
app = webapp2.WSGIApplication([('/', MainHandler), ('/index.html', MainHandler), ('/cca.html', ccaHandler), ('/overview.html', overviewHandler), 
								('/chosendate.html', eventdateHandler), ('/ge.html', geHandler)],
                              debug=True)


