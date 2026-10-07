# ================================================================== CHOIX DU KART et MODE BATAILLE
# Exécuté à la fin de rp_part.py (mêmes variables : fn, patch_fn, KK, KART, COLORS, TEXTC, RGB, ITEMS, CHARGES, base, tail...).
# Choix du kart : mg.kty (1 Standard, 2 Bolide, 3 Mini, 4 Costaud) et mg.kcol (1..8, 0 = couleur automatique), via
# /trigger mg.kch (1..4 = type, 11..18 = couleur) ou la fenêtre mg:kart_choice affichée au départ de chaque course.
# Bataille ($kbat = 1, arène t3) : 3 ballons par pilote ; chaque coup (objet, chute, Chomp) en crève un ; 0 ballon = éliminé ;
# le dernier en lice gagne, sinon le plus de ballons au bout de 3 minutes.
KNAMES = {1: ('Standard', 'white', 'Équilibré en tout.'),
          2: ('Bolide', 'red', 'Vitesse max +10 %, mais accélère et tourne moins bien.'),
          3: ('Mini', 'green', 'Accélère fort et tourne serré, vitesse max -7 %, moins freiné dans l\'herbe.'),
          4: ('Costaud', 'gold', 'Vitesse max +4 %, accélère lentement, peu freiné hors piste, tête-à-queue plus courts.')}
CNAMES = ['Rouge', 'Bleu', 'Vert', 'Jaune', 'Violet', 'Orange', 'Cyan', 'Rose']
STATS = {1: (100, 5, 100, 45), 2: (110, 4, 85, 45), 3: (93, 7, 120, 52), 4: (104, 3, 90, 58)}   # vitesse max, accélération, virage %, hors piste
BAT_TIME = 3600

# ---- fenêtres de choix : 1) le modèle, 2) la couleur (qui valide : le pilote est prêt)
def dialog(name, title, body, acts, cols, extra=None):
    """extra : texte en plus sous l'explication (portraits des karts, police mg:kart du resource pack)."""
    els = [{"type": "minecraft:plain_message", "contents": body, "width": 300}]
    if extra: els.append({"type": "minecraft:plain_message", "contents": extra, "width": 400})
    wr(os.path.join(DATA, 'mg', 'dialog', name + '.json'), json.dumps({
        "type": "minecraft:multi_action", "title": title, "body": els,
        "columns": cols, "can_close_with_escape": True, "pause": False, "after_action": "close", "actions": acts}, ensure_ascii=False, indent=2) + chr(10))
def glyph(t, k): return chr(0xE000 + 16 * (t - 1) + (k - 1))
NL = chr(10)

# barres de caractéristiques (sur 10), façon Mario Kart
BARS = {1: (6, 6, 6, 3, 5), 2: (9, 4, 4, 3, 6), 3: (4, 9, 9, 6, 2), 4: (7, 3, 5, 8, 9)}
BARN = ('Vitesse', 'Accélération', 'Maniabilité', 'Tout-terrain', 'Poids')
def bars(t):
    out = []
    for label, v in zip(BARN, BARS[t]):
        out += [{"text": NL + f"{label}  ", "color": "gray"}, {"text": "▮" * v, "color": "gold"}, {"text": "▮" * (10 - v), "color": "dark_gray"}]
    return out

acts = []
for t, (name, colr, desc) in KNAMES.items():
    acts.append({"label": [{"text": f"🏎 {name}", "color": colr, "bold": True}], "width": 150,
                 "tooltip": [{"text": f"{name}" + NL, "color": colr, "bold": True}, {"text": desc, "color": "gray"}] + bars(t),
                 "action": {"type": "minecraft:run_command", "command": f"trigger mg.kch set {t}"}})
T1 = [{"text": "🏎 Choisis ton kart (1/2)", "color": "gold", "bold": True}]
B1 = [{"text": "Clique sur un kart pour le choisir (survole-le pour ses caractéristiques), puis choisis sa couleur." + NL, "color": "gray"},
      {"text": "La course part quand tout le monde a choisi (1 minute au plus).", "color": "dark_gray"}]
def cell(t, k):
    """portrait cliquable : clic = choisir ce modèle, survol = ses caractéristiques."""
    n, colr, d = KNAMES[t]
    return {"text": glyph(t, k), "font": "mg:kart", "color": "white",
            "click_event": {"action": "run_command", "command": f"trigger mg.kch set {t}"},
            "hover_event": {"action": "show_text", "value": [{"text": n + NL, "color": colr, "bold": True}, {"text": d, "color": "gray"}] + bars(t)
                            + [{"text": NL + NL + "Clic : choisir ce kart", "color": "yellow"}]}}
