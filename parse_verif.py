#!/usr/bin/env python

# Script

# read an XML file, get the data, and verify the data conforms to a certain format using regular expressions

# imports
import re
from xml.dom import minidom

# open and move XML code to xmldoc
xmldoc = minidom.parse('c:\Python27\Code\\xml_and_re\gggg.xml')
itemlist = xmldoc.getElementsByTagName('person')
print(len(itemlist))

i=0

# go through each item in the XML list
for i in range(len(itemlist)-1):

    # ---------------------------------------------------------
    # get each element from the XML
    # ---------------------------------------------------------

    name = itemlist[i].getElementsByTagName('name')[0].firstChild.nodeValue
    phone = itemlist[i].getElementsByTagName('phone')[0].firstChild.nodeValue
    notes = itemlist[i].getElementsByTagName('notes')[0].firstChild.nodeValue
    phys_traits = itemlist[i].getElementsByTagName('phys_traits')
    hair = phys_traits[0].getElementsByTagName('hair_color')[0].firstChild.nodeValue
    eyes = phys_traits[0].getElementsByTagName('eye_color')[0].firstChild.nodeValue
    height = phys_traits[0].getElementsByTagName('height')[0].firstChild.nodeValue

    print "name: ", name
    print "phone: ", phone
    print "notes: ", notes
    print "hair: ", hair
    print "eyes: ", eyes
    print "height: ", height

    # ---------------------------------------------------------
    # Verify each variable against a regular expression template
    # ---------------------------------------------------------

    #Verify phone number

    print "Verify phone number:"
    if re.match("\d{3}[-\.\s]\d{3}[-\.\s]\d{4}", phone):
        print "phone matches 1"
    elif re.match("\(\d{3}\)\s*\d{3}[-\.\s]\d{4}", phone):
        print "phone matches 2"
    elif re.match("\d{3}[-\.\s]\d{4}", phone):
        print "phone matches 3"
    elif re.match("^\s*(?:\d\s*){10}$", phone):
        print "phone matches 4"
    else:
        print "invalid phone number"


    #verify name

    print "Verify name:"
    if re.match(r"^[a-zA-Z]+ [a-zA-Z]+$", name):
        print "name matches 1"
    elif re.match(r"^[a-zA-Z]+$", name):
        print "name matches 2"
    else:
        print "invalid name"

    #verify height

    print "Verify height:"
    if re.match(r"^[2-7]'\s?[0-9]''$|^[2-7]'\s?1[0-1]''$|^[2-7]'$", height):
        print "height matches 1"
    else:
        print "invalid or ridiculous height"


    # verify hair

    if hair in ['brown' , 'black' , 'blonde' , 'red']:
        print "hair accepted"
    else:
        print "invalid hair"

    # verify eye color

    if eyes in ['brown','blue','green']:
        print "eyes accepted"
    else:
        print "invalid eyes"

    print " " # blank line
    pause = raw_input("Press enter to see next")