import soco
import configparser
import time



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


def loadConfig():
    # load the configuration file from the INI
    print("Loading config")
    
def saveConfig():
    """ save the configuration file from the INI."""
    print("Saving config")


def pickZones():
    """ Run Sonos Discovery, show all zones, let user's pick which ones they want to play to """
    
    playzones = []

    # need to try to load zones from config files

    # need to give option to change.

    # find all zones on the network
    for zone in soco.discover():
        # list each zone, ask if they want to use it
        if input("Add " + zone.player_name + " Y/N:").upper() == "Y":
            playzones.append(zone)
            print("added")
            
    # show them which ones they choose
    print("All playzones----")

    for zone in playzones:
        print(zone.player_name)

    print("-----")
    
    return playzones


def main():
    """ SonosMidi main loop """
    
    # here we go.  The real shebang.

    # figure out what zones are available
    zones = pickZones()
    print(zones)

    # if no zones selected, or found get out
    if len(zones) == 0:
        print("No zones selected.  Exiting.")
        exit()

    print("playing")
    for zone in zones:
        zone.play()

    time.sleep(3)

    print("stopping")
    for zone in zones:
        zone.pause()
    
    
    
    # pick a button for play/pause

    # playpause = input("Press a key for play/pause")

    

    # pick a button for louder/softer

    # show what's playing,  save it to a button
    
    

if __name__== "__main__":
    main()

