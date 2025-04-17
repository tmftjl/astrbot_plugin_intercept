from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.provider import ProviderRequest
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import re

@register("intercept", "dggb", "拦截特定消息不触发llm", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    
    @filter.on_llm_request()
    async def my_custom_hook_1(self, event: AstrMessageEvent, req: ProviderRequest): # 请注意有三个参数
        message = event.message_str.strip()  # 获取并去除多余空格
        logger.info(f"{message}")
        # 使用正则表达式检查消息是否以 "秧秧ww"、"秧秧#" 或 "秧秧/" 开头
        if re.match(r"^(ww|#|/|gs)", message):
            logger.info(f"有前缀: {message}")
            event.stop_event()  # 阻止事件继续传播
        else:
            logger.info(f"无前缀: {message}")

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
