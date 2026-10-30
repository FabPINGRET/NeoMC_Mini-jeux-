"""🪑 S'asseoir et emotes au spawn (lobby seulement) : python tools/lobby/gen_sit.py .
(depuis la racine ; idempotent ; APRÈS tools/cosmetics/gen_hats.py, AVANT tools/variantes/gen_variants.py qui passe en dernier ;
aussi APRÈS tools/lobby/gen_lobby.py et tools/hall/gen_hall.py, dont il relit les constructions (bancs, conteneurs) : à relancer après eux)

- 🪑 S'asseoir (mg.opt 76, bouton du menu Échap) : sur un banc sous les pieds ou adjacent (spruce_stairs[half=bottom] :
  ceux de gen_lobby.py), sinon par terre ; on se lève avec le même bouton, Maj ou en quittant le spawn. Le siège est un
  item_display (tag mg.seat) que le joueur monte (tag mg.sit). Réglage de hauteur : SEAT_DY (banc) et GROUND_DY (sol), à ajuster en jeu.
  Un banc occupé (siège à moins de 0,3) est sauté : sit/bench_at, appelé pour chaque candidat de sit/bench, retourne 0.
- Clic droit sur un banc du spawn ou du Hall : s'y assoit (ou se lève s'il y est déjà) ; zones cliquables, liste des bancs et advancement
  dans sit_bench.py (importé ici, jamais lancé seul).
- 🎉 Objet « Emotes » (pomme de terre empoisonnée habillée en éclat d'améthyste, hotbar.8, clic droit = fenêtre des emotes) : donné,
  retiré, rendu et purgé des conteneurs du spawn par sit_item.py (importé ici).
- 🎉 Emotes (mg.opt 83 : fenêtre mg:lobby_emotes ; 77 ✋ Salut, 78 ♪ Danse, 79 🎉 Fête, 80 😵 Étourdi) : particules et son à 16 blocs,
  message en actionbar à 10 blocs, recharge 3 s (mg.lsc = tick de la dernière emote), et un mouvement du joueur (coups de bras, rotation :
  sit_move.py, importé ici ; mg.lsk = emote en cours, mg.lse = image, tag mg.lsm).
- Admin (menu 🎉 Événements du lobby) : 81 coupe / rétablit tout cela ($sitoff mg.st = 1 : coupé, absent : actif), 82 affiche
  les compteurs d'usage (mg.lsn : $sit, $emo1..4, $itm objet, $bnc clic sur un banc). Couper retire aussi les zones des bancs et l'objet.
- Refus (sit/ok) : hors du spawn, partie / survie / plot / visite / parkour / kart / élytra / duel / GTA / Terra Nova / Mini Party /
  mini-moi du ragoût, spectateur, déjà en véhicule, arène PvP et terrain de foot souterrains : message court en actionbar.
- Une partie qui démarre (core/request), core/load et desinstaller relèvent les joueurs et retirent les sièges ; core/tick appelle
  lobby/sit/tick (sièges orphelins : Maj vanilla, reconnexion) tant qu'un joueur est assis et vide les sièges sinon.
Tags : mg.sit (joueur assis), mg.seat (siège), mg.seatn (siège en cours de pose), mg.seato (candidat orphelin, balayage de sit/tick) ;
mg.bench, mg.lbc (sit_bench.py) ; mg.lsg, mg.lsw (sit_item.py) ; mg.lsm (sit_move.py).
mg.opt 76..83 ; objectifs mg.lsc, mg.lsn, mg.lsb (recharge du clic sur un banc), mg.lse, mg.lsk (sit_move.py).
Relancer ce script après gen_events.py (qui réécrit dialog/lobby_events.json, donc les boutons 81 et 82) ; après gen_tp_general.py
les lignes de core/opt changent seulement d'ordre. Glyphes : seulement ceux déjà présents dans data/.
"""
import json
import os
import runpy
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arcade'))
import common as C
import sit_bench as SB                                              # noqa: E402
import sit_item as SI                                               # noqa: E402
import sit_move as SM                                               # noqa: E402
from foot_build import FOOT_ZONE
from theme_world import LOBBY_BOX

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
BENCHES = SB.benches()                   # avant toute écriture : le générateur s'arrête ici si les bancs (spawn, Hall) sont introuvables
w, js = C.w, C.js
SEAT_DY = 0.5                            # hauteur du siège au-dessus du bloc d'un escalier (surface basse) : à régler en jeu
GROUND_DY = 0                            # idem sur le sol, au niveau des pieds
OPT_SIT, OPT_EMOTE, OPT_TOGGLE, OPT_STATS, OPT_MENU = 76, 77, 81, 82, 83     # emotes : 77..80
COOLDOWN = 60                            # ticks entre deux emotes
PVP_ZONE = 'x=-12,y=40,z=-10,dx=51,dy=20,dz=45'     # le souterrain PvP (ZONE de gen_pvpcave.py) : pas d'assise
# le terrain de foot souterrain (FOOT_ZONE de foot_build.py, constantes seules : l'import ne lance rien) : pas d'assise non plus
# Tags « occupé ailleurs » : BUSY de sit_item.py (liste partagée avec la pêche, gen_fish.py)
BUSY = SI.BUSY
OK_SEL = f'@s[{LOBBY_BOX},' + ','.join(f'tag=!{t}' for t in BUSY) + ',gamemode=!spectator]'
FACING = [('east', 90), ('west', -90), ('north', 0), ('south', 180)]      # facing de l'escalier -> yaw du siège (dos au dossier)
# où chercher un banc : sous les pieds (debout sur le dossier), aux pieds (marche basse), puis les 4 voisins
AT = [(0, -1, 0), (0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]
NOTE = lambda t: {'text': t, 'color': 'gray'}                          # noqa: E731
# emote : (numéro, glyphe, nom, couleur, verbe, particule (nom, dy, dx, dy, dz, vitesse, nombre), son, hauteur du son)
EMOTES = [(1, '✋', 'Salut', 'gold', 'salue tout le monde !', ('happy_villager', 2, 0.4, 0.3, 0.4, 0, 8), 'entity.villager.yes', 1.2),
          (2, '♪', 'Danse', 'aqua', 'danse !', ('note', 2.2, 0.6, 0.2, 0.6, 1, 6), 'block.note_block.bell', 1.5),
          (3, '🎉', 'Fête', 'light_purple', 'fait la fête !', ('firework', 1.5, 0.5, 0.6, 0.5, 0.12, 20), 'entity.firework_rocket.twinkle', 1),
          (4, '😵', 'Étourdi', 'yellow', 'est étourdi...', ('crit', 2.1, 0.35, 0.1, 0.35, 0.15, 10), 'entity.villager.hurt', 1.3)]


def rel(v):
    return '~' if not v else f'~{v}'


def actionbar(text, color='gray'):
    return 'title @s actionbar ' + js({'text': text, 'color': color})


# ---------------------------------------------------------------- vérifications : ok (silencieux), can (avec messages)
w('lobby/sit/ok', ['# @s : peut être assis / faire une emote ici ? Retourne 1 ou 0, sans message (sit/tick s\'en sert pour relever)',
                   '# core/opt tourne sans « at @s » : la dimension se lit à la position du joueur',
                   'execute at @s unless dimension minecraft:overworld run return 0',
                   'execute if score $sitoff mg.st matches 1 run return 0',
                   f'execute unless entity {OK_SEL} run return 0',
                   f'execute if entity @s[{PVP_ZONE}] run return 0',
                   f'execute if entity @s[{FOOT_ZONE}] run return 0',
                   'return 1'])
w('lobby/sit/can', ['# @s : peut s\'asseoir / faire une emote ? Retourne 1 ou 0 ; refus : message court en actionbar',
                    'execute if score $sitoff mg.st matches 1 run ' + actionbar('🪑 Assis et emotes désactivés par un admin.'),
                    'execute if score $sitoff mg.st matches 1 run return 0',
                    'execute unless function mg:lobby/sit/ok run ' + actionbar('🪑 Pas possible ici (au spawn, hors activité).'),
                    'execute unless function mg:lobby/sit/ok run return 0',
                    '# déjà dans un véhicule (kart...) : non ; assis, c\'est notre propre siège',
                    'execute unless entity @s[tag=mg.sit] if predicate mg:in_vehicle run ' + actionbar('🪑 Descends d\'abord de ton véhicule.'),
                    'execute unless entity @s[tag=mg.sit] if predicate mg:in_vehicle run return 0',
                    'return 1'])

# ---------------------------------------------------------------- s'asseoir : try -> bench / sol -> seat ; stand ; tick
w('lobby/sit/try', ['# @s : bouton « S\'asseoir » (mg.opt 76) : se lève si déjà assis, sinon banc sous les pieds ou adjacent, sinon par terre',
                    'execute if entity @s[tag=mg.sit] run return run function mg:lobby/sit/stand',
                    'execute unless function mg:lobby/sit/can run return 0',
                    'execute unless entity @s[nbt={OnGround:1b}] run return run ' + actionbar('🪑 Pose-toi d\'abord au sol.'),
                    '# core/opt tourne sans « at @s » : les coordonnées relatives de sit/bench se lisent à la position du joueur',
                    'execute at @s if function mg:lobby/sit/bench run return 1',
                    f'execute at @s positioned ~ {rel(GROUND_DY)} ~ run return run function mg:lobby/sit/seat'])
w('lobby/sit/bench', ['# @s : un banc (spruce_stairs[half=bottom]) sous les pieds ou à côté, et libre ? Oui : s\'y assoit (sit/seat), retourne 1 ; non : retourne 0',
                      '# un banc occupé est sauté (sit/bench_at retourne 0) : le candidat suivant, puis le sol'] +
  [f'execute positioned {p} align xyz if function mg:lobby/sit/bench_at run return 1' for p in (' '.join(rel(v) for v in a) for a in AT)] +
  ['return 0'])
w('lobby/sit/bench_at', ['# @s : position = coin du bloc (align xyz). Banc libre (pas de siège à moins de 0,3) ? Oui : s\'y assoit (sit/seat), retourne 1 ; non : 0',
                         f'# siège au centre du bloc, {SEAT_DY} au-dessus de son pied (SEAT_DY) ; regard vers la marche basse : yaw opposé au facing '
                         '(east 90, west -90, north 0, south 180)',
                         f'execute positioned ~0.5 {rel(SEAT_DY)} ~0.5 if entity @e[type=minecraft:item_display,tag=mg.seat,distance=..0.3] run return 0'] +
  [f'execute if block ~ ~ ~ minecraft:spruce_stairs[half=bottom,facing={f}] positioned ~0.5 {rel(SEAT_DY)} ~0.5 '
   f'rotated {yaw} 0 run return run function mg:lobby/sit/seat' for f, yaw in FACING] + ['return 0'])
w('lobby/sit/seat', ['# @s = joueur ; position = point d\'assise, rotation = sens du regard (posés par sit/try ou sit/bench) ; retourne 1',
                     'summon minecraft:item_display ~ ~ ~ {Tags:["mg.seat","mg.seatn"]}',
                     '# s\'asseoir arrête le mouvement d\'une emote en cours (sit_move.py), avant le tp qui fixe le regard',
                     'execute if entity @s[tag=mg.lsm] run function mg:lobby/sit/move_stop',
                     'tp @s ~ ~ ~ ~ ~',
                     'execute store success score #sitm mg.st run ride @s mount @e[type=minecraft:item_display,tag=mg.seatn,distance=..1,sort=nearest,limit=1]',
                     'execute if score #sitm mg.st matches 1 run tag @s add mg.sit',
                     'execute if score #sitm mg.st matches 1 run scoreboard players add $sit mg.lsn 1',
                     'execute if score #sitm mg.st matches 1 run ' + actionbar('🪑 Assis · Maj pour te lever'),
                     'execute if score #sitm mg.st matches 0 run ' + actionbar('🪑 Impossible de s\'asseoir ici.'),
                     'execute if score #sitm mg.st matches 0 run kill @e[type=minecraft:item_display,tag=mg.seatn,distance=..1]',
                     'tag @e[type=minecraft:item_display,tag=mg.seatn] remove mg.seatn',
                     'return 1'])
w('lobby/sit/stand', ['# @s : se lève. Le siège occupé est retiré (le joueur en descend) ; aucun autre véhicule n\'est touché',
                      'execute on vehicle if entity @s[type=minecraft:item_display,tag=mg.seat] run kill @s',
                      'tag @s remove mg.sit'])
w('lobby/sit/tick', ['# Appelé chaque tick (core/tick) tant qu\'un joueur porte mg.sit',
                     '# refus (partie, survie, plot, coupé par un admin...) : on se lève',
                     'execute as @a[tag=mg.sit] unless function mg:lobby/sit/ok run function mg:lobby/sit/stand',
                     '# balayage : tout siège et tout assis sont candidats (mg.seato) ; chacun perd la marque s\'il est lié à l\'autre',
                     'tag @e[type=minecraft:item_display,tag=mg.seat] add mg.seato',
                     'tag @a[tag=mg.sit] add mg.seato',
                     'execute as @a[tag=mg.sit] on vehicle if entity @s[type=minecraft:item_display,tag=mg.seat] run tag @s remove mg.seato',
                     'execute as @e[type=minecraft:item_display,tag=mg.seat] on passengers if entity @s[tag=mg.sit] run tag @s remove mg.seato',
                     '# restent : les assis sans siège (Maj vanilla, reconnexion, mort) et les sièges sans assis',
                     'execute as @a[tag=mg.seato] run function mg:lobby/sit/stand',
                     'kill @e[type=minecraft:item_display,tag=mg.seato]',
                     'tag @a remove mg.seato'])

# ---------------------------------------------------------------- emotes
for k, glyph, name, col, verb, (pn, py, dx, dy, dz, sp, n), sound, pitch in EMOTES:
    w(f'lobby/sit/emote_{k}', [
        f'# Emote {glyph} {name} (mg.opt {OPT_EMOTE + k - 1}, @s = joueur) : particules et son à 16 blocs, message à 10 blocs, recharge {COOLDOWN // 20} s',
        'execute unless function mg:lobby/sit/can run return 0',
        'execute store result score #sitn mg.st run time query gametime',
        'scoreboard players operation #sitc mg.st = @s mg.lsc',
        f'scoreboard players add #sitc mg.st {COOLDOWN}',
        'execute if score @s mg.lsc matches 1.. if score #sitn mg.st < #sitc mg.st run return run ' + actionbar('⏳ Patiente un instant...'),
        'scoreboard players operation @s mg.lsc = #sitn mg.st',
        f'scoreboard players add $emo{k} mg.lsn 1',
        f'execute at @s run particle minecraft:{pn} ~ {rel(py)} ~ {dx} {dy} {dz} {sp} {n} normal @a[distance=..16]',
        f'execute at @s run playsound minecraft:{sound} player @a[distance=..16] ~ ~ ~ 1 {pitch}',
        'execute at @s run title @a[distance=..10,tag=!mg.play,tag=!mg.pkr,tag=!mg.lk,tag=!mg.ely,tag=!mg.elyf] actionbar ' + js(
            [{'text': glyph + ' ', 'color': col}, {'selector': '@s', 'color': 'yellow'}, NOTE(' ' + verb)])] +
        SM.start_lines(k))
w('lobby/sit/menu', ['# @s : fenêtre des emotes', 'dialog show @s mg:lobby_emotes'])

# ---------------------------------------------------------------- admin : activer / couper, compteurs
w('lobby/sit/admin_toggle', ['# Admin (@s) : coupe / rétablit l\'assise, les emotes, l\'objet 🎉 et les zones des bancs du lobby ($sitoff mg.st = 1 : coupé, absent : actif)',
                             'execute store success score #sitw mg.st if score $sitoff mg.st matches 1',
                             'execute if score #sitw mg.st matches 1 run scoreboard players reset $sitoff mg.st',
                             '# $lbx absent : sit/bench_check repose les zones des bancs au prochain passage (toutes les 2 s)',
                             'execute if score #sitw mg.st matches 1 run scoreboard players reset $lbx mg.st',
                             'execute if score #sitw mg.st matches 1 run return run tellraw @s ' + js({'text': '🪑 Assis et emotes du lobby : activés.', 'color': 'green'}),
                             'scoreboard players set $sitoff mg.st 1',
                             'execute as @a[tag=mg.sit] run function mg:lobby/sit/stand',
                             SB.KILL,
                             f'clear @a {SI.PRED}',
                             'tellraw @s ' + js({'text': '🪑 Assis et emotes du lobby : désactivés.', 'color': 'red'})])
COUNTERS = [('$sit', '🪑 Assis'), ('$bnc', '🪑 Clic banc'), ('$itm', '🎉 Objet')] + [(f'$emo{k}', f'{g} {nm}') for k, g, nm, *_ in EMOTES]
w('lobby/sit/admin_stats', ['# Admin (@s) : compteurs d\'usage (assis, emotes), depuis la création de l\'objectif mg.lsn'] +
  [f'execute unless score {n} mg.lsn matches 0.. run scoreboard players set {n} mg.lsn 0' for n, _ in COUNTERS] +
  ['execute if score $sitoff mg.st matches 1 run tellraw @s ' + js({'text': '🪑 Assis et emotes : désactivés', 'color': 'red'}),
   'execute unless score $sitoff mg.st matches 1 run tellraw @s ' + js({'text': '🪑 Assis et emotes : activés', 'color': 'green'}),
   'tellraw @s ' + js([{'text': 'Usage : ', 'color': 'gray'}] + sum([[
       {'text': ('' if i == 0 else ' · ') + lab + ' ', 'color': 'white'},
       {'score': {'name': n, 'objective': 'mg.lsn'}, 'color': 'yellow'}] for i, (n, lab) in enumerate(COUNTERS)], []))])

# ---------------------------------------------------------------- fenêtres : emotes (écrite ici), boutons du menu Échap et des événements
def act(label, color, opt, tip):
    return {'label': [{'text': label, 'color': color, 'bold': True}], 'tooltip': [{'text': tip, 'color': 'gray'}],
            'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.opt set {opt}'}}


