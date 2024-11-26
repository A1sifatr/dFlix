import xbmcplugin
import xbmcgui
import xbmc
import sys

# Create a function to list items in the Kodi interface
def list_items():
    # Define the video URL (can be a direct stream URL or a file path)
    video_url = "http://172.16.50.14/DHAKA-FLIX-14/Hindi%20Movies/"
    
    # Create a list item (this is what the user will click on in Kodi)
    li = xbmcgui.ListItem("Sample Video", iconImage="icon.png", thumbnailImage="fanart.jpg")
    
    # Set the video URL as the playback URL
    li.setPath(video_url)
    
    # Add the item to the Kodi menu
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=video_url, listitem=li)
    
    # Optionally, you can add more items if needed

# Initialize the add-on handle (used by Kodi to handle the add-on)
addon_handle = int(sys.argv[1])

# List the video items
list_items()

# End the directory and tell Kodi to display the items
xbmcplugin.endOfDirectory(addon_handle)
