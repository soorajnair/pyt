import urllib2
import base64
username = 'achenard'
password = '***'
password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, 'http://oscbamboo01:8085/', username, password)
auth_handler = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)
xmlparameters = '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><comment author="achenard"><content>A build result comment.</content></comment>'
theurl = 'http://oscbamboo01:8085/rest/api/latest/result/TONY-TONY-44/comment'
encodedstring = base64.encodestring(username+":"+password)[:-1]
auth = "Basic %s" % encodedstring
headers = {"Authorization": auth}
req = urllib2.Request(theurl, xmlparameters, headers)
req.add_header('Content-Type', 'application/xml; charset=utf-8')
req.add_header('Content-Length', len(xmlparameters))
handle = urllib2.urlopen(req)