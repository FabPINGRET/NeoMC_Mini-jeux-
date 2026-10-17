"""🪑 Clic droit sur un banc (importé par gen_sit.py, jamais lancé seul) : s'asseoir sur CE banc, au spawn et au Hall.

Chaque banc (spruce_stairs[half=bottom]) porte une zone cliquable : une interaction (tag mg.bench, 1,05 x 1,05) posée sur le bloc.
- Liste des bancs, jamais écrite à la main : ceux du spawn viennent de theme_world.W (les fonctions de construction du spawn), ceux du
  Hall de la lecture de hall/build.mcfunction (la sortie de tools/hall/gen_hall.py, qui s'exécute à l'import : pas importable). Le
  générateur s'arrête si une liste est vide ou si un banc n'est pas au niveau du sol du spawn (y 64). Il doit donc passer APRÈS
  gen_lobby.py et gen_hall.py, et être relancé après eux. scan() sert aussi à sit_item.py (conteneurs du spawn).
- lobby/sit/benches : repose toutes les zones (un `if block` par banc : un bloc remplacé n'a pas de zone), puis note leur nombre ($lbx mg.st).
- lobby/sit/bench_check, toutes les 2 s (core/tick, $lan mg.t = 30) : coupé par un admin = zones tuées ; sinon, une fois mg:setup fait
  et tous les chunks de bancs chargés (`if loaded`, un par chunk : les zones d'un chunk déchargé ne se comptent pas), les zones dont le
  bloc n'est plus un banc sont tuées, puis si le nombre de zones diffère de $lbx : benches. Les chunks du Hall (x -10..-7, z 19..31)
  sont déjà dans le forceload du spawn (-16..16).
- Clic : advancement mg:lobby_bench (player_interacted_with_entity sur une interaction mg.bench) -> bench_adv -> bench_hit (la zone
  qui a reçu le clic de CE joueur : mg.lbc) -> bench_click (@s = joueur, position = banc) : se lève s'il est assis sur ce banc, sinon
  s'assoit (sit/can puis sit/bench_at). Recharge de 10 ticks par joueur (mg.lsb = tick du dernier clic).
Tags : mg.bench (zone), mg.lbc (joueur qui vient de cliquer). Compteurs : $bnc (mg.lsn), $lbx (mg.st).
"""
import json
import os

import common as C
import theme_world as TW

OVW = 'execute in minecraft:overworld '
ZONES = 'minecraft:interaction,tag=mg.bench'
KILL = f'kill @e[type={ZONES}]'
CLICK_DELAY = 10                         # ticks entre deux clics d'un même joueur
SECOND_LINE = 'execute if score $lan mg.t matches 30 run function mg:lobby/sit/bench_check'
HEADER = '# Désinstallation (OP) — retire scoreboards, équipes, décor et zones chargées'     # ancre commune (theme_core.py)
HEADER_NOTE = ('# À lancer depuis le spawn (chunks chargés) : les zones de bancs (interaction mg.bench) d\'un chunk non chargé '
               'survivent à la désinstallation')


def is_bench(blk):
    return TW.bid(blk) == 'minecraft:spruce_stairs' and TW.states(blk).get('half', 'bottom') == 'bottom'


def scan(wanted):
    """Positions des blocs dont wanted(bloc) est vrai : (spawn, hall). Spawn : theme_world.W (relu depuis les fonctions de construction) ;
    Hall : setblock / fill de hall/build.mcfunction (généré par gen_hall.py)."""
    TW.load(C.F)
    spawn = {k for k, b in TW.W.items() if wanted(b)}
    hall = set()
    with open(os.path.join(C.F, 'hall', 'build.mcfunction'), encoding='utf-8') as f:
        for line in f:
            m = TW.CMD.match(line.strip())
            if not m or not wanted(TW.block_and_mode(m[8])[0]):
                continue
            x1, y1, z1 = int(m[2]), int(m[3]), int(m[4])
            x2, y2, z2 = (x1, y1, z1) if m[5] is None else (int(m[5]), int(m[6]), int(m[7]))
            hall |= {(x, y, z) for x in range(min(x1, x2), max(x1, x2) + 1) for y in range(min(y1, y2), max(y1, y2) + 1)
                     for z in range(min(z1, z2), max(z1, z2) + 1)}
    return spawn, hall


def benches():
    """Liste triée des bancs (spawn + Hall) ; à appeler tôt : le générateur s'arrête avant d'avoir écrit quoi que ce soit."""
    spawn, hall = scan(is_bench)
    if not spawn or not hall:
        raise SystemExit(f'sit_bench : aucun banc trouvé (spawn {len(spawn)}, hall {len(hall)})')
    allb = sorted(spawn | hall)
    bad = [k for k in allb if k[1] != TW.G + 1]
    if bad:
        raise SystemExit(f'sit_bench : banc hors du niveau du sol (y {TW.G + 1}) : {bad}')
    print('Bancs :', len(allb), f'(spawn {len(spawn)}, hall {len(hall)}, communs {len(spawn & hall)})')
    return allb


