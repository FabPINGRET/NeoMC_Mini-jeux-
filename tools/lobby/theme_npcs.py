"""PNJ des décors saisonniers (importé par gen_themes.py, jamais lancé seul) : sorcière (Halloween), lutin (Noël).

Un PNJ par thème, toujours au même endroit (SPOT, sous le grand champignon près du buffet) : corps (sorcière NoAI, ou mannequin
immobile) + zone cliquable (interaction, tag mg.thnpci) + indication (text_display). Tous portent mg.thx (retirés par
lobby/theme/clear) ; le corps porte aussi mg.thmob (retiré par lobby/theme/gone) et mg.thnpc. Surtout pas mg.npc : return_lobby et
bedwars/prepare tuent ce tag. Cadeau : objet tagué custom_data mg_thg (ragoût mystère / feux d'artifice), recharge de 30 s
(objectif mg.thc, secondes) ; rien n'est donné à qui tient déjà 2 objets du PNJ (le lutin en donne 3). Les feux d'artifice ont un
budget par joueur (mg.thfw, +3 par don) : une étoile prise dans un coffre ou ramassée ne part pas. Cadeaux retirés à la bascule du
thème, à chaque lancement de partie, et chaque seconde chez les joueurs occupés ailleurs (partie, plot, élytres, kart...).
Fichiers : lobby/theme/<t>/npc (idempotent : retire puis repose), <t>/npc_give ; communs : npc_use, npc_second, fw_use (feux d'artifice
de Noël : l'étoile consommée déclenche l'advancement mg:theme_fw, écrit ici). Tout reste sous lobby/theme/ (cf. theme_world.load).
check_spot() arrête le générateur si l'emplacement n'est plus libre ; prepare() la vérifie et réserve la place (à appeler avant les thèmes).
"""
import json
import os

import common as C
from theme_mobs import THEME_TAG
from theme_water import FOUNT
from theme_world import ELYTRA_PADS, NOT_SOLID, PAD_MARGIN, W, bid, free, reserve

SPOT = (22, 64, 22)                      # pieds du PNJ (case) ; le PNJ est au centre de la case
YAW = 135                                # regarde vers le centre du spawn
BUFFET = (24, 63, 19)                    # bloc d'or du buffet
COOLDOWN = 30                            # secondes entre deux cadeaux
GIFT = '*[minecraft:custom_data~{mg_thg:1b}]'
BUSY = ['mg.play', 'mg.ely', 'mg.elyf', 'mg.xso', 'mg.lk', 'mg.inplot', 'mg.visit']   # joueurs occupés : pas de cadeau gardé
OVW = 'execute in minecraft:overworld run '
POS = f'{SPOT[0] + 0.5} {SPOT[1]} {SPOT[2] + 0.5}'
LOADED = f'{SPOT[0]} {SPOT[1]} {SPOT[2]}'


def check_spot():
    """Le générateur s'arrête si le PNJ n'a plus sa place (sol, volume libre, voisins) : appelé après theme_world/theme_water.load()."""
    x, y, z = SPOT
    if (x, y - 1, z) not in W or bid(W[(x, y - 1, z)]) in NOT_SOLID:
        raise SystemExit(f'theme_npcs : pas de sol solide sous {SPOT}')
    if any((x, yy, z) in W for yy in range(y, y + 3)):
        raise SystemExit(f'theme_npcs : {SPOT} (y {y}..{y + 2}) occupé dans le modèle du spawn')
    if not all(free(x, yy, z) for yy in range(y, y + 4)):
        raise SystemExit(f'theme_npcs : {SPOT} refusé par free() (plot, zone modifiée ou réservée)')
    if max(abs(x - BUFFET[0]), abs(z - BUFFET[2])) <= 2:
        raise SystemExit(f'theme_npcs : {SPOT} à 2 blocs du buffet {BUFFET}')
    if any(max(abs(x - px), abs(z - pz)) <= PAD_MARGIN for px, pz in ELYTRA_PADS):
        raise SystemExit(f'theme_npcs : {SPOT} trop près d\'un socle d\'élytra')
    if any(max(abs(x - fx), abs(z - fz)) <= 2 for fx, _, fz in FOUNT):
        raise SystemExit(f'theme_npcs : {SPOT} à 2 blocs d\'une fontaine')