dialog('kart_choice', T1, B1, acts, 2)
for k in range(1, 9):
    # 2 x 2 portraits, dans l'ordre des boutons ; les lignes vides réservent la hauteur des images
    dialog(f'kart_choice_c{k}', T1, B1, acts, 2,
           [{"text": NL * 7}, cell(1, k), {"text": " ", "font": "mg:kart"}, cell(2, k),
            {"text": NL * 8}, cell(3, k), {"text": " ", "font": "mg:kart"}, cell(4, k), {"text": NL}])

# couleur : l'aperçu se met à jour à chaque clic, « Valider » rend le pilote prêt
cacts = [{"label": [{"text": "█ ", "color": tc}, {"text": cname, "color": tc, "bold": True}], "width": 100,
          "action": {"type": "minecraft:run_command", "command": f"trigger mg.kch set {10 + k}"}} for k, (cname, tc) in enumerate(zip(CNAMES, TEXTC), 1)]
cacts.append({"label": [{"text": "🎲 Auto", "color": "white"}], "width": 100,
              "tooltip": [{"text": "Une couleur différente pour chaque pilote (et tu es prêt)", "color": "gray"}],
              "action": {"type": "minecraft:run_command", "command": "trigger mg.kch set 19"}})
cacts.append({"label": [{"text": "◀ Modèle", "color": "gray"}], "width": 100,
              "action": {"type": "minecraft:run_command", "command": "trigger mg.kch set 30"}})
cacts.append({"label": [{"text": "✔ Valider", "color": "green", "bold": True}], "width": 100,
              "tooltip": [{"text": "Je suis prêt pour le départ", "color": "gray"}],
              "action": {"type": "minecraft:run_command", "command": "trigger mg.kch set 20"}})
T2 = [{"text": "🎨 Couleur du kart (2/2)", "color": "gold", "bold": True}]
B2 = [{"text": "Clique une couleur pour la voir sur ton kart, puis ", "color": "gray"}, {"text": "✔ Valider", "color": "green", "bold": True}, {"text": ".", "color": "gray"}]
dialog('kart_color', T2, B2, cacts, 3)
for t, (n, colr, d) in KNAMES.items():
    for k, (c, cname, tc) in enumerate(zip(COLORS, CNAMES, TEXTC), 1):
        dialog(f'kart_color_t{t}_c{k}', T2, B2, cacts, 3,
               [{"text": NL * 13}, {"text": glyph(t, k), "font": "mg:kartxl", "color": "white"}, {"text": NL * 3},
                {"text": n + "  ", "color": colr, "bold": True}, {"text": cname, "color": tc, "bold": True}] + bars(t))
for f in os.listdir(os.path.join(DATA, 'mg', 'dialog')):
    if f.startswith('kart_color_t') and f.count('_') == 2: os.remove(os.path.join(DATA, 'mg', 'dialog', f))
fn('show_models', 'execute if score $rp mg.st matches 0 run return run dialog show @s mg:kart_choice\n' +
   ''.join(f'execute if score @s mg.kcol matches {k} run return run dialog show @s mg:kart_choice_c{k}\n' for k in range(1, 9)) +
   'dialog show @s mg:kart_choice_c1\n')
sc = ['execute if score $rp mg.st matches 0 run return run dialog show @s mg:kart_color',
      'scoreboard players operation $kcs mg.st = @s mg.kcol', 'execute unless score $kcs mg.st matches 1..8 run scoreboard players set $kcs mg.st 1']
sc += [f'execute if score @s mg.kty matches {t} if score $kcs mg.st matches {k} run return run dialog show @s mg:kart_color_t{t}_c{k}' for t in KNAMES for k in range(1, 9)]
sc.append('dialog show @s mg:kart_color_t1_c1')
fn('show_colors', '\n'.join(sc) + '\n')

