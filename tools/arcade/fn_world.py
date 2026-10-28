"""⛏ Filon : île, entités, régénération du chunk, butin des coffres. Exécuté par gen_filon.py (exec : mêmes globals), jamais seul."""

# ---------------------------------------------------------------- île (construite une fois)
def disc(r, y, block, hole=True):
    out = []
    for z in range(CZ - math.ceil(r), CZ + math.ceil(r) + 1):
        dz = z - CZ + 0.5
        if abs(dz) > r:
            continue
        hw = math.sqrt(r * r - dz * dz)
        x1, x2 = math.floor(CX - hw + 0.5), math.floor(CX + hw - 0.5)
        if x1 <= x2:
            out.append(f'fill {x1} {y} {z} {x2} {y} {z} minecraft:{block}')
    return out


ISL = ['# ⛏ Île du Filon (générée par tools/arcade/gen_filon.py ; le monde des mini-jeux est vide à cet endroit)']
ISL += disc(R, YT, 'grass_block')
for y in (YT - 1, YT - 2, YT - 3):
    ISL += disc(R - 0.5, y, 'coarse_dirt')
for y in range(YT - 4, 58, -1):                        # dessous en cône
    t = (y - 56) / (YT - 4 - 56)
    ISL += disc(max(3.0, (R - 1) * t ** 0.7), y, 'packed_mud' if y % 7 else 'mossy_cobblestone')
# bord : barrière invisible sur le pourtour de l'herbe
cells = set()
for z in range(CZ - R - 1, CZ + R + 2):
    for x in range(CX - R - 1, CX + R + 2):
        if (x + 0.5 - CX) ** 2 + (z + 0.5 - CZ) ** 2 <= R * R:
            cells.add((x, z))
edge = [(x, z) for (x, z) in cells if any((x + a, z + b) not in cells for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)))]
ISL += [f'fill {x} {YT + 1} {z} {x} {YT + 3} {z} minecraft:barrier' for (x, z) in sorted(edge)]
# puits de la mine : murs indestructibles, fond en bedrock
ISL += [f'fill -1 {YB - 1} {Z0 - 1} 16 {YB - 1} {Z0 + 16} minecraft:bedrock',
        f'fill -1 {YB} {Z0 - 1} 16 {YT - 6} {Z0 - 1} minecraft:bedrock', f'fill -1 {YB} {Z0 + 16} 16 {YT - 6} {Z0 + 16} minecraft:bedrock',
        f'fill -1 {YB} {Z0} -1 {YT - 6} {Z0 + 15} minecraft:bedrock', f'fill 16 {YB} {Z0} 16 {YT - 6} {Z0 + 15} minecraft:bedrock',
        f'fill -1 {YT - 5} {Z0 - 1} 16 {YT} {Z0 - 1} minecraft:reinforced_deepslate', f'fill -1 {YT - 5} {Z0 + 16} 16 {YT} {Z0 + 16} minecraft:reinforced_deepslate',
        f'fill -1 {YT - 5} {Z0} -1 {YT} {Z0 + 15} minecraft:reinforced_deepslate', f'fill 16 {YT - 5} {Z0} 16 {YT} {Z0 + 15} minecraft:reinforced_deepslate']
# chemin autour du puits, place nord (comptoir, magasin, tableau), arche de sortie
ISL += [f'fill -3 {YT} {Z0 - 3} 18 {YT} {Z0 - 2} minecraft:dirt_path', f'fill -3 {YT} {Z0 + 17} 18 {YT} {Z0 + 18} minecraft:dirt_path',
        f'fill -3 {YT} {Z0 - 1} -2 {YT} {Z0 + 16} minecraft:dirt_path', f'fill 17 {YT} {Z0 - 1} 18 {YT} {Z0 + 16} minecraft:dirt_path',
        f'fill -2 {YT} {Z0 - 18} 18 {YT} {Z0 - 4} minecraft:polished_andesite', f'fill -1 {YT} {Z0 - 17} 17 {YT} {Z0 - 5} minecraft:smooth_stone',
        f'fill 7 {YT} {Z0 - 21} 9 {YT} {Z0 - 19} minecraft:dirt_path']