def prepare():
    """Vérifie l'emplacement puis réserve la place du PNJ : aucun décor ni animal dedans (à appeler avant la génération des thèmes)."""
    check_spot()
    x, y, z = SPOT
    reserve(x - 1, x + 1, y, y + 3, z - 1, z + 1)


# ------------------------------------------------------------------ corps
TAGS_BODY = [THEME_TAG, 'mg.thmob', 'mg.thnpc']
TAGS_INT = [THEME_TAG, 'mg.thnpc', 'mg.thnpci']
TAGS_HINT = [THEME_TAG, 'mg.thnpc']
LEATHER = '{{id:"minecraft:leather_{p}",count:1,components:{{"minecraft:dyed_color":{c}}}}}'
SANTA = '{id:"minecraft:flower_banner_pattern",count:1,components:{"minecraft:item_model":"mg:hat/santa"}}'
ELF_GREEN = 3050286
ELF_RED = 13369344


def witch_body():
    nm = C.js({'text': 'Sorcière', 'color': 'gold'})
    return [OVW + f'summon minecraft:witch {POS} {{Rotation:[{YAW}f,0f],Tags:{C.js(TAGS_BODY)},NoAI:1b,Silent:1b,Invulnerable:1b,'
            f'PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CustomName:{nm},'
            'equipment:{mainhand:{id:"minecraft:suspicious_stew",count:1}},drop_chances:{mainhand:0f}}']


def elf_body():
    """Mannequin immobile à l'échelle 0,8 ; bonnet de Noël du resource pack si $rp = 1, sinon casque en cuir rouge."""
    nm = C.js({'text': 'Lutin de Noël', 'color': 'green'})
    worn = ','.join(f'{s}:' + LEATHER.format(p=p, c=ELF_GREEN) for s, p in (('chest', 'chestplate'), ('legs', 'leggings'), ('feet', 'boots')))
    out = []
    for cond, head in (('if', SANTA), ('unless', LEATHER.format(p='helmet', c=ELF_RED))):
        out.append(f'execute {cond} score $rp mg.st matches 1 in minecraft:overworld run summon minecraft:mannequin {POS} '
                   f'{{Rotation:[{YAW}f,0f],Tags:{C.js(TAGS_BODY)},NoGravity:1b,Invulnerable:1b,Silent:1b,'
                   f'immovable:1b,hide_description:1b,CustomName:{nm},attributes:[{{id:"minecraft:scale",base:0.8}}],'
                   f'equipment:{{head:{head},{worn}}}}}')
    return out


# ------------------------------------------------------------------ cadeaux
def gate(icon, color):
    """Recharge pas finie, ou déjà 2 objets du PNJ en main : le joueur (@s) repart sans cadeau."""
    return [f'execute if score @s mg.thc matches 1.. run return run title @s actionbar [{{"text":"{icon} Reviens dans ","color":"{color}"}},'
            '{"score":{"name":"@s","objective":"mg.thc"},"color":"yellow"},{"text":" s","color":"' + color + '"}]',
            f'execute store result score $thg mg.st run clear @s {GIFT} 0',
            f'execute if score $thg mg.st matches 2.. run return run title @s actionbar {{"text":"{icon} Utilise d\'abord ton cadeau !","color":"{color}"}}']


STEW_EFFECTS = [('invisibility', 400), ('glowing', 200), ('nausea', 160), ('darkness', 200), ('hunger', 200), ('luck', 400)]


