import soco
import configparser



# Andy's Amazing Midi Sonos Controller

# command line options
# -setup
# -play

# Setup
#   Discover Zones
#   Let users pick one or more zones to play the music on.
#   Save zone to config file
# Instruct users to pick a song or a playlist
# If a playlist, choose random or start at the top.
# Press a button on midi keyboard to perform action
# Ask for knob or slider for volume
# Ask for a button for pause/start

for zone in soco.discover():
    print(zone.player_name)
    print(zone.get_current_transport_info())
    zone.play()


    