for (x1, sgn) in ((0, 1), (12, -1)):                      # échoppes : comptoir (ouest), magasin (est)
    ISL += [f'fill {x1} {YT + 1} {Z0 - 15} {x1 + 4} {YT + 1} {Z0 - 15} minecraft:spruce_planks',
            f'fill {x1} {YT + 2} {Z0 - 16} {x1 + 4} {YT + 4} {Z0 - 16} minecraft:stripped_spruce_wood',
            f'fill {x1} {YT + 1} {Z0 - 16} {x1 + 4} {YT + 1} {Z0 - 16} minecraft:stripped_spruce_wood',
            f'fill {x1} {YT + 2} {Z0 - 15} {x1} {YT + 4} {Z0 - 15} minecraft:spruce_fence', f'fill {x1 + 4} {YT + 2} {Z0 - 15} {x1 + 4} {YT + 4} {Z0 - 15} minecraft:spruce_fence',
            f'fill {x1} {YT + 5} {Z0 - 16} {x1 + 4} {YT + 5} {Z0 - 14} minecraft:spruce_slab[type=bottom]',
            f'setblock {x1 + 2} {YT + 4} {Z0 - 14} minecraft:lantern[hanging=true]']
# décor des échoppes sans interface ouvrable (baril verrouillé, pas d'enclume ni de table de forge utilisables en aventure)
ISL += [f'setblock 1 {YT + 2} {Z0 - 15} minecraft:barrel[facing=up]{{lock:{{items:"minecraft:barrier"}}}}', f'setblock 3 {YT + 2} {Z0 - 15} minecraft:gold_block',
        f'setblock 13 {YT + 2} {Z0 - 15} minecraft:lodestone', f'setblock 15 {YT + 2} {Z0 - 15} minecraft:cut_copper',
        f'fill 6 {YT + 1} {Z0 - 17} 10 {YT + 1} {Z0 - 17} minecraft:polished_andesite', f'fill 6 {YT + 2} {Z0 - 17} 10 {YT + 5} {Z0 - 17} minecraft:dark_oak_planks',
        f'fill 6 {YT + 6} {Z0 - 17} 10 {YT + 6} {Z0 - 17} minecraft:dark_oak_slab[type=bottom]',
        # arche de sortie (nord)
        f'fill 6 {YT + 1} {Z0 - 21} 6 {YT + 4} {Z0 - 21} minecraft:stripped_dark_oak_log', f'fill 10 {YT + 1} {Z0 - 21} 10 {YT + 4} {Z0 - 21} minecraft:stripped_dark_oak_log',
        f'fill 6 {YT + 5} {Z0 - 21} 10 {YT + 5} {Z0 - 21} minecraft:dark_oak_planks', f'setblock 8 {YT + 6} {Z0 - 21} minecraft:lantern',
        f'fill 7 {YT + 1} {Z0 - 21} 9 {YT + 4} {Z0 - 21} minecraft:purple_stained_glass']
for (x, z) in ((-3, Z0 - 3), (18, Z0 - 3), (-3, Z0 + 18), (18, Z0 + 18), (-2, Z0 - 18), (18, Z0 - 18)):
    ISL += [f'fill {x} {YT + 1} {z} {x} {YT + 3} {z} minecraft:dark_oak_fence', f'setblock {x} {YT + 4} {z} minecraft:lantern']
# arbres et buissons (hors place, hors puits, hors chemin)
spots = []
while len(spots) < 22:
    a, d = rnd.uniform(0, 2 * math.pi), rnd.uniform(14, R - 4)
    x, z = round(CX + d * math.cos(a)), round(CZ + d * math.sin(a))
    if -6 <= x <= 22 and Z0 - 23 <= z <= Z0 + 21:
        continue
    if all((x - a2) ** 2 + (z - b2) ** 2 >= 36 for a2, b2 in spots):
        spots.append((x, z))
for i, (x, z) in enumerate(spots):
    ISL.append(f'execute positioned {x} {YT + 1} {z} run place feature minecraft:{["oak", "birch", "oak", "spruce"][i % 4]}')
for _ in range(90):
    x, z = rnd.randint(CX - R + 3, CX + R - 3), rnd.randint(CZ - R + 3, CZ + R - 3)
    if (x - CX) ** 2 + (z - CZ) ** 2 < (R - 2) ** 2 and not (-4 <= x <= 20 and Z0 - 22 <= z <= Z0 + 19):
        ISL.append(f'execute if block {x} {YT + 1} {z} minecraft:air if block {x} {YT} {z} minecraft:grass_block run setblock {x} {YT + 1} {z} '
                   f'minecraft:{rnd.choice(["short_grass", "short_grass", "fern", "poppy", "dandelion", "cornflower", "azure_bluet"])}')
w(f'{P}/island', ISL)

