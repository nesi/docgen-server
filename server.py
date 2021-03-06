# server.py
#
# A web server for receiving uploads of software module lists from NeSI
# clusters. Uses web.py.
#
# Written by Benjamin Roberts, 2015

import os
import sys
import web
from web.wsgiserver import CherryPyWSGIServer
from ClientCertCapableSSLAdapter import ClientCertCapableSSLAdapter

basedir = os.path.dirname(os.path.realpath(__file__))

CherryPyWSGIServer.ssl_adapter = ClientCertCapableSSLAdapter(certificate = os.path.join(basedir,"ssl_certs","docs.crt"),
                                                             private_key = os.path.join(basedir,"ssl_certs","docs.key"),
                                                             certificate_chain = None,
                                                             client_CA = os.path.join(basedir,"ssl_certs","docs.crt"),
                                                             client_check = 'required',
                                                             check_host = False)

if (os.geteuid() == 0):
    logdir = os.path.join(os.sep, "var", "log")
else:
    logdir = os.path.expanduser("~")
logfile = os.path.join(logdir, "docgen-server.log")
logfilehandle = open(logfile, 'a', 0)
sys.stdout = logfilehandle
sys.stderr = logfilehandle

templatedir = os.path.join(basedir,"templates")
render = web.template.render(templatedir)
urls = (
    '/', 'index',
    '/(pan|fitzroy|beatrice|kerr|foster|popper)', 'upload'
)

class index:
    def GET(self):
        return render.index()


class upload:
    def GET(self, name):
        return render.upload()

    def POST(self, name):
        x = web.input(myfile={})
        filedir = os.path.join(os.sep,"var","www","module-uploads") # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            foutname = name + '.txt'
            fout = open(os.path.join(filedir,foutname),'w') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        raise web.seeother("/upload")


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
