from http import server
from os import listdir,path,makedirs,chdir,remove
from string import Template
from distutils.dir_util import copy_tree
import shutil
import sys
import socket,socketserver
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', 0))
local_ip_address = s.getsockname()[0]
IP = s.getsockname()[0] 
PORT = 80

print("Running FBI server 0.1")

public = "public"
ciapath = "."

if len(sys.argv) > 2:
	PORT = int(sys.argv[2])
elif len(sys.argv) > 1:
	ciapath = sys.argv[1]
	if path.exists(ciapath):
		print("* CIA path:\t",ciapath)
	else:
		print("* FATAL ERROR:\t","No such path:\t",ciapath);		
		sys.exit()
else:
	print("* CIA path:\t","Current directory")

ciafolder = ciapath[ciapath.rfind("/")+1:]
print("* folder name:\t",ciafolder)


def findcias(ciapath):
	allfiles = listdir(ciapath)
	ciafiles = {}

	for name in allfiles:
		if name.endswith(".cia"):
			ciafiles[name] = name

	return ciafiles

ciafiles = findcias(ciapath)

while len(ciafiles) == 0:
	print("Warning: No CIA files found! Press any key to quit..")
	input("[Oh, okay..]");
	sys.exit()

print("* CIA's found:\t",len(ciafiles));

makedirs(public)


jsonfiles = json.dumps(ciafiles)
jsdata = Template("""
	CIA=$ciafiles;
	IP='$ip';
	PORT=$port;
	
""").substitute(ciafiles=jsonfiles,ip=IP,port=PORT);

if path.exists(public):
	shutil.rmtree(public)
	print("* removed old public folder.")

copy_tree('preset',public)

datafile = open(public+"/data.js",'w')
datafile.write(jsdata)
datafile.close()

filelist = listdir(public);
copy_tree('public',ciapath)

print("* copied public files to:\t",ciapath)
shutil.rmtree(public)
chdir(ciapath)

print("* starting server on ",IP,":",PORT)
Handler = server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("* QR Codes served at: http://"+IP+":"+str(PORT)+"/index.html")

try:
	httpd.serve_forever()
except KeyboardInterrupt:
	pass
print("\n* Server stopped")
httpd.socket.close()
for filename in filelist:
	remove(ciapath+"/"+filename)
print("* removed public files from:\t",ciapath)
print("Thank you for using FBIServer.")