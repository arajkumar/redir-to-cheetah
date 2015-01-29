import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.redirect('http://cheetah.in.nds.com:4321?'+self.request.query_string)
        #self.response.write(self.request.query_string)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
