# coding: utf8

#中间件
MIDDLEWARES = [
    'rust.middlewares.check_point_middleware.CheckPointMiddleware', #必须在列表首位！！
    'rust.middlewares.user_login_middleware.UserLoginMiddleware',
    'rust.middlewares.user_middleware.UserMiddleware',
]

