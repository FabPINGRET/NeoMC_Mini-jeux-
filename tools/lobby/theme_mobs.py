"""Animaux des décors saisonniers (importé par gen_themes.py, jamais lancé seul).

Tenus à un nombre fixe, réapparaissent sur un point d'herbe tiré au hasard (lobby/theme/spot), ramenés s'ils sortent
du spawn. Habillage (resource pack) : item_display « tête » monté sur l'animal, tourné comme lui à chaque tick.
load() tire SPOTS à partir de theme_world.W (déjà chargé) ; écriture : write_mobs (un thème), write_common (partagées).
"""
import random

import common as C
from theme_world import G, GROUND, PLANTS, W, bid, free

MOB_BOX = 'x=-78,y=50,z=-78,dx=156,dy=70,dz=156'
MOB_BASE = 'PersistenceRequired:1b,Invulnerable:1b,DeathLootTable:"minecraft:empty"'
SPOTS = []                               # points d'herbe où un animal peut apparaître (x, y, z)


def load():
    """À appeler une fois theme_world.load() fait."""
    rs = random.Random(20261013)
    cand = [(x, y + 1, z) for (x, y, z), b in sorted(W.items())
            if bid(b) in GROUND and y >= G - 1 and 100 <= x * x + z * z <= 62 * 62 and free(x, y + 1, z)
            and bid(W.get((x, y + 1, z))) in PLANTS | {'minecraft:air'} and (x, y + 2, z) not in W and (x, y + 3, z) not in W]
    SPOTS.extend(sorted(rs.sample(cand, min(48, len(cand)))))


def mob(key, entity, n, nbt='', dress=None, rand_yaw=False, rp_nbt=None):
    """dress = (modèle du resource pack, translation [x, y, z], échelle, invisible ?) ;
    rp_nbt = NBT utilisé à la place de nbt quand le resource pack est activé (variante dont la texture n'existe que dans le pack)"""
    return {'key': key, 'entity': entity, 'n': n, 'nbt': nbt, 'dress': dress, 'yaw': rand_yaw, 'rp_nbt': rp_nbt}


