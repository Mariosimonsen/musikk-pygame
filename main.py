from pygame import mixer 


class AudioPlayer:
    def __init__(self):
        self.mixer = mixer
        self.music = mixer.music
        self.mixer.init()

    def load(self, file):
        self.music.load(file)

   
    def play(self, loops=0, start=0.0, fade_ms=0):
        """
        :param loops: loops is an optional integer argument, which is 0 
            by default, which indicates how many times to repeat 
            the music. The music repeats indefinitely if this 
            argument is set to -1. 

        :param start: start is an optional float argument, which is 0.0 
            by default, which denotes the position in time from which 
            the music starts playing. The starting position depends on 
            the format of the music played. MP3 and OGG use the position
            as time in seconds. For MP3 files the start time position 
            selected may not be accurate as things like variable bit 
            rate encoding and ID3 tags can throw off the timing 
            calculations. For MOD music it is the pattern order number. 
            Passing a start position will raise a NotImplementedError
            if the start position cannot be set.

        :param fade_ms: fade_ms is an optional integer argument, which 
            is 0 by default, which denotes the period of time 
            (in milliseconds) over which the music will fade up from 
            volume level 0.0 to full volume (or the volume level 
            previously set by set_volume()). The sample may end before 
            the fade-in is complete. If the music is already streaming 
            fade_ms is ignored.

        :return: None
        """
        self.music.play()

    def volume(self, value):
        """
        Set the volume of the music playback.

        :param value: The volume argument is a float between 0.0 and 
            1.0 that sets the volume level. When new music is loaded 
            the volume is reset to full volume. If volume is a negative 
            value it will be ignored and the volume will remain set at 
            the current level. If the volume argument is greater than 
            1.0, the volume will be set to 1.0.
        
        :return: None
        """
        self.music.set_volume(value)

    def print_volume(self):
        """
        get the music volume

        Returns the current volume for the mixer. The value will be between 0.0 and 1.0.

        :return: None
        """
        return self.music.get_volume()
    
    def quit(self):
        """
        uninitialize the mixer

        This will uninitialize pygame.mixerpygame module for loading and
        playing sounds. All playback will stop and any loaded Sound 
        objects may not be compatible with the mixer if it is 
        reinitialized later.

        :return: None

        """
        self.mixer.quit()
    
    def unload(self):
        """
        Unload the currently loaded music to free up resources

        This closes resources like files for any music that may be 
        loaded

        New in pygame 2.0.0.

        :return: None
        """
        self.music.unload()
    
    def rewind(self):
        """
        restart music

        Resets playback of the current music to the beginning. 
        If pause() has previously been used to pause the music, the 
        music will remain paused.

        Note: rewind() supports a limited number of file types and 
        notably WAV files are NOT supported. For unsupported file types 
        use play() which will restart the music that's already playing 
        (note that this will start the music playing again even if 
        previously paused).

        :return:
        """
        self.music.rewind()
    
    def stop(self):
        """
        
        stop the music playback
        :return: None
        """
        self.music.stop()
    
    def pause(self):
        """
        
        temporarily stop music playback
        :return: None
        """
        self.music.pause()
    
    def unpause(self):
        """
        This will resume the playback of a music stream after it has 
        been paused.

        :return: None
        """
        self.music.unpause()

    def fadeout(self, time: int):
        """
        Fade out and stop the currently playing music.

        :param time: time argument denotes the integer milliseconds for 
            which the fading effect is generated.
        
        Note, that this function blocks until the music has faded out. 
        Calls to fadeout() and set_volume() will have no effect during 
        this time. If an event was set using set_endevent() it will be 
        called after the music has faded.

        :return: None

        """
        self.music.fadeout(time)
    
    def get_busy(self):
        """
        Check if the music stream is playing

        Returns True when the music stream is actively playing. When the
        music is idle this returns False. In pygame 2.0.1 and above this
        function returns False when the music is paused. In pygame 1 it 
        returns True when the music is paused.

        Changed in pygame 2.0.1: Returns False when music paused.

        :return: None
        """
        self.music.get_busy()
    
    def set_pos(self, value):
        """
        This sets the position in the music file where playback will 
        start. The meaning of "pos", a float (or a number that can be 
        converted to a float), depends on the music format.

        For MOD files, pos is the integer pattern number in the module. 
        For OGG it is the absolute position, in seconds, from the 
        beginning of the sound. For MP3 files, it is the relative 
        position, in seconds, from the current position. For absolute 
        positioning in an MP3 file, first call rewind()

        Other file formats are unsupported. Newer versions of SDL_mixer
        have better positioning support than earlier ones. 
        A pygame.errorstandard pygame exception is raised if a 
        particular format does not support positioning.

        Function set_pos() calls underlying SDL_mixer function 
        Mix_SetMusicPosition

        New in pygame 1.9.2

        :return: None
        """
        self.music.set_pos(value)

    def get_pos(self):
        """
        This gets the number of milliseconds that the music has been 
        playing for. The returned time only represents how long the 
        music has been playing; it does not take into account any 
        starting position offsets.

        Returns -1 if get_pos failed due to music not playing.

        :return: time
        """
        self.music.get_pos()
    
    def queue(self, file):
        """
        This will load a sound file and queue it. A queued sound file 
        will begin as soon as the current sound naturally ends. Only 
        one sound can be queued at a time. Queuing a new sound while 
        another sound is queued will result in the new sound becoming 
        the queued sound. Also, if the current sound is ever stopped or 
        changed, the queued sound will be lost.

        If you are loading from a file object, the namehint parameter 
        can be used to specify the type of music data in the object. 
        For example: queue(fileobj, "ogg")

        The following example will play music by Bach six times, then 
        play music by Mozart once:
        
        pygame.mixer.music.load('bach.ogg')
        pygame.mixer.music.play(5)        # Plays six times, not five!
        pygame.mixer.music.queue('mozart.ogg')

        Changed in pygame 2.0.2: Added optional namehint argument

        Changed in pygame-ce 2.2.0: Raises FileNotFoundError instead of 
        pygame.errorstandard pygame exception if file cannot be found

        :return: None
        """
        self.music.queue(file)
    
    def set_endevent(self):
        """
        This causes pygame to signal (by means of the event queue) 
        when the music is done playing. The argument determines the type
        of event that will be queued.

        The event will be queued every time the music finishes, 
        not just the first time. To stop the event from being queued, 
        call this method with no argument.

        :return: None
        """
        self.music.set_endevent()
    
    def get_endevent(self):
        """
        get the event a channel sends when playback stops

        Returns the event type to be sent every time the music finishes 
        playback. If there is no endevent the function returns 
        pygame.NOEVENT.

        :return: None
        
        """
        self.music.get_endevent()
    
    def get_metadata(self):
        """
        Get metadata of the specified or currently loaded music stream

        If no arguments are passed returns a dictionary containing 
        metadata of the currently loaded music stream, raises an 
        exception if a music stream is not loaded. Available keys are 
        "title", "album", "artist", "copyright". Values are strings 
        containing corresponding retrieved metadata. If particular 
        metadata was not found the value is an empty string. Here is an 
        example: {'title': 'Small Tone', 'album': 'Tones', 'artist': 
        'Audacity Generator', 'copyright': ''}

        Refer to the pygame.mixer.music.load()Load a music file for 
        playback function for arguments regarding specifying a file or 
        a file-like object whose metadata you want to retrieve. For 
        this function all arguments are optional, however, specifying 
        only the namehint will raise an exception.

        Since the underlying functionality was introduced in version 
        2.6.0 of SDL_mixer, calling this function with an older version 
        of SDL_mixer will return a dictionary with all values being set 
        to empty strings. You can find your version of SDL_mixer by 
        using pygame.mixer.get_sdl_mixer_version()get the mixer's SDL 
        version.
        New in pygame-ce 2.1.4.

        :return: dict
        """
        self.music.get_metadata()


mp3 = 'file.mp3'

player = AudioPlayer()
player.load(mp3)
player.play()
player.volume(0.05)
print(player.print_volume())
