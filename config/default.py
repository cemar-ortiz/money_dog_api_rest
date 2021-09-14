# Genera la tuya utilizando algun generador o método de generación
SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'

# Para propagar las excepciones y poder manejarlas a nivel aplicacion
PROPAGATE_EXCEPTIONS = True

# Database configuration (adaptar esto para PostgreSQL)
SQLALCHEMY_DATABASE_URI = 'sqlite:///films.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False

# Deshabilita las sugerencias de otros endpoints relacionados
# con alguno que no exista
ERROR_404_HELP = False