# ------------------------------------------------------------------ fonctions écrites
def write_mobs(T, label, mobs):
    """Écrit T/mobs (comptage chaque seconde), T/<animal> (apparition) et T/dress_<animal> (habillage) d'un thème."""
    w, js = C.w, C.js
    mob_lines = [f'# {label} : animaux du thème, chaque seconde (joueur au spawn : chunks chargés, comptes justes)',
                 'execute unless entity @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,limit=1] run return 0',
                 f'execute as @e[tag=mg.thmob] unless entity @s[{MOB_BOX}] run function mg:lobby/theme/spot {{f:"lobby/theme/back"}}']
    for m in mobs:
        sel = f'@e[type={m["entity"]},tag=mg.th_{m["key"]}]'
        mob_lines += [f'execute store result score $thn mg.st if entity {sel}',
                      f'execute if score $thn mg.st matches ..{m["n"] - 1} run function mg:lobby/theme/spot {{f:"{T}/{m["key"]}"}}',
                      f'execute if score $thn mg.st matches {m["n"] + 1}.. as {sel[:-1]},limit=1,sort=random] run function mg:lobby/theme/gone']
        tags = ['mg.thm', 'mg.thmob', f'mg.th_{m["key"]}'] + (['mg.thdress'] if m['dress'] else [])
        summon = lambda nb: f'summon {m["entity"]} ~ ~ ~ {{Tags:{js(tags)},{MOB_BASE}{"," + nb if nb else ""}}}'
        body = [f'# {label} : un animal du thème à cet endroit (appelé par lobby/theme/spot)']
        if m['rp_nbt']:
            body += ['execute if score $rp mg.st matches 1 run ' + summon(m['rp_nbt']), 'execute unless score $rp mg.st matches 1 run ' + summon(m['nbt'])]
        else:
            body.append(summon(m['nbt']))
        if m['yaw']:
            body.append(f'execute as @e[type={m["entity"]},tag=mg.th_{m["key"]},distance=..0.1] store result entity @s Rotation[0] float 1 run random value 0..359')
        w(f'{T}/{m["key"]}', body)
        if m['dress']:
            model, (tx, ty, tz), sc, invis = m['dress']
            w(f'{T}/dress_{m["key"]}', [f'# {label} : habillage resource pack (@s = animal, position = animal)',
                                        'summon minecraft:item_display ~ ~ ~ {Tags:["mg.thm","mg.thrid","mg.thnew"],item_display:"head",'
                                        'teleport_duration:3,item:{id:"minecraft:flower_banner_pattern",count:1,components:'
                                        f'{{"minecraft:item_model":"{model}"}}}},transformation:{{left_rotation:[0f,0f,0f,1f],'
                                        f'right_rotation:[0f,0f,0f,1f],translation:[{tx}f,{ty}f,{tz}f],scale:[{sc}f,{sc}f,{sc}f]}}}}',
                                        'ride @e[type=minecraft:item_display,tag=mg.thnew,limit=1] mount @s',
                                        'tag @e[tag=mg.thnew] remove mg.thnew'] +
              (['effect give @s minecraft:invisibility infinite 0 true'] if invis else []))
    if any(m['dress'] for m in mobs):
        mob_lines += ['# habillage : chaque animal à habiller a son item_display monté, les orphelins disparaissent',
                      'execute if score $rp mg.st matches 1 run tag @e[tag=mg.thdress] add mg.thnd',
                      'execute as @e[type=minecraft:item_display,tag=mg.thrid] on vehicle run tag @s remove mg.thnd'] + \
                     [f'execute as @e[tag=mg.thnd,tag=mg.th_{m["key"]}] at @s run function mg:{T}/dress_{m["key"]}'
                      for m in mobs if m['dress']] + \
                     ['tag @e[tag=mg.thnd] remove mg.thnd',
                      'tag @e[type=minecraft:item_display,tag=mg.thrid] add mg.thor',
                      'execute as @e[tag=mg.thmob] on passengers run tag @s remove mg.thor',
                      'kill @e[tag=mg.thor]']
    if any(m['entity'] == 'minecraft:allay' for m in mobs):
        mob_lines += ['# un objet donné à un allay retombe par terre (on ne le perd pas, l\'allay ne le duplique pas)',
                      'execute as @e[type=minecraft:allay,tag=mg.thmob] if items entity @s weapon.mainhand * at @s run function mg:lobby/theme/allay_drop']
    w(f'{T}/mobs', mob_lines)


def write_common():
    """Fonctions partagées par tous les thèmes : spot, back, gone, clear, allay_drop."""
    w = C.w
    w('lobby/theme/spot', ['# Point d\'herbe du spawn tiré au hasard : y lance mg:$(f) (exécutant conservé) — généré par gen_themes.py',
                           f'execute store result score $thp mg.st run random value 1..{len(SPOTS)}'] +
      [f'$execute if score $thp mg.st matches {i} positioned {x + 0.5} {y} {z + 0.5} run function mg:$(f)' for i, (x, y, z) in enumerate(SPOTS, 1)])
    w('lobby/theme/back', ['# Animal du thème sorti du spawn : ramené sur un point au hasard (appelé par lobby/theme/spot)', 'tp @s ~ ~ ~'])
    w('lobby/theme/gone', ['# Retire un animal du thème sans animation de mort ni butin (@s)',
                           'execute on passengers run kill @s[type=minecraft:item_display]',
                           'execute at @s run tp @s ~ -300 ~', 'kill @s'])
    w('lobby/theme/clear', ['# Retire toutes les entités des thèmes (titre, animaux, habillages)',
                            'kill @e[type=minecraft:item_display,tag=mg.thrid]',
                            'execute as @e[tag=mg.thmob] run function mg:lobby/theme/gone', 'kill @e[tag=mg.thm]'])
    w('lobby/theme/allay_drop', ['# Allay du thème qui tient un objet (@s, position = allay) : l\'objet retombe au sol',
                                 'summon minecraft:item ~ ~ ~ {Tags:["mg.thdrop"],Item:{id:"minecraft:stone",count:1},PickupDelay:10s}',
                                 'data modify entity @e[type=minecraft:item,tag=mg.thdrop,limit=1] Item set from entity @s equipment.mainhand',
                                 'tag @e[tag=mg.thdrop] remove mg.thdrop',
                                 'item replace entity @s weapon.mainhand with minecraft:air'])
