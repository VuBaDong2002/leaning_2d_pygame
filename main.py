import sys
import pygame

from setting import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join
from data import Data
from debug import debug
from ui import UI
from overworld import Overworld
from support import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("super pirate word")
        self.clock = pygame.time.Clock()
        self.import_assets()

        self.ui = UI(self.font, self.ui_frames)
        self.data = Data(self.ui)
        self.tmx_maps = {0: load_pygame(join('D:\\export\\game_2d_python', 'data', 'levels', '0.tmx')),
                         1: load_pygame(join('D:\\export\\game_2d_python', 'data', 'levels', '1.tmx')),
                         2: load_pygame(join('D:\\export\\game_2d_python', 'data', 'levels', '2.tmx')),
                         3: load_pygame(join('D:\\export\\game_2d_python', 'data', 'levels', '3.tmx')),
                         4: load_pygame(join('D:\\export\\game_2d_python', 'data', 'levels', '4.tmx')),
                         5: load_pygame(join('D:\\export\\game_2d_python', 'data', 'levels', '5.tmx')),
                         6: load_pygame(join('D:\\export\\game_2d_python', 'data', 'levels', '6.tmx')),
                        }
        self.tmx_overworld = load_pygame(join('D:\\export\\game_2d_python', 'data', 'levels', '0.tmx'))
        self.current_stage = Level(self.tmx_maps[0], self.level_frames,self.audio_file, self.data,self.switch_stage)
        # self.current_stage = Overworld(tmx_map = self.tmx_overworld, data = self.data, overworld_frames = self.overworld_games)

    def switch_stage(self, target, unlock =0):
        if target == 'level':
            self.current_stage = Level(self.tmx_maps[self.data.current_level], self.level_frames, self.data, self.switch_stage)
        else:
            if unlock > 0:
                self.data.unlocked_level = unlock
            else:
                self.data.health -= 1
            self.current_stage = Overworld(self.tmx_overworld, self.data, self.overworld_games, self.switch_stage)

    def import_assets(self):
        self.level_frames = {
            'flag': import_folder('D:\\export\\game_2d_python','graphics','level','flag'),
            'saw': import_folder('D:\\export\\game_2d_python','graphics','enemies','saw','animation'),
            'saw_chain': import_image('D:\\export\\game_2d_python','graphics','enemies','saw','saw_chain'),
            'floor_spike':import_folder('D:\\export\\game_2d_python','graphics','enemies','floor_spikes'),
            'palms':import_sub_folders('D:\\export\\game_2d_python','graphics','level','palms'),
            'candle': import_folder('D:\\export\\game_2d_python', 'graphics','level', 'candle'),
            'window':import_folder('D:\\export\\game_2d_python','graphics','level','window'),
            'big_chain':import_folder('D:\\export\\game_2d_python','graphics','level','big_chains'),
            'small_chain':import_folder('D:\\export\\game_2d_python','graphics','level','small_chains'),
            'candle_light':import_folder('D:\\export\\game_2d_python','graphics','level','candle light'),
            'player': import_sub_folders('D:\\export\\game_2d_python', 'graphics', 'player'),
            'helicopter':import_folder('D:\\export\\game_2d_python','graphics','level','helicopter'),
            'boat': import_folder('D:\\export\\game_2d_python','graphics','objects','boat'),
            'spike':import_image('D:\\export\\game_2d_python','graphics','enemies','spike_ball', 'Spiked Ball'),
            'spike_chain':import_image('D:\\export\\game_2d_python','graphics','enemies','spike_ball', 'spiked_chain'),
            'tooth': import_folder('D:\\export\\game_2d_python','graphics','enemies','tooth', 'run'),
            'shell': import_sub_folders('D:\\export\\game_2d_python', 'graphics','enemies','shell'),
            'pearl':import_image('D:\\export\\game_2d_python','graphics','enemies','bullets', 'pearl'),
            'items': import_sub_folders('D:\\export\\game_2d_python', 'graphics','items'),
            'particle': import_folder('D:\\export\\game_2d_python', 'graphics', 'effects', 'particle' ),
            'water_top': import_folder('D:\\export\\game_2d_python', 'graphics','level', 'water', 'top'),
            'water_body': import_image('D:\\export\\game_2d_python', 'graphics','level', 'water', 'body'),
            'bg_tiles': import_folder_dict('D:\\export\\game_2d_python', 'graphics', 'level', 'bg', 'tiles'),
            'cloud_small': import_folder('D:\\export\\game_2d_python', 'graphics', 'level', 'clouds', 'small'),
            'cloud_large': import_image('D:\\export\\game_2d_python', 'graphics', 'level', 'clouds', 'large_cloud')
        }

        self.font = pygame.font.Font(join('D:\\export\\game_2d_python','graphics','ui','runescape_uf.ttf'), 40)

        self.ui_frames = {
            'heart': import_folder('D:\\export\\game_2d_python','graphics','ui','heart'),
            'coin': import_image('D:\\export\\game_2d_python','graphics','ui','coin')
        }

        self.overworld_games = {
            'palms': import_folder('D:\\export\\game_2d_python','graphics', 'overworld', 'palm'),
            'water': import_folder('D:\\export\\game_2d_python','graphics', 'overworld', 'water'),
            'path': import_folder_dict('D:\\export\\game_2d_python','graphics', 'overworld', 'path'),
            'icon': import_sub_folders('D:\\export\\game_2d_python','graphics', 'overworld', 'icon')
        }

        self.audio_file = {
            'coin': pygame.mixer.Sound(join('D:\\export\\game_2d_python','audio', 'coin.wav'))
        }

    def check_game_over(self):
        if self.data.health <= 0:
            pygame.quit()
            sys.exit()

    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit ()

            self.check_game_over()
            self.current_stage.run(dt)
            self.ui.update(dt)
            # debug(self.data.coins)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()