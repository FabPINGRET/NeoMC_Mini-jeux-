"""🎉 Mouvement des emotes (importé par gen_sit.py, jamais lancé seul) : chaque emote fait aussi bouger le joueur.

Seulement deux commandes vanilla : `swing @s <main>` (coup de bras) et `rotate @s <rotation>` (tête / corps). Ni saut, ni effet, ni
mouvement : le joueur reste où il est (assis compris : rotate et swing marchent sur un passager). Chaque mouvement a une somme nulle :
le regard revient où il était (Fête : tour complet, 8 x 45 = 360 ; le générateur vérifie la somme de chaque mouvement).
Limite acceptée : près de ±90 le tangage est borné par le jeu, le retour n'est alors pas exactement nul.
- emote_{k} (gen_sit.py, core/opt) termine par start_lines(k) : mg.lsk = k (quelle emote), mg.lse = -1 (image courante : move_step
  l'avance à 0), tag mg.lsm. L'image 0 est jouée par move_tick le même tick (core/tick vient APRÈS core/opt), une seule fois.
- core/tick -> move_tick (seulement si quelqu'un porte mg.lsm) -> move_step, une fois par joueur « at @s » : sans lui, le `~` de rotate
  se lirait dans la rotation de celui qui exécute. Abandon (sit/ok refuse : hors du spawn, partie, coupé par un admin ; ou mg.lsk
  inconnu) -> move_stop ; sinon mg.lse + 1, puis move_{k} (mg.lsk) joue les commandes de cette image.
- move_{k} : une ligne `if score @s mg.lse matches F` par commande ; la dernière appelle move_stop à la fin de la durée.
- Une seule rotation par joueur et par tick (rotate lit la rotation source avant l'application des précédentes).
- S'asseoir (sit/seat, gen_sit.py) arrête le mouvement en cours (move_stop) avant le tp du siège.
- La recharge des emotes (COOLDOWN de gen_sit.py, passé à write()) dépasse la plus longue : une emote ne démarre jamais en plein mouvement.
Tag : mg.lsm (mouvement en cours). Objectifs : mg.lse (image), mg.lsk (emote). Fonctions : lobby/sit/move_*.
"""
import re

import common as C

DESC = {1: 'Salut : bras qui s\'agite quatre fois, petit hochement de tête',
        2: 'Danse : bras en alternance, balancement gauche-droite du corps',
        3: 'Fête : un tour complet sur soi-même, puis bras en alternance',
        4: 'Étourdi : la tête décrit deux cercles'}


def swing(f, hand='mainhand'):
    return f, f'swing @s {hand}'


def rot(f, yaw=0, pitch=0):
    return f, f'rotate @s ~{yaw or ""} ~{pitch or ""}'


def _moves():
    """{emote: (durée en ticks, [(image, commande)])}, calculé ici plutôt qu'écrit à la main."""
    salut = [swing(f) for f in (0, 5, 10, 15)] + [rot(0, pitch=-10), rot(12, pitch=10)]
    danse = [swing(f, 'mainhand' if f % 8 == 0 else 'offhand') for f in range(0, 48, 4)]
    danse += [rot(f, y) for f, y in zip((0, 8, 16, 24, 32, 40), (20, -40, 40, -40, 40, -20))]
    fete = [rot(f, 45) for f in range(0, 16, 2)]                             # 8 x 45 = 360, un pas tous les 2 ticks
    fete += [swing(f, 'mainhand' if i % 2 == 0 else 'offhand') for i, f in enumerate((16, 20, 24, 28))]
    cercle = [(12, -6), (12, 6), (-12, 6), (-12, -6)]                       # deux tours : la somme est nulle
    etourdi = [rot(4 * i, *cercle[i % 4]) for i in range(8)]
    return {1: (24, salut), 2: (48, danse), 3: (32, fete), 4: (32, etourdi)}