choose = ['# Choix du kart de @s (/trigger mg.kch : 1..4 = modèle, 11..18 = couleur, 19 = couleur auto, 20 = valider, 30 = fenêtre des modèles)',
          'execute if score @s mg.kch matches 30 run function mg:kart/show_models',
          'execute if score @s mg.kch matches 30 run return run function mg:kart/choose_end',
          'execute if score @s mg.kch matches 1..4 run scoreboard players operation @s mg.kty = @s mg.kch',
          'execute if score @s mg.kch matches 11..18 run scoreboard players operation @s mg.kcol = @s mg.kch',
          'execute if score @s mg.kch matches 11..18 run scoreboard players remove @s mg.kcol 10',
          'execute if score @s mg.kch matches 19 run scoreboard players set @s mg.kcol 0',
          'execute if score @s mg.kch matches 19..20 run tag @s add mg.kok',
          'execute if score @s mg.kch matches 11..18 run function mg:kart/show_colors',
          'execute if score @s mg.kch matches 19..20 run title @s actionbar [{"text":"✔ Prêt ! ","color":"green","bold":true},{"text":"En attente des autres pilotes...","color":"gray"}]',
          'execute if score @s mg.kch matches 1..4 run function mg:kart/show_colors']
for t, (name, colr, desc) in KNAMES.items():
    choose.append(f'execute if score @s mg.kch matches {t} run title @s actionbar [{{"text":"🏎 Kart ","color":"gray"}},{{"text":"{name}","color":"{colr}","bold":true}},{{"text":" : {desc}","color":"gray"}}]')
choose += ['function mg:kart/kk',
           f'scoreboard players operation {KK} mg.kty = @s mg.kty',
           f'execute if score @s mg.kcol matches 1..8 run scoreboard players operation {KK} mg.kcol = @s mg.kcol',
           f'execute as {KK} at @s run function mg:kart/kart_paint',
           'execute if score $kbat mg.st matches 1 run function mg:kart/bat_balloons',
           'tag @e[tag=mg.kk] remove mg.kk',
           'execute at @s run playsound minecraft:ui.button.click master @s ~ ~ ~ 0.6 1.2',
           'function mg:kart/choose_end']
fn('choose', '\n'.join(choose) + '\n')
fn('choose_end', 'scoreboard players reset @s mg.kch\nscoreboard players enable @s mg.kch\n')
fn('hold', '''# Compte à rebours du kart retenu (vrai) tant que tous les pilotes n'ont pas choisi leur kart, 1 minute au plus
execute if score $timer mg.st matches 101 run title @a[tag=mg.play] subtitle [{"text":"🎥 Appuie sur ","color":"gray"},{"text":"F5","color":"yellow","bold":true},{"text":" pour voir ton kart en 3e personne","color":"gray"}]
execute unless entity @a[tag=mg.play,tag=!mg.kok] run return fail
execute if score $kwait mg.st matches 1200.. run return fail
scoreboard players add $kwait mg.st 1
scoreboard players enable @a[tag=mg.play] mg.kch
execute as @a[tag=mg.play] if score @s mg.kch matches 1.. run function mg:kart/choose
execute store result score $knr mg.st if entity @a[tag=mg.play,tag=!mg.kok]
scoreboard players set $kws mg.st 1200
scoreboard players operation $kws mg.st -= $kwait mg.st
scoreboard players operation $kws mg.st /= #k20 mg.st
scoreboard players operation $kwm mg.st = $kwait mg.st
scoreboard players operation $kwm mg.st %= #k10 mg.st
execute if score $kwm mg.st matches 0 run title @a[tag=mg.play,tag=mg.kok] actionbar [{"text":"⏳ En attente de ","color":"gray"},{"score":{"name":"$knr","objective":"mg.st"},"color":"yellow","bold":true},{"text":" pilote(s) qui choisissent leur kart... ","color":"gray"},{"score":{"name":"$kws","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
execute if score $kwm mg.st matches 0 run title @a[tag=mg.play,tag=!mg.kok] actionbar [{"text":"🏎 Choisis ton kart ! ","color":"gold","bold":true},{"text":"Départ dans ","color":"gray"},{"score":{"name":"$kws","objective":"mg.st"},"color":"yellow"},{"text":" s au plus","color":"gray"}]
execute if score $kwm mg.st matches 0 as @a[tag=mg.play] run function mg:kart/place_seat
execute if score $kwait mg.st matches 200 run tellraw @a[tag=mg.play,tag=!mg.kok] [{"text":"🏎 ","color":"gold"},{"text":"[Choisir mon kart]","color":"yellow","bold":true,"click_event":{"action":"run_command","command":"trigger mg.kch set 30"}},{"text":" : la course attend ton choix.","color":"gray"}]
execute if score $kwait mg.st matches 800 run tellraw @a[tag=mg.play,tag=!mg.kok] [{"text":"🏎 ","color":"gold"},{"text":"[Choisir mon kart]","color":"yellow","bold":true,"click_event":{"action":"run_command","command":"trigger mg.kch set 30"}},{"text":" : départ dans 20 secondes !","color":"gray"}]
return 1
''')
paint = ['# @s = kart : couleur (bloc) et modèle 3D (pack) selon ses mg.kty / mg.kcol']
paint += [f'execute if score $rp mg.st matches 0 if score @s mg.kcol matches {k} run data modify entity @s block_state.Name set value "minecraft:{c}_concrete"'
          for k, c in enumerate(COLORS, 1)]
