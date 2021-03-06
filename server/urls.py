""" URLs for the app """
from webapp2 import Route


ROUTES = [
    # Stat endpoints
    Route('/api/v1/mediasiteStats/printOuts/', handler='app.views.api.v1.mediasite_stats.SongPrintOutsHandler'),
    Route('/api/v1/mediasiteStats/songCount/', handler='app.views.api.v1.mediasite_stats.SongCountHandler'),
    Route('/api/v1/mediasiteStats/userCount/', handler='app.views.api.v1.mediasite_stats.UserCountHandler'),

    Route('/api/v1/songs/get/', handler='app.views.api.v1.songs.SongsApiHandler'),
    Route('/api/v1/song/', handler='app.views.api.v1.songs.SongApiHandler'),
    Route('/api/v1/song/<song_id>', handler='app.views.api.v1.songs.SongApiHandler'),
    Route('/api/v1/song/<song_id>/track/', handler='app.views.api.v1.songs.SongSheetGenerationApiHandler'),
    Route('/api/v1/user/login/', handler='app.views.api.v1.user.LoginHandler'),
    Route('/api/v1/user/get/<user_id:\d+>', handler='app.views.api.v1.user.GetUserInfoHandler'),
    Route('/api/v1/cityoauth/callback/', handler='app.views.api.v1.oauth.OauthRedirectCallbackHandler'),
    Route('/api/v1/cityoauth/login/', handler='app.views.api.v1.oauth.OauthLoginHandler'),
    Route('/<:.*>', handler='app.views.main.MainView'),  # Enables React Router to do it's thing with urls.
]
