import pygame


class Sound:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            "move": pygame.mixer.Sound("sounds/move.wav"),
            "win": pygame.mixer.Sound("sounds/win.mp3"),
            "tied": pygame.mixer.Sound("sounds/tied.mp3"),
            "reset": pygame.mixer.Sound("sounds/reset.mp3"),
        }

    def play_sound(self, sound_key):
        if sound_key in self.sounds:
            self.sounds[sound_key].play()

    def stop_all_sounds(self):
        pygame.mixer.stop()

    def cleanup(self):
        pygame.mixer.quit()