paint += ['execute if score $rp mg.st matches 1 on passengers if entity @s[tag=mg.k3d] run kill @s',
          'execute if score $rp mg.st matches 1 run function mg:kart/rp_kart']
fn('kart_paint', '\n'.join(paint) + '\n')
fn('pre_tick', '''# Pendant le compte à rebours : prise en compte des choix de kart
execute unless score $game mg.st matches 61 run return 0
execute unless score $state mg.st matches 1 run return 0
scoreboard players enable @a[tag=mg.play] mg.kch
execute as @a[tag=mg.play] if score @s mg.kch matches 1.. run function mg:kart/choose
schedule function mg:kart/pre_tick 5t
''')

# ---- caractéristiques des karts
spd = ['scoreboard players set $kmx mg.st 100\n'] + [
    f'execute if score @s mg.kty matches {t} run scoreboard players set $kmx mg.st {v}\n' for t, (v, a, tu, o) in STATS.items() if t > 1]
patch_fn('speed', 'scoreboard players set $kmx mg.st 100\n', ''.join(spd))
patch_fn('speed', 'execute if score $kro mg.st matches 0 if score $kg mg.st matches 1 run scoreboard players set $kmx mg.st 45\n',
         ''.join(f'execute if score $kro mg.st matches 0 if score $kg mg.st matches 1 if score @s mg.kty matches {t} run scoreboard players set $kmx mg.st {o}\n'
                 for t, (v, a, tu, o) in STATS.items()) +
         'execute if score $kro mg.st matches 0 if score $kg mg.st matches 1 unless score @s mg.kty matches 1..4 run scoreboard players set $kmx mg.st 45\n')
patch_fn('speed', 'execute if score $kf mg.st matches 1 if score $kb mg.st matches 0 run scoreboard players add @s mg.ksp 5\n',
         'scoreboard players set $kac mg.st 5\n' +
         ''.join(f'execute if score @s mg.kty matches {t} run scoreboard players set $kac mg.st {a}\n' for t, (v, a, tu, o) in STATS.items() if t > 1) +
         'execute if score $kf mg.st matches 1 if score $kb mg.st matches 0 run scoreboard players operation @s mg.ksp += $kac mg.st\n')
patch_fn('steer', 'execute if score $ka mg.st matches 70.. run scoreboard players set $kT mg.st 45\n',
         'execute if score $ka mg.st matches 70.. run scoreboard players set $kT mg.st 45\n' +
         ''.join(f'execute if score @s mg.kty matches {t} run scoreboard players operation $kT mg.st *= #kt{tu} mg.st\n'
                 f'execute if score @s mg.kty matches {t} run scoreboard players operation $kT mg.st /= #k100 mg.st\n' for t, (v, a, tu, o) in STATS.items() if t > 1))
patch_fn('prepare', 'scoreboard players set #k100 mg.st 100\n',
         'scoreboard players set #k100 mg.st 100\n' + ''.join(f'scoreboard players set #kt{tu} mg.st {tu}\n' for t, (v, a, tu, o) in STATS.items() if t > 1))
patch_fn('hit', 'scoreboard players set @s mg.khi 20\n',
         'execute if score $kbat mg.st matches 1 unless score @s mg.khi matches 1.. run function mg:kart/bat_pop\n'
         'scoreboard players set @s mg.khi 20\nexecute if score @s mg.kty matches 4 run scoreboard players set @s mg.khi 12\n')

# ---- crochets du mode bataille et du choix dans le moteur
patch_fn('drive', '# Pilotage du kart de @s (chaque tick)\n',
         '# Pilotage du kart de @s (chaque tick)\nexecute if entity @s[tag=mg.kout] run return 0\nexecute if score @s mg.kch matches 1.. run function mg:kart/choose\n')
