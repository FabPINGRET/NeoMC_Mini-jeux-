"""🎣 Pêche à l'étang : prises et record (importé par gen_fish.py, jamais lancé seul).

L'advancement mg:lobby_fish (fish_rod.py : hameçon remonté avec un objet, canne marquée) appelle lobby/fish/catch (@s = joueur) :
- catch : marque le joueur (mg.lfc : lobby/fish/after tuera le tick suivant les objets vanilla et les orbes d'XP), pose un marqueur mg.lfm à
  l'hameçon (le bobber dont le joueur est l'origine) marqué aussi mg.lfx le temps de la prise (ses effets sortent de CE marqueur, pas de celui
  d'un autre joueur), puis tire la prise. Plus de garde (lobby/fish/keep : canne perdue, pêche coupée) : rien n'est tiré.
- roll : tirage de 1 à 1000 (#lfr dans mg.st), puis un `return run function c_<clé>` par seuil cumulé de CATCHES (la somme des poids fait 1000).
- c_<clé> : compteur ($catch, $gold ou $junk dans mg.lfn), taille tirée dans la fourchette du genre (#lfs, en cm, dans mg.st), message, son et
  particules au marqueur. Genres : common (poisson commun), rare (annonce à qui est à moins de 24 blocs), gold (poisson doré : annonce à tout le
  lobby), junk (déchet drôle, sans taille).
- pb : un poisson plus grand que le record du joueur (mg.lfb, en cm) le remplace et passe par hall/top (plaque « Plus belle prise » du Hall).
"""
import common as C
from theme_world import LOBBY

AT = 'execute at @e[type=minecraft:marker,tag=mg.lfx,limit=1] run '
# clé, poids (sur 1000), genre, libellé, couleur, taille en cm (min, max) ou phrase du déchet
CATCHES = [('gardon', 160, 'common', 'un gardon', 'white', (10, 40)),
           ('truite', 160, 'common', 'une truite', 'green', (10, 40)),
           ('perche', 140, 'common', 'une perche', 'yellow', (10, 40)),
           ('carpe', 140, 'common', 'une carpe', 'gold', (10, 40)),
           ('brochet', 60, 'rare', 'un brochet', 'aqua', (40, 80)),
           ('esturgeon', 40, 'rare', 'un esturgeon', 'light_purple', (40, 80)),
           ('dore', 30, 'gold', 'un poisson doré', 'gold', (80, 120)),
           ('botte', 90, 'junk', 'une vieille botte', 'gray', 'Zut... une vieille botte !'),
           ('canard', 70, 'junk', 'un canard en plastique', 'yellow', 'Coin-coin ! Un canard en plastique.'),
           ('chaussette', 60, 'junk', 'une chaussette trouée', 'gray', 'Beurk, une chaussette trouée.'),
           ('bidon', 50, 'junk', 'un bidon rouillé', 'dark_gray', 'Un bidon rouillé... ça ne se mange pas.')]
assert sum(c[1] for c in CATCHES) == 1000, 'les poids de CATCHES doivent faire 1000'


def size_text(col, label):
    """Texte « Une carpe de N cm » (N = #lfs) en actionbar."""
    return [{'text': '🎣 ', 'color': 'aqua'}, {'text': label[0].upper() + label[1:], 'color': col, 'bold': True},
            {'text': ' de ', 'color': 'gray'}, {'score': {'name': '#lfs', 'objective': 'mg.st'}, 'color': 'yellow'}, {'text': ' cm', 'color': 'gray'}]


def fx(sound, pitch, particle, spec):
    """Son et particules au marqueur de la prise (à 16 blocs)."""
    return [AT + f'playsound minecraft:{sound} player @a[distance=..16] ~ ~ ~ 1 {pitch}',
            AT + f'particle minecraft:{particle} ~ ~0.3 ~ {spec} normal @a[distance=..16]']