def stew(effect, ticks):
    return ('minecraft:suspicious_stew[minecraft:custom_data={mg_thg:1b},minecraft:custom_name={"text":"Ragoût mystère","color":"gold","italic":false},'
            'minecraft:lore=[{"text":"Une sorcière y a jeté un peu de tout…","color":"gray","italic":false},'
            '{"text":"Effet : surprise !","color":"dark_purple","italic":false}],'
            f'minecraft:food={{nutrition:0,saturation:0f,can_always_eat:true}},!minecraft:use_remainder,'
            f'minecraft:suspicious_stew_effects=[{{id:"minecraft:{effect}",duration:{ticks}}}]]')


STAR = ('minecraft:firework_star[minecraft:custom_data={mg_thg:1b,mg_thfw:1b},minecraft:item_model="minecraft:firework_rocket",'
        'minecraft:custom_name={"text":"Feu d\'artifice du lutin","color":"red","italic":false},'
        'minecraft:lore=[{"text":"Clic droit à ciel ouvert : il part tout seul.","color":"gray","italic":false}],'
        'minecraft:enchantment_glint_override=true,'
        'minecraft:consumable={consume_seconds:0.05f,animation:"none",sound:"minecraft:entity.firework_rocket.launch",has_consume_particles:false},'
        'minecraft:use_cooldown={seconds:1.5f}]')


def witch_give():
    lines = ['# 🎃 La sorcière donne un ragoût mystère (@s = joueur) ; appelé par lobby/theme/npc_use'] + gate('🎃', 'gold')
    lines.append(f'execute store result score $thr mg.st run random value 1..{len(STEW_EFFECTS)}')
    lines += [f'execute if score $thr mg.st matches {i} run give @s {stew(e, t)}' for i, (e, t) in enumerate(STEW_EFFECTS, 1)]
    return lines + [f'scoreboard players set @s mg.thc {COOLDOWN}',
                    'execute at @s run playsound minecraft:entity.witch.celebrate neutral @a[distance=..16] ~ ~ ~ 1 1',
                    'execute at @e[type=minecraft:interaction,tag=mg.thnpci,limit=1] run particle minecraft:witch ~ ~1 ~ 0.3 0.5 0.3 0.05 15 normal',
                    'title @s actionbar {"text":"🎃 Hihihi… un ragoût mystère !","color":"gold"}']


def elf_give():
    lines = ['# 🎄 Le lutin donne trois feux d\'artifice (@s = joueur) ; appelé par lobby/theme/npc_use'] + gate('🎄', 'green')
    return lines + [f'give @s {STAR} 3', 'scoreboard players add @s mg.thfw 3', f'scoreboard players set @s mg.thc {COOLDOWN}',
                    'execute at @s run playsound minecraft:block.note_block.bell neutral @a[distance=..16] ~ ~ ~ 1 1.2',
                    'execute at @e[type=minecraft:interaction,tag=mg.thnpci,limit=1] run particle minecraft:happy_villager ~ ~1 ~ 0.3 0.5 0.3 0.05 15 normal',
                    'title @s actionbar {"text":"🎄 Joyeux Noël ! À lancer à ciel ouvert.","color":"green"}']


# nom, couleur du nom, taille de la zone cliquable (largeur, hauteur), hauteur de l'indication, corps, cadeau
NPCS = {'witch': ('🎃 Sorcière', 'gold', (0.9, 2.1), 2.45, witch_body, witch_give),
        'elf': ('🎄 Lutin de Noël', 'green', (0.7, 1.6), 1.95, elf_body, elf_give)}


