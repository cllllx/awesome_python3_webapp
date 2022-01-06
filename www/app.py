import logging

logging.basicConfig(level=logging.INFO)
# 将日志打印到标准输出：为了方便检查错误，默认值为WARNING，则只显示大于等于WARNING级别的日志

import asyncio, os, json, time  # json:用于数据传输,减少代码量
from datetime import datetime  # 日期

from aiohttp import web  # 构建http服务器


# 处理URL:传入的request是aiohttp.web.request的实例，返回response实例
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type': 'text/html'})


# 创建web服务器实例
'''原始是用@asyncio.coroutine;yield from
   python3.5以后加入了async io/await关键字
   用法为 async def
   send=await '''

'''定义init函数，标记为协程，
   loop:协程参数
   app:web服务器实例，服务器用于处理url,HTTP协议
'''


async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    # 将URL注册进route,使URL与index处理函数绑定，因此当浏览器输入url时返回相应处理函数内容
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    # 启动监听服务，参数传入监听的IP，端口，http协议簇
    logging.info("server started at http://127.0.0.1:9000...")
    return srv
    # 返回监听服务


loop = asyncio.get_event_loop()
# 创建一个事件循环
# 创建事件循环的目的是因为协程对象开始运行需要在一个已经运作的协程中。
loop.run_until_complete(init(loop))
# 是一个阻塞调用，将协程注册到事件循环，并启动事件循环，直到返回结果。
# 实际就是将传入的协程对象，用ensure_future函数包装成一个future
loop.run_forever()
# 即一直运行协程，直到调用stop()函数
