"""⚔ Terra Nova RPG, 2e couche : difficulté par zone, élites et butin, caractéristiques et fiche de personnage, quêtes secondaires,
trésors cachés, succès et titres, XP partagée en groupe, chiffres de dégâts. Exécuté à la fin de tv_rpg.py (même espace de noms).

Scores : mg.trsp points à répartir, mg.trs1 Vigueur, mg.trs2 Force, mg.trs3 Agilité, mg.trs4 Précision (10 au plus chacune),
mg.trkt monstres abattus, mg.trel élites abattues, mg.trac succès (bits), mg.trtc trésors (bits), mg.trsq quêtes secondaires (bits faites),
mg.trsa quêtes secondaires acceptées (bits), mg.trq4 progression de la quête du volcan.
"""
ZM = {'v': 2, 'n': 3, 'e': 4, 'w': 5, 's': 6}               # multiplicateur de zone × 2 (vallée ×1 … volcan ×3)
ZONE_ADJ = {'v': '', 'n': 'des brumes', 'e': 'des plaines', 'w': 'du canyon', 's': 'des cendres'}
ZONE_COL = {'v': 'green', 'n': 'dark_aqua', 'e': 'gold', 'w': 'red', 's': 'dark_red'}

# ================================================================ difficulté par zone + élites (appliqué aux monstres qui apparaissent)
for k, m2 in ZM.items():
    if k == 'v':
        continue
    w(f'{P}/zone/{k}', [f'# Monstres apparus dans la zone {k} (marqués mg.trnew) : PV et dégâts ×{m2 / 2:g}, une chance sur 10 d\'élite',
                        f'execute as @e[tag=mg.trnew] run attribute @s minecraft:max_health modifier add mg:trzone {m2 / 2 - 1:g} add_multiplied_base',
                        f'execute as @e[tag=mg.trnew] run attribute @s minecraft:attack_damage modifier add mg:trzone {(m2 / 2 - 1) * 0.6:g} add_multiplied_base',
                        'execute as @e[tag=mg.trnew] store result entity @s Health float 1 run attribute @s minecraft:max_health get',
                        f'scoreboard players set @e[tag=mg.trnew] mg.trzm {m2}',
                        f'execute if predicate mg:tv_c10 as @e[tag=mg.trnew,tag=mg.tvhos,sort=random,limit=1] run function mg:{P}/elite'])
EL = ['# @s devient une élite : affixe au hasard, PV ×2, contour doré, butin d\'élite à sa mort',
      'tag @s add mg.trelite', 'attribute @s minecraft:max_health modifier add mg:trelite 1 add_multiplied_total',
      'execute store result entity @s Health float 1 run attribute @s minecraft:max_health get',
      'data merge entity @s {DeathLootTable:"mg:terra/elite",CustomNameVisible:1b}',
      'execute store result score $r mg.st run random value 1..3',
      'execute if score $r mg.st matches 1 run effect give @s minecraft:speed infinite 1 true',
      'execute if score $r mg.st matches 1 run effect give @s minecraft:strength infinite 0 true',
      'execute if score $r mg.st matches 1 run data merge entity @s {CustomName:{"text":"★ Élite enragée","color":"gold","bold":true}}',
      'execute if score $r mg.st matches 2 run attribute @s minecraft:scale modifier add mg:trelite 0.35 add_multiplied_base',
      'execute if score $r mg.st matches 2 run attribute @s minecraft:knockback_resistance base set 1',
      'execute if score $r mg.st matches 2 run data merge entity @s {CustomName:{"text":"★ Colosse","color":"gold","bold":true}}',
      'execute if score $r mg.st matches 3 run effect give @s minecraft:regeneration infinite 1 true',
      'execute if score $r mg.st matches 3 run data merge entity @s {CustomName:{"text":"★ Élite régénérante","color":"gold","bold":true}}',
      'scoreboard players operation $tvi mg.st = @s mg.tvid',
      'execute as @e[tag=mg.tvp] if score @s mg.tvid = $tvi mg.st run data merge entity @s {Glowing:1b,glow_color_override:16766720}']
