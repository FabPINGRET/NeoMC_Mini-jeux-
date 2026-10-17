"""🎩 Chapeaux cosmétiques : choisis dans une galerie souterraine sous le Hall, portés en permanence (lobby et parties).

    python tools/cosmetics/gen_hats.py .      (après tools/lobby/gen_themes.py : ancre `lobby/theme/tick` de core/tick)

- Le chapeau choisi (score mg.hat, 0 = aucun) est remis sur la tête dès qu'elle est vide ; s'il traîne ailleurs dans l'inventaire
  (curseur, main secondaire, sac), il est retiré. Un casque de jeu occupe la tête : le chapeau suit alors la tête (item_display
  téléporté chaque tick, relié au joueur par mg.hid).
- Pas de chapeau pour les invisibles (cache-cache, caméléons…), les spectateurs, la survie, ni sans le resource pack ($rp 0).
- Raretés : communs libres ; rares, épiques, légendaires selon les victoires (mg.wins) ; chapeaux de saison seulement pendant
  le décor Halloween ($theme 1) ou Noël ($theme 2), rangés automatiquement à la fin de la saison.
- Galerie : marche sur le présentoir devant le Hall (-20 64 8) pour descendre ; clic sur un piédestal = porter ce chapeau.
  Pas de bouton dans le menu : la galerie est le seul moyen de choisir.
Modèles : tools/resourcepack/hats_rp.py (mêmes données : hats_data.py).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arcade'))
import common as C
from hats_data import HATS, RARITY, SEASON

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
HAT = '*[minecraft:custom_data~{mg_hat:1b}]'
X0, X1, Y0, Y1, Z0, Z1 = -34, -16, 45, 51, 8, 26     # intérieur de la galerie (sol y 44, plafond y 52), dans la roche sous le Hall
ENTRY = (-20, 64, 8)                                  # présentoir d'entrée (devant le Hall, zone déjà dégagée des arbres)
LAND_IN, LAND_OUT = '-24.5 45 24.5 180 0', '-19.5 64 5.5 180 0'
EXIT = (-26, 45, 26)                                  # dalle de sortie (3 blocs, contre le mur sud)
PED = {'commun': 'smooth_quartz', 'rare': 'prismarine_bricks', 'epique': 'purpur_block', 'legendaire': 'gold_block',
       'halloween': 'carved_pumpkin[facing=south]', 'noel': 'packed_ice'}
ICON = {'halloween': '🎃', 'noel': '🎄'}
assert [h[0] for h in HATS] == list(range(1, len(HATS) + 1))


def rng(rar):
    ns = [h[0] for h in HATS if h[3] == rar]
    assert ns == list(range(ns[0], ns[-1] + 1)), rar      # numéros contigus par rareté
    return f'{ns[0]}..{ns[-1]}'


def item(key, name, rar):
    """Objet porté : modèle mg:hat/<key>, s'équipe sur la tête, aucun autre usage (motif de bannière retiré)."""
    lab, col, _ = RARITY[rar]
    return ('minecraft:flower_banner_pattern[!minecraft:provides_banner_patterns,'
            f'minecraft:item_model="mg:hat/{key}",minecraft:equippable={{slot:"head",equip_sound:"minecraft:item.armor.equip_leather"}},'
            f'minecraft:custom_data={{mg_hat:1b}},minecraft:item_name={js({"text": "🎩 " + name, "color": col})},'
            f'minecraft:lore=[{js({"text": f"Chapeau {lab.lower()} · galerie sous le Hall", "color": "gray", "italic": False})}]]')


def disp_item(key):
    return f'{{id:"minecraft:flower_banner_pattern",count:1,components:{{"minecraft:item_model":"mg:hat/{key}"}}}}'


NL = chr(10)
TF = 'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[%sf,%sf,%sf]}'

# ------------------------------------------------------------------ porter le chapeau
w('hat/tick', ['# 🎩 Chapeaux (généré par tools/cosmetics/gen_hats.py) : chapeau choisi toujours sur la tête, galerie sous le Hall',
               'execute if score $rp mg.st matches 1 as @a[scores={mg.hat=1..}] at @s run function mg:hat/guard',
               'scoreboard players add $hatt mg.st 1',
               'execute if score $hatt mg.st matches 20.. run function mg:hat/second',
               f'execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,gamemode=adventure,x={ENTRY[0]},y={ENTRY[1]},'
               f'z={ENTRY[2]},dx=0.99,dy=1.5,dz=0.99] run function mg:hat/enter',
               f'execute as @a[x={EXIT[0]},y={EXIT[1]},z={EXIT[2]},dx=2.99,dy=1.5,dz=0.99] run function mg:hat/leave',
               f'execute if entity @a[x={X0},y={Y0},z={Z0},dx={X1 - X0},dy={Y1 - Y0},dz={Z1 - Z0}] run function mg:hat/gallery_tick'])