# ---------------------------------------------------------------- entités de l'île (comptoir, magasin, marché, sortie, panneaux)
TR = 'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[%sf,%sf,%sf]}'


def tdisp(x, y, z, text, s=1.0, tag='', bg=True):
    return (f'summon minecraft:text_display {x} {y} {z} {{Tags:["mg.fne"{tag}],billboard:"center",line_width:260,'
            + ('' if bg else 'background:0,') + f'text:{js(text)},{TR % (s, s, s)}}}')


def inter(x, y, z, tag, wd=2.0, h=2.2):
    return f'summon minecraft:interaction {x} {y} {z} {{Tags:["mg.fne","mg.fni","{tag}"],width:{wd}f,height:{h}f,response:1b}}'


ENT = ['# Entités de l\'île du Filon (tag mg.fne) : retirées puis reposées', f'kill @e[tag=mg.fne,{AREA}]',
       inter(2.5, YT + 1, Z0 - 13.5, 'mg.fni_sell', 4.2, 2.6), inter(14.5, YT + 1, Z0 - 13.5, 'mg.fni_shop', 4.2, 2.6),
       inter(8.5, YT + 1, Z0 - 15.5, 'mg.fni_mkt', 5.2, 4.5), inter(8.5, YT + 1, Z0 - 20.5, 'mg.fni_exit', 3.2, 4),
       tdisp(2.5, YT + 4.1, Z0 - 13.5, [TXT('💰 COMPTOIR', 'gold', bold=True), TXT('\nclic droit : tout vendre au cours du moment', 'yellow')], 0.9),
       tdisp(14.5, YT + 4.1, Z0 - 13.5, [TXT('🛒 MAGASIN', 'aqua', bold=True), TXT('\npioches, enchantements, épées, armures…', 'yellow')], 0.9),
       tdisp(8.5, YT + 6.6, Z0 - 20.5, [TXT('⌂ Retour au lobby', 'green', bold=True), TXT('\nclic droit sur l\'arche', 'gray')], 0.9),
       f'summon minecraft:text_display 8.5 {YT + 2.0} {Z0 - 16.45} {{Tags:["mg.fne","mg.fnboard"],billboard:"fixed",line_width:220,'
       f'text:{js(TXT("📈 Cours du marché", "gold", bold=True))},{TR % (0.55, 0.55, 0.55)}}}',
       tdisp(8.5, YT + 9.5, Z0 - 8.5, [TXT('⛏ FILON', 'gold', bold=True), TXT('\nMine le chunk, vends, améliore-toi.\nLe chunk se régénère toutes les 45 min.', 'gray', bold=False)], 1.6, bg=False),
       tdisp(8.5, YT + 1.8, Z0 - 2.5, [TXT('⬇ La mine ⬇', 'yellow', bold=True), TXT('\nsaute dedans (pas de dégâts de chute)\n🪢 corde (case 9) pour remonter\n⚔ PvP dans la mine pendant les phases annoncées', 'gray', bold=False)], 0.7)]
w(f'{P}/ents', ENT)

# ---------------------------------------------------------------- régénération du chunk
ORES = [('ore_coal', 18, 60, 98), ('ore_copper_small', 10, 60, 98), ('ore_copper_large', 3, 60, 95), ('ore_iron', 16, 45, 98), ('ore_iron_small', 8, 40, 98),
        ('ore_gold', 8, 40, 75), ('ore_redstone', 8, 40, 62), ('ore_lapis', 6, 40, 70), ('ore_diamond_small', 5, 40, 55), ('ore_diamond_medium', 2, 40, 52),
        ('ore_emerald', 6, 70, 98), ('ore_andesite', 2, 50, 98), ('ore_diorite', 2, 50, 98), ('ore_granite', 2, 50, 98), ('ore_tuff', 2, 40, 69),
        ('ore_gravel', 3, 40, 98)]
EVENTS = [(1, 12, 'Une veine de diamants', [('ore_diamond_large', 4, 40, 60), ('ore_diamond_medium', 4, 40, 60)], []),
          (13, 22, 'De l\'or, beaucoup d\'or', [('ore_gold', 10, 40, 90)], [('raw_gold_block', 3, 40, 80)]),
          (23, 30, 'Une géode', [], []),
          (31, 36, 'Des coffres enfouis', [], []),
          (37, 41, 'Des débris antiques', [], [('ancient_debris', 4, 40, 60)])]
