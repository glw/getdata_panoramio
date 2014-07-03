import os, urllib, urlparse, json, pprint
#from simplejson.compat import StringIO

pp = pprint.PrettyPrinter(indent=4)

url = 'http://www.panoramio.com/map/get_panoramas.php?set=public&from=0&to=100&minx=-88.945&miny=40.745&maxx=-86.942&maxy=42.747&size=medium&mapfilter=false'

c = urllib.urlopen(url)

j = json.loads(c.read())

target = open (filename, 'w')

target.write(str(j))
#If you can get StringIO to import from simplejson.compat this would prettify the output
#Have submitted a question on SO http://stackoverflow.com/questions/24520389/pip-installation-of-simplejson-did-not-come-with-compat-py
#target.write(simplejson.dumps(simplejson.loads(jstr), indent=4, sort_keys=True))

target.close()
