from load import app, application, translation_server, parsed_args

application
app
translation_server.start(parsed_args.config)
print("started model server")

if __name__ == '__main__':
    print("started model server")
    app.run()
