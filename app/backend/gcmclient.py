from flask_restful import Resource

import requests
from flask import request
from actions import access_token_matches
from BeautifulSoup import BeautifulSoup
from actions import sendNotification

from raven.handlers.logging import SentryHandler
from raven import Client
from raven.conf import setup_logging
import logging

client = Client('https://c08e468ddcf148d3bed9966345bdb7f4:5c4227f8d4fd4b1e94d01ebe03e29883@app.getsentry.com/23855')
handler = SentryHandler(client)
setup_logging(handler)
logger = logging.getLogger(__name__)

class GCMClient(Resource):
    def post(self):
        request_params = request.get_json()
        try:
            email_id = request_params['email']
            access_token = request_params['access_token']

            gcm_id= request_params['gcm_id']
            message= request_params['message']
        except KeyError as ke:
            logger.error(ke)
        except Exception as e:
            logger.error(e)

        if email_id == None or access_token ==None or gcm_id == None or message == None:
            return {'status':400,'message':'Bad Request'},400
        elif access_token_matches(email_id,access_token) == False:
            return {'status':401,'message':'Access Unauthorized'},401

        logger.warning("GCM push gcm_id= %s, message= %s",gcm_id,message)

        response={'status':200,'message':sendNotification(gcm_id,message)}
        return response