def write_json(path, d):
    with open(os.path.join(C.D, 'dialog', path), 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')


def add_buttons(path, buttons, before=None):
    """Insère les boutons absents (clé : leur commande) dans une fenêtre, avant le bouton de commande « before » (sinon à la fin) ;
    l'infobulle des boutons déjà présents est alignée sur celle d'ici."""
    p = os.path.join(C.D, 'dialog', path)
    d = json.load(open(p, encoding='utf-8'))
    have = {a['action'].get('command'): a for a in d['actions']}
    new = [b for b in buttons if b['action']['command'] not in have]
    stale = [(have[b['action']['command']], b) for b in buttons if b['action']['command'] in have
             and have[b['action']['command']].get('tooltip') != b['tooltip']]
    for old, b in stale:                                  # bouton déjà là : seule l'infobulle est remise à jour
        old['tooltip'] = b['tooltip']
    if not new and not stale:
        return
    i = next((i for i, a in enumerate(d['actions']) if a['action'].get('command') == before), len(d['actions']))
    d['actions'][i:i] = new
    write_json(path, d)


write_json('lobby_emotes.json', {
    'type': 'minecraft:multi_action', 'title': {'text': '🎉 Emotes', 'color': 'light_purple', 'bold': True},
    'pause': False, 'can_close_with_escape': True,
    'body': [{'type': 'minecraft:plain_message', 'contents': [
        {'text': f'Une emote animée, visible par les joueurs autour de toi (spawn seulement, une toutes les {COOLDOWN // 20} s).', 'color': 'gray'}]}],
    'columns': 2, 'exit_action': {'label': [{'text': 'Fermer', 'color': 'gray'}]},
    'actions': [act(f'{g} {nm}', c, OPT_EMOTE + k - 1, f'Fait une emote « {nm} »') for k, g, nm, c, *_ in EMOTES] +
               [act('🪑 S\'asseoir / se lever', 'gold', OPT_SIT, 'Sur un banc sous les pieds ou adjacent, sinon par terre, ou clic droit sur un banc ; Maj pour se lever')]})
add_buttons('main_menu.json', [
    act('🪑 S\'asseoir', 'gold', OPT_SIT, 'Sur un banc sous les pieds ou adjacent, sinon par terre (spawn), ou clic droit sur un banc ; Maj ou le même bouton pour se lever'),
    act('🎉 Emotes ▸', 'light_purple', OPT_MENU, 'Salut, danse, fête, étourdi : une emote visible autour de toi (spawn)')],
    before='trigger mg.sv set 3')
add_buttons('lobby_events.json', [
    act('🪑 Assis/emotes on/off', 'gold', OPT_TOGGLE, 'Active ou coupe l\'assise et les emotes du lobby (actif par défaut)'),
    act('🪑 Stats', 'aqua', OPT_STATS, 'Affiche les compteurs d\'usage (assis, emotes)')], before='trigger mg.menu')

# texte d'accueil du menu Échap (écrit par un autre générateur) : mentionne l'assise et les emotes
p = os.path.join(C.D, 'dialog', 'main_menu.json')
d = json.load(open(p, encoding='utf-8'))
txt = d['body'][0]['contents'][0]
if txt['text'] == 'Survie, Mini Party et aide.':
    txt['text'] = 'Survie, Mini Party, assis/emotes et aide.'
    write_json('main_menu.json', d)

# menu texte de repli des événements (lobby/ev/menu_chat, réécrit par gen_events.py) : les deux boutons admin, après le dernier (Déco Noël)
CHAT_LAST = ('🎄 Déco Noël', 'red', 74, 'Pose ou retire le décor de Noël du spawn (réversible)')    # dernier EV_BTN de gen_events.py


def chat_line(t, c, o, tip):
    return ('tellraw @s ["",' + js({'text': ' [' + t + ']', 'color': c, 'click_event': {'action': 'run_command', 'command': f'trigger mg.opt set {o}'},
                                    'hover_event': {'action': 'show_text', 'value': tip}}) + ']')


C.patch('lobby/ev/menu_chat', chat_line(*CHAT_LAST), [
    chat_line('🪑 Assis/emotes on/off', 'gold', OPT_TOGGLE, 'Active ou coupe l\'assise et les emotes du lobby (actif par défaut)'),
    chat_line('🪑 Stats', 'aqua', OPT_STATS, 'Affiche les compteurs d\'usage (assis, emotes)')])

# ---------------------------------------------------------------- câblage (une ligne par patch)
C.objectives([('mg.lsc', 'dummy'), ('mg.lsn', 'dummy')])
C.objectives([('mg.lsb', 'dummy')])                                     # recharge du clic sur un banc (sit_bench.py)
ANCHOR = 'scoreboard objectives add mg.st dummy'
KILL = 'kill @e[type=minecraft:item_display,tag=mg.seat]'
UNTAG = 'tag @a remove mg.sit'
C.patch('core/load', ANCHOR, [KILL])
C.patch('core/load', KILL, [UNTAG])
C.patch('core/load', KILL, ['# Sièges du lobby (s\'asseoir)'], where='before')
C.patch('desinstaller', 'kill @e[tag=mg.npc]', [KILL])
C.patch('desinstaller', KILL, [UNTAG])
TICK = 'execute if entity @a[tag=mg.sit] run function mg:lobby/sit/tick'
C.patch('core/tick', 'execute if entity @a[tag=mg.visit] run function mg:plot/visit_guard', [TICK])
# sièges sans aucun assis : balayage toutes les 2 s (même cadence que les nettoyages voisins : $lan mg.t = 30)
SWEEP = ('execute unless entity @a[tag=mg.sit] if entity @e[type=minecraft:item_display,tag=mg.seat,limit=1] '
         'run kill @e[type=minecraft:item_display,tag=mg.seat]')
C.drop_lines('core/tick', [SWEEP])                                    # ancienne version (chaque tick)
C.patch('core/tick', TICK, ['execute if score $lan mg.t matches 30 ' + SWEEP[len('execute '):]])
C.patch('core/request', 'execute as @a[tag=mg.play,tag=mg.elyf] run function mg:elytra/free_stop',
        ['execute as @a[tag=mg.play,tag=mg.sit] run function mg:lobby/sit/stand'], where='before')
# core/opt : tout autre choix du menu relève d'abord l'assis (avant une téléportation) ; 76..83 sont les boutons d'assise et d'emotes
C.patch('core/opt', '# Options du menu (@s = joueur, mg.opt = valeur)', [
    f'execute if entity @s[tag=mg.sit] unless score @s mg.opt matches {OPT_SIT}..{OPT_MENU} run function mg:lobby/sit/stand'])
RESET = 'scoreboard players reset @s mg.opt'
for line in ([f'execute if score @s mg.opt matches {OPT_SIT} run function mg:lobby/sit/try'] +
             [f'execute if score @s mg.opt matches {OPT_EMOTE + k - 1} run function mg:lobby/sit/emote_{k}' for k, *_ in EMOTES] +
             [f'execute if score @s mg.opt matches {OPT_TOGGLE}..{OPT_STATS} unless entity @s[tag=mg.admin] run tellraw @s '
              '{"text":"⚠ Réservé aux admins.","color":"red"}',
              f'execute if score @s mg.opt matches {OPT_TOGGLE} if entity @s[tag=mg.admin] run function mg:lobby/sit/admin_toggle',
              f'execute if score @s mg.opt matches {OPT_STATS} if entity @s[tag=mg.admin] run function mg:lobby/sit/admin_stats',
              f'execute if score @s mg.opt matches {OPT_MENU} run function mg:lobby/sit/menu']):
    C.patch('core/opt', RESET, [line], where='before')
# objet 🎉 Emotes et clic droit sur un banc (sit_item.py, sit_bench.py) : fonctions et advancements, puis leurs lignes (après celles ci-dessus)
SI.write(BUSY)
SB.write(BENCHES, rel(SEAT_DY), actionbar)
SM.write(COOLDOWN)
SI.wire(UNTAG)
SB.wire(UNTAG)
SM.wire(UNTAG)
print('Assis / emotes OK :', len(EMOTES), 'emotes')

# Les notes des joueurs remplacent les étoiles dans les menus (et la fenêtre mg:lobby_emotes devient rate/d/) : à refaire après chaque régénération des menus
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rating', 'gen_rating.py'), run_name='__main__')
