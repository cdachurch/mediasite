"""
Oauth APIs
"""
import logging
import urllib

import webapp2

from app.domain.mediasite_jwts import create_jwt_from_user_data
from app.models.user import User

from thecitysdk import TheCitySDK
from settings import THE_CITY_LOGIN_REDIRECT_URI, THE_CITY_APP_ID, THE_CITY_OAUTH_CALLBACK_URI


class OauthLoginHandler(webapp2.RequestHandler):
    def get(self):
        next_url = self.request.GET.get('nextUrl', '')  # Pass along where they were trying to go
        self.redirect(THE_CITY_LOGIN_REDIRECT_URI.format(THE_CITY_APP_ID,
                                                         urllib.quote(THE_CITY_OAUTH_CALLBACK_URI, safe=''),
                                                         urllib.quote(next_url)))


class OauthRedirectCallbackHandler(webapp2.RequestHandler):
    def get(self):
        code = self.request.GET.get('code')

        if code:
            user_info = TheCitySDK.post_for_user_token(code)
            sdk = TheCitySDK(user_info.get('access_token'))
            user_permissions = sdk.get_user_permissions()
            if 'error_code' not in user_permissions:
                if sdk.user_is_in_worship_arts(user_permissions):
                    logging.info('This user can join our site')
                    user_info_dict = sdk.get_basic_user_info()
                    user_info_dict['jwt'] = create_jwt_from_user_data(user_permissions, user_info_dict)
                    User.put_from_city_dict(user_info_dict)

                    redirect_to = self.request.GET.get('state', '/songs')
                    self.redirect('/login?success=true&userId={}&nextUrl={}'.format(user_info_dict['id'], redirect_to))
                else:
                    logging.info('This user needs to be added to a Worship Arts group on The City')
                    # TODO: Redirect to a different landing page explaining the purpose of this site and who to contact.
                    self.redirect('/')
            else:
                self.redirect('/login')
