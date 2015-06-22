import web

from web.wsgiserver import CherryPyWSGIServer

CherryPyWSGIServer.ssl_certificate = "/home/brob695/docgen-server/ssl_certs/docs.crt"
CherryPyWSGIServer.ssl_private_key = "/home/brob695/docgen-server/ssl_certs/docs.key"

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
