import os
from dotenv import load_dotenv
from flask import Flask, redirect, request, session, render_template
from requests_oauthlib import OAuth2Session

load_dotenv()

app = Flask(__name__)
app.secret_key = 'a_secret_key'


CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

print(CLIENT_ID)
print(CLIENT_SECRET)
REDIRECT_URI = 'http://127.0.0.1:5000/callback'

# This scope will allow access to the user's playlists
SCOPE = 'playlist-read-private'

# Disable SSL requirement for OAuth2 for local testing only
# Never disable this in production
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

@app.route('/')
def home():
    pass

@app.route('/login')
def login():
    pass


# @app.route('/login')
# def login():
      #TODO: If token present AND valid: skip authorization
#     spotify = OAuth2Session(CLIENT_ID, scope=SCOPE, redirect_uri=REDIRECT_URI)
#     authorization_url, state = spotify.authorization_url('https://accounts.spotify.com/authorize')
#     session['oauth_state'] = state
#     return redirect(authorization_url)

# @app.route('/callback')
# def callback():
#     spotify = OAuth2Session(CLIENT_ID, state=session['oauth_state'], redirect_uri=REDIRECT_URI)
#     token, refresh_token = spotify.fetch_token('https://accounts.spotify.com/api/token',
#                                 client_secret=CLIENT_SECRET,
#                                 authorization_response=request.url)
#     session['oauth_token'] = token
#     session['oauth_refresh_token'] = refresh_token
#     return redirect('/playlists')

# @app.route('/playlists')
# def playlists():
#     # if !checkIfTokenValid():
#     #     refreshToken() # https://developer.spotify.com/documentation/web-api/tutorials/refreshing-tokens
#     spotify = OAuth2Session(CLIENT_ID, token=session['oauth_token'])
#     response = spotify.get('https://api.spotify.com/v1/me/playlists')
#     playlists = response.json()['items']
#     # TODO: Initiate a "cron job" to request playlist once per week
#     # initiatePlaylistCronJob(session['oauth_token'], session['oauth_refresh_token'])
#     return render_template('playlists.html', playlists=playlists)

def initiatePlaylistCronJob(token, refresh_token):
    for i in range(100):
        await one week
        requestPlaylist(token, refresh_token)
    pass


if __name__ == '__main__':
    app.run(debug=True)