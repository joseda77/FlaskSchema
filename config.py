import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    instance_relative_config = True


class Development(Config):
    # Configuración general
    DEBUG = True
    TESTING = False
    SECRET_KEY = '3yYq4rZ1nPjjD4xW9MK9uU5pi-Aj5BHU'


class Testing(Config):
    SECRET_KEY = '3yYq4rZ1nPjjD4xW9MK9uU5pi-Aj5BHU'
    TESTING = True
    DEBUG = True


# class Production(Config):
#    pass

config = {
    'development': Development,
    'testing': Testing,
    'default': Development
}