RG = ['# ⛏ Régénération du chunk de mine (les joueurs dedans remontent d\'abord)',
      f'execute as @a[tag=mg.fnw,{PIT}] run function mg:{P}/to_surface',
      f'kill @e[type=minecraft:item,x=0,y={YB - 1},z={Z0},dx=15,dy={YT - YB + 2},dz=15]',
      f'kill @e[type=minecraft:tnt,x=-2,y={YB - 2},z={Z0 - 2},dx=19,dy={YT - YB + 6},dz=19]']
RG += [f'fill 0 {y} {Z0} 15 {y} {Z0 + 15} minecraft:{"stone" if y >= 70 else "deepslate"}' for y in range(YT, YB - 1, -1)]
# richesse du filon tirée au sort (50 à 150 % des filons de base, secret) : chaque filon a $fnrich % de chances d'être posé,
# et ($fnrich − 100) % d'être posé une 2e fois
RG += ['execute store result score $fnrich mg.st run random value 50..150']
for f, n, y1, y2 in ORES:
    for lo in (1, 101):
        RG += ['execute store result score #fr mg.st run random value %d..%d' % (lo, lo + 99),
               f'execute if score #fr mg.st <= $fnrich mg.st run function mg:{P}/rpf {{f:"{f}",y1:{y1},y2:{y2}}}'] * n
RG += ['# jackpots ordinaires : bloc d\'or brut (30 %), débris antique (25 %), coffre enfoui (40 %), bloc de fer brut (35 %)',
       'execute store result score #fr mg.st run random value 1..100',
       f'execute if score #fr mg.st matches ..30 run function mg:{P}/rset {{b:"raw_gold_block",y1:40,y2:85}}',
       'execute store result score #fr mg.st run random value 1..100',
       f'execute if score #fr mg.st matches ..25 run function mg:{P}/rset {{b:"ancient_debris",y1:40,y2:60}}',
       'execute store result score #fr mg.st run random value 1..100',
       f'execute if score #fr mg.st matches ..35 run function mg:{P}/rset {{b:"raw_iron_block",y1:50,y2:95}}',
       'execute store result score #fr mg.st run random value 1..100',
       f'execute if score #fr mg.st matches ..40 run function mg:{P}/chest',
       '# régénération exceptionnelle (≈ 4 fois sur 10) : rumeur annoncée, contenu gardé secret',
       'execute store result score $fnev mg.st run random value 1..100']
for a, b, _, ores, blocks in EVENTS:
    for f, n, y1, y2 in ores:
        RG += [f'execute if score $fnev mg.st matches {a}..{b} run function mg:{P}/rpf {{f:"{f}",y1:{y1},y2:{y2}}}'] * n
    for bl, n, y1, y2 in blocks:
        RG += [f'execute if score $fnev mg.st matches {a}..{b} run function mg:{P}/rset {{b:"{bl}",y1:{y1},y2:{y2}}}'] * n
RG += [f'execute if score $fnev mg.st matches 23..30 run function mg:{P}/geode',
       f'execute if score $fnev mg.st matches 31..36 run function mg:{P}/chest', f'execute if score $fnev mg.st matches 31..36 run function mg:{P}/chest',
       f'execute if score $fnev mg.st matches 31..36 run function mg:{P}/chest',
       'execute store result score #fr mg.st run random value 1..100', f'execute if score #fr mg.st matches ..15 run function mg:{P}/geode',
       '# cycle : PvP 3 min tout de suite, une autre phase au hasard entre 15 et 35 min, compteur de saison',
       'scoreboard players set $fnt mg.st 0', 'scoreboard players set $fnpend mg.st 0', 'scoreboard players set $fnrp mg.st 1',
       'execute store result score $fnpr mg.st run random value 900..2100', 'scoreboard players add $fnsc mg.st 1',
       f'execute if score $fnsc mg.st matches {SEASON_N}.. run schedule function mg:{P}/season_end 5s',
       'title @a[tag=mg.fnw] title {"text":"⛏ Filon régénéré !","color":"gold","bold":true}',
       'title @a[tag=mg.fnw] subtitle {"text":"⚔ PvP dans la mine pendant 3 min","color":"red"}',
       'execute if score $fnev mg.st matches ..41 run tellraw @a[tag=mg.fnw] {"text":"✨ Rumeur : ce filon cache quelque chose d\'exceptionnel…","color":"light_purple","italic":true}',
       'execute as @a[tag=mg.fnw] at @s run playsound minecraft:block.anvil.land master @s ~ ~ ~ 0.6 0.6',
       f'function mg:{P}/pvp_check']