def write(bl, dy, actionbar):
    """Écrit les fonctions lobby/sit/bench* et l'advancement mg:lobby_bench ; bl = benches(), dy = rel(SEAT_DY) de gen_sit.py
    (hauteur du siège, ex. '~0.5'), actionbar = l'aide de gen_sit.py."""
    w = C.w
    w('lobby/sit/benches', ['# Repose les zones cliquables des bancs (généré : liste des bancs du spawn et du Hall), puis note leur nombre', KILL] +
      [f'{OVW}if block {x} {y} {z} minecraft:spruce_stairs[half=bottom] run summon minecraft:interaction {x + 0.5} {y} {z + 0.5} '
       '{Tags:["mg.bench"],width:1.05f,height:1.05f,response:1b}' for x, y, z in bl] +
      [f'execute store result score $lbx mg.st if entity @e[type={ZONES}]'])
    chunks = sorted({(x >> 4, z >> 4) for x, _, z in bl})
    w('lobby/sit/bench_check', ['# Toutes les 2 s (core/tick) : zones cliquables des bancs ; refait toutes les zones si leur nombre a changé',
                                f'execute if score $sitoff mg.st matches 1 run {KILL}',
                                'execute if score $sitoff mg.st matches 1 run return 0',
                                'execute unless score $setup mg.st matches 1 run return 0',
                                '# un chunk de bancs pas chargé : on attend (ses zones ne se comptent pas)'] +
      [f'{OVW}unless loaded {cx * 16 + 8} {TW.G + 1} {cz * 16 + 8} run return 0' for cx, cz in chunks] +
      ['# un banc remplacé par un autre bloc perd sa zone',
       f'execute as @e[type={ZONES}] at @s unless block ~ ~ ~ minecraft:spruce_stairs[half=bottom] run kill @s',
       f'execute store result score #lbc mg.st if entity @e[type={ZONES}]',
       'execute unless score #lbc mg.st = $lbx mg.st run function mg:lobby/sit/benches'])
    w('lobby/sit/bench_adv', ['# @s : a interagi avec une zone de banc (advancement mg:lobby_bench) ; mg.lbc le distingue des autres joueurs',
                              'advancement revoke @s only mg:lobby_bench',
                              'tag @s add mg.lbc',
                              f'execute as @e[type={ZONES},distance=..8] if data entity @s interaction run function mg:lobby/sit/bench_hit',
                              'tag @s remove mg.lbc'])
    w('lobby/sit/bench_hit', ['# @s = zone de banc avec un clic enregistré ; pas celui du joueur mg.lbc : on la laisse',
                              'execute on target unless entity @s[tag=mg.lbc] run return 0',
                              'data remove entity @s interaction',
                              '# « at @s » avant « on target » : @s devient le joueur, la position reste celle du banc',
                              'execute at @s on target run function mg:lobby/sit/bench_click'])
    seat = f'positioned ~0.5 {dy} ~0.5'
    w('lobby/sit/bench_click', ['# @s = joueur, position = centre du banc (posés par bench_hit) : s\'y assoit, ou se lève s\'il y est déjà',
                                'execute store result score #lbn mg.st run time query gametime',
                                'scoreboard players operation #lbd mg.st = @s mg.lsb',
                                f'scoreboard players add #lbd mg.st {CLICK_DELAY}',
                                'execute if score @s mg.lsb matches 1.. if score #lbn mg.st < #lbd mg.st run return 0',
                                'scoreboard players operation @s mg.lsb = #lbn mg.st',
                                '# assis sur ce banc : on se lève (le siège est à SEAT_DY au-dessus du pied du banc)',
                                f'execute if entity @s[tag=mg.sit] positioned ~ {dy} ~ on vehicle if entity @s[type=minecraft:item_display,tag=mg.seat,distance=..0.3] '
                                'run return run execute on passengers run function mg:lobby/sit/stand',
                                '# banc pris par un autre : message, et un joueur déjà assis garde sa place',
                                f'execute align xyz {seat} if entity @e[type=minecraft:item_display,tag=mg.seat,distance=..0.3] '
                                'run return run ' + actionbar('🪑 Place déjà prise.'),
                                '# assis ailleurs (autre banc, sol) : on se lève d\'abord',
                                'execute if entity @s[tag=mg.sit] run function mg:lobby/sit/stand',
                                'execute unless function mg:lobby/sit/can run return 0',
                                'execute align xyz if function mg:lobby/sit/bench_at run scoreboard players add $bnc mg.lsn 1'])
    os.makedirs(os.path.join(C.D, 'advancement'), exist_ok=True)
    with open(os.path.join(C.D, 'advancement', 'lobby_bench.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'criteria': {'use': {'trigger': 'minecraft:player_interacted_with_entity', 'conditions': {'entity': [{
            'condition': 'minecraft:entity_properties', 'entity': 'this',
            'predicate': {'minecraft:entity_type': 'minecraft:interaction', 'minecraft:nbt': '{Tags:["mg.bench"]}'}}]}}},
            'rewards': {'function': 'mg:lobby/sit/bench_adv'}}, f, ensure_ascii=False, indent=2)
        f.write('\n')


def wire(untag):
    """Câblage (une ligne par patch) : à appeler après les patchs de core/load, core/tick et desinstaller de gen_sit.py ; untag = sa ligne UNTAG."""
    C.patch('core/load', untag, [KILL, 'scoreboard players reset $lbx mg.st'])
    C.patch('core/tick', 'execute if entity @a[tag=mg.sit] run function mg:lobby/sit/tick', [SECOND_LINE], where='before')
    C.patch('desinstaller', untag, [KILL, 'advancement revoke @a only mg:lobby_bench', 'tag @a remove mg.lbc'])
    C.patch('desinstaller', HEADER, [HEADER_NOTE])
