#########################################################
# CIS 117 Python Programming: Lab 5                     #
#                                                       #
# URL, HTML, Decoding, Lists                            #
#                                                       #
#########################################################

from urllib.request import urlopen

response = urlopen("http://www.nasonline.org")
html = response.read()
html = html.decode()

topics = ['research', 'climate', 'evolution', 'cultural', 'leadership', 'policy']
count1 = html.count(topics[0])
count2 = html.count(topics[1])
count3 = html.count(topics[2])
count4 = html.count(topics[3])
count5 = html.count(topics[4])
count6 = html.count(topics[5])

print ("{} appears {} times".format(topics[0], count1))
print ("{} appears {} times".format(topics[1], count2))
print ("{} appears {} times".format(topics[2], count3))
print ("{} appears {} times".format(topics[3], count4))
print ("{} appears {} times".format(topics[4], count5))
print ("{} appears {} times".format(topics[5], count6))

#####
#research appears 3 times
#climate appears 8 times
#evolution appears 4 times
#cultural appears 4 times
#leadership appears 2 times
#policy appears 4 times
#####