MOVES = _moves()
UNTAG = 'tag @a remove mg.lsm'
TICK_LINE = 'execute if entity @a[tag=mg.lsm] run function mg:lobby/sit/move_tick'


def start_lines(k):
    """Dernières lignes de emote_{k} (gen_sit.py), une fois la recharge acceptée : @s = joueur. mg.lse = -1 : move_tick (core/tick, après
    core/opt) avance à 0 et joue l'image 0 le même tick, une seule fois."""
    return ['# mouvement (sit_move.py) : l\'image 0 est jouée par core/tick -> move_tick, le même tick',
            f'scoreboard players set @s mg.lsk {k}',
            'scoreboard players set @s mg.lse -1',
            'tag @s add mg.lsm']


def _check(k, length, frames, cooldown):
    """Garde-fous du générateur : images dans la durée, une rotation par tick, regard de retour (tangage nul, cap à 360 près), durée < recharge."""
    assert all(0 <= f < length for f, _ in frames), k
    rots = [(f, re.fullmatch(r'rotate @s ~(\S*) ~(\S*)', c)) for f, c in frames if c.startswith('rotate')]
    assert len({f for f, _ in rots}) == len(rots), f'emote {k} : deux rotate dans le même tick'
    yaw, pitch = (sum(float(m[i] or 0) for _, m in rots) for i in (1, 2))
    assert yaw % 360 == 0 and pitch == 0, f'emote {k} : le regard ne revient pas (cap {yaw}, tangage {pitch})'
    assert length < cooldown, f'emote {k} : durée {length} >= recharge {cooldown}'


def write(cooldown):
    """cooldown = COOLDOWN de gen_sit.py (ticks entre deux emotes)."""
    w = C.w
    for k, (length, frames) in MOVES.items():
        _check(k, length, frames, cooldown)
        w(f'lobby/sit/move_{k}', [f'# @s at @s : commandes de l\'image mg.lse du mouvement de l\'emote {DESC[k]} ({length} ticks)'] +
          [f'execute if score @s mg.lse matches {f} run {c}' for f, c in sorted(frames, key=lambda t: t[0])] +
          [f'execute if score @s mg.lse matches {length}.. run function mg:lobby/sit/move_stop'])
    w('lobby/sit/move_stop', ['# @s : fin (ou abandon) du mouvement de l\'emote', 'tag @s remove mg.lsm',
                              'scoreboard players reset @s mg.lse', 'scoreboard players reset @s mg.lsk'])
    w('lobby/sit/move_step', ['# @s at @s (move_tick) : une image de plus du mouvement de l\'emote ; refus de sit/ok (spawn quitté, partie, admin) : arrêt',
                              'execute unless function mg:lobby/sit/ok run return run function mg:lobby/sit/move_stop',
                              f'execute unless score @s mg.lsk matches 1..{max(MOVES)} run return run function mg:lobby/sit/move_stop',
                              'scoreboard players add @s mg.lse 1'] +
      [f'execute if score @s mg.lsk matches {k} run return run function mg:lobby/sit/move_{k}' for k in MOVES])
    w('lobby/sit/move_tick', ['# Appelé chaque tick (core/tick) tant qu\'un joueur porte mg.lsm ; « at @s » : le ~ de rotate lit sa rotation',
                              'execute as @a[tag=mg.lsm] at @s run function mg:lobby/sit/move_step'])


def wire(untag):
    """Câblage (une ligne par patch) : à appeler après les patchs de core/load, core/tick et desinstaller de gen_sit.py ; untag = sa ligne UNTAG."""
    C.objectives([('mg.lse', 'dummy'), ('mg.lsk', 'dummy')])
    C.patch('core/load', untag, [UNTAG])
    C.patch('core/tick', 'execute if entity @a[tag=mg.sit] run function mg:lobby/sit/tick', [TICK_LINE])
    C.patch('desinstaller', untag, [UNTAG])
