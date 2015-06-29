import web
from web.wsgiserver import CherryPyWSGIServer
from ClientCertCapableSSLAdapter import ClientCertCapableSSLAdapter

CherryPyWSGIServer.ssl_adapter = ClientCertCapableSSLAdapter(certificate = "ssl_certs/docs.crt",
                                                             private_key = "ssl_certs/docs.key",
                                                             certificate_chain = None,
                                                             client_CA = 'ssl_certs/docs.crt',
                                                             client_check = 'required',
                                                             check_host = False)

render = web.template.render('templates/')
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
        filedir = '/var/www/module-uploads' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            fout = open(filedir +'/'+ name + '.txt','w') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        raise web.seeother('/upload')


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