w('hat/guard', ['# @s : joueur avec un chapeau choisi, à sa position (chaque tick)',
                'execute if entity @s[tag=mg.surv] run return run function mg:hat/strip',
                'execute if entity @s[gamemode=spectator] run return run function mg:hat/strip',
                'execute if predicate mg:invisible run return run function mg:hat/strip',
                f'execute if items entity @s container.* {HAT} run clear @s {HAT}',
                f'execute if items entity @s player.crafting.* {HAT} run clear @s {HAT}',
                f'execute if items entity @s weapon.offhand {HAT} run item replace entity @s weapon.offhand with minecraft:air',
                f'execute if items entity @s player.cursor {HAT} run item replace entity @s player.cursor with minecraft:air',
                'execute unless items entity @s armor.head * run function mg:hat/wear',
                f'execute if entity @s[tag=mg.hatd] if items entity @s armor.head {HAT} run function mg:hat/unfollow',
                f'execute if items entity @s armor.head {HAT} run return 0',
                '# casque de jeu sur la tête : le chapeau suit la tête',
                'function mg:hat/follow'])
w('hat/strip', ['# @s : chapeau retiré (invisible, spectateur, survie) ; remis par mg:hat/guard dès que possible',
                f'clear @s {HAT}',
                'execute if entity @s[tag=mg.hatd] run function mg:hat/unfollow'])
w('hat/wear', ['# @s : tête vide → chapeau choisi'] +
  [f'execute if score @s mg.hat matches {n} run return run item replace entity @s armor.head with {item(k, nm, r)}' for n, k, nm, r, _ in HATS] +
  ['scoreboard players set @s mg.hat 0'])
w('hat/follow', ['# @s : joueur coiffé d\'un casque de jeu → présentoir (item_display) collé à sa tête, tourné comme lui',
                 'execute unless score @s mg.hid matches 1.. run scoreboard players add $hid_n mg.st 1',
                 'execute unless score @s mg.hid matches 1.. run scoreboard players operation @s mg.hid = $hid_n mg.st',
                 'scoreboard players operation $hid mg.st = @s mg.hid',
                 'scoreboard players operation $hhn mg.st = @s mg.hat',
                 'execute as @e[type=minecraft:item_display,tag=mg.hatf] if score @s mg.hid = $hid mg.st run tag @s add mg.hatt',
                 'execute as @e[type=minecraft:item_display,tag=mg.hatt] unless score @s mg.hat = $hhn mg.st run kill @s',
                 'execute unless entity @e[type=minecraft:item_display,tag=mg.hatt,limit=1] run function mg:hat/follow_new',
                 'execute anchored eyes positioned ^ ^ ^ run tp @e[type=minecraft:item_display,tag=mg.hatt,limit=1] ~ ~ ~ ~ ~',
                 'tag @e[type=minecraft:item_display,tag=mg.hatt] remove mg.hatt',
                 'tag @s add mg.hatd'])
w('hat/follow_new', ['# @s : joueur ; nouveau présentoir (centre du modèle = centre de la tête, taille du rendu « tête » : 0,625)'] +
  [f'execute if score @s mg.hat matches {n} run summon minecraft:item_display ~ ~1.6 ~ {{Tags:["mg.hat","mg.hatf","mg.hatt"],'
   f'item_display:"head",teleport_duration:1,{TF % ((0.625,) * 3)},item:{disp_item(k)}}}' for n, k, _, _, _ in HATS] +
  ['scoreboard players operation @e[type=minecraft:item_display,tag=mg.hatt] mg.hid = @s mg.hid',
   'scoreboard players operation @e[type=minecraft:item_display,tag=mg.hatt] mg.hat = @s mg.hat'])
w('hat/unfollow', ['# @s : joueur ; son présentoir est retiré',
                   'scoreboard players operation $hid mg.st = @s mg.hid',
                   'execute as @e[type=minecraft:item_display,tag=mg.hatf] if score @s mg.hid = $hid mg.st run kill @s',
                   'tag @s remove mg.hatd'])
