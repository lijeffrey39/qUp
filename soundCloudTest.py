import soundcloud
from selenium import webdriver
import os


CLIENT_ID = 'a3dd183a357fcff9a6943c0d65664087'

temp = 'b45b1aa10f1ac2941910a7f0d10f8e28'
CLIENT_SECRET = '7e10d33e967ad42574124977cf7fa4b7'
# MAGIC_CLIENT_ID = 'b45b1aa10f1ac2941910a7f0d10f8e28'
REDIRECT_URL = 'google.com'

# AGGRESSIVE_CLIENT_ID = 'OmTFHKYSMLFqnu2HHucmclAptedxWXkq'
# APP_VERSION = '1481046241'


# PROJECT_ROOT = os.getcwd()
# DRIVER_BIN = os.path.join(PROJECT_ROOT, 'chromedriver')
# driver = webdriver.Chrome(executable_path = DRIVER_BIN)

page_size = 10
client = soundcloud.Client(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token = '1-120878-192120258-6ae03ce627ab6')
print(dir(client))
print(client.authorize_url)


# AUTH_URL = client.authorize_url()
# driver.get(AUTH_URL) ## open Firefox to access Soundcloud
# # code = raw_input("WAITING FOR ACCESS... type ENTER")

# # code = driver.current_url.replace(REDIRECT_URL+'/?code=','')[:-1]
# # ACCESS_TOKEN = client.exchange_token(code).access_token

# USER = client.get('/me').permalink

# # FILE = "SOUNDCLOUD.%s.access_token" % USER
# # FILE_W = open(FILE,'w')
# # FILE_W.write(ACCESS_TOKEN)
# # FILE_W.close()
# driver.quit()

# current_user = client.get('/me/tracks')


# user = client.get('/users/sir-isaac-nooton')
# userId = user.id
# print(userId)

# tracks = client.get('/users/' + str(userId) + '/tracks')


# tracks = client.get('/tracks', q='migos', limit=page_size)

# print(tracks)

# for t in tracks:

# 	stream_url = client.get(t.stream_url, allow_redirects=False)
# 	# print the tracks stream URL
# 	print(t.title)


# tracks = client.get('/users', q='migos', limit=page_size)

# print(tracks)

# tracks = client.get('/tracks', order='hotness', limit=page_size, q='migos')
# for track in tracks:
#     print(track.title)



users = client.get('/me/playlists', order='hotness', limit=page_size)
for user in users:
	print(user.permalink_url)
	# stream_url = client.get(t.stream_url, allow_redirects=False)
	# print(t.title)
	# print(stream_url.title)

# print(tracks)

# # get the tracks streaming URL
# stream_url = client.get(tracks[0].stream_url, allow_redirects=False)

# # print the tracks stream URL
# print(stream_url.location)


# # list tracks in playlist
# for track in playlist.tracks:
# 	# print(track)
# 	print(track['waveform_url'])