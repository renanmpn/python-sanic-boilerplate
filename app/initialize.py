import os
import datetime

from sanic import Sanic
from gino.ext.sanic import Gino

from app import config as config_module
from app import database, api
from app.domain import security_domain


config = config_module.get_config()

app = Sanic()
app.config.from_object(config)

database.AppRepository.db = Gino(app=app)

api.create_api(app)


@app.middleware('request')
async def print_on_request(request):
    print(request)
    token = request.cookies.get('myToken')
    decrypted_token = security_domain.Security.decrypt_token(token)

    if decrypted_token is not None:
        decrypted_token['datetime'] = str(datetime.datetime.now())
        setattr(request, 'authenticated', True)
    setattr(request, 'user', decrypted_token)


def run():
    """
    Run the Sanic app in a development environment
    """
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