w('hat/second', ['# Chaque seconde : sans resource pack, hors saison, objets perdus, présentoirs orphelins',
                 'scoreboard players set $hatt mg.st 0',
                 f'execute unless score $rp mg.st matches 1 run clear @a {HAT}',
                 'execute unless score $rp mg.st matches 1 run kill @e[type=minecraft:item_display,tag=mg.hatf]',
                 'execute unless score $rp mg.st matches 1 run tag @a remove mg.hatd',
                 '# galerie absente ou recouverte (construction du spawn par étapes, monde déjà installé) : reconstruite',
                 f'execute if score $setup mg.st matches 1 if data storage mg:lobby v6 unless block {X0} {Y0 - 1} {Z0} minecraft:polished_deepslate '
                 'run function mg:hat/build',
                 f'execute if score $setup mg.st matches 1 if data storage mg:lobby v6 unless block {X0 + 1} {Y0 + 3} {Z0 + 1} minecraft:air '
                 'run function mg:hat/build',
                 f'execute as @a unless score @s mg.hat matches 1.. run clear @s {HAT}'] +
  [f'execute unless score $theme mg.st matches {t} as @a[scores={{mg.hat={rng(r)}}}] run function mg:hat/off_season' for r, t in SEASON.items()] +
  [f'execute as @e[type=minecraft:item] if items entity @s contents {HAT} run kill @s',
   'tag @e[type=minecraft:item_display,tag=mg.hatf] add mg.hato',
   'execute as @a[tag=mg.hatd] run function mg:hat/keep',
   'kill @e[type=minecraft:item_display,tag=mg.hato]'])
w('hat/keep', ['# @s : joueur avec un présentoir ; le sien n\'est pas orphelin',
               'scoreboard players operation $hid mg.st = @s mg.hid',
               'execute as @e[type=minecraft:item_display,tag=mg.hato] if score @s mg.hid = $hid mg.st run tag @s remove mg.hato'])
w('hat/off_season', ['# @s : chapeau de saison, la saison est finie',
                     'scoreboard players set @s mg.hat 0',
                     'function mg:hat/strip',
                     'tellraw @s ' + js([{'text': '🎩 ', 'color': 'gold'}, {'text': 'La saison est finie : ton chapeau de saison est rangé jusqu\'à l\'an prochain.', 'color': 'gray'}])])

# ------------------------------------------------------------------ galerie : choix
LOCK = []
for r in ('rare', 'epique', 'legendaire'):
    lab, col, need = RARITY[r]
    LOCK.append(f'execute if score $hn mg.st matches {rng(r)} unless score @s mg.wins matches {need}.. run return run tellraw @s ' + js([
        {'text': '🔒 ', 'color': 'red'}, {'text': f'Chapeau {lab.lower()}', 'color': col}, {'text': f' : {need} victoires requises (tu en as ', 'color': 'gray'},
        {'score': {'name': '@s', 'objective': 'mg.wins'}, 'color': 'gold'}, {'text': ').', 'color': 'gray'}]))
for r, t in SEASON.items():
    lab, col, _ = RARITY[r]
    LOCK.append(f'execute if score $hn mg.st matches {rng(r)} unless score $theme mg.st matches {t} run return run tellraw @s ' + js([
        {'text': '🔒 ', 'color': 'red'}, {'text': f'{ICON[r]} Chapeau de {lab}', 'color': col}, {'text': ' : seulement pendant la saison.', 'color': 'gray'}]))
w('hat/gallery_tick', ['# Quelqu\'un est dans la galerie : clics sur les piédestaux',
                       'execute as @e[type=minecraft:interaction,tag=mg.hati] if data entity @s interaction run function mg:hat/click',
                       'execute as @e[type=minecraft:interaction,tag=mg.hati] if data entity @s attack run function mg:hat/click'])
w('hat/click', ['# @s : piédestal cliqué (mg.st = n° du chapeau, 0 = sans chapeau)',
                'scoreboard players operation $hn mg.st = @s mg.st',
                'execute if data entity @s interaction on target run function mg:hat/pick',
                'execute if data entity @s attack on attacker run function mg:hat/pick',
                'data remove entity @s interaction',
                'data remove entity @s attack'])
