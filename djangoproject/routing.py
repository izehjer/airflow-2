from channels.auth import AuthMiddleware, AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter
from chat import routing as d 
application =  ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            d.websocket_urlpatterns
        )
    )
})