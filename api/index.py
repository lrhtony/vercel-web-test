from sanic import Sanic
from sanic.response import redirect

app = Sanic('vercel-sanic-test')


@app.route('/')
async def index(request):
    return redirect('https://vercel.com/')

if __name__ == '__main__':
    app.run(auto_reload=True, port=8000)
