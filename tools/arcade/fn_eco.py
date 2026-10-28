"""⛏ Filon : marché, vente, magasin, corde et dynamite, mort en PvP, phases PvP. Exécuté par gen_filon.py (exec : mêmes globals), jamais seul."""

# ---------------------------------------------------------------- marché : cours de chaque objet (en %), tableau
MK = ['# 📈 Nouveau cours du marché (toutes les 15 min)']
for i, (_, _, _, _, lo, hi) in enumerate(SELL):
    MK += [f'scoreboard players operation $fo{i} mg.st = $fm{i} mg.st', f'execute store result score $fm{i} mg.st run random value {lo}..{hi}']
MK += [f'function mg:{P}/board', 'tellraw @a[tag=mg.fnw] {"text":"📈 Le cours du marché a changé : va voir le tableau du comptoir !","color":"gold"}']
w(f'{P}/market', MK)
BD = ['# Tableau du marché : prix du moment (tas de 64 pour les pierres) et tendance']
parts = [TXT('📈 COURS DU MARCHÉ', 'gold', bold=True), TXT('\n(change toutes les 15 min)\n', 'gray')]
shown = [i for i, s in enumerate(SELL) if s[3]]
BD += [f'scoreboard players operation #pp mg.st = $fm0 mg.st', 'scoreboard players operation #pp mg.st *= #fn64 mg.st',
       'scoreboard players operation #pp mg.st /= #fn100 mg.st', 'execute store result storage mg:filon b.s int 1 run scoreboard players get #pp mg.st',
       'data modify storage mg:filon b.sc set value "green"', 'execute if score $fm0 mg.st < $fo0 mg.st run data modify storage mg:filon b.sc set value "red"']
parts += [TXT('Pierre (×64) : '), {'text': '$(s)', 'color': '$(sc)'}, TXT(' pts\n')]
for i in shown:
    _, base, nm, _, _, _ = SELL[i]
    BD += [f'scoreboard players set #pp mg.st {base}', f'scoreboard players operation #pp mg.st *= $fm{i} mg.st', 'scoreboard players operation #pp mg.st /= #fn100 mg.st',
           f'execute store result storage mg:filon b.p{i} int 1 run scoreboard players get #pp mg.st',
           f'data modify storage mg:filon b.a{i} set value "▲"', f'data modify storage mg:filon b.c{i} set value "green"',
           f'execute if score $fm{i} mg.st < $fo{i} mg.st run data modify storage mg:filon b.a{i} set value "▼"',
           f'execute if score $fm{i} mg.st < $fo{i} mg.st run data modify storage mg:filon b.c{i} set value "red"',
           f'execute if score $fm{i} mg.st = $fo{i} mg.st run data modify storage mg:filon b.a{i} set value "="',
           f'execute if score $fm{i} mg.st = $fo{i} mg.st run data modify storage mg:filon b.c{i} set value "gray"']
    parts += [TXT(f'{nm} : '), {'text': f'$(p{i}) $(a{i})', 'color': f'$(c{i})'}, TXT(' pts\n')]
BD += [f'function mg:{P}/board_set with storage mg:filon b']
w(f'{P}/board', BD)
w(f'{P}/board_set', [f'$data modify entity @e[type=minecraft:text_display,tag=mg.fnboard,limit=1] text set value {js(parts)}'])
CONSTS = ['scoreboard players set #fn100 mg.st 100', 'scoreboard players set #fn64 mg.st 64', 'scoreboard players set #fn2 mg.st 2'] + \
         [f'scoreboard players set #fb{i} mg.st {s[1]}' for i, s in enumerate(SELL)] + \
         [f'execute unless score $fm{i} mg.st matches 1.. run scoreboard players set $fm{i} mg.st 100' for i in range(NS)] + \
         [f'execute unless score $fo{i} mg.st matches 1.. run scoreboard players set $fo{i} mg.st 100' for i in range(NS)] + \
         ['execute unless score $fnsea mg.st matches 1.. run scoreboard players set $fnsea mg.st 1', 'execute unless score $fnt mg.st matches 0.. run scoreboard players set $fnt mg.st 0',
          'execute unless score $fnsc mg.st matches 0.. run scoreboard players set $fnsc mg.st 0',
          'execute unless score $fnpr mg.st matches 1.. run scoreboard players set $fnpr mg.st 1500',
          'execute unless score $fnpend mg.st matches 0.. run scoreboard players set $fnpend mg.st 1',
          'team add mg_fn', 'team modify mg_fn friendlyFire false', 'team modify mg_fn color gold', 'team modify mg_fn seeFriendlyInvisibles false',
          'bossbar add mg:filon ""', 'bossbar set mg:filon max 2700', 'bossbar set mg:filon style notched_10']