def write_npc(T, label, kind):
    """Écrit T/npc et T/npc_give ; renvoie (lignes de reskin, lignes de fx, lignes de off) du thème."""
    name, color, (wd, ht), hy, body, give = NPCS[kind]
    hint = C.js([{'text': name, 'color': color, 'bold': True}, {'text': '\nClic droit', 'color': 'yellow'}])
    C.w(f'{T}/npc', [f'# {label} : PNJ « {name} » (corps, zone cliquable, indication) ; idempotent, appelé par {T}/reskin et chaque seconde par {T}/fx',
                     f'execute in minecraft:overworld unless loaded {LOADED} run return 0',
                     'execute as @e[tag=mg.thnpc,tag=mg.thmob] run function mg:lobby/theme/gone', 'kill @e[tag=mg.thnpc]'] + body() +
      [OVW + f'summon minecraft:interaction {POS} {{Tags:{C.js(TAGS_INT)},width:{wd}f,height:{ht}f,response:1b}}',
       OVW + f'summon minecraft:text_display {SPOT[0] + 0.5} {SPOT[1] + hy} {SPOT[2] + 0.5} {{Tags:{C.js(TAGS_HINT)},billboard:"center",'
       f'background:0,shadow:1b,text:{hint}}}'])
    C.w(f'{T}/npc_give', give())
    return ([f'function mg:{T}/npc'],
            [f'execute in minecraft:overworld unless score $thrs mg.st matches 1.. if loaded {LOADED} {m} run function mg:{T}/npc'
             for m in ('unless entity @e[type=minecraft:interaction,tag=mg.thnpci]', 'unless entity @e[tag=mg.thnpc,tag=mg.thmob]')],
            [f'clear @a[tag=!mg.surv] {GIFT}', 'scoreboard players reset @a[tag=!mg.surv] mg.thfw'])


# ------------------------------------------------------------------ fonctions communes
FIREWORKS = [('star', '[I;11743532]', '[I;16777215]', 'has_trail:true'),            # rouge
             ('large_ball', '[I;3887386]', '[I;15790320]', 'has_twinkle:true'),      # vert
             ('burst', '[I;15790320]', '[I;12040119]', 'has_twinkle:true'),          # blanc
             ('star', '[I;15435844]', '[I;11743532]', 'has_trail:true,has_twinkle:true')]   # or


def write_common(themes):
    """themes = [(id, clé)] des thèmes qui ont un PNJ. Écrit npc_use, npc_second, fw_use et l'advancement mg:theme_fw."""
    w = C.w
    who = 'if entity @s[tag=!mg.play,tag=!mg.surv,gamemode=!spectator]'
    w('lobby/theme/npc_use', ['# @s : zone cliquable du PNJ cliqué (appelé chaque tick par lobby/theme/tick) : cadeau du thème en place'] +
      [f'execute if data entity @s interaction on target {who} if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/npc_give'
       for tid, key in themes] +
      [f'execute if data entity @s attack on attacker {who} if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/npc_give'
       for tid, key in themes] + ['data remove entity @s interaction', 'data remove entity @s attack'])
    w('lobby/theme/npc_second', ['# Chaque seconde (lobby/theme/tick) : recharge des cadeaux, objets retirés aux joueurs occupés ailleurs',
                                 'scoreboard players remove @a[scores={mg.thc=1..}] mg.thc 1'] + [f'clear @a[tag={t}] {GIFT}' for t in BUSY])
    sky = ' '.join(f'if block ~ ~{dy} ~ #mg:sky_clear' for dy in range(2, 15))
    w('lobby/theme/fw_use', ['# 🎄 Étoile de feu d\'artifice consommée (advancement mg:theme_fw ; @s = joueur) : fusée à 4 explosions de Noël, tirée au hasard',
                             'advancement revoke @s only mg:theme_fw',
                             '# budget épuisé (étoile de coffre ou ramassée) : consommée sans effet',
                             'execute unless score @s mg.thfw matches 1.. run return run title @s actionbar {"text":"🎄 Plus de feu d\'artifice à lancer.","color":"gray"}',
                             f'execute store success score $thf mg.st {sky}',
                             'execute if score $thf mg.st matches 0 run title @s actionbar {"text":"🎄 À ciel ouvert !","color":"red"}',
                             'execute if score $thf mg.st matches 0 run return run function mg:lobby/theme/fw_back',
                             '# l\'explosion (~10 blocs plus haut, rayon de dégâts 5) ne doit blesser personne',
                             'execute store success score $thf mg.st positioned ~ ~10 ~ if entity @a[distance=..6]',
                             'execute if score $thf mg.st matches 1 run title @s actionbar {"text":"🎄 Trop de monde autour !","color":"red"}',
                             'execute if score $thf mg.st matches 1 run return run function mg:lobby/theme/fw_back',
                             'scoreboard players remove @s mg.thfw 1',
                             f'execute store result score $thr mg.st run random value 1..{len(FIREWORKS)}'] +
      [f'execute if score $thr mg.st matches {i} at @s run summon minecraft:firework_rocket ~ ~2 ~ {{LifeTime:20,FireworksItem:{{id:"minecraft:firework_rocket",'
       f'count:1,components:{{"minecraft:fireworks":{{flight_duration:1,explosions:[{{shape:"{sh}",colors:{c},fade_colors:{f},{fl}}}]}}}}}}}}'
       for i, (sh, c, f, fl) in enumerate(FIREWORKS, 1)])
    w('lobby/theme/fw_back', ['# Feu d\'artifice refusé (@s = joueur) : l\'étoile consommée lui est rendue (sauf en créatif : elle n\'est pas consommée)',
                              'execute if entity @s[gamemode=creative] run return 0', f'give @s {STAR} 1'])
    tag = os.path.join(C.D, 'tags', 'block', 'sky_clear.json')      # « ciel dégagé » : air, ou bloc de lumière (invisible)
    os.makedirs(os.path.dirname(tag), exist_ok=True)
    with open(tag, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps({'values': ['#minecraft:air', 'minecraft:light']}, indent=2) + '\n')
    path = os.path.join(C.D, 'advancement', 'theme_fw.json')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    adv = {'criteria': {'fw': {'trigger': 'minecraft:consume_item', 'conditions': {'item': {'predicates': {
        'minecraft:custom_data': '{mg_thfw:1b}'}}}}}, 'rewards': {'function': 'mg:lobby/theme/fw_use'}}
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(adv, indent=2, ensure_ascii=False) + '\n')


