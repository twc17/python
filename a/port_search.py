#!/usr/bin/python3

"""
Title: port_search.py
Language: python3
Author: Troy Caro <twc17@pitt.edu>
Purpose: Search Cisco Catalyst series switches on PittNET by port description
"""

from helper import *

# Start
print("Content-type:text/html\r\n\r\n")       

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get port address from html form
port = form.getvalue('port_address')
usr = form.getvalue('user_name')
passwd = form.getvalue('password')

print("""
<html>

<head><title>Port Lookup Tool</title></head>

<body>
""")
print("<h1>Results for <b>" + form.getvalue('port_address') + "</b></h1>" )

# Check to see if the port maps to a switch before going any further
# port_address() is set to exit if it can't find the switch
hst, cmd = port_address(port)
output = execute(hst, usr, passwd, cmd)

if (output == ""):
    print("<p> I found the switch, but not the port :/ </p>")
    # Haven't quite figured out the best way to handle this yet
    print("<p> If the device is connected, you can try searching by MAC address <a href='mac_search.html?port_address='" + port + "'>here</a>. </p>")
    sys.exit(1)

print("<p>" + output + "</p>")
print("""
</body>
</html>
""")