# ---------------------------------------------------------------- vente
SL = ['# 💰 @s vend tout ce qui est vendable dans son inventaire, au cours du moment', 'scoreboard players set #tot mg.st 0']
for i, (iid_, *_) in enumerate(SELL):
    SL += [f'execute store result score #n mg.st run clear @s {iid(iid_)}', f'scoreboard players operation #n mg.st *= #fb{i} mg.st',
           f'scoreboard players operation #n mg.st *= $fm{i} mg.st', 'scoreboard players operation #tot mg.st += #n mg.st']
SL += ['scoreboard players operation #tot mg.st /= #fn100 mg.st',
       'execute if score #tot mg.st matches ..0 run return run tellraw @s {"text":"Rien à vendre : va miner ! ⛏","color":"gray"}',
       'scoreboard players operation @s mg.fnp += #tot mg.st', 'scoreboard players operation @s mg.fns += #tot mg.st',
       'tellraw @s [{"text":"💰 Vendu pour ","color":"gold"},{"score":{"name":"#tot","objective":"mg.st"},"color":"yellow","bold":true},{"text":" pts. Solde : ","color":"gold"},'
       '{"score":{"name":"@s","objective":"mg.fnp"},"color":"yellow"},{"text":" — saison : ","color":"gray"},{"score":{"name":"@s","objective":"mg.fns"},"color":"gray"}]',
       'execute if score #tot mg.st matches 1000.. run tellraw @a[tag=mg.fnw] [{"text":"💎 ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" vient de vendre pour ","color":"gray"},{"score":{"name":"#tot","objective":"mg.st"},"color":"aqua","bold":true},{"text":" pts !","color":"gray"}]',
       'execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1.1', 'execute at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.4']
w(f'{P}/sell', SL)

# ---------------------------------------------------------------- magasin (fenêtre)
SH = ['# 🛒 Fenêtre du magasin : libellés et prix selon les niveaux de @s',
      'execute store result storage mg:filon s.p int 1 run scoreboard players get @s mg.fnp']
for n, obj, tiers, mx in SHOP:
    SH.append(f'data modify storage mg:filon s.a{n} set value "{mx}"')
    for lv, (price, lbl) in tiers.items():
        SH.append(f'execute if score @s {obj} matches {lv} run data modify storage mg:filon s.a{n} set value "{lbl} — {price} pts"')
SH.append(f'function mg:{P}/shop_show with storage mg:filon s')
w(f'{P}/shop', SH)
acts = [{'label': [{'text': f'$(a{n})', 'color': 'yellow'}], 'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.fnt set {n}'}} for n, *_ in SHOP]
acts += [{'label': [{'text': f'{lbl} — {pr} pts', 'color': 'white'}], 'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.fnt set {n}'}} for n, pr, lbl, _ in ITEMS]
acts.append({'label': [{'text': '📈 Cours du marché', 'color': 'gold'}], 'action': {'type': 'minecraft:run_command', 'command': 'trigger mg.fnt set 21'}})
DLG = {'type': 'minecraft:multi_action', 'title': {'text': '🛒 Magasin du Filon', 'color': 'aqua', 'bold': True},
       'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': 'Solde : ', 'color': 'gray'}, {'text': '$(p) pts', 'color': 'yellow', 'bold': True},
                                                                  {'text': '\nTes améliorations sont gardées jusqu\'à la fin de la saison.', 'color': 'gray'}]}],
       'actions': acts, 'columns': 2, 'pause': False, 'can_close_with_escape': True}
w(f'{P}/shop_show', ['$dialog show @s ' + json.dumps(DLG, ensure_ascii=False, separators=(',', ':'))])

BUY = ['# Trigger mg.fnt (@s) : 1-9 achats, 20 vendre, 21 cours du marché, 30 retour au lobby',
       'execute unless entity @s[tag=mg.fnw] run return run scoreboard players reset @s mg.fnt',
       f'execute if score @s mg.fnt matches 30 run return run function mg:{P}/leave',
       f'execute unless entity @s[{PLAZA}] run tellraw @s {{"text":"⚠ Approche-toi du comptoir et du magasin (place de l\'île).","color":"red"}}',
       f'execute unless entity @s[{PLAZA}] run return run scoreboard players reset @s mg.fnt',
       f'execute if score @s mg.fnt matches 20 run function mg:{P}/sell',
       f'execute if score @s mg.fnt matches 21 run function mg:{P}/market_show',
       'scoreboard players set #c mg.st -1']
