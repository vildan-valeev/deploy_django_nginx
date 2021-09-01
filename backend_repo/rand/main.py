from aiohttp import web
import random

app = web.Application()
routes = web.RouteTableDef()


@routes.get('/rand/')
async def handle(request: web.Request) -> web.Response:
    """Получаем апдейты"""
    r_int = random.randint(100, 200)

    return web.Response(status=200, text=f'<h1>{r_int}</h1>',
                        content_type='text/html')  # status=200


@routes.get('/tik/')
async def handle(request: web.Request) -> web.Response:
    """Получаем апдейты"""

    return web.Response(status=200, text=f'tik',
                        )  # status=200


app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, port=6000)
