from sanic import Sanic
from infrastructure.configs.main import GlobalConfig
from infrastructure.database import init_db
from sanic_openapi import swagger_blueprint, openapi2_blueprint
# from modules.translation_request.main import translation_request_bp

from infrastructure.configs import ServerTypeEnum, get_cnf, GlobalConfig

from infrastructure.interceptors.exeption_interceptor import ExceptionInterceptor
from infrastructure.adapters.kafka.main import init_kafka

async def listener_before_server_start(*args, **kwargs):
    print("before_server_start")
    
async def listener_after_server_start(*args, **kwargs):
    print("after_server_start")
    
async def listener_before_server_stop(*args, **kwargs):    
    print("before_server_stop")
    
async def listener_after_server_stop(*args, **kwargs):
    print("after_server_stop")

def init_routes(app: Sanic) -> Sanic:
    from modules.translation_request.main import translation_request_bp

    app.blueprint(swagger_blueprint)
    app.blueprint(translation_request_bp)
    
    return app

async def init_app():

    config: GlobalConfig = get_cnf()
    
    app: Sanic = Sanic(
        config.APP_CONFIG.APP_NAME, 
        strict_slashes=config.APP_CONFIG.STRICT_SLASHES
    )

    app.config.update_config(config.dict())

    init_db(config.CASSANDRA_DATABASE)

    await init_kafka(config)

    app = init_routes(app)

    app.error_handler = ExceptionInterceptor()

    if config.SERVER_TYPE == ServerTypeEnum.uvicorn.value:

        app.register_listener(listener_after_server_start, 'after_server_start')
        app.register_listener(listener_before_server_stop, 'before_server_stop')

    elif config.SERVER_TYPE == ServerTypeEnum.built_in.value:

        app.register_listener(listener_before_server_start, 'before_server_start')
        app.register_listener(listener_after_server_start, 'after_server_start')
        app.register_listener(listener_before_server_stop, 'before_server_stop')
        app.register_listener(listener_after_server_stop, 'after_server_stop')
    
    return app
