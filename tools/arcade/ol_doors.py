"""🌙 Ombrelune : portes de quête (citadelle, porte de Khazgarde, pyramide).

Ouvertes quand l'étape est finie par un joueur : door/<k>_open ouvre pour tout le monde et mémorise l'état dans mg:ombre doors.<k>.
Refermées par la synchro des stations (st/<région>, rejouée à chaque changement de SV) seulement si ce drapeau est absent : sinon un joueur
déjà au-delà de l'étape resterait bloqué (q/int_p n'active les pylônes que si mg.olch == i). Le drapeau est effacé par world_build / wb_done
(reconstruction : les portes sont reposées fermées) et par la désinstallation (gen_ombrelune.py).
Rattrapage : door/catchup rouvre toute porte sans drapeau dès qu'un joueur d'Ombrelune a dépassé l'étape qui l'ouvre (mg.olch >= étape + 1 :
q/actdone<i> ouvre la porte puis q/adv incrémente mg.olch). Appelé après la synchro (st/done), à l'entrée (enter) et chaque seconde (second) :
`fill` n'écrit que dans des chunks chargés, d'où la garde `if loaded` (sinon le drapeau serait posé alors que la porte reste fermée) ; une porte
lointaine se rouvre donc quand un joueur approche et que ses chunks se chargent.
"""
import ol_quest as Q
import ol_structs as S
from ol_core import w

SP = S.SPOTS
x1, y1, z1, x2, y2, z2 = SP['kgate_door']
cx1, cy1, cz1, cx2, cy2, cz2 = SP['cit_gate']
px, py, pz = SP['pyr_door']
DOORS_KEY = 'doors'
BOX = {'kgate': (x1, y1, z1, x2, y2, z2), 'citadel': (cx1, cy1, cz1, cx2, cy2, cz2), 'pyramid': (px - 1, py, pz, px + 1, py + 2, pz)}
CLOSED = {'kgate': 'deepslate_tiles', 'citadel': 'iron_bars', 'pyramid': 'chiseled_sandstone'}
DOORS = {k: ([f'fill {" ".join(map(str, b))} minecraft:air'], [f'fill {" ".join(map(str, b))} minecraft:{CLOSED[k]}']) for k, b in BOX.items()}
DOORS_GUARD = f'execute unless data storage mg:ombre {DOORS_KEY}.{{}} run '
DOORS_CLOSE = [DOORS_GUARD.format(k) + l for k, (_, cl) in DOORS.items() for l in cl]        # lignes de STAT : fermeture gardée par le drapeau
# étape de campagne qui ouvre chaque porte, tirée des données de quête (st(..., door=<k>)) : pas de valeur en dur
STEP = {s['door']: i for i, s in enumerate(Q.STEPS) if s.get('door')}
assert set(STEP) == set(DOORS), f'portes de quête {sorted(STEP)} != portes générées {sorted(DOORS)}'
# ancienne grille de la citadelle (dans l'enceinte, x2) : posée par l'ancien build et l'ancien st/<région> d'un serveur déjà construit, que rien
# ne refait (monde construit une seule fois). Vidée par la synchro des stations ; sans danger : y + 1..8 est de l'air dans l'état généré.
# Transitoire : à retirer (avec la ligne de test correspondante) une fois le serveur live reconstruit (world_build).
DOORS_LEGACY = ['fill {} {} {} {} {} {} minecraft:air'.format(*SP['cit_gate_old'])]
for k, (op, _) in DOORS.items():
    b = BOX[k]       # coordonnées absolues (appelée sous `execute in <dimension>`, parfois sans joueur : le son se joue au centre de la porte)
    w(f'door/{k}_open', [f'# Porte {k} : ouverte', f'playsound minecraft:block.iron_door.open master @a[tag=mg.olw] {(b[0] + b[3] + 1) / 2} {(b[1] + b[4] + 1) / 2} '
                         f'{(b[2] + b[5] + 1) / 2} 1 0.5'] + op + [f'data modify storage mg:ombre {DOORS_KEY}.{k} set value 1b'])
w('door/catchup', ['# Contexte : dimension. Rouvre toute porte sans drapeau si un joueur d\'Ombrelune a dépassé son étape (coins chargés requis)'] +
  [f'execute unless data storage mg:ombre {DOORS_KEY}.{k} if loaded {b[0]} {b[1]} {b[2]} if loaded {b[3]} {b[4]} {b[5]} '
   f'if entity @a[tag=mg.olw,scores={{mg.olch={STEP[k] + 1}..}}] run function mg:ombre/door/{k}_open' for k, b in BOX.items()])