def wire():
    """Objectif de recharge, boucle de clic, recharge à la seconde, nettoyages (partie, désinstallation, sweep sans thème)."""
    C.objectives([('mg.thc', 'dummy'), ('mg.thfw', 'dummy')])
    C.patch('lobby/theme/tick', 'scoreboard players add $tht mg.st 1',
            ['execute as @e[type=minecraft:interaction,tag=mg.thnpci] if data entity @s interaction run function mg:lobby/theme/npc_use',
             'execute as @e[type=minecraft:interaction,tag=mg.thnpci] if data entity @s attack run function mg:lobby/theme/npc_use'], where='before')
    C.patch('lobby/theme/tick', 'scoreboard players set $tht mg.st 0', ['function mg:lobby/theme/npc_second'])
    # lancement d'une partie : plus de cadeau ni d'effet de ragoût chez les participants
    C.patch('core/request', 'clear @a[tag=!mg.surv] minecraft:snowball',
            [f'clear @a[tag=!mg.surv] {GIFT}', 'scoreboard players reset @a[tag=!mg.surv] mg.thfw'] + [f'effect clear @a[tag=mg.play] minecraft:{e}' for e, _ in STEW_EFFECTS])
    # sans thème (ancien monde) : les restes du PNJ (zone cliquable, indication) partent avec le corps, au même balayage
    C.patch('core/tick', 'execute if score $lan mg.t matches 30 unless score $theme mg.st matches 1.. unless data storage mg:lobby theme '
            'as @e[tag=mg.thmob] run function mg:lobby/theme/gone',
            ['execute if score $lan mg.t matches 30 unless score $theme mg.st matches 1.. unless data storage mg:lobby theme run kill @e[tag=mg.thnpc]'])
    C.patch('desinstaller', 'kill @e[tag=mg.npc]',
            [f'clear @a {GIFT}', 'kill @e[tag=mg.thnpc]', 'advancement revoke @a only mg:theme_fw',
             f'execute as @e[type=minecraft:item] if items entity @s contents {GIFT} run kill @s'])
