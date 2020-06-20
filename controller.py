import web
import json
from Model import RegisterModel

web.config.debug = False

urls = (
    "/", "home",
    "/register", "register",
    "/login", "login",
    "/logout", "logout",
    "/postregister", "postregister",
    "/postlogin", "postlogin",
    "/article-(.+)", "article"

)
#a tuple / connects to home class
#/register connects to register class
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={"username":None})
session_data = session._initializer
render = web.template.render("View/Templates", base="MainLayout", globals={"session":session_data, "current_user":session_data["username"]})
class home:
    def GET(self):
        return render.Home()

class register:
    def GET(self):
        return render.Register()
class login:
    def GET(self):
        #finds Login.html
        return render.Login()
class article:
    def GET(self, name):
        print("PARAM IS ", name)
        rm = RegisterModel.RegisterModel()
        data = rm.findPost(name)
        if data:
            return render.Article(data["title"], data["content"])
        else:
            return render.Article("404 NOT FOUND", "We could not find what you're looking for.")

class logout:
    def GET(self):
        #deletes the session
        try:
            session_data["username"] = None
            session["username"] = None
            session.kill()
            return "OK"
        except:
            return "NOK"



class postregister:
    def POST(self):
        data = web.input()
        rm = RegisterModel.RegisterModel()
        try:
            rm.insertUser(data.username, data.password)
            result = "OK"
        except:
            result = "NOK"
        return result

class postlogin:
    def POST(self):
        data = web.input()
        print("LOGIN DATA", data)
        rm = RegisterModel.RegisterModel()

        result = rm.login(data.username, data.password)
        if result == 1:
            session_data["username"] = data.username
            print("SESSION DATA", session_data)
            return "OK"
        else:
            return "NOK"

if __name__ == "__main__":
    app.run()