w('hat/pick', ['# @s : joueur ; $hn = chapeau choisi',
               'execute unless score $rp mg.st matches 1 run return run tellraw @s ' + js({'text': 'Les chapeaux demandent le resource pack NeoMC.', 'color': 'red'}),
               'execute if score $hn mg.st matches 0 run return run function mg:hat/remove'] + LOCK +
  ['execute if score $hn mg.st = @s mg.hat run return run tellraw @s ' + js({'text': 'Tu portes déjà ce chapeau.', 'color': 'gray'}),
   'scoreboard players operation @s mg.hat = $hn mg.st',
   'function mg:hat/strip',
   'function mg:hat/wear_now',
   'playsound minecraft:item.armor.equip_leather master @s ~ ~ ~ 1 1.2',
   'particle minecraft:happy_villager ~ ~2.1 ~ 0.3 0.2 0.3 0 10'] +
  [f'execute if score $hn mg.st matches {n} run tellraw @s ' + js([{'text': '🎩 Tu portes maintenant : ', 'color': 'gray'}, {'text': nm, 'color': RARITY[r][1], 'bold': True}])
   for n, _, nm, r, _ in HATS])
w('hat/wear_now', ['# @s : chapeau posé tout de suite si la tête est libre (sinon : présentoir au prochain tick)',
                   'execute unless items entity @s armor.head * run function mg:hat/wear'])
w('hat/remove', ['# @s : sans chapeau',
                 'scoreboard players set @s mg.hat 0',
                 'function mg:hat/strip',
                 'playsound minecraft:item.armor.equip_generic master @s ~ ~ ~ 1 0.8',
                 'tellraw @s ' + js({'text': '🎩 Chapeau rangé.', 'color': 'gray'})])
w('hat/enter', ['# @s : descend dans la galerie',
                f'tp @s {LAND_IN}',
                'playsound minecraft:block.beacon.activate master @s ~ ~ ~ 0.6 1.6',
                'tellraw @s ' + js([{'text': '🎩 Galerie des chapeaux', 'color': 'gold', 'bold': True},
                                    {'text': ' : clique sur un piédestal pour porter son chapeau, partout et pendant les parties. ✦ Victoires : ', 'color': 'gray'},
                                    {'score': {'name': '@s', 'objective': 'mg.wins'}, 'color': 'gold'}])])
w('hat/leave', ['# @s : remonte devant le Hall',
                f'tp @s {LAND_OUT}',
                'playsound minecraft:block.beacon.deactivate master @s ~ ~ ~ 0.6 1.6'])

# ------------------------------------------------------------------ galerie : construction
SLOTS = [(0, None, 'Sans chapeau', None)] + [(n, k, nm, r) for n, k, nm, r, _ in HATS]
COLS = list(range(X0 + 2, X1 - 1, 2))                 # 8 colonnes
ROWS = list(range(Z1 - 4, Z0, -3))                    # de l'entrée (sud) vers le fond
assert len(COLS) * len(ROWS) >= len(SLOTS), (len(COLS), len(ROWS))
B = ['# 🎩 Galerie des chapeaux sous le Hall (généré par tools/cosmetics/gen_hats.py) ; relancée par rp_on / rp_off, reconstruite par hat/second si absente',
     'kill @e[tag=mg.hatg]',
     f'fill {X0 - 1} {Y0 - 1} {Z0 - 1} {X1 + 1} {Y1 + 1} {Z1 + 1} minecraft:deepslate_tiles hollow',
     f'fill {X0} {Y0 - 1} {Z0} {X1} {Y0 - 1} {Z1} minecraft:polished_deepslate',
     f'fill {X0} {Y1 + 1} {Z0} {X1} {Y1 + 1} {Z1} minecraft:dark_oak_planks',
     f'fill {X0 - 1} {Y0} {Z0 - 1} {X1 + 1} {Y0} {Z1 + 1} minecraft:polished_blackstone_bricks replace minecraft:deepslate_tiles',
     f'fill {X0 - 1} {Y1} {Z0 - 1} {X1 + 1} {Y1} {Z1 + 1} minecraft:chiseled_deepslate replace minecraft:deepslate_tiles']
B += [f'setblock {x} {Y1 + 1} {z} minecraft:ochre_froglight' for x in range(X0 + 1, X1, 4) for z in range(Z0 + 1, Z1, 4)]
B += [f'fill {x} {Y0 - 1} {Z0} {x} {Y0 - 1} {Z1} minecraft:red_terracotta' for x in (X0 + 1, X1 - 1)]
B += [f'fill {EXIT[0]} {Y0 - 1} {EXIT[2]} {EXIT[0] + 2} {Y0 - 1} {EXIT[2]} minecraft:emerald_block',
      f'summon minecraft:text_display {EXIT[0] + 1.5} {Y0 + 2.3} {EXIT[2] + 0.3} {{Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,'
      f'text:{js([{"text": "⬆ Retour au spawn", "color": "green", "bold": True}, {"text": NL + "marche sur les blocs d" + chr(39) + "émeraude", "color": "gray"}])}}}',
      f'summon minecraft:text_display {(X0 + X1 + 1) / 2} {Y1 - 0.4} {Z1 - 1.5} {{Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,'
      f'text:{js([{"text": "🎩 Galerie des chapeaux", "color": "gold", "bold": True}, {"text": NL + "clique sur un piédestal · les victoires débloquent les plus rares", "color": "gray"}])},'
      f'{TF % ((1.2,) * 3)}}}']