def catch_lines(kind, label, col, size):
    js = C.js
    if kind == 'junk':
        return ['scoreboard players add $junk mg.lfn 1', 'title @s actionbar ' + js({'text': '🎣 ' + size, 'color': col})] + \
               fx('entity.villager.no', 1.2, 'smoke', '0.2 0.1 0.2 0.02 8')
    lo, hi = size
    L = ['scoreboard players add $catch mg.lfn 1'] + (['scoreboard players add $gold mg.lfn 1'] if kind == 'gold' else []) + [
        f'execute store result score #lfs mg.st run random value {lo}..{hi}']
    name = {'text': label, 'color': col, 'bold': True}
    sized = [name, {'text': ' de ', 'color': 'gray'}, {'score': {'name': '#lfs', 'objective': 'mg.st'}, 'color': 'yellow'}, {'text': ' cm', 'color': 'gray'}]
    if kind == 'common':
        L += ['title @s actionbar ' + js(size_text(col, label))] + fx('entity.fishing_bobber.splash', 1.2, 'splash', '0.3 0.1 0.3 0.1 12')
    elif kind == 'rare':
        L += ['title @s subtitle ' + js(sized), 'title @s title ' + js({'text': '⭐ Belle prise !', 'color': 'gold', 'bold': True}),
              'tellraw @a[distance=..24] ' + js([{'selector': '@s', 'color': 'yellow'}, {'text': ' a sorti ', 'color': 'gray'}] + sized + [{'text': ' !', 'color': 'gray'}])
              ] + fx('entity.player.levelup', 1.4, 'happy_villager', '0.4 0.3 0.4 0 14')
    else:
        L += ['title @s subtitle ' + js(sized), 'title @s title ' + js({'text': '✨ POISSON DORÉ ✨', 'color': 'gold', 'bold': True}),
              f'tellraw {LOBBY} ' + js([{'text': '✨ ', 'color': 'gold'}, {'selector': '@s', 'color': 'yellow'}, {'text': ' a sorti ', 'color': 'gray'}] + sized +
                                       [{'text': ' !', 'color': 'gray'}])
              ] + fx('entity.firework_rocket.twinkle', 1, 'firework', '0.3 0.5 0.3 0.12 24')
    return L + ['function mg:lobby/fish/pb']


def write():
    w, js = C.w, C.js
    w('lobby/fish/catch', ['# @s : a remonté sa ligne avec un objet (advancement mg:lobby_fish) : marque le joueur, pose un marqueur à l\'hameçon, tire la prise',
                           'advancement revoke @s only mg:lobby_fish',
                           'tag @s add mg.lfc',
                           'execute as @e[type=minecraft:fishing_bobber,distance=..40] at @s on origin if entity @s[tag=mg.lfc] run '
                           'summon minecraft:marker ~ ~ ~ {Tags:["mg.lfm","mg.lfx"]}',
                           'execute unless function mg:lobby/fish/keep run return run tag @e[type=minecraft:marker,tag=mg.lfx] remove mg.lfx',
                           'function mg:lobby/fish/roll',
                           'tag @e[type=minecraft:marker,tag=mg.lfx] remove mg.lfx'])
    roll, acc = ['# @s : tirage de la prise (1..1000, dans #lfr) : un seuil cumulé par prise, la première qui correspond termine',
                 'execute store result score #lfr mg.st run random value 1..1000'], 0
    for key, weight, *_ in CATCHES:
        acc += weight
        roll.append(f'execute if score #lfr mg.st matches ..{acc} run return run function mg:lobby/fish/c_{key}')
    w('lobby/fish/roll', roll)
    for key, weight, kind, label, col, size in CATCHES:
        w(f'lobby/fish/c_{key}', [f'# Prise : {label} ({kind}, poids {weight} sur 1000) ; @s = joueur, effets au marqueur mg.lfx'] + catch_lines(kind, label, col, size))
    w('lobby/fish/pb', ['# @s : plus grande prise que son record (#lfs en cm) ? Oui : record remplacé, message, plaque du Hall',
                        'scoreboard players add @s mg.lfb 0',
                        'execute unless score #lfs mg.st > @s mg.lfb run return 0',
                        'scoreboard players operation @s mg.lfb = #lfs mg.st',
                        'tellraw @s ' + js([{'text': '⭐ Nouveau record perso : ', 'color': 'yellow'},
                                            {'score': {'name': '#lfs', 'objective': 'mg.st'}, 'color': 'gold', 'bold': True}, {'text': ' cm', 'color': 'gray'}]),
                        'function mg:hall/top {obj:"mg.lfb",key:"fish",lbl:"🎣 Plus belle prise",col:"aqua",unit:" cm"}'])
