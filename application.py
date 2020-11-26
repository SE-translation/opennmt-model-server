from load import app, application, translation_server

application
app



if __name__ == '__main__':
    #starting model server
    translation_server.start("available_models/conf.json")
    print("started model server")
    app.run()