w(f'{P}/regen', RG)
w(f'{P}/rpf', ['# Macro {f, y1, y2} : un filon (place feature) à une position au hasard du chunk',
               '$execute store result storage mg:filon p.y int 1 run random value $(y1)..$(y2)',
               'execute store result storage mg:filon p.x int 1 run random value 1..14',
               f'execute store result storage mg:filon p.z int 1 run random value {Z0 + 1}..{Z0 + 14}',
               '$data modify storage mg:filon p.f set value "$(f)"', f'function mg:{P}/pf with storage mg:filon p'])
w(f'{P}/pf', ['$execute positioned $(x) $(y) $(z) run place feature minecraft:$(f)'])
w(f'{P}/rset', ['# Macro {b, y1, y2} : un bloc jackpot (2 à 4 collés) à une position au hasard du chunk',
                '$execute store result storage mg:filon p.y int 1 run random value $(y1)..$(y2)',
                'execute store result storage mg:filon p.x int 1 run random value 1..13',
                f'execute store result storage mg:filon p.z int 1 run random value {Z0 + 1}..{Z0 + 13}',
                '$data modify storage mg:filon p.f set value "$(b)"', f'function mg:{P}/set with storage mg:filon p'])
w(f'{P}/set', ['$setblock $(x) $(y) $(z) minecraft:$(f)', 'execute store result score #fr mg.st run random value 0..2',
               '$execute if score #fr mg.st matches 1.. positioned $(x) $(y) $(z) run setblock ~1 ~ ~ minecraft:$(f)',
               '$execute if score #fr mg.st matches 2.. positioned $(x) $(y) $(z) run setblock ~ ~1 ~ minecraft:$(f)'])
w(f'{P}/chest', ['# Coffre enfoui (butin au hasard : loot table mg:filon/treasure)',
                 'execute store result storage mg:filon p.y int 1 run random value 41..90',
                 'execute store result storage mg:filon p.x int 1 run random value 1..14',
                 f'execute store result storage mg:filon p.z int 1 run random value {Z0 + 1}..{Z0 + 14}',
                 f'function mg:{P}/chest_at with storage mg:filon p'])
w(f'{P}/chest_at', ['$setblock $(x) $(y) $(z) minecraft:chest{LootTable:"mg:filon/treasure"}'])
w(f'{P}/geode', ['# Géode d\'améthyste au milieu du chunk (assez loin des murs pour être posée)',
                 'execute store result storage mg:filon p.y int 1 run random value 48..82',
                 'execute store result storage mg:filon p.x int 1 run random value 6..9',
                 f'execute store result storage mg:filon p.z int 1 run random value {Z0 + 6}..{Z0 + 9}',
                 'data modify storage mg:filon p.f set value "amethyst_geode"', f'function mg:{P}/pf with storage mg:filon p'])
os.makedirs(os.path.join(C.D, 'loot_table', 'filon'), exist_ok=True)
with open(os.path.join(C.D, 'loot_table', 'filon', 'treasure.json'), 'w', encoding='utf-8', newline='\n') as f:
    E = lambda name, wgt, lo, hi, extra=None: dict(type='minecraft:item', name=name, weight=wgt,
                                                   functions=[dict(function='minecraft:set_count', count=dict(type='minecraft:uniform', min=lo, max=hi))] + (extra or []))
    json.dump({'type': 'minecraft:chest', 'pools': [
        {'rolls': 1, 'entries': [
            E('minecraft:gold_nugget', 3, 1, 2, [dict(function='minecraft:set_components', components={
                'minecraft:custom_data': {'fn_lucky': True}, 'minecraft:item_name': {'text': '🍀 Pépite de chance', 'color': 'gold'},
                'minecraft:enchantment_glint_override': True})]),
            E('minecraft:diamond', 5, 3, 7), E('minecraft:emerald', 4, 4, 8), E('minecraft:raw_gold', 6, 8, 16),
            E('minecraft:enchanted_golden_apple', 1, 1, 1), E('minecraft:ancient_debris', 2, 1, 2)]},
        {'rolls': {'type': 'minecraft:uniform', 'min': 1, 'max': 3}, 'entries': [
            E('minecraft:raw_iron', 4, 4, 12), E('minecraft:coal', 4, 8, 20), E('minecraft:lapis_lazuli', 3, 6, 14), E('minecraft:redstone', 3, 8, 18),
            E('minecraft:cooked_beef', 2, 4, 8)]}]}, f, ensure_ascii=False, indent=2)
    f.write('\n')