patch_fn('tick', 'scoreboard players enable @a[tag=mg.play] mg.kv\n', 'scoreboard players enable @a[tag=mg.play] mg.kv\nscoreboard players enable @a[tag=mg.play] mg.kch\n')
patch_fn('tick', 'execute if score $ktime mg.st matches 8400.. run return run function mg:kart/end\n',
         'execute if score $ktime mg.st matches 8400.. run return run function mg:kart/end\n'
         'execute store result score $kal mg.st if entity @a[tag=mg.play,tag=!mg.kout]\n'
         'execute if score $kbat mg.st matches 1 if score $kn mg.st matches 2.. if score $kal mg.st matches ..1 run return run function mg:kart/end\n'
         f'execute if score $kbat mg.st matches 1 if score $ktime mg.st matches {BAT_TIME}.. run return run function mg:kart/end\n')
patch_fn('rescue', 'execute at @s run playsound minecraft:entity.chicken.egg master @s ~ ~ ~ 1 1\n',
         'execute at @s run playsound minecraft:entity.chicken.egg master @s ~ ~ ~ 1 1\nexecute if score $kbat mg.st matches 1 run function mg:kart/bat_pop\n')
patch_fn('progress', 'scoreboard players operation @s mg.kpg = @s mg.klp\n',
         'execute if score $kbat mg.st matches 1 run return run function mg:kart/bat_progress\nscoreboard players operation @s mg.kpg = @s mg.klp\n')
patch_fn('hud', '# Barre du bas : tour, position, objet (et charges), vitesse\n',
         '# Barre du bas : tour, position, objet (et charges), vitesse\nexecute if score $kbat mg.st matches 1 run return run function mg:kart/bat_hud\n')
patch_fn('prepare', 'execute as @a[tag=mg.play] run function mg:kart/show_models\n', 'execute as @a[tag=mg.play] run function mg:kart/show_models\n'
         'tellraw @a[tag=mg.play] [{"text":"\\n🎥 ","color":"aqua"},{"text":"Avant le départ : appuie sur ","color":"white"},{"text":"F5","color":"yellow","bold":true},'
         '{"text":" pour conduire en vue 3e personne (derrière ton kart). Ton objet est dans toute la barre : clic droit pour l\'utiliser.\\n","color":"white"}]\n')
patch_fn('place_all', 'execute as @a[tag=mg.play] run function mg:kart/place_seat\n',
         'execute as @a[tag=mg.play] run function mg:kart/place_seat\n'
         'execute if score $kbat mg.st matches 1 as @a[tag=mg.play] run function mg:kart/bat_init\n'
         'schedule function mg:kart/pre_tick 5t\n')
patch_fn('go', 'tellraw @a[tag=mg.play] [{"text":"🏎 ","color":"gold"},{"text":"KART"',
         'execute if score $kbat mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🎈 ","color":"red"},{"text":"BATAILLE","color":"red","bold":true},'
         '{"text":" : chaque pilote a 3 ballons. Un coup (objet, Chomp, chute dans les douves) en crève un ; plus de ballon = éliminé. '
         'Dernier en lice ou le plus de ballons au bout de 3 minutes ! Boîtes ? = objets (dans toute la barre), clic droit pour les utiliser.","color":"gray"}]\n'
         'execute unless score $kbat mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🏎 ","color":"gold"},{"text":"KART"')
patch_fn('item_roll', 'scoreboard players operation @s mg.kit = $kgv mg.st\n',
         'execute if score $kbat mg.st matches 1 if score $kgv mg.st matches 14 run scoreboard players set $kgv mg.st 12\n'
         'scoreboard players operation @s mg.kit = $kgv mg.st\n')
patch_fn('end', 'tellraw @a[tag=!mg.surv] [{"text":"\\n🏁 CLASSEMENT DE LA COURSE"',
         'execute if score $kbat mg.st matches 1 run tellraw @a[tag=!mg.surv] [{"text":"\\n🎈 CLASSEMENT DE LA BATAILLE","color":"red","bold":true}]\n'
         'execute unless score $kbat mg.st matches 1 run tellraw @a[tag=!mg.surv] [{"text":"\\n🏁 CLASSEMENT DE LA COURSE"')

