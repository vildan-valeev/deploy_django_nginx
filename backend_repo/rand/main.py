from aiohttp import web
import random

app = web.Application()
routes = web.RouteTableDef()


@routes.get('/rand/')
async def handle(request: web.Request) -> web.Response:
    """Получаем апдейты"""
    r = random.randint(100, 200)
    text = f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Title</title></head><body><h1>{r}</h1' \
           f'></body></html>'
    # text = f'<h1>{r}</h1>'
    return web.Response(status=200, text=text,
                        content_type='text/html', )  # status=200


@routes.get('/tik/')
async def handle(request: web.Request) -> web.Response:
    """Получаем апдейты"""
    return web.Response(status=200, text=f'tik',
                        )  # status=200


app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, port=6000)
