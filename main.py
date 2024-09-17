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

        :param loops: 
        :param start: 
        :param fade_ms: 
        :return: 
        """
        self.music.play()

    def volume(self, value):
        self.music.set_volume(value)

    def print_volume(self):
        return self.music.get_volume()
    
    def quit(self):
        self.mixer.quit()
    
    def unload(self):
        self.music.unload()
    
    def rewind(self):
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
        self.music.unpause()

    def fadeout(self, time: int):
        self.music.fadeout(time)
    
    def get_busy(self):
        self.music.get_busy()
    
    def set_pos(self, value):
        self.music.set_pos(value)

    def get_pos(self):
        self.music.get_pos()
    
    def queue(self, file):
        self.music.queue(file)
    
    def set_endevent(self):
        self.music.set_endevent()
    
    def get_endevent(self):
        self.music.get_endevent()
    
    def get_metadata(self):
        self.music.get_metadata()


mp3 = 'file.mp3'

player = AudioPlayer()
player.load(mp3)
player.play()
player.volume(0.05)
print(player.print_volume())