for n, obj, tiers, _ in SHOP:
    for lv, (price, _) in tiers.items():
        BUY.append(f'execute if score @s mg.fnt matches {n} if score @s {obj} matches {lv} run scoreboard players set #c mg.st {price}')
    BUY.append(f'execute if score @s mg.fnt matches {n} if score #c mg.st matches -1 run tellraw @s {{"text":"C\'est déjà le niveau maximum.","color":"gray"}}')
for n, pr, _, _ in ITEMS:
    BUY.append(f'execute if score @s mg.fnt matches {n} run scoreboard players set #c mg.st {pr}')
BUY += ['execute if score #c mg.st matches 0.. if score @s mg.fnp < #c mg.st run tellraw @s [{"text":"Pas assez de points (","color":"red"},{"score":{"name":"#c","objective":"mg.st"},"color":"yellow"},{"text":" requis).","color":"red"}]',
        'execute if score #c mg.st matches 0.. if score @s mg.fnp < #c mg.st at @s run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.6',
        'execute if score #c mg.st matches 0.. if score @s mg.fnp < #c mg.st run scoreboard players set #c mg.st -1',
        f'execute if score #c mg.st matches 0.. run function mg:{P}/buy_ok', 'scoreboard players reset @s mg.fnt']
w(f'{P}/cmd', BUY)
OK = ['# Achat payé (#c) : niveau suivant ou objet', 'scoreboard players operation @s mg.fnp -= #c mg.st']
for n, obj, _, _ in SHOP:
    OK.append(f'execute if score @s mg.fnt matches {n} run scoreboard players add @s {obj} 1')
for n, _, _, give in ITEMS:
    OK.append(f'execute if score @s mg.fnt matches {n} run give @s {DYN if give == "DYN" else give}')
OK += [f'execute if score @s mg.fnt matches 1..6 run function mg:{P}/kit', f'function mg:{P}/effects',
       'execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 0.8',
       'tellraw @s [{"text":"🛒 Acheté ! Solde : ","color":"aqua"},{"score":{"name":"@s","objective":"mg.fnp"},"color":"yellow"},{"text":" pts","color":"aqua"}]',
       f'execute if score @s mg.fnt matches 1..6 run function mg:{P}/shop']
w(f'{P}/buy_ok', OK)
MS = ['# Fenêtre « cours du marché » (même contenu que le tableau)', f'function mg:{P}/board']
w(f'{P}/market_show', MS + [f'function mg:{P}/market_dlg with storage mg:filon b'])
w(f'{P}/market_dlg', ['$dialog show @s ' + json.dumps({'type': 'minecraft:notice', 'title': {'text': '📈 Cours du marché', 'color': 'gold', 'bold': True},
                                                       'body': [{'type': 'minecraft:plain_message', 'width': 300, 'contents': parts[1:]}], 'pause': False},
                                                      ensure_ascii=False, separators=(',', ':'))])

# ---------------------------------------------------------------- objets utilisables : corde, dynamite
w(f'{P}/use', ['# @s a fait un clic droit avec un bâton (corde ou dynamite)', 'scoreboard players reset @s mg.fnu',
               f'execute if items entity @s weapon.mainhand *[minecraft:custom_data~{{fn_rope:1b}}] run return run function mg:{P}/rope',
               f'execute if items entity @s weapon.mainhand *[minecraft:custom_data~{{fn_dyn:1b}}] run return run function mg:{P}/dyn',
               f'execute if items entity @s weapon.offhand *[minecraft:custom_data~{{fn_rope:1b}}] run return run function mg:{P}/rope',
               f'execute if items entity @s weapon.offhand *[minecraft:custom_data~{{fn_dyn:1b}}] run return run function mg:{P}/dyn'])
w(f'{P}/rope', ['# 🪢 Corde de remontée (recharge 120 s)',
                'execute if score @s mg.fncd matches 1.. run return run title @s actionbar [{"text":"🪢 Corde en recharge : ","color":"gray"},{"score":{"name":"@s","objective":"mg.fncd"},"color":"yellow"},{"text":" s","color":"gray"}]',
                'execute unless entity @s[tag=mg.fnin] run return run title @s actionbar {"text":"Tu es déjà à la surface.","color":"gray"}',
                f'function mg:{P}/to_surface', f'scoreboard players set @s mg.fncd {ROPE_S}',
                'execute at @s run playsound minecraft:entity.leash_knot.place master @s ~ ~ ~ 1 0.8',
                'title @s actionbar {"text":"🪢 Remonté à la surface !","color":"gold"}'])
