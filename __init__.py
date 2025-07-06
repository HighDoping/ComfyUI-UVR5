WEB_DIRECTORY = "./web"
from .nodes import (
    UVR5,
    AudioPathtoString,
    LoadAudioPath,
    LoadNativeAudio,
    PreViewAudio,
    StringToAudioPath,
)

# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "UVR5_Node": UVR5,
    "LoadAudioPath": LoadAudioPath,
    "PreViewAudio": PreViewAudio,
    "LoadNativeAudio": LoadNativeAudio,
    "AudioPathtoString": AudioPathtoString,
    "StringToAudioPath": StringToAudioPath,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "UVR5_Node": "UVR5 Node",
    "LoadAudioPath": "LoadAudioPath",
    "PreViewAudio": "PreView Audio",
    "LoadNativeAudio": "Load Native Audio",
    "AudioPathtoString": "Audio Path to String",
    "StringToAudioPath": "String to Audio Path",
}
