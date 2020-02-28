#!/usr/bin/env python3

# A simple script to accept input from an html form,
# parse the information, and do something - which in this case
# is to give user feedback with a simple html page.


#use a python cgi package
import cgi

#get the output of the form 

data = cgi.FieldStorage()

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name

v_name = data.getvalue('name')
colo = data.getvalue('color')


# send an html response.
print("""
<html>
<body>
<style>body[background-color: &s]<style>
<p>
Thanks, %s
</p>
</body>
</html>
""" % colo %v_name