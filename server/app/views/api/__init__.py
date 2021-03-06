"""
API endpoints
"""
import logging
import json
import webapp2


class JsonApiHandler(webapp2.RequestHandler):
    def render_response(self, data=None, additional_info=None, status_code=200):
        return_dict = {
            'data': data,
            'status': status_code,
        }
        if type(additional_info) == dict:
            return_dict.update(additional_info)
        # logging.info('Response sent to client was: {}'.format(json.dumps(return_dict)))
        self.response.out.write(json.dumps(return_dict))