# ---- ballons
BAL = [(1, -0.45, 1.35, -0.7), (2, 0.0, 1.62, -0.85), (3, 0.45, 1.35, -0.7)]
fn('bat_init', '''# Début de bataille : 3 ballons pour @s
scoreboard players set @s mg.kbl 3
function mg:kart/bat_balloons
''')
bb = ['# Ballons du kart de @s (autant que mg.kbl), à sa couleur',
      'scoreboard players operation $me mg.st = @s mg.ri',
      'execute as @e[type=minecraft:item_display,tag=mg.kbal] if score @s mg.ri = $me mg.st run kill @s',
      'function mg:kart/kk',
      'execute unless entity @e[tag=mg.kk] run return 0',
      'data modify storage mg:kart bal.m set value "minecraft:red_wool"',
      'execute if score $rp mg.st matches 1 run data modify storage mg:kart bal.m set value "mg:balloon"',
      f'data modify storage mg:kart bal.c set value {RGB["red"]}']
bb += [f'execute if score {KK} mg.kcol matches {k} run data modify storage mg:kart bal.c set value {RGB[c]}' for k, c in enumerate(COLORS, 1)]
for s, x, y, z in BAL:
    bb += [f'data modify storage mg:kart bal.s set value {s}', f'data modify storage mg:kart bal.x set value {x}f',
           f'data modify storage mg:kart bal.y set value {y}f', f'data modify storage mg:kart bal.z set value {z}f',
           f'execute if score @s mg.kbl matches {s}.. at {KK} run function mg:kart/bat_bal with storage mg:kart bal']
bb += ['scoreboard players operation @e[type=minecraft:item_display,tag=mg.kbaln] mg.ri = @s mg.ri',
       f'execute as @e[type=minecraft:item_display,tag=mg.kbaln] run ride @s mount {KK}',
       f'execute as {KK} at @s on passengers run rotate @s ~ 0',
       'tag @e[tag=mg.kbaln] remove mg.kbaln']
fn('bat_balloons', '\n'.join(bb) + '\n')
fn('bat_bal', '$summon minecraft:item_display ~ ~ ~ {Tags:["mg.kbal","mg.kbal$(s)","mg.kbaln","mg.kpart"],teleport_duration:2,'
   'item:{id:"minecraft:leather_horse_armor",components:{"minecraft:item_model":"$(m)","minecraft:dyed_color":$(c)}},'
   'transformation:{translation:[$(x),$(y),$(z)],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.7f,0.7f,0.7f]}}\n')