w(f'{P}/elite', EL)
with open(os.path.join(C.D, 'predicate', 'tv_c10.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'condition': 'minecraft:random_chance', 'chance': 0.1}, f, indent=2)
    f.write('\n')


def loot_item(n, name, col, model, lore):
    return {'function': 'minecraft:set_components', 'components': {
        'minecraft:custom_data': {'trloot': n}, 'minecraft:item_model': model, 'minecraft:enchantment_glint_override': True,
        'minecraft:custom_name': {'text': name, 'color': col, 'italic': False, 'bold': True},
        'minecraft:lore': [{'text': lore, 'color': 'gray', 'italic': False}]}}


ELITE_LOOT = {'type': 'minecraft:entity', 'pools': [
    {'rolls': 1, 'conditions': [{'condition': 'minecraft:killed_by_player'}], 'entries': [
        {'type': 'minecraft:item', 'name': 'minecraft:paper', 'functions': [loot_item(1, '📦 Butin d\'élite', 'gold', 'minecraft:bundle', 'Ramasse-le : crédits, trophées…')]}]},
    {'rolls': 1, 'conditions': [{'condition': 'minecraft:killed_by_player'}, {'condition': 'minecraft:random_chance', 'chance': 0.25}], 'entries': [
        {'type': 'minecraft:item', 'name': 'minecraft:paper', 'functions': [loot_item(2, '💎 Gemme d\'ambre', 'light_purple', 'minecraft:amethyst_shard',
                                                                                     'Ramasse-la : +1 point de caractéristique')]}]}]}
os.makedirs(os.path.join(C.D, 'loot_table', 'terra'), exist_ok=True)
with open(os.path.join(C.D, 'loot_table', 'terra', 'elite.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump(ELITE_LOOT, f, indent=2, ensure_ascii=False)
    f.write('\n')
# ramassage du butin (toutes les 10 ticks)
w(f'{P}/loot', ['# @s a ramassé du butin d\'élite / des gemmes : ouverture',
                'execute store result score $n mg.st run clear @s *[custom_data~{trloot:1}]', f'execute if score $n mg.st matches 1.. run function mg:{P}/loot_open',
                'execute store result score $g mg.st run clear @s *[custom_data~{trloot:2}]', f'execute if score $g mg.st matches 1.. run function mg:{P}/loot_gem'])
w(f'{P}/loot_open', ['# Un butin d\'élite : récompense tirée au sort selon la zone (×1 à ×3)', 'scoreboard players add @s mg.trel 1',
                     'execute store result score $r mg.st run random value 1..100',
                     'scoreboard players operation $c mg.st = @s mg.trrg', 'scoreboard players add $c mg.st 1',
                     'scoreboard players set #60 mg.st 60', 'scoreboard players operation $c mg.st *= #60 mg.st',
                     'scoreboard players operation @s mg.tvc += $c mg.st',
                     'tellraw @s [{"text":"📦 Butin d\'élite : +","color":"gold"},{"score":{"name":"$c","objective":"mg.st"},"color":"yellow"},{"text":" ₵","color":"yellow"}]',
                     'execute if score $r mg.st matches 1..30 run scoreboard players add @s mg.trgr 3',
                     'execute if score $r mg.st matches 1..30 run tellraw @s {"text":"  +3 griffes","color":"gray"}',
                     'execute if score $r mg.st matches 31..50 run scoreboard players add @s mg.trvn 2',
                     'execute if score $r mg.st matches 31..50 run tellraw @s {"text":"  +2 glandes à venin","color":"gray"}',
                     'execute if score $r mg.st matches 51..65 run scoreboard players add @s mg.trai 2',
                     'execute if score $r mg.st matches 51..65 run tellraw @s {"text":"  +2 ailes","color":"gray"}',
                     'execute if score $r mg.st matches 66..75 run scoreboard players add @s mg.trdn 2',
                     'execute if score $r mg.st matches 66..75 run tellraw @s {"text":"  +2 dents","color":"gray"}',
                     'execute if score $r mg.st matches 76..80 run scoreboard players add @s mg.trec 1',
                     'execute if score $r mg.st matches 76..80 run tellraw @s {"text":"  +1 écaille de spinosaure (rare !)","color":"dark_aqua"}',
                     f'function mg:{P}/xp {{n:80}}', 'execute at @s run playsound minecraft:block.chest.open player @s ~ ~ ~ 0.7 1.2',
                     'scoreboard players remove $n mg.st 1', f'execute if score $n mg.st matches 1.. run function mg:{P}/loot_open'])
w(f'{P}/loot_gem', ['scoreboard players operation @s mg.trsp += $g mg.st',
                    'tellraw @s [{"text":"💎 Gemme d\'ambre : +","color":"light_purple"},{"score":{"name":"$g","objective":"mg.st"},"color":"light_purple","bold":true},{"text":" point(s) de caractéristique à répartir (carnet, case 6)","color":"gray"}]',
                    'execute at @s run playsound minecraft:block.amethyst_block.chime player @s ~ ~ ~ 1 1.2'])

# ================================================================ XP des combats : zone, groupe, compteur
w(f'{P}/xpk', ['# @s a abattu un monstre : XP × zone (selon sa position), partage de moitié aux colons à 24 blocs, compteur',
               'scoreboard players add @s mg.trkt 1', '$scoreboard players set $xk mg.st $(n)', 'scoreboard players set $zm mg.st 2',
               'execute if score @s mg.trrg matches 1 run scoreboard players set $zm mg.st 3', 'execute if score @s mg.trrg matches 2 run scoreboard players set $zm mg.st 4',
               'execute if score @s mg.trrg matches 3 run scoreboard players set $zm mg.st 5', 'execute if score @s mg.trrg matches 4 run scoreboard players set $zm mg.st 6',
               'scoreboard players operation $xk mg.st *= $zm mg.st', 'scoreboard players operation $xk mg.st /= #2 mg.st',
               'execute store result storage mg:terra s.xp int 1 run scoreboard players get $xk mg.st', f'function mg:{P}/xpm with storage mg:terra s',
               'scoreboard players operation $xk mg.st /= #2 mg.st', 'execute store result storage mg:terra s.xp int 1 run scoreboard players get $xk mg.st',
               f'execute at @s as @a[tag=mg.tvw,distance=0.1..24] run function mg:{P}/xpm with storage mg:terra s'])

# ================================================================ caractéristiques, carnet du colon (fiche)
STATS = [(1, 'mg.trs1', '❤ Vigueur', 'red', '+2 PV par point'), (2, 'mg.trs2', '⚔ Force', 'gold', '+0,5 dégât de mêlée par point'),
         (3, 'mg.trs3', '💨 Agilité', 'green', '+2 % de vitesse par point'), (4, 'mg.trs4', '🎯 Précision', 'aqua', '+1 dégât de fusil tous les 2 points')]
w(f'{P}/st/apply', ['# @s : bonus des caractéristiques (modificateurs mg:trst*)',
                    'attribute @s minecraft:max_health modifier remove mg:trst', 'attribute @s minecraft:attack_damage modifier remove mg:trst',
                    'attribute @s minecraft:movement_speed modifier remove mg:trst',
                    'execute store result storage mg:terra st.v float 2 run scoreboard players get @s mg.trs1',
                    'execute store result storage mg:terra st.f float 0.5 run scoreboard players get @s mg.trs2',
                    'execute store result storage mg:terra st.a float 0.02 run scoreboard players get @s mg.trs3',
                    f'function mg:{P}/st/apply_m with storage mg:terra st'])
w(f'{P}/st/apply_m', ['$attribute @s minecraft:max_health modifier add mg:trst $(v) add_value',
                      '$attribute @s minecraft:attack_damage modifier add mg:trst $(f) add_value',
                      '$attribute @s minecraft:movement_speed modifier add mg:trst $(a) add_multiplied_base'])
w(f'{P}/st/remove', ['attribute @s minecraft:max_health modifier remove mg:trst', 'attribute @s minecraft:attack_damage modifier remove mg:trst',
                     'attribute @s minecraft:movement_speed modifier remove mg:trst'])
for n, obj, name, col, eff in STATS:
    w(f'{P}/st/add_{n}', [f'# @s met un point en {name}', 'execute unless score @s mg.trsp matches 1.. run return run tellraw @s {"text":"Aucun point à répartir.","color":"gray"}',
                          f'execute if score @s {obj} matches 10.. run return run tellraw @s {{"text":"{name} est déjà au maximum (10).","color":"gray"}}',
                          'scoreboard players remove @s mg.trsp 1', f'scoreboard players add @s {obj} 1', f'function mg:{P}/st/apply',
                          f'tellraw @s [{{"text":"{name} ","color":"{col}","bold":true}},{{"score":{{"name":"@s","objective":"{obj}"}},"color":"white"}},{{"text":" / 10  ({eff})","color":"gray"}}]',
                          'execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.7 1.4', f'function mg:{P}/sheet'])
w(f'{P}/st/reset', ['# @s : réinitialise ses points (200 ₵)', 'execute unless score @s mg.tvc matches 200.. run return run tellraw @s {"text":"Il faut 200 ₵ pour redistribuer tes points.","color":"red"}',
                    'scoreboard players remove @s mg.tvc 200'] + [f'scoreboard players operation @s mg.trsp += @s {o}' for _, o, *_r in STATS] +
  [f'scoreboard players set @s {o} 0' for _, o, *_r in STATS] + [f'function mg:{P}/st/apply', 'tellraw @s {"text":"♻ Points redistribuables (200 ₵).","color":"yellow"}',
                                                                 f'function mg:{P}/sheet'])
SHEET = [{'text': '\n📖 Carnet du colon — ', 'color': 'gold', 'bold': True}, {'selector': '@s', 'color': 'yellow'},
         {'text': '\n⭐ Niveau ', 'color': 'gold'}, {'score': {'name': '@s', 'objective': 'mg.trlv'}, 'color': 'yellow', 'bold': True},
         {'text': '   XP ', 'color': 'aqua'}, {'score': {'name': '@s', 'objective': 'mg.trxp'}, 'color': 'aqua'},
         {'text': '   ₵ ', 'color': 'green'}, {'score': {'name': '@s', 'objective': 'mg.tvc'}, 'color': 'green'},
         {'text': '\n☠ Monstres abattus ', 'color': 'gray'}, {'score': {'name': '@s', 'objective': 'mg.trkt'}, 'color': 'white'},
         {'text': '   ★ Élites ', 'color': 'gray'}, {'score': {'name': '@s', 'objective': 'mg.trel'}, 'color': 'white'},
         {'text': '\n✦ Points à répartir : ', 'color': 'light_purple'}, {'score': {'name': '@s', 'objective': 'mg.trsp'}, 'color': 'light_purple', 'bold': True}]
for n, obj, name, col, eff in STATS:
    SHEET += [{'text': f'\n {name} ', 'color': col}, {'score': {'name': '@s', 'objective': obj}, 'color': 'white', 'bold': True}, {'text': '/10 ', 'color': 'gray'},
              {'text': '[+]', 'color': 'green', 'bold': True, 'click_event': {'action': 'run_command', 'command': f'/trigger mg.trtk set {700 + n}'},
               'hover_event': {'action': 'show_text', 'value': eff}}]
SHEET += [{'text': '\n ', 'color': 'gray'}, {'text': '[♻ Redistribuer : 200 ₵]', 'color': 'yellow', 'click_event': {'action': 'run_command', 'command': '/trigger mg.trtk set 709'}},
          {'text': '  ', 'color': 'gray'}, {'text': '[🏆 Succès]', 'color': 'gold', 'click_event': {'action': 'run_command', 'command': '/trigger mg.trtk set 720'}},
          {'text': '  ', 'color': 'gray'}, {'text': '[📖 Bestiaire]', 'color': 'aqua', 'click_event': {'action': 'run_command', 'command': '/trigger mg.trtk set 210'}}]
CARNET = (f'{WF}[custom_data={{tv:15}},item_model="minecraft:writable_book",unbreakable={{}},custom_name={nm("📖 Carnet du colon", "gold")},'
          f'lore={lo("Clic droit : fiche de personnage,", "caractéristiques, succès, bestiaire")}]')
w(f'{P}/sheet', ['# @s : fiche de personnage dans le chat (scores résolus côté serveur)', 'scoreboard players enable @s mg.trtk', 'tellraw @s ' + js(SHEET),
                 'execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1'])
w(f'{P}/carnet_kit', [f'item replace entity @s hotbar.5 with {CARNET}'])

# ================================================================ chiffres de dégâts (texte flottant)
w(f'{P}/dmgnum', ['# Chiffre de dégâts au-dessus de @s (macro d), qui monte et disparaît',
                  '$summon minecraft:text_display ~ ~1.8 ~ {Tags:["mg.tv","mg.trdmg"],billboard:"center",teleport_duration:10,text:{"text":"-$(d)","color":"red","bold":true},background:0,shadow:1b,see_through:1b}',
                  'scoreboard players set @e[tag=mg.trdmg,distance=..2.5,sort=nearest,limit=1] mg.tvst 12'])
w(f'{P}/dmg_tick', ['# Chiffres de dégâts : montée puis disparition', 'scoreboard players remove @e[type=minecraft:text_display,tag=mg.trdmg] mg.tvst 1',
                    'execute as @e[type=minecraft:text_display,tag=mg.trdmg,scores={mg.tvst=11}] at @s run tp @s ~ ~0.9 ~',
                    'kill @e[type=minecraft:text_display,tag=mg.trdmg,scores={mg.tvst=..0}]'])

# ================================================================ trésors cachés
TC = ['# Tous les 5 ticks : ramassage des trésors (accroupi à 2 blocs)']
DECO = ['# Session : décor des trésors cachés (coffre enterré, fanion)']
for i, (k, x, y, z) in enumerate(CACHES):
    TC.append(f'execute positioned {x + 0.5} {y} {z + 0.5} as @a[tag=mg.tvw,distance=..2.2] if predicate mg:sneak run function mg:{P}/tc/{i}')
    DECO += [f'execute if block {x} {y} {z} minecraft:air run setblock {x} {y} {z} minecraft:barrel[facing=up]',
             f'execute if block {x + 1} {y} {z} minecraft:air run setblock {x + 1} {y} {z} minecraft:spruce_fence',
             f'execute if block {x + 1} {y + 1} {z} minecraft:air run setblock {x + 1} {y + 1} {z} minecraft:spruce_fence',
             f'execute if block {x + 1} {y + 2} {z} minecraft:air run setblock {x + 1} {y + 2} {z} minecraft:red_wool']
    m = ZM[k]
    w(f'{P}/tc/{i}', [f'# @s ouvre le trésor caché n° {i + 1} ({k})'] + bit_test('mg.trtc', i) +
      ['execute if score $b mg.st matches 1 run return run title @s actionbar {"text":"🗝 Déjà fouillé","color":"gray"}',
       f'scoreboard players operation @s mg.trtc += #p{i} mg.st', f'scoreboard players add @s mg.tvc {75 * m}',
       f'scoreboard players add @s mg.trgr {m}', f'function mg:{P}/xp {{n:{60 * m}}}',
       'execute store result score $r mg.st run random value 1..3', 'execute if score $r mg.st matches 1 run scoreboard players add @s mg.trsp 1',
       'title @s times 5 40 10', 'title @s title {"text":"🗝 TRÉSOR CACHÉ","color":"gold","bold":true}',
       f'title @s subtitle {js(TEXT(f"+{75 * m} ₵, +{m} griffes" , "yellow"))}',
       'execute if score $r mg.st matches 1 run tellraw @s {"text":"  💎 et une gemme d\'ambre : +1 point de caractéristique !","color":"light_purple"}',
       'execute at @s run playsound minecraft:block.chest.open player @s ~ ~ ~ 1 0.8', 'execute at @s run particle minecraft:happy_villager ~ ~1 ~ 0.6 0.6 0.6 0 20'])
TC += [f'execute positioned {x + 0.5} {y + 1.2} {z + 0.5} run particle minecraft:end_rod ~ ~ ~ 0.15 0.3 0.15 0.01 1' for (k, x, y, z) in CACHES]
w(f'{P}/tc_tick', TC)
w(f'{P}/tc_deco', DECO)

# ================================================================ quêtes secondaires (un PNJ par région)
SIDE = {  # n° : (clé, PNJ, camp n°, titre, texte, type, objet/score, quantité, récompenses (xp, crédits, extra))
    1: ('ermite', '🌿 Bastien, ermite', 2, 'Remèdes du marais',
        'Le venin des dilophosaures, bien dosé, soigne les fièvres de la colonie. Rapporte-m\'en 5 glandes et je te donne de quoi te soigner.',
        'give', 'mg.trvn', 5, (300, 150, 'medk'), True),
    2: ('nyla2', '🏹 Nyla, éclaireuse', 3, 'Le ciel des Aiguilles',
        'Les ptéranodons attaquent nos patrouilles. Rapporte 6 ailes pour prouver que le ciel est dégagé.', 'give', 'mg.trai', 6, (400, 200, None), True),
    3: ('ines', '⛏ Inès, prospectrice', 4, 'La mine maudite',
        'Ma mine, à l\'ouest de l\'arche, grouille de slashers et d\'un alpha énorme. Nettoie-la et elle est à toi… enfin, ses filons.',
        'dungeon', 2, 1, (500, 300, 'point'), False),
    4: ('arno', '🌋 Arno, vulcanologue', 5, 'Les gardiens de cendre',
        'Les carnotaures du Mont Cendre m\'empêchent de prendre mes mesures. Abats-en 3 sur le volcan.', 'kill_s', 'mg.trq4', 3, (600, 400, 'gem'), False),
}
SIDE_NPCS = {}
for q, (key, name, campn, title, text, typ, obj, qty, (xp, cr, extra), rep) in SIDE.items():
    c = [cc for cc in CAMPS if cc[0] == campn][0]
    cx, cy, cz = c[3] - 2.5, c[4], c[5] - 0.5
    if key == 'nyla2':
        continue
    SIDE_NPCS[q] = (key, name, (cx - 2.5, cy, cz - 2.5))
for q, (key, name, pos) in SIDE_NPCS.items():
    nid = 4 + q
    NPCS[nid] = (key, name, 'yellow', pos, 0, {'ermite': 'minecraft:cleric', 'ines': 'minecraft:toolsmith', 'arno': 'minecraft:mason'}[key])
for q, (key, name, campn, title, text, typ, obj, qty, (xp, cr, extra), rep) in SIDE.items():
    bit = q - 1
    rew = f'{xp} XP, {cr} ₵' + {'medk': ', 3 trousses de soins', 'point': ', 1 point de caractéristique', 'gem': ', 1 gemme d\'ambre', None: ''}[extra]
    D = dlg(name, 'yellow', text + f'\nRécompense : {rew}.', [(f'Accepter : {title}', 'green', 'Quête secondaire', 800 + q * 10 + 1),
                                                              (f'Rendre la quête', 'gold', 'Si l\'objectif est rempli', 800 + q * 10 + 2)])
    w(f'{P}/sq/{q}_talk', [f'# @s parle de la quête secondaire « {title} »'] + bit_test('mg.trsq', bit) +
      ([f'execute if score $b mg.st matches 1 run return run tellraw @s {js(TEXT(name + " : « Merci encore, colon. »", "yellow"))}'] if not rep else []) + show(D))
    ACC = [f'# @s accepte « {title} »'] + bit_test('mg.trsa', bit) + ['execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}']
    if not rep:
        ACC += bit_test('mg.trsq', bit) + ['execute if score $b mg.st matches 1 run return 0']
    ACC += [f'scoreboard players operation @s mg.trsa += #p{bit} mg.st', f'tellraw @s {js([TEXT("📜 Quête secondaire : ", "yellow", bold=True), TEXT(title + " — " + text.split(".")[0] + ".", "gray")])}']
    if typ == 'kill_s':
        ACC.append(f'scoreboard players set @s {obj} 0')
    w(f'{P}/sq/{q}_accept', ACC)
    TURN = [f'# @s rend « {title} »'] + bit_test('mg.trsa', bit) + ['execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d\'abord la quête.","color":"gray"}']
    if typ == 'give':
        TURN += [f'execute unless score @s {obj} matches {qty}.. run return run tellraw @s {js(TEXT(f"Il en faut {qty}.", "red"))}', f'scoreboard players remove @s {obj} {qty}']
    elif typ == 'dungeon':
        TURN += bit_test('mg.trdg', obj) + ['execute if score $b mg.st matches 0 run return run tellraw @s {"text":"L\'alpha de la mine rôde toujours…","color":"red"}']
    else:
        TURN += [f'execute unless score @s {obj} matches {qty}.. run return run tellraw @s [{{"text":"Carnotaures abattus sur le volcan : ","color":"red"}},{{"score":{{"name":"@s","objective":"{obj}"}},"color":"yellow"}},{{"text":" / {qty}","color":"yellow"}}]']
    TURN += [f'scoreboard players operation @s mg.trsa -= #p{bit} mg.st'] + bit_test('mg.trsq', bit) + \
            [f'execute if score $b mg.st matches 0 run scoreboard players operation @s mg.trsq += #p{bit} mg.st',
             f'scoreboard players add @s mg.tvc {cr}', f'function mg:{P}/xp {{n:{xp}}}', 'title @s times 5 40 10', f'title @s title {js(TEXT("✔ " + title, "yellow", bold=True))}',
             f'title @s subtitle {js(TEXT(rew, "gray"))}', 'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1']
    TURN += {'medk': [f'give @s {MEDK} 3'], 'point': ['scoreboard players add @s mg.trsp 1'], 'gem': ['scoreboard players add @s mg.trsp 1'], None: []}[extra]
    w(f'{P}/sq/{q}_turn', TURN)
w(f'{P}/npc_ermite', [f'function mg:{P}/sq/1_talk'])
w(f'{P}/npc_ines', [f'function mg:{P}/sq/3_talk'])
w(f'{P}/npc_arno', [f'function mg:{P}/sq/4_talk'])
SQ_TK = [f'execute if score $tk mg.st matches {800 + q * 10 + 1} run function mg:{P}/sq/{q}_accept' for q in SIDE] + \
        [f'execute if score $tk mg.st matches {800 + q * 10 + 2} run function mg:{P}/sq/{q}_turn' for q in SIDE]

# ================================================================ succès et titres
ACH = [  # (n°, titre, description, condition (ligne execute if …), XP)
    (0, 'Premier sang', 'Abattre un premier monstre', 'score @s mg.trkt matches 1..', 50),
    (1, 'Chasseur', 'Abattre 50 monstres', 'score @s mg.trkt matches 50..', 200),
    (2, 'Exterminateur', 'Abattre 250 monstres', 'score @s mg.trkt matches 250..', 600),
    (3, 'Chasseur d\'élites', 'Abattre 10 élites', 'score @s mg.trel matches 10..', 400),
    (4, 'Reine déchue', 'Vaincre le Spinosaure', 'score @s mg.trch matches 45..', 300),
    (5, 'Briseur de fort', 'Vaincre le lieutenant Varek', 'score @s mg.trch matches 64..', 300),
    (6, 'Régicide', 'Vaincre le Roi Tyran', 'score @s mg.trch matches 85..', 500),
    (7, 'Naturaliste', 'Compléter le bestiaire', f'score @s mg.trbs matches {2 ** 13 - 1}', 400),
    (8, 'Maître des donjons', 'Terminer les 4 donjons', 'score @s mg.trdg matches 15', 600),
    (9, 'Chasseur de trésors', 'Trouver les 15 trésors cachés', f'score @s mg.trtc matches {2 ** len(CACHES) - 1}', 500),
    (10, 'Légende vivante', 'Atteindre le niveau 20', 'score @s mg.trlv matches 20..', 1000),
    (11, 'Fortuné', 'Posséder 5000 ₵', 'score @s mg.tvc matches 5000..', 300),
]
AC = ['# Toutes les 5 s, @s : succès débloqués']
for n, title, desc, cond, xp in ACH:
    w(f'{P}/ach/{n}', [f'# Succès : {title}'] + bit_test('mg.trac', n) + ['execute if score $b mg.st matches 1 run return 0',
                                                                         f'scoreboard players operation @s mg.trac += #p{n} mg.st', f'function mg:{P}/xp {{n:{xp}}}',
                                                                         'tellraw @a[tag=mg.tvw] ' + js([TEXT('🏆 ', 'gold'), {'selector': '@s', 'color': 'yellow'},
                                                                                                          TEXT(' obtient le titre ', 'gray'), TEXT('« ' + title + ' »', 'gold', bold=True),
                                                                                                          TEXT(' (' + desc + ')', 'dark_gray')]),
                                                                         'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.3'])
    AC.append(f'execute if {cond} run function mg:{P}/ach/{n}')
w(f'{P}/achievements', AC)
AL = ['# @s : liste des succès', 'tellraw @s ' + js(TEXT('\n🏆 Succès et titres', 'gold', bold=True))]
for n, title, desc, cond, xp in ACH:
    AL += bit_test('mg.trac', n)
    AL.append('execute if score $b mg.st matches 1 run tellraw @s ' + js([TEXT(' ✔ ', 'green'), TEXT(title, 'gold', bold=True), TEXT(' — ' + desc, 'gray')]))
    AL.append('execute if score $b mg.st matches 0 run tellraw @s ' + js([TEXT(' ✖ ', 'dark_gray'), TEXT(title, 'gray'), TEXT(' — ' + desc, 'dark_gray')]))
w(f'{P}/ach_list', AL)

# ================================================================ boucles et câblage
w(f'{P}/tick2', ['# Chaque tick (dimension) : butin, trésors, chiffres de dégâts',
                 f'execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw] if items entity @s container.* *[custom_data~{{trloot:1}}] run function mg:{P}/loot',
                 f'execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw] if items entity @s container.* *[custom_data~{{trloot:2}}] run function mg:{P}/loot',
                 f'execute if score $tvq5 mg.st matches 0 run function mg:{P}/tc_tick', f'function mg:{P}/dmg_tick'])
w(f'{P}/second2', ['# Chaque seconde : succès (toutes les 5 s), quête du volcan',
                   f'execute if score $trq3 mg.st matches 0 as @a[tag=mg.tvw] run function mg:{P}/achievements'])
TK2 = [f'execute if score $tk mg.st matches {700 + n} run function mg:{P}/st/add_{n}' for n, *_r in STATS] + \
      [f'execute if score $tk mg.st matches 709 run function mg:{P}/st/reset', f'execute if score $tk mg.st matches 710 run function mg:{P}/sheet',
       f'execute if score $tk mg.st matches 720 run function mg:{P}/ach_list'] + SQ_TK
w(f'{P}/tk2', ['# Choix de la 2e couche du RPG ($tk)'] + TK2)
C.objectives([(o, 'dummy') for o in ('mg.trsp', 'mg.trs1', 'mg.trs2', 'mg.trs3', 'mg.trs4', 'mg.trkt', 'mg.trel', 'mg.trac', 'mg.trtc', 'mg.trsq', 'mg.trsa',
                                     'mg.trq4', 'mg.trzm')])

# PNJ secondaires (session), aiguillage des PNJ réécrit, Nyla : quête des ailes après son chapitre
SU2 = ['# Session : PNJ des quêtes secondaires, décor des trésors'] + [f'function mg:{P}/tc_deco']
for nid, (key, name, col, (x, y, z), rot, prof) in NPCS.items():
    if nid < 5:
        continue
    SU2 += [f'summon minecraft:villager {x} {y} {z} {{Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[{rot}f,0f],'
            f'VillagerData:{{profession:"{prof}",level:5,type:"minecraft:swamp"}},Offers:{{Recipes:[]}},CustomName:{js(TEXT(name, col))},CustomNameVisible:1b}}',
            f'summon minecraft:interaction {x} {y} {z} {{Tags:["mg.tv","mg.trnpc","mg.tvn"],width:1.1f,height:2.2f,response:1b}}',
            f'scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid {nid}', 'tag @e[tag=mg.tvn] remove mg.tvn',
            tdisp(x, y + 2.35, z, [TEXT('❗ Quête secondaire\n', 'yellow', bold=True), TEXT('clic droit', 'gray', bold=False)], 0.6)]
w(f'{P}/setup2', SU2)
w(f'{P}/st/backfill', ['scoreboard players operation @s mg.trsp = @s mg.trlv', 'scoreboard players remove @s mg.trsp 1'])
w(f'{P}/npc', ['# @s parle au PNJ $npc'] + [f'execute if score $npc mg.st matches {nid} run return run function mg:{P}/npc_{key}' for nid, (key, *_r) in NPCS.items()])
w(f'{P}/d/nyla_gen', ['execute if score @s mg.trch matches 60.. run return run function mg:terra/rpg/sq/2_talk'] +
  show(dlg('🏹 Nyla, éclaireuse', 'green', 'Les plaines sont belles mais dangereuses : méfie-toi des ptéranodons près des Aiguilles.',
           [('📜 Rappel de l\'objectif', 'yellow', 'Objectif en cours', 9)])))
w(f'{P}/kc_hook', ['# @s a abattu un carnotaure : quête du vulcanologue (sur le volcan)'] + bit_test('mg.trsa', 3) +
  ['execute if score $b mg.st matches 1 if score @s mg.trrg matches 4 run scoreboard players add @s mg.trq4 1',
   'execute if score $b mg.st matches 1 if score @s mg.trrg matches 4 run tellraw @s [{"text":"🌋 Gardiens de cendre : ","color":"gold"},{"score":{"name":"@s","objective":"mg.trq4"},"color":"yellow"},{"text":" / 3","color":"yellow"}]'])
