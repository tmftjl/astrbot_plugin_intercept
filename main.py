from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("helloworld", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    
    # 注册消息触发器。无论用户发什么消息，都会触发这个插件。
    @filter.message()
    async def handle_message(self, event: AstrMessageEvent):
        """处理所有消息，无论内容如何都回空消息"""
        # 无论用户发送什么消息，都不会回复任何内容。
        logger.info("Received message: " + event.message_str)  # 打印收到的消息（仅日志记录）
        
        # 通过 yield 返回空消息，这样用户的请求就不会收到任何回应。
        yield event.plain_result("")  # 空消息

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
