import web
from web.wsgiserver import CherryPyWSGIServer
from ClientCertCapableSSLAdapter import ClientCertCapableSSLAdapter

CherryPyWSGIServer.ssl_adapter = ClientCertCapableSSLAdapter(certificate = "ssl_certs/docs.crt",
                                                             private_key = "ssl_certs/docs.key",
                                                             certificate_chain = None,
                                                             client_CA = 'ssl_certs/docs.crt',
                                                             client_check = 'required',
                                                             check_host = False)

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
