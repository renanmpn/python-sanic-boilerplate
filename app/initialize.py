import os

from sanic import Sanic
from gino.ext.sanic import Gino

from app import config as config_module
from app import database, api

config = config_module.get_config()

app = Sanic()
app.config.from_object(config)

database.AppRepository.db = Gino(app=app)

api.create_api(app)


for handler, (rule, router) in app.router.routes_names.items():
    print(rule)

def run():
    """
    Run the Sanic app in a development environment
    """
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
