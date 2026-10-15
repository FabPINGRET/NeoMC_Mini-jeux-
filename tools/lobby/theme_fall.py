"""Chutes saisonnières par intermittence (importé par gen_themes.py, jamais lancé seul) : feuilles d'Halloween, neige de Noël.

Les particules « qui tombent » ne sont plus continues : elles démarrent et s'arrêtent au hasard, avec un fondu de LEVELS secondes.
Tout vit dans le scoreboard mg.st (aucun objectif de plus) :
  $thw : 1 = ça tombe, 0 = accalmie (absent = pas encore tiré : le premier tirage met 1) ;
  $thd : secondes restantes avant la prochaine bascule (tirage aléatoire dans ON ou OFF) ;
  $thi : intensité 0..LEVELS (monte ou descend de 1 par seconde), lue par <thème>/fx : 0 = rien, sinon <thème>/fall.
lobby/theme/fall_tick (chaque seconde, appelé par lobby/theme/tick) fait vivre le cycle ; lobby/theme/fall_flip bascule.
<thème>/on part en chute immédiate (fondu d'entrée) ; lobby/theme/off efface les trois scores (reset : absents jusqu'au prochain on).
Les scores survivent à /reload et au redémarrage : le cycle reprend où il en était.
"""
import common as C

w = C.w

ON = (60, 240)          # durée d'une chute, en secondes (min, max)
OFF = (60, 180)         # durée d'une accalmie, en secondes (min, max)
LEVELS = 8              # secondes de fondu (intensité maximale)
STEPS = 4               # paliers de densité de <thème>/fall ; chacun couvre LEVELS // STEPS niveaux
assert LEVELS % STEPS == 0, 'LEVELS doit être un multiple de STEPS'

# Halloween : la cendre (ash) et les âmes (soul) restent continues exprès, seules les feuilles font partie du cycle.
# thème -> [(particule avec sa position et ses écarts, nombre par seconde à pleine intensité)]
SPECS = {
    'halloween': [(f'minecraft:tinted_leaves{{color:[{c}]}} ~ ~7 ~ 10 3 10 0', n)
                  for c, n in (('0.93,0.45,0.08,1.0', 5), ('0.78,0.16,0.08,1.0', 3), ('0.95,0.72,0.15,1.0', 3), ('0.52,0.30,0.14,1.0', 2))],
    'noel': [('minecraft:snowflake ~ ~6 ~ 10 4 10 0', 30), ('minecraft:white_ash ~ ~3 ~ 8 3 8 0', 20)],
}


def _draw(var, lo_hi):
    return f'store result score {var} mg.st run random value {lo_hi[0]}..{lo_hi[1]}'


def fx_call(key, lobby):
    """Lignes de <thème>/fx (à déplier avec *) : la chute est rejouée à chaque joueur du spawn tant que l'intensité est
    au-dessus de 0 ; aucune ligne pour un thème sans SPECS."""
    if key not in SPECS:
        return []
    return [f'execute if score $thi mg.st matches 1.. in minecraft:overworld as {lobby} at @s run function mg:lobby/theme/{key}/fall']


def on_lines():
    """Lignes de <thème>/on : la chute démarre tout de suite (intensité 0, elle monte d'1 par seconde)."""
    return ['# chute de particules : démarre tout de suite, avec fondu d\'entrée (voir theme_fall.py)',
            'scoreboard players set $thw mg.st 1', f'execute {_draw("$thd", ON)}', 'scoreboard players set $thi mg.st 0']


def off_lines():
    """Lignes de lobby/theme/off : le cycle est remis à zéro (rien ne reste dans le scoreboard)."""
    return ['scoreboard players reset $thw mg.st', 'scoreboard players reset $thd mg.st', 'scoreboard players reset $thi mg.st']


def write_common():
    w('lobby/theme/fall_tick', ['# Cycle des chutes (chaque seconde, appelé par lobby/theme/tick) : compte à rebours, bascule, fondu',
                                'scoreboard players add $thi mg.st 0', 'scoreboard players remove $thd mg.st 1',
                                'execute if score $thd mg.st matches ..0 run function mg:lobby/theme/fall_flip',
                                f'execute if score $thw mg.st matches 1 if score $thi mg.st matches ..{LEVELS - 1} run scoreboard players add $thi mg.st 1',
                                'execute if score $thw mg.st matches 0 if score $thi mg.st matches 1.. run scoreboard players remove $thi mg.st 1'])
    w('lobby/theme/fall_flip', ['# Chute <-> accalmie, avec une nouvelle durée tirée au hasard (absent : 1, ça tombe)',
                                'execute store success score $thw mg.st unless score $thw mg.st matches 1',
                                f'execute if score $thw mg.st matches 1 {_draw("$thd", ON)}',
                                f'execute if score $thw mg.st matches 0 {_draw("$thd", OFF)}'])


def write_fall(key, label):
    """<thème>/fall : exécuté par chaque joueur du spawn, en son point ; le nombre de particules suit l'intensité $thi."""
    per = LEVELS // STEPS
    ls = [f'# {label} : particules qui tombent, densité selon $thi (1..{LEVELS}) ; appelé par {key}/fx']
    for spec, n in SPECS[key]:
        for k in range(1, STEPS + 1):
            cnt = max(1, int(n * k / STEPS + 0.5))
            ls.append(f'execute if score $thi mg.st matches {per * (k - 1) + 1}..{per * k} run particle {spec} {cnt} normal @s')
    w(f'lobby/theme/{key}/fall', ls)
