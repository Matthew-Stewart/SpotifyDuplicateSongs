from apiInfo import *
import sys
import spotipy
import spotipy.util as util
import re
from collections import Counter
from collections import defaultdict
from pprint import pprint

remixes = False

def split_title(str):
   if remixes:
      return str.split(' - ')[0].split(' (')[0]
   else:
      return str

scope = 'user-library-read'

if len(sys.argv) > 2 and len(sys.argv) < 5:
   user = sys.argv[1]
   playlist_id = sys.argv[2]
   if len(sys.argv) == 4:
      if (sys.argv[3] == '-r'):
         remixes = True
      else:
         print "Invalid option: %s" % (sys.argv[3],)
         sys.exit()
else:
   print "Usage: %s user playlist [-r]" % (sys.argv[0],)
   sys.exit()

token = util.prompt_for_user_token(username, scope, Client_ID, Client_Secret, Redirect_URI)

if token:
   sp = spotipy.Spotify(auth=token)
   next = ""
   offset = 0
   all_artists_songs = defaultdict(set)
   duplicates = set()
   while next is not None:
      results = sp.user_playlist_tracks(user, playlist_id, "items(track(name,artists(name))),limit,offset,next", 100, offset)
      next = results['next']
      offset = results['offset'] + results['limit']
      for item in results['items']:
         artists = set()
         track = item['track']
         track_title = split_title(track['name'])
         artists_names = [x['name'] for x in track['artists']]
         artists_str = ", ".join(artists_names)
         for artist in artists_names:
            for track_tuple in all_artists_songs[artist]:
               if split_title(track_tuple[1]) == track_title:
                  duplicates.add((artists_str, track['name']))
                  duplicates.add(track_tuple)
            all_artists_songs[artist].add((artists_str, track['name']))
   if len(duplicates) > 0:
      duplicates_sorted = sorted(duplicates)
      width = max(len(x[0]) for x in duplicates_sorted)
      print("Artist".ljust(width) + "  Track")
      print("------".ljust(width) + "  -----")
      for a in duplicates_sorted:
         print "%s  %s" % (a[0].ljust(width), a[1])
else:
   print "Can't get token for", username