w(f'{P}/to_surface', [f'tp @s {SPAWN[0]} {SPAWN[1]} {SPAWN[2]} 0 0', 'tag @s remove mg.fnin', 'team join mg_fn @s'])
w(f'{P}/dyn', ['# 🧨 Dynamite : seulement dans la mine, sous la surface (les murs du puits protègent l\'île)',
               f'execute unless entity @s[x=0,y={YB - 1},z={Z0},dx=15,dy={95 - YB},dz=15] run return run title @s actionbar {{"text":"🧨 Seulement dans la mine, au moins 4 blocs sous la surface.","color":"red"}}',
               'execute anchored eyes positioned ^ ^ ^1.2 run summon minecraft:tnt ~ ~-0.5 ~ {fuse:40,Tags:["mg.fntnt"]}',
               'clear @s minecraft:warped_fungus_on_a_stick[minecraft:custom_data~{fn_dyn:1b}] 1',
               'title @s actionbar {"text":"🧨 Recule ! 2 secondes…","color":"red","bold":true}'])

# ---------------------------------------------------------------- mort (PvP) : la moitié du sac passe au tueur
DI = ['# @s est mort (inventaire gardé) : en PvP, la moitié de ce qu\'il n\'a pas vendu passe au tueur', 'scoreboard players reset @s mg.fnd',
      f'spawnpoint @s {math.floor(SPAWN[0])} {SPAWN[1]} {math.floor(SPAWN[2])}', 'tag @s remove mg.fnin',
      'execute unless score $fnpvp mg.st matches 1 run return 0',
      'tag @a remove mg.fnkl', 'tag @a[tag=mg.fnw,scores={mg.fnk=1..},limit=1] add mg.fnkl',
      'execute unless entity @a[tag=mg.fnkl] run return 0']
for i, (iid_, *_) in enumerate(SELL):
    DI += [f'execute store result score #n mg.st run clear @s {iid(iid_)} 0', 'scoreboard players operation #n mg.st /= #fn2 mg.st',
           f'execute if score #n mg.st matches 1.. store result storage mg:filon x.n int 1 run scoreboard players get #n mg.st',
           f'execute if score #n mg.st matches 1.. run data modify storage mg:filon x.c set value "{iid(iid_)}"',
           f'execute if score #n mg.st matches 1.. run data modify storage mg:filon x.g set value \'{GIVE_ID.get(iid_, iid(iid_))}\'',
           f'execute if score #n mg.st matches 1.. run function mg:{P}/xfer with storage mg:filon x']
DI += ['tellraw @a[tag=mg.fnw] [{"text":"⚔ ","color":"red"},{"selector":"@a[tag=mg.fnkl]","color":"yellow"},{"text":" a détroussé ","color":"gray"},{"selector":"@s","color":"yellow"},{"text":" (la moitié de son sac).","color":"gray"}]',
       'tag @a remove mg.fnkl']
w(f'{P}/died', DI)
w(f'{P}/xfer', ['$clear @s $(c) $(n)', '$give @a[tag=mg.fnkl,limit=1] $(g) $(n)'])

# ---------------------------------------------------------------- PvP (dans la mine seulement)
w(f'{P}/pvp_check', ['# PvP actif ? 3 min après une régénération (faite avec des joueurs), ou la phase au hasard du cycle',
                     'scoreboard players set #pv mg.st 0',
                     f'execute if score $fnrp mg.st matches 1 if score $fnt mg.st matches ..{PVP_S - 1} run scoreboard players set #pv mg.st 1',
                     'scoreboard players operation #pe mg.st = $fnpr mg.st', f'scoreboard players add #pe mg.st {PVP_S}',
                     'execute if score $fnt mg.st >= $fnpr mg.st if score $fnt mg.st < #pe mg.st run scoreboard players set #pv mg.st 1',
                     'execute if score #pv mg.st matches 1 unless score $fnpvp mg.st matches 1 run tellraw @a[tag=mg.fnw] {"text":"⚔ PvP OUVERT dans la mine (3 min) ! En surface, tu ne crains rien.","color":"red","bold":true}',
                     'execute if score #pv mg.st matches 1 unless score $fnpvp mg.st matches 1 as @a[tag=mg.fnw] at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 1.2',
                     'execute if score #pv mg.st matches 0 if score $fnpvp mg.st matches 1 run tellraw @a[tag=mg.fnw] {"text":"🕊 Fin du PvP : la mine redevient paisible.","color":"green"}',
                     'execute if score #pv mg.st matches 0 if score $fnpvp mg.st matches 1 run team join mg_fn @a[tag=mg.fnw]',
                     'scoreboard players operation $fnpvp mg.st = #pv mg.st',
                     f'execute if score $fnt mg.st matches {PVP_S}.. run scoreboard players set $fnrp mg.st 0'])
w(f'{P}/pvp_now', ['# Admin : phase PvP de 3 min tout de suite', 'scoreboard players operation $fnpr mg.st = $fnt mg.st', f'function mg:{P}/pvp_check'])