for i, (n, k, nm, r) in enumerate(SLOTS):
    row, col = divmod(i, len(COLS))
    left = len(SLOTS) - row * len(COLS)
    x = COLS[col + max(0, (len(COLS) - left) // 2)] if left < len(COLS) else COLS[col]
    z = ROWS[row]
    cx, cz = x + 0.5, z + 0.5
    B.append(f'setblock {x} {Y0} {z} minecraft:{PED[r] if r else "polished_blackstone"}')
    if r is None:
        sub = {'text': NL + 'retire ton chapeau', 'color': 'gray'}
    elif r in SEASON:
        sub = {'text': NL + f'{ICON[r]} {RARITY[r][0]} seulement', 'color': RARITY[r][1]}
    elif RARITY[r][2]:
        sub = {'text': NL + f'{RARITY[r][0]} · {RARITY[r][2]} victoires', 'color': RARITY[r][1]}
    else:
        sub = {'text': NL + RARITY[r][0], 'color': 'gray'}
    col_name = RARITY[r][1] if r else 'white'
    B.append(f'summon minecraft:text_display {cx} {Y0 + 3.15} {cz} {{Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,'
             f'text:{js([{"text": ("✖ " if r is None else "") + nm, "color": col_name, "bold": True}, sub])},{TF % ((0.5,) * 3)}}}')
    if k:
        B.append(f'execute if score $rp mg.st matches 1 run summon minecraft:armor_stand {cx} {Y0 + 1} {cz} {{Tags:["mg.hat","mg.hatg"],Invisible:1b,'
                 f'Marker:1b,NoGravity:1b,Invulnerable:1b,Rotation:[0f,0f],equipment:{{head:{disp_item(k)}}}}}')
    B.append(f'summon minecraft:interaction {cx} {Y0 + 1} {cz} {{Tags:["mg.hat","mg.hatg","mg.hati"],width:0.9f,height:2.2f,response:1b}}')
    B.append(f'scoreboard players set @e[type=minecraft:interaction,tag=mg.hati,x={cx},y={Y0 + 1},z={cz},distance=..0.1] mg.st {n}')
ex, ey, ez = ENTRY
B += [f'summon minecraft:text_display {ex + 0.5} {ey + 2.4} {ez + 0.5} {{Tags:["mg.hat","mg.hatg"],billboard:"center",background:0,'
      f'text:{js([{"text": "🎩 Galerie des chapeaux", "color": "gold", "bold": True}, {"text": NL + "marche ici pour descendre", "color": "gray"}])}}}',
      f'execute if score $rp mg.st matches 1 run summon minecraft:item_display {ex + 0.5} {ey + 1.3} {ez + 0.5} {{Tags:["mg.hat","mg.hatg","mg.lspin"],'
      f'billboard:"fixed",item_display:"head",item:{disp_item("top_hat")},{TF % ((1.4,) * 3)}}}']
w('hat/build', B)

# ------------------------------------------------------------------ câblage
os.makedirs(os.path.join(C.D, 'predicate'), exist_ok=True)
with open(os.path.join(C.D, 'predicate', 'invisible.json'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(js({'condition': 'minecraft:entity_properties', 'entity': 'this',
                'predicate': {'effects': {'minecraft:invisibility': {}}}}) + '\n')
C.objectives([('mg.hat', 'dummy'), ('mg.hid', 'dummy')])
C.patch('core/tick', 'execute if score $theme mg.st matches 1.. run function mg:lobby/theme/tick', ['function mg:hat/tick'])
C.patch('rp_on', 'function mg:lobby/armory_build', ['function mg:hat/build'])
C.patch('rp_off', 'function mg:lobby/armory_build', ['function mg:hat/build'])
C.patch('desinstaller', 'kill @e[tag=mg.lby]', ['kill @e[tag=mg.hat]', f'clear @a {HAT}'])
C.forceload([f'forceload add {X0 - 1} {Z0 - 1} {X1 + 1} {Z1 + 1}'])
print('Chapeaux OK :', len(HATS), 'chapeaux,', len(B), 'lignes de galerie')
