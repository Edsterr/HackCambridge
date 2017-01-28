from klein import run, route

@route('/')
def home(request):

    print(request.content.read())
    return 'Hello, world!'

run("127.0.0.1", 8136)
