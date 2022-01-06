import logging
logging.basicConfig(level=logging.INFO)
# 将日志打印到标准输出：为了方便检查错误，默认值为WARNING，则只显示大于等于WARNING级别的日志

import asyncio,os,json,time   #json:用于数据传输,减少代码量
from datetime import datetime #日期

from aiohttp import web  #构建http服务器

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})

async def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv=await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv
loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