fn('bat_pop', '''# @s perd un ballon (touché, tombé) ; plus de ballon = éliminé
execute if score @s mg.kbl matches ..0 run return 0
scoreboard players remove @s mg.kbl 1
scoreboard players operation $me mg.st = @s mg.ri
scoreboard players operation $kbs mg.st = @s mg.kbl
scoreboard players add $kbs mg.st 1
execute as @e[type=minecraft:item_display,tag=mg.kbal] if score @s mg.ri = $me mg.st run function mg:kart/bat_burst
title @s subtitle [{"text":"🎈 Ballon crevé ! ","color":"red"},{"score":{"name":"@s","objective":"mg.kbl"},"color":"white","bold":true},{"text":" restant(s)","color":"gray"}]
title @s title ""
execute if score @s mg.kbl matches ..0 run function mg:kart/bat_out
''')
fn('bat_burst', '''# @s = ballon : crevé si c'est celui du rang $kbs
execute if score $kbs mg.st matches 1 unless entity @s[tag=mg.kbal1] run return 0
execute if score $kbs mg.st matches 2 unless entity @s[tag=mg.kbal2] run return 0
execute if score $kbs mg.st matches 3 unless entity @s[tag=mg.kbal3] run return 0
execute at @s run particle minecraft:poof ~ ~1.4 ~ 0.2 0.2 0.2 0.05 12
execute at @s run playsound minecraft:entity.firework_rocket.blast master @a[tag=mg.play,distance=..30] ~ ~ ~ 1 1.8
kill @s
''')
fn('bat_out', f'''# @s n'a plus de ballon : éliminé, son kart explose, il regarde la suite d'en haut
tag @s add mg.kout
tag @s add mg.kfin
scoreboard players add $kouto mg.st 1
scoreboard players operation @s mg.kfp = $kouto mg.st
scoreboard players operation $me mg.st = @s mg.ri
execute as {KART}] if score @s mg.ri = $me mg.st at @s run particle minecraft:explosion_emitter ~ ~0.5 ~ 0 0 0 0 1
execute as {KART}] if score @s mg.ri = $me mg.st at @s run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..40] ~ ~ ~ 1 0.8
ride @s dismount
execute as {KART}] if score @s mg.ri = $me mg.st on passengers unless entity @s[type=minecraft:player] run kill @s
execute as {KART}] if score @s mg.ri = $me mg.st run kill @s
execute as @e[type=minecraft:item_display,tag=mg.kcam] if score @s mg.ri = $me mg.st run kill @s
execute as @e[type=minecraft:item_display,tag=mg.khead] if score @s mg.ri = $me mg.st run kill @s
gamemode spectator @s
function mg:kart/t3/spec_tp
title @s title [{{"text":"ÉLIMINÉ","color":"red","bold":true}}]
title @s subtitle [{{"text":"Plus de ballon : regarde la fin de la bataille","color":"gray"}}]
tellraw @a[tag=mg.play] [{{"text":"🎈 ","color":"red"}},{{"selector":"@s","color":"yellow"}},{{"text":" a perdu tous ses ballons !","color":"gray"}}]
''')
fn('bat_progress', '''# Classement en bataille : en lice (100 + ballons) devant les éliminés (ordre d'élimination)
scoreboard players operation @s mg.kpg = @s mg.kbl
scoreboard players add @s mg.kpg 100
execute if entity @s[tag=mg.kout] run scoreboard players operation @s mg.kpg = @s mg.kfp
''')
bh = ['# Barre du bas en bataille : ballons, temps restant, objet, vitesse',
      'execute if entity @s[tag=mg.kout] run return run title @s actionbar [{"text":"💥 Éliminé : attends la fin de la bataille","color":"gray"}]',
      'scoreboard players operation $kmh mg.st = @s mg.ksp', 'scoreboard players operation $kmh mg.st *= #kkmh mg.st',
      'scoreboard players operation $kmh mg.st /= #k100 mg.st', 'execute if score $kmh mg.st matches ..-1 run scoreboard players operation $kmh mg.st *= #km1 mg.st',
      f'scoreboard players set $ksl mg.st {BAT_TIME}', 'scoreboard players operation $ksl mg.st -= $ktime mg.st', 'scoreboard players operation $ksl mg.st /= #k20 mg.st']
bbase = ('{"text":"🎈 ","color":"red"},{"score":{"name":"@s","objective":"mg.kbl"},"color":"white","bold":true},{"text":"   ⏱ ","color":"gold"},'
         '{"score":{"name":"$ksl","objective":"mg.st"},"color":"yellow"},{"text":" s   ","color":"gold"},')
bh.append(f'execute unless score @s mg.khi matches 1.. if score @s mg.kit matches 0 run title @s actionbar [{bbase}{{"text":"(pas d\'objet)","color":"dark_gray"}}{tail}]')
for k, (name, color) in ITEMS.items():
    extra = ',{"text":" ×","color":"gray"},{"score":{"name":"@s","objective":"mg.kic"},"color":"white","bold":true}' if k in CHARGES else ''
    bh.append(f'execute unless score @s mg.khi matches 1.. if score @s mg.kit matches {k} run title @s actionbar [{bbase}{{"text":"{name}","color":"{color}","bold":true}}{extra},{{"text":" (clic droit)","color":"gray"}}{tail}]')
fn('bat_hud', '\n'.join(bh) + '\n')
fn('bat_tick', '''# Bataille : un peu de musique d'ambiance pour les 30 dernières secondes
execute if score $ktime mg.st matches 3000 run tellraw @a[tag=mg.play] [{"text":"⏱ 30 secondes !","color":"gold","bold":true}]
execute if score $ktime mg.st matches 3000 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 1 1.2
''')

# ---- objet dans toutes les cases de la barre (le clic droit marche quelle que soit la case tenue ; tout disparaît à l'utilisation)
fn('item_fill', ''.join(f'item replace entity @s hotbar.{k} from entity @s hotbar.4' + chr(10) for k in (0, 1, 2, 3, 5, 6, 7, 8)))
patch_fn('item_give', 'scoreboard players set @s mg.kic 1' + chr(10), 'function mg:kart/item_fill' + chr(10) + 'scoreboard players set @s mg.kic 1' + chr(10))

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sound_part.py'), encoding='utf-8').read())
