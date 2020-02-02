# -*- coding: utf-8 -*-
import datetime
import jwt


class Security(object):

    @staticmethod
    def create_elsys_token(self):
        return {'x': 'x', 'y': 'y', 'datetime': str(datetime.datetime.now())}

    @staticmethod
    def encrypt_token(token):
        return jwt.encode(token, 'my-custom-seed', algorithm='HS256')

    @staticmethod
    def decrypt_token(token):
        try:
            return jwt.decode(token, 'my-custom-seed', algorithm='HS256')
        except Exception:
            return None
