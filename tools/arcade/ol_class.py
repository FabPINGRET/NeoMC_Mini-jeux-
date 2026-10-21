"""⚔ Ombrelune : niveaux, caractéristiques, classes, mana, compétences, équipement par paliers (forge). Module importé par gen_ombrelune.py.

Scores (gardés d'une visite à l'autre) : mg.ollv niveau (1..35), mg.olxp XP, mg.olcl classe (0 aucune, 1 chevalier, 2 rôdeur, 3 mage, 4 clerc),
mg.ols1..4 Vigueur, Force, Agilité, Esprit (sans plafond), mg.olsp points à répartir, mg.olwt palier d'arme (1..9), mg.olat palier d'armure (0..9).
Pendant la visite : mg.olmp / mg.olmm mana (barre d'XP = mana), mg.olc1..4 recharges des compétences (ticks).
"""
from ol_core import w, wjson, js, P, TEXT, nm, lo, WF, dlg, show, bit_test, say

LV_MAX = 35
CLASSES = {
    1: ('chevalier', '⚔ Chevalier', 'gold', 'Robuste : +3 cœurs, +2 armure, bouclier. Ses compétences frappent au corps à corps (Force).'),
    2: ('rodeur', '🏹 Rôdeur', 'green', 'Agile : +12 % de vitesse, chutes amorties, arc puissant. Ses compétences visent de loin (Agilité).'),
    3: ('mage', '🔮 Mage', 'light_purple', 'Érudit : +40 mana, mana plus rapide, bâton de sorts. Ses sorts font de gros dégâts (Esprit).'),
    4: ('clerc', '✚ Clerc', 'yellow', 'Soigneur : +2 cœurs, +20 mana, soigne ses alliés et châtie les morts-vivants (Esprit).'),
}
# compétences : (classe, emplacement 1..4) -> (nom, coût en mana, recharge en ticks, niveau requis, description, modèle)
AB = {
    (1, 1): ('Frappe du bouclier', 12, 120, 1, 'Coup en cône devant toi, repousse', 'minecraft:shield'),
    (1, 2): ('Cri de guerre', 25, 400, 5, 'Force et résistance 8 s (alliés à 8 blocs), provoque les monstres', 'minecraft:goat_horn'),
    (1, 3): ('Tourbillon', 30, 200, 10, 'Frappe tout autour de toi (4,5 blocs)', 'minecraft:iron_axe'),
    (1, 4): ('Jugement de l\'Aube', 60, 900, 18, 'Ultime : déflagration dorée (7 blocs), ralentit', 'minecraft:nether_star'),
    (2, 1): ('Tir perçant', 10, 80, 1, 'Flèche magique qui traverse tous les ennemis (40 blocs)', 'minecraft:spectral_arrow'),
    (2, 2): ('Pluie de flèches', 30, 300, 5, 'Zone visée : 4 volées de flèches', 'minecraft:arrow'),
    (2, 3): ('Piège à loups', 20, 240, 10, 'Piège à tes pieds : immobilise et blesse (3 au plus)', 'minecraft:tripwire_hook'),
    (2, 4): ('Œil du faucon', 50, 800, 18, 'Ultime : ennemis à 30 blocs marqués (armure réduite), vitesse', 'minecraft:spyglass'),
    (3, 1): ('Boule de feu', 15, 60, 1, 'Projectile qui explose (3 blocs) et enflamme', 'minecraft:fire_charge'),
    (3, 2): ('Lance de givre', 15, 100, 5, 'Gèle la cible (lenteur III, 4 s)', 'minecraft:blue_ice'),
    (3, 3): ('Chaîne d\'éclairs', 30, 200, 10, 'Frappe les 4 ennemis les plus proches (12 blocs)', 'minecraft:lightning_rod'),
    (3, 4): ('Météore', 70, 900, 18, 'Ultime : un météore s\'écrase là où tu vises (6 blocs)', 'minecraft:magma_block'),
    (4, 1): ('Lumière guérisseuse', 18, 120, 1, 'Soigne les alliés à 8 blocs', 'minecraft:glow_berries'),
    (4, 2): ('Châtiment sacré', 15, 80, 5, 'Rayon de lumière (24 blocs), double contre les morts-vivants', 'minecraft:blaze_rod'),
    (4, 3): ('Bénédiction', 30, 500, 10, 'Absorption et résistance (alliés à 10 blocs)', 'minecraft:golden_apple'),
    (4, 4): ('Aube sacrée', 70, 1200, 18, 'Ultime : grand soin + lumière qui brûle les ennemis (10 blocs)', 'minecraft:beacon'),
}
STATS = [(1, 'mg.ols1', '❤ Vigueur', 'red', '+2 PV par point'), (2, 'mg.ols2', '⚔ Force', 'gold', '+0,5 dégât de mêlée, compétences du chevalier'),
         (3, 'mg.ols3', '💨 Agilité', 'green', '+1,5 % de vitesse, compétences du rôdeur'), (4, 'mg.ols4', '✦ Esprit', 'aqua', '+8 mana, puissance des sorts et soins')]

# ================================================================ constantes, XP, niveaux
w('consts', ['# Constantes (puissances de 2, diviseurs)'] + [f'scoreboard players set #p{i} mg.st {2 ** i}' for i in range(31)] +
  [f'scoreboard players set #{n} mg.st {n}' for n in (2, 3, 4, 5, 8, 10, 12, 20, 40, 50, 60, 100, 1000)] + ['scoreboard players set #m1 mg.st -1'])
w('xp', ['# @s gagne $(n) XP', '$scoreboard players add @s mg.olxp $(n)', '$tellraw @s {"text":"  +$(n) XP","color":"aqua"}', f'function mg:{P}/lvchk'])
w('lvchk', ['# @s : passage(s) de niveau (besoin = 100 + 50 × niveau)', f'execute if score @s mg.ollv matches {LV_MAX}.. run return run scoreboard players set @s mg.olxp 0',
            'scoreboard players operation $need mg.st = @s mg.ollv', 'scoreboard players operation $need mg.st *= #50 mg.st',
            'scoreboard players add $need mg.st 100', 'execute if score @s mg.olxp < $need mg.st run return 0',
            'scoreboard players operation @s mg.olxp -= $need mg.st', 'scoreboard players add @s mg.ollv 1', f'function mg:{P}/lvup', f'function mg:{P}/lvchk'])
w('lvup', ['# @s monte de niveau', 'title @s times 5 50 15',
           'title @s title [{"text":"⭐ NIVEAU ","color":"gold","bold":true},{"score":{"name":"@s","objective":"mg.ollv"},"color":"yellow","bold":true}]',
           'title @s subtitle {"text":"+1 point de caractéristique (journal, case 8)","color":"gray"}', 'scoreboard players add @s mg.olsp 1',
           'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2',
           'execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.4 0.8 0.4 0.4 40',
           'tellraw @a[tag=mg.olw] [{"text":"⭐ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" atteint le niveau ","color":"gray"},{"score":{"name":"@s","objective":"mg.ollv"},"color":"gold","bold":true}]',
           f'function mg:{P}/stats', 'function mg:core/heal', f'function mg:{P}/kit_ab',
           'execute if score @s mg.ollv matches 5 run tellraw @s {"text":"✨ Nouvelle compétence débloquée (case 4) !","color":"light_purple"}',
           'execute if score @s mg.ollv matches 10 run tellraw @s {"text":"✨ Nouvelle compétence débloquée (case 5) !","color":"light_purple"}',
           'execute if score @s mg.ollv matches 18 run tellraw @s {"text":"✨ Compétence ultime débloquée (case 6) !","color":"gold"}'])

# ================================================================ statistiques : PV, dégâts, vitesse, mana max
w('stats', ['# @s : bonus du niveau (+1 PV par niveau), des caractéristiques et de la classe',
            'attribute @s minecraft:max_health modifier remove mg:ollv',
            'execute store result storage mg:ombre st.lv int 1 run scoreboard players get @s mg.ollv',
            'execute store result storage mg:ombre st.v float 2 run scoreboard players get @s mg.ols1',
            'execute store result storage mg:ombre st.f float 0.5 run scoreboard players get @s mg.ols2',
            'execute store result storage mg:ombre st.a float 0.015 run scoreboard players get @s mg.ols3',
            f'function mg:{P}/stats_m with storage mg:ombre st', f'function mg:{P}/cl/passive', f'function mg:{P}/mana_max'])
w('stats_m', ['attribute @s minecraft:max_health modifier remove mg:olst', 'attribute @s minecraft:attack_damage modifier remove mg:olst',
              'attribute @s minecraft:movement_speed modifier remove mg:olst',
              '$attribute @s minecraft:max_health modifier add mg:ollv $(lv) add_value',
              '$attribute @s minecraft:max_health modifier add mg:olst $(v) add_value',
              '$attribute @s minecraft:attack_damage modifier add mg:olst $(f) add_value',
              '$attribute @s minecraft:movement_speed modifier add mg:olst $(a) add_multiplied_base'])
w('stats_rm', ['# @s quitte Ombrelune : bonus retirés'] + [f'attribute @s minecraft:{a} modifier remove mg:{m}' for a in
                                                        ('max_health', 'attack_damage', 'movement_speed', 'armor', 'knockback_resistance', 'safe_fall_distance')
                                                        for m in ('ollv', 'olst', 'olcl')])
w('mana_max', ['# @s : mana max = 50 + 4 × niveau + 8 × Esprit (+40 mage, +20 clerc)', 'scoreboard players operation @s mg.olmm = @s mg.ollv',
               'scoreboard players operation @s mg.olmm *= #4 mg.st', 'scoreboard players add @s mg.olmm 50',
               'scoreboard players operation $e mg.st = @s mg.ols4', 'scoreboard players operation $e mg.st *= #8 mg.st',
               'scoreboard players operation @s mg.olmm += $e mg.st', 'execute if score @s mg.olcl matches 3 run scoreboard players add @s mg.olmm 40',
               'execute if score @s mg.olcl matches 4 run scoreboard players add @s mg.olmm 20',
               'execute if score @s mg.olmp > @s mg.olmm run scoreboard players operation @s mg.olmp = @s mg.olmm'])
# mana : régénération (chaque seconde) + affichage dans la barre d'XP (niveau = mana, barre = mana / max)
w('mana_tick', ['# @s : +2 mana par seconde (+1 tous les 3 points d\'Esprit, +2 mage), barre d\'XP',
                'scoreboard players operation $e mg.st = @s mg.ols4', 'scoreboard players operation $e mg.st /= #3 mg.st', 'scoreboard players add $e mg.st 2',
                'execute if score @s mg.olcl matches 3 run scoreboard players add $e mg.st 2',
                'scoreboard players operation @s mg.olmp += $e mg.st',
                'execute if score @s mg.olmp > @s mg.olmm run scoreboard players operation @s mg.olmp = @s mg.olmm', f'function mg:{P}/mana_bar'])
MB = ['# @s : barre d\'XP = mana (niveau affiché = mana, remplissage = mana / max)',
      'execute store result storage mg:ombre mb.l int 1 run scoreboard players get @s mg.olmp',
      '# points du niveau L : 2L+7 (L ≤ 15), 5L-38 (L ≤ 30), 9L-158 au-delà',
      'scoreboard players operation $L mg.st = @s mg.olmp',
      'scoreboard players operation $need mg.st = $L mg.st', 'scoreboard players operation $need mg.st *= #2 mg.st', 'scoreboard players add $need mg.st 7',
      'execute if score $L mg.st matches 16..30 run scoreboard players operation $need mg.st = $L mg.st',
      'execute if score $L mg.st matches 16..30 run scoreboard players operation $need mg.st *= #5 mg.st',
      'execute if score $L mg.st matches 16..30 run scoreboard players remove $need mg.st 38',
      'execute if score $L mg.st matches 31.. run scoreboard players operation $need mg.st = $L mg.st',
      'execute if score $L mg.st matches 31.. run scoreboard players operation $t mg.st = #4 mg.st',
      'execute if score $L mg.st matches 31.. run scoreboard players operation $need mg.st *= #8 mg.st',
      'execute if score $L mg.st matches 31.. run scoreboard players operation $need mg.st += $L mg.st',
      'execute if score $L mg.st matches 31.. run scoreboard players remove $need mg.st 158',
      'scoreboard players operation $pt mg.st = @s mg.olmp', 'scoreboard players operation $pt mg.st *= $need mg.st',
      'scoreboard players operation $pt mg.st /= @s mg.olmm', 'scoreboard players remove $pt mg.st 1',
      'execute if score $pt mg.st matches ..-1 run scoreboard players set $pt mg.st 0',
      'execute store result storage mg:ombre mb.p int 1 run scoreboard players get $pt mg.st',
      f'function mg:{P}/mana_bar_m with storage mg:ombre mb']
w('mana_bar', MB)
w('mana_bar_m', ['xp set @s 0 points', '$xp set @s $(l) levels', '$xp set @s $(p) points'])
w('mana_use', ['# @s dépense $(m) mana (renvoie 0 s\'il n\'en a pas assez)', '$execute unless score @s mg.olmp matches $(m).. run return run function mg:ombre/cl/nomana',
               '$scoreboard players remove @s mg.olmp $(m)', f'function mg:{P}/mana_bar', 'return 1'])
w('cl/nomana', say('✦ Pas assez de mana', 'aqua') + ['playsound minecraft:block.amethyst_block.hit player @s ~ ~ ~ 0.8 0.6', 'return 0'])

# ================================================================ choix de la classe (maître d'armes Orren, guilde)
CL_D = dlg('🎖 Choisis ta voie', 'gold', 'Chaque classe a un talent permanent et quatre compétences (cases 3 à 6, clic droit), débloquées aux niveaux 1, 5, 10 et 18. '
           'Tu pourras en changer en revenant me voir.', [(CLASSES[n][1], CLASSES[n][2], CLASSES[n][3], 600 + n) for n in CLASSES])
w('cl/menu', ['# @s : choix de la classe'] + show(CL_D))
for n, (key, name, col, desc) in CLASSES.items():
    w(f'cl/pick_{n}', [f'# @s devient {name}', f'execute if score @s mg.olcl matches {n} run return run tellraw @s ' + js(TEXT('Tu suis déjà cette voie.', 'gray')),
                       f'scoreboard players set @s mg.olcl {n}'] + [f'scoreboard players set @s mg.olc{i} 0' for i in range(1, 5)] +
      [f'function mg:{P}/stats', f'function mg:{P}/kit', 'title @s times 5 50 15', f'title @s title {js(TEXT(name.upper(), col, bold=True))}',
       f'title @s subtitle {js(TEXT(desc.split(":")[0], "gray"))}', 'tellraw @s ' + js([TEXT('🎖 Classe : ', 'gold'), TEXT(name, col, bold=True), TEXT('. ' + desc, 'gray')]),
       'execute at @s run playsound minecraft:item.armor.equip_netherite player @s ~ ~ ~ 1 1',
       f'execute if score @s mg.olch matches 1 run function mg:{P}/q/adv'])
w('cl/passive', ['# @s : talents de la classe (modificateurs mg:olcl)'] + [f'attribute @s minecraft:{a} modifier remove mg:olcl' for a in
                                                                           ('max_health', 'armor', 'movement_speed', 'safe_fall_distance', 'knockback_resistance')] +
  ['execute if score @s mg.olcl matches 1 run attribute @s minecraft:max_health modifier add mg:olcl 6 add_value',
   'execute if score @s mg.olcl matches 1 run attribute @s minecraft:armor modifier add mg:olcl 2 add_value',
   'execute if score @s mg.olcl matches 1 run attribute @s minecraft:knockback_resistance modifier add mg:olcl 0.3 add_value',
   'execute if score @s mg.olcl matches 2 run attribute @s minecraft:movement_speed modifier add mg:olcl 0.12 add_multiplied_base',
   'execute if score @s mg.olcl matches 2 run attribute @s minecraft:safe_fall_distance modifier add mg:olcl 6 add_value',
   'execute if score @s mg.olcl matches 4 run attribute @s minecraft:max_health modifier add mg:olcl 4 add_value'])

# ================================================================ équipement par paliers
TIER = {1: ('rouillé', 'gray'), 2: ('d\'acier', 'white'), 3: ('sylvestre', 'green'), 4: ('de givre', 'aqua'), 5: ('des marais', 'dark_green'),
        6: ('solaire', 'yellow'), 7: ('draconique', 'red'), 8: ('runique', 'blue'), 9: ('de l\'Aube', 'gold')}
MAT_OF = {1: 'stone', 2: 'iron', 3: 'iron', 4: 'diamond', 5: 'diamond', 6: 'golden', 7: 'netherite', 8: 'netherite', 9: 'netherite'}


def fem(a):
    return 'rouillée' if a == 'rouillé' else a


def attr(dmg, spd):
    return (f'attribute_modifiers=[{{type:"minecraft:attack_damage",id:"mg:olw",amount:{dmg},operation:"add_value",slot:"mainhand"}},'
            f'{{type:"minecraft:attack_speed",id:"mg:olws",amount:{spd},operation:"add_value",slot:"mainhand"}}]')


def weapon(cl, t):
    nmt, col = TIER[t]
    glint = ',enchantment_glint_override=true' if t >= 7 else ''
    if cl == 1:
        return (f'minecraft:{MAT_OF[t]}_sword[custom_data={{olwp:1b}},unbreakable={{}}{glint},custom_name={nm("🗡 Épée " + fem(nmt), col)},'
                f'lore={lo(f"Palier {t} · Chevalier", "Dégâts " + str(5 + 2 * t))},{attr(4 + 2 * t, -2.4)}]')
    if cl == 2:
        pw = min(5, (t + 1) // 2) if t < 9 else 6
        return (f'minecraft:bow[custom_data={{olwp:1b}},unbreakable={{}}{glint},custom_name={nm("🏹 Arc " + nmt, col)},'
                f'lore={lo(f"Palier {t} · Rôdeur", "Puissance " + str(pw))},enchantments={{"minecraft:power":{pw},"minecraft:infinity":1,"minecraft:punch":{1 if t >= 4 else 0}}}]').replace(',"minecraft:punch":0', '')
    if cl == 3:
        return (f'{WF}[custom_data={{ol:30,olwp:1b}},item_model="minecraft:{"blaze_rod" if t < 5 else ("breeze_rod" if t < 9 else "end_rod")}",unbreakable={{}}{glint},'
                f'custom_name={nm("🔮 Bâton " + nmt, col)},lore={lo(f"Palier {t} · Mage", "Clic droit : trait magique (gratuit)", "Puissance des sorts +" + str(2 * t))},'
                f'use_cooldown={{seconds:0.6f,cooldown_group:"mg:olstaff"}}]')
    return (f'minecraft:mace[custom_data={{olwp:1b}},unbreakable={{}}{glint},custom_name={nm("🔨 Masse " + fem(nmt), col)},'
            f'lore={lo(f"Palier {t} · Clerc", "Dégâts " + str(4 + 2 * t))},{attr(3 + 2 * t, -2.8)}]')


def dagger(t):
    nmt, col = TIER[t]
    return (f'minecraft:{MAT_OF[t]}_sword[custom_data={{olwp:2b}},unbreakable={{}},custom_name={nm("🔪 Dague " + fem(nmt), col)},'
            f'lore={lo("Arme de mêlée de secours")},{attr(2 + t, -1.6)}]')


ARM_MAT = {0: 'leather', 1: 'leather', 2: 'chainmail', 3: 'iron', 4: 'iron', 5: 'diamond', 6: 'diamond', 7: 'netherite', 8: 'netherite', 9: 'netherite'}
ARM_NAME = {0: 'Tenue de voyage', 1: 'Cuir renforcé', 2: 'Cotte de mailles', 3: 'Armure d\'acier', 4: 'Armure de givre', 5: 'Armure de diamant',
            6: 'Armure solaire', 7: 'Armure d\'écailles', 8: 'Armure runique', 9: 'Armure de l\'Aube'}
ARM_TRIM = {4: ('diamond', 'coast'), 6: ('gold', 'dune'), 7: ('redstone', 'rib'), 8: ('lapis', 'ward'), 9: ('gold', 'silence')}
CL_COL = {0: 8606770, 1: 10511680, 2: 3887386, 3: 6697881, 4: 15132390}


def armor(t, cl):
    out = []
    m = ARM_MAT[t]
    nmt = ARM_NAME[t]
    prot = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 5}[t]
    for s, p in (('head', 'helmet'), ('chest', 'chestplate'), ('legs', 'leggings'), ('feet', 'boots')):
        extra = f',enchantments={{"minecraft:protection":{prot}}}' if prot else ''
        if m == 'leather':
            extra += f',dyed_color={CL_COL[cl]}'
        if t in ARM_TRIM:
            extra += f',trim={{material:"minecraft:{ARM_TRIM[t][0]}",pattern:"minecraft:{ARM_TRIM[t][1]}"}}'
        if t >= 9:
            extra += ',enchantment_glint_override=true'
        out.append((s, f'minecraft:{m}_{p}[unbreakable={{}},custom_data={{olarm:{t}b}},custom_name={nm("🛡 " + nmt, "gold" if t >= 9 else "gray")}{extra}]'))
    return out


JOURNAL = (f'{WF}[custom_data={{ol:6}},item_model="minecraft:writable_book",unbreakable={{}},custom_name={nm("📖 Journal de l\'aventurier", "gold")},'
           f'lore={lo("Clic droit : quête, personnage, caractéristiques,", "bestiaire, succès, matériaux")}]')
WHISTLE = (f'{WF}[custom_data={{ol:5}},item_model="minecraft:goat_horn",unbreakable={{}},custom_name={nm("🐴 Sifflet du destrier", "yellow")},'
           f'lore={lo("Clic droit : ton cheval accourt et tu le montes")},use_cooldown={{seconds:2f,cooldown_group:"mg:olhorse"}}]')
MANA_POT = f'minecraft:honey_bottle[custom_data={{olmana:1b}},item_model="minecraft:potion",custom_name={nm("✦ Potion de mana", "aqua")},lore={lo("Boire : +60 mana")}]'
HEAL_POT = f'minecraft:potion[potion_contents={{potion:"minecraft:strong_healing"}},custom_name={nm("✚ Potion de soin", "red")}]'


def ab_item(cl, s, locked=False):
    name, cost, cd, lv, desc, model = AB[(cl, s)]
    col = CLASSES[cl][2]
    if locked:
        return (f'minecraft:gray_dye[custom_data={{ollock:1b}},custom_name={nm("🔒 " + name, "dark_gray")},'
                f'lore={lo(f"Se débloque au niveau {lv}", desc)}]')
    return (f'{WF}[custom_data={{ol:{cl * 10 + s}}},item_model="{model}",unbreakable={{}},custom_name={nm(name, col)},'
            f'lore={lo(desc, f"Mana : {cost}   Recharge : {cd / 20:g} s")},use_cooldown={{seconds:{cd / 20:g}f,cooldown_group:"mg:olab{cl}{s}"}}]')


KIT = ['# @s : équipement (classe, paliers d\'arme et d\'armure, compétences, journal)',
       'clear @s *[custom_data~{olwp:1b}]', 'clear @s *[custom_data~{olwp:2b}]', 'clear @s minecraft:arrow', 'clear @s minecraft:shield',
       'clear @s *[custom_data~{ol:6}]', 'clear @s *[custom_data~{ol:5}]']
for cl in range(1, 5):
    for t in range(1, 10):
        KIT.append(f'execute if score @s mg.olcl matches {cl} if score @s mg.olwt matches {t}{".." if t == 9 else ""} run item replace entity @s hotbar.0 with {weapon(cl, t)}')
for t in range(1, 10):
    KIT.append(f'execute if score @s mg.olcl matches 2 if score @s mg.olwt matches {t}{".." if t == 9 else ""} run item replace entity @s hotbar.1 with {dagger(t)}')
KIT += ['execute if score @s mg.olcl matches 2 run item replace entity @s inventory.26 with minecraft:arrow',
        'execute if score @s mg.olcl matches 1 run item replace entity @s weapon.offhand with minecraft:shield[unbreakable={},custom_name={"text":"🛡 Écu de Havreclair","color":"gold","italic":false}]',
        f'execute if score @s mg.olcl matches 0 run item replace entity @s hotbar.0 with {dagger(1)}']
for cl in range(0, 5):
    for t in range(0, 10):
        KIT += [f'execute if score @s mg.olcl matches {cl} if score @s mg.olat matches {t}{".." if t == 9 else ""} run item replace entity @s armor.{s} with {i}'
                for s, i in armor(t, cl)]
KIT += [f'function mg:{P}/kit_ab', f'item replace entity @s hotbar.7 with {JOURNAL}',
        f'execute if score @s mg.olhorse matches 1.. run item replace entity @s hotbar.6 with {WHISTLE}']
w('kit', KIT)
KA = ['# @s : objets de compétences (cases 3 à 6) selon la classe et le niveau', 'clear @s *[custom_data~{ollock:1b}]']
for cl in range(1, 5):
    for s in range(1, 5):
        lv = AB[(cl, s)][3]
        KA.append(f'execute if score @s mg.olcl matches {cl} unless items entity @s hotbar.{s + 1} *[custom_data~{{ol:{cl * 10 + s}}}] if score @s mg.ollv matches {lv}.. '
                  f'run item replace entity @s hotbar.{s + 1} with {ab_item(cl, s)}')
        KA.append(f'execute if score @s mg.olcl matches {cl} unless score @s mg.ollv matches {lv}.. run item replace entity @s hotbar.{s + 1} with {ab_item(cl, s, True)}')
KA.append('execute if score @s mg.olcl matches 0 run item replace entity @s hotbar.2 with minecraft:paper[custom_name={"text":"Choisis ta classe à la guilde","color":"gray","italic":false}]')
w('kit_ab', KA)

# ================================================================ forge (paliers) : coûts
FORGE_W = {2: (120, 1, 6, 3), 3: (300, 2, 8, 6), 4: (600, 3, 10, 10), 5: (1000, 4, 12, 14), 6: (1600, 5, 14, 18), 7: (2500, 6, 16, 22), 8: (3800, 7, 18, 26)}
FORGE_A = {1: (80, 1, 4, 2), 2: (220, 1, 8, 5), 3: (450, 2, 10, 8), 4: (800, 3, 12, 11), 5: (1200, 4, 14, 15), 6: (1800, 5, 16, 19), 7: (2800, 6, 18, 23),
           8: (4200, 7, 20, 27)}

# ================================================================ compétences : clic droit
USE = ['# @s : clic droit avec un objet d\'Ombrelune',
       'execute if items entity @s weapon.mainhand *[custom_data~{ol:30}] run return run function mg:ombre/cl/bolt',
       'execute if items entity @s weapon.mainhand *[custom_data~{ol:5}] run return run function mg:ombre/horse',
       'execute if items entity @s weapon.mainhand *[custom_data~{ol:6}] run return run function mg:ombre/journal']
for (cl, s) in AB:
    USE.append(f'execute if items entity @s weapon.mainhand *[custom_data~{{ol:{cl * 10 + s}}}] run return run function mg:ombre/cl/try {{c:{cl},s:{s}}}')
w('use', USE)
w('cl/try', ['# @s : compétence $(c)/$(s) : recharge, mana, puis effet', '$execute if score @s mg.olc$(s) matches 1.. run return run function mg:ombre/cl/wait {s:$(s)}',
             '$function mg:ombre/cl/cost_$(c)$(s)'])
for (cl, s), (name, cost, cd, lv, desc, model) in AB.items():
    w(f'cl/cost_{cl}{s}', [f'# {name} : {cost} mana, recharge {cd} ticks', f'execute store result score $ok mg.st run function mg:{P}/mana_use {{m:{cost}}}',
                           'execute unless score $ok mg.st matches 1 run return 0', f'scoreboard players set @s mg.olc{s} {cd}',
                           f'function mg:{P}/cl/pow', f'function mg:{P}/cl/a{cl}{s}'])
w('cl/wait', ['$scoreboard players operation $s mg.st = @s mg.olc$(s)', 'scoreboard players add $s mg.st 19', 'scoreboard players operation $s mg.st /= #20 mg.st',
              'scoreboard players set @s mg.olal 20',
              'title @s actionbar [{"text":"⏳ Compétence prête dans ","color":"gray"},{"score":{"name":"$s","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gray"}]',
              'playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.4 1.6'])
w('cl/pow', ['# @s : puissance des compétences : $pf (Force + 2 × palier), $pa (Agilité + 2 × palier), $pw (Esprit + 2 × palier)',
             'scoreboard players operation $t2 mg.st = @s mg.olwt', 'scoreboard players operation $t2 mg.st *= #2 mg.st',
             'scoreboard players operation $pf mg.st = @s mg.ols2', 'scoreboard players operation $pf mg.st += $t2 mg.st',
             'scoreboard players operation $pa mg.st = @s mg.ols3', 'scoreboard players operation $pa mg.st += $t2 mg.st',
             'scoreboard players operation $pw mg.st = @s mg.ols4', 'scoreboard players operation $pw mg.st += $t2 mg.st', 'tag @s add mg.olcast'])


def dmg_set(base, var, mul=1, div=1):
    """Lignes : storage mg:ombre s.d = base + var × mul / div."""
    return [f'scoreboard players operation $d mg.st = {var} mg.st', f'scoreboard players operation $d mg.st *= #{mul} mg.st' if mul != 1 else '#',
            f'scoreboard players operation $d mg.st /= #{div} mg.st' if div != 1 else '#', f'scoreboard players add $d mg.st {base}',
            'execute store result storage mg:ombre s.d int 1 run scoreboard players get $d mg.st']


def dclean(L):
    return [l for l in L if l != '#']


# mg:spell : message « magic » mais hors du tag witch_resistant_to (les sorcières réduisent minecraft:magic à 15 %) ; armure ignorée et pas de recul comme magic
wjson('damage_type/spell.json', {'message_id': 'magic', 'exhaustion': 0.0, 'scaling': 'never'})
for _t in ('bypasses_armor', 'no_knockback'):
    wjson(f'../minecraft/tags/damage_type/{_t}.json', {'replace': False, 'values': [{'id': 'mg:spell', 'required': False}]})
w('cl/hit', ['# @s (monstre) : dégâts $(d) du lanceur (tag mg.olcast), chiffre flottant', '$damage @s $(d) mg:spell by @a[tag=mg.olcast,limit=1]',
             '$summon minecraft:text_display ~ ~2 ~ {Tags:["mg.ol","mg.oldmg"],billboard:"center",teleport_duration:10,text:{"text":"-$(d)","color":"gold","bold":true},background:0,shadow:1b,see_through:1b}',
             'scoreboard players set @e[tag=mg.oldmg,distance=..2.5,sort=nearest,limit=1] mg.olst 12'])
w('cl/hit2', ['# @s (mort-vivant) : dégâts doublés', 'execute store result storage mg:ombre s2.d int 2 run data get storage mg:ombre s.d',
             'function mg:ombre/cl/hit with storage mg:ombre s2'])
w('dmg_tick', ['# Chiffres de dégâts : montée puis disparition', 'scoreboard players remove @e[type=minecraft:text_display,tag=mg.oldmg] mg.olst 1',
               'execute as @e[type=minecraft:text_display,tag=mg.oldmg,scores={mg.olst=11}] at @s run tp @s ~ ~0.9 ~',
               'kill @e[type=minecraft:text_display,tag=mg.oldmg,scores={mg.olst=..0}]'])
w('cl/end', ['tag @a remove mg.olcast'])


def ray(name, step_fn_lines, length, part):
    """Rayon générique : avance de 0,5 bloc, s'arrête sur un bloc plein ; step_fn_lines = lignes exécutées à chaque pas (contexte position)."""
    w(f'cl/{name}', [f'# Rayon {name} : un pas de 0,5 bloc', part, 'scoreboard players add $olr mg.st 1'] + step_fn_lines +
      ['execute unless block ~ ~ ~ #mg:tv_pass run return run function mg:ombre/cl/' + name + '_end',
       f'execute if score $olr mg.st matches {length * 2}.. run return run function mg:{P}/cl/{name}_end',
       f'execute positioned ^ ^ ^0.5 run function mg:{P}/cl/{name}'])


# ---- Chevalier
w('cl/a11', ['# Frappe du bouclier : cône devant soi'] + dclean(dmg_set(6, '$pf')) +
  ['playsound minecraft:item.shield.block player @a ~ ~ ~ 1 0.7', 'execute anchored eyes positioned ^ ^ ^1.8 run particle minecraft:sweep_attack ~ ~-0.3 ~ 0.6 0.2 0.6 0 4',
   'execute positioned ^ ^ ^2 as @e[tag=mg.olm,distance=..2.6] at @s run function mg:ombre/cl/k_bash with storage mg:ombre s', f'function mg:{P}/cl/end'])
w('cl/k_bash', ['$function mg:ombre/cl/hit {d:$(d)}', 'effect give @s minecraft:slowness 2 2 true',
                'execute unless entity @s[tag=mg.olbig] facing entity @a[tag=mg.olcast,limit=1] feet rotated ~180 -20 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:ombre/vec {d:1.2}',
                'execute unless entity @s[tag=mg.olbig] run function mg:ombre/push'])
w('cl/a12', ['# Cri de guerre', 'playsound minecraft:event.raid.horn player @a ~ ~ ~ 1 1.3', 'particle minecraft:angry_villager ~ ~2 ~ 1.5 0.5 1.5 0 15',
             'effect give @a[tag=mg.olw,distance=..8] minecraft:strength 8 0', 'effect give @a[tag=mg.olw,distance=..8] minecraft:resistance 8 0',
             'execute as @e[tag=mg.olm,distance=..10] run damage @s 0.01 minecraft:generic by @a[tag=mg.olcast,limit=1]', f'function mg:{P}/cl/end'])
w('cl/a13', ['# Tourbillon'] + dclean(dmg_set(10, '$pf')) +
  ['playsound minecraft:entity.player.attack.sweep player @a ~ ~ ~ 1 0.6', 'particle minecraft:sweep_attack ~ ~1 ~ 2 0.3 2 0 16',
   'execute as @e[tag=mg.olm,distance=..4.5] at @s run function mg:ombre/cl/k_bash with storage mg:ombre s', f'function mg:{P}/cl/end'])
w('cl/a14', ['# Jugement de l\'Aube'] + dclean(dmg_set(24, '$pf', 2)) +
  ['playsound minecraft:item.trident.thunder player @a ~ ~ ~ 1 0.8', 'playsound minecraft:entity.generic.explode player @a ~ ~ ~ 1 1.2',
   'particle minecraft:flash{color:[1.0,0.85,0.3,1.0]} ~ ~1 ~ 0 0 0 0 1 force', 'particle minecraft:end_rod ~ ~0.5 ~ 4 0.3 4 0.1 120 force',
   'particle minecraft:totem_of_undying ~ ~1 ~ 2 1 2 0.3 60 force',
   'execute as @e[tag=mg.olm,distance=..7] at @s run function mg:ombre/cl/k_judg with storage mg:ombre s', f'function mg:{P}/cl/end'])
w('cl/k_judg', ['$function mg:ombre/cl/hit {d:$(d)}', 'effect give @s minecraft:slowness 4 3 true', 'effect give @s minecraft:levitation 1 3 true'])
# ---- Rôdeur
w('cl/a21', ['# Tir perçant'] + dclean(dmg_set(8, '$pa')) +
  ['playsound minecraft:entity.arrow.shoot player @a ~ ~ ~ 1 1.4', 'scoreboard players set $olr mg.st 0',
   'execute anchored eyes positioned ^ ^ ^0.6 run function mg:ombre/cl/pierce', 'tag @e[tag=mg.olhitn] remove mg.olhitn', f'function mg:{P}/cl/end'])
ray('pierce', ['execute positioned ~-0.6 ~-0.6 ~-0.6 as @e[tag=mg.olm,tag=!mg.olhitn,dx=0.2,dy=0.2,dz=0.2] positioned ~0.6 ~0.6 ~0.6 run function mg:ombre/cl/pierce_hit with storage mg:ombre s'],
    40, 'particle minecraft:dust{color:[0.6,1.0,0.5],scale:0.8} ~ ~ ~ 0 0 0 0 1 force')
w('cl/pierce_hit', ['$function mg:ombre/cl/hit {d:$(d)}', 'tag @s add mg.olhitn', 'particle minecraft:crit ~ ~1 ~ 0.3 0.4 0.3 0.2 10'])
w('cl/pierce_end', ['particle minecraft:crit ~ ~ ~ 0.1 0.1 0.1 0.1 6'])
w('cl/a22', ['# Pluie de flèches : zone visée (30 blocs)'] + dclean(dmg_set(5, '$pa', 1, 2)) +
  ['scoreboard players set $olr mg.st 0', 'scoreboard players operation $own mg.st = @s mg.olpid',
   'execute anchored eyes positioned ^ ^ ^0.6 run function mg:ombre/cl/aim', 'playsound minecraft:entity.arrow.shoot player @a ~ ~ ~ 1 0.7', f'function mg:{P}/cl/end'])
ray('aim', ['execute if entity @e[tag=mg.olm,distance=..1.5] run return run function mg:ombre/cl/aim_end'], 30, 'particle minecraft:dust{color:[0.6,1.0,0.5],scale:0.5} ~ ~ ~ 0 0 0 0 1')
w('cl/aim_end', ['# fin du rayon de visée : zone de pluie (4 volées)', 'execute align xyz positioned ~0.5 ~1 ~0.5 run summon minecraft:marker ~ ~ ~ {Tags:["mg.ol","mg.olrain","mg.olnn"]}',
                 'scoreboard players set @e[tag=mg.olnn] mg.olst 4', 'scoreboard players operation @e[tag=mg.olnn] mg.olo = $own mg.st',
                 'execute store result score @e[tag=mg.olnn] mg.olpw run scoreboard players get $d mg.st', 'tag @e[tag=mg.olnn] remove mg.olnn'])
w('cl/rain', ['# @s (zone de pluie, chaque seconde) : une volée', 'scoreboard players remove @s mg.olst 1',
              'particle minecraft:crit ~ ~4 ~ 2 0.2 2 0 60 force', 'particle minecraft:dust{color:[0.6,1.0,0.5],scale:1} ~ ~2 ~ 2 2 2 0 40 force',
              'playsound minecraft:entity.arrow.hit player @a ~ ~ ~ 1 0.8',
              'scoreboard players operation $own mg.st = @s mg.olo', 'tag @a remove mg.olcast', 'execute as @a[tag=mg.olw] if score @s mg.olpid = $own mg.st run tag @s add mg.olcast',
              'execute store result storage mg:ombre s.d int 1 run scoreboard players get @s mg.olpw',
              'execute as @e[tag=mg.olm,distance=..4.5] at @s run function mg:ombre/cl/hit with storage mg:ombre s', 'tag @a remove mg.olcast',
              'execute if score @s mg.olst matches ..0 run kill @s'])
w('cl/a23', ['# Piège à loups (3 au plus)', 'scoreboard players operation $own mg.st = @s mg.olpid', 'scoreboard players set $n mg.st 0',
             'execute as @e[type=minecraft:marker,tag=mg.oltrap] if score @s mg.olo = $own mg.st run scoreboard players add $n mg.st 1',
             'execute if score $n mg.st matches 3.. as @e[type=minecraft:marker,tag=mg.oltrap,sort=furthest,limit=1] if score @s mg.olo = $own mg.st run function mg:ombre/cl/trap_rm'] +
  dclean(dmg_set(10, '$pa')) +
  ['execute align xyz positioned ~0.5 ~ ~0.5 run summon minecraft:marker ~ ~ ~ {Tags:["mg.ol","mg.oltrap","mg.olnn"]}',
   'execute align xyz positioned ~0.5 ~ ~0.5 run summon minecraft:block_display ~ ~ ~ {Tags:["mg.ol","mg.oltrapd","mg.olnn"],block_state:{Name:"minecraft:heavy_weighted_pressure_plate"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.45f,0f,-0.45f],scale:[0.9f,1f,0.9f]}}',
   'scoreboard players add $oltid mg.st 1', 'scoreboard players operation @e[tag=mg.olnn] mg.olid = $oltid mg.st',
   'scoreboard players operation @e[tag=mg.olnn] mg.olo = $own mg.st', 'execute store result score @e[tag=mg.olnn,tag=mg.oltrap] mg.olpw run scoreboard players get $d mg.st',
   'tag @e[tag=mg.olnn] remove mg.olnn', 'playsound minecraft:block.chain.place player @a ~ ~ ~ 0.8 0.8', f'function mg:{P}/cl/end'])
w('cl/trap_rm', ['scoreboard players operation $tid mg.st = @s mg.olid', 'execute as @e[tag=mg.oltrapd] if score @s mg.olid = $tid mg.st run kill @s', 'kill @s'])
w('cl/trap_fire', ['# @s (piège) : un monstre marche dessus', 'scoreboard players operation $own mg.st = @s mg.olo', 'tag @a remove mg.olcast',
                   'execute as @a[tag=mg.olw] if score @s mg.olpid = $own mg.st run tag @s add mg.olcast',
                   'execute store result storage mg:ombre s.d int 1 run scoreboard players get @s mg.olpw',
                   'execute as @e[tag=mg.olm,distance=..1.4,sort=nearest,limit=1] at @s run function mg:ombre/cl/trap_hit with storage mg:ombre s',
                   'playsound minecraft:block.chain.break hostile @a ~ ~ ~ 1 0.6', 'particle minecraft:crit ~ ~0.5 ~ 0.4 0.3 0.4 0.2 15',
                   'tag @a remove mg.olcast', 'function mg:ombre/cl/trap_rm'])
w('cl/trap_hit', ['$function mg:ombre/cl/hit {d:$(d)}', 'effect give @s minecraft:slowness 4 6 true'])
w('cl/a24', ['# Œil du faucon', 'playsound minecraft:entity.parrot.imitate.phantom player @a ~ ~ ~ 1 1.5', 'effect give @s minecraft:speed 10 1',
             'execute as @e[tag=mg.olm,distance=..30] run function mg:ombre/cl/mark', f'function mg:{P}/cl/end'])
w('cl/mark', ['effect give @s minecraft:glowing 10 0 true', 'attribute @s minecraft:armor modifier remove mg:olmark',
              'attribute @s minecraft:armor modifier add mg:olmark -10 add_value', 'scoreboard players set @s mg.olmk 10'])
w('cl/unmark', ['attribute @s minecraft:armor modifier remove mg:olmark', 'scoreboard players reset @s mg.olmk'])
# ---- Mage
w('cl/bolt', ['# Trait magique du bâton (gratuit)', 'execute if score @s mg.olc0 matches 1.. run return 0', 'scoreboard players set @s mg.olc0 12',
              f'function mg:{P}/cl/pow'] + dclean(dmg_set(4, '$pw')) +
  ['playsound minecraft:entity.illusioner.cast_spell player @a ~ ~ ~ 0.6 1.6', 'scoreboard players set $olr mg.st 0',
   'execute anchored eyes positioned ^ ^ ^0.6 run function mg:ombre/cl/boltr', f'function mg:{P}/cl/end'])
ray('boltr', ['execute positioned ~-0.6 ~-0.6 ~-0.6 as @e[tag=mg.olm,dx=0.2,dy=0.2,dz=0.2,limit=1] positioned ~0.6 ~0.6 ~0.6 run return run function mg:ombre/cl/bolt_hit with storage mg:ombre s'],
    30, 'particle minecraft:dust{color:[0.75,0.45,1.0],scale:0.9} ~ ~ ~ 0 0 0 0 1 force')
w('cl/bolt_hit', ['$function mg:ombre/cl/hit {d:$(d)}', 'particle minecraft:witch ~ ~1 ~ 0.3 0.4 0.3 0 10', 'scoreboard players set $olr mg.st 999'])
w('cl/boltr_end', ['particle minecraft:witch ~ ~ ~ 0.1 0.1 0.1 0 5'])
w('cl/a31', ['# Boule de feu'] + dclean(dmg_set(10, '$pw')) +
  ['playsound minecraft:entity.blaze.shoot player @a ~ ~ ~ 1 1', 'scoreboard players set $olr mg.st 0',
   'execute anchored eyes positioned ^ ^ ^0.6 run function mg:ombre/cl/fire', f'function mg:{P}/cl/end'])
ray('fire', ['execute positioned ~-0.6 ~-0.6 ~-0.6 if entity @e[tag=mg.olm,dx=0.2,dy=0.2,dz=0.2] positioned ~0.6 ~0.6 ~0.6 run return run function mg:ombre/cl/fire_end'],
    30, 'particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.01 3 force')
w('cl/fire_end', ['# explosion de la boule de feu', 'scoreboard players set $olr mg.st 999', 'particle minecraft:explosion ~ ~ ~ 0.5 0.5 0.5 0 3 force',
                  'particle minecraft:flame ~ ~ ~ 1.5 1 1.5 0.05 60 force', 'playsound minecraft:entity.generic.explode player @a ~ ~ ~ 0.8 1.3',
                  'execute as @e[tag=mg.olm,distance=..3] at @s run function mg:ombre/cl/fire_hit with storage mg:ombre s'])
w('cl/fire_hit', ['$function mg:ombre/cl/hit {d:$(d)}', 'data merge entity @s {Fire:80s}'])
w('cl/a32', ['# Lance de givre'] + dclean(dmg_set(8, '$pw')) +
  ['playsound minecraft:block.glass.break player @a ~ ~ ~ 1 1.4', 'scoreboard players set $olr mg.st 0',
   'execute anchored eyes positioned ^ ^ ^0.6 run function mg:ombre/cl/frost', f'function mg:{P}/cl/end'])
ray('frost', ['execute positioned ~-0.6 ~-0.6 ~-0.6 as @e[tag=mg.olm,dx=0.2,dy=0.2,dz=0.2,limit=1] positioned ~0.6 ~0.6 ~0.6 run return run function mg:ombre/cl/frost_hit with storage mg:ombre s'],
    30, 'particle minecraft:snowflake ~ ~ ~ 0.05 0.05 0.05 0 2 force')
w('cl/frost_hit', ['$function mg:ombre/cl/hit {d:$(d)}', 'effect give @s minecraft:slowness 4 2 true', 'particle minecraft:item_snowball ~ ~1 ~ 0.4 0.6 0.4 0 30',
                   'scoreboard players set $olr mg.st 999'])
w('cl/frost_end', ['particle minecraft:snowflake ~ ~ ~ 0.3 0.3 0.3 0 10'])
w('cl/a33', ['# Chaîne d\'éclairs : les 4 ennemis les plus proches (12 blocs)'] + dclean(dmg_set(12, '$pw')) +
  ['playsound minecraft:item.trident.thunder player @a ~ ~ ~ 0.8 1.6',
   'execute as @e[tag=mg.olm,distance=..12,sort=nearest,limit=4] at @s run function mg:ombre/cl/chain_hit with storage mg:ombre s', f'function mg:{P}/cl/end'])
w('cl/chain_hit', ['$function mg:ombre/cl/hit {d:$(d)}', 'particle minecraft:electric_spark ~ ~1 ~ 0.3 1 0.3 0.4 40 force',
                   'particle minecraft:end_rod ~ ~3 ~ 0.05 2 0.05 0 20 force'])
w('cl/a34', ['# Météore : zone visée (40 blocs), impact 1,5 s plus tard'] + dclean(dmg_set(30, '$pw', 2)) +
  ['scoreboard players set $olr mg.st 0', 'scoreboard players operation $own mg.st = @s mg.olpid',
   'execute anchored eyes positioned ^ ^ ^0.6 run function mg:ombre/cl/meteo', 'playsound minecraft:entity.wither.shoot player @a ~ ~ ~ 1 0.6', f'function mg:{P}/cl/end'])
ray('meteo', ['execute if entity @e[tag=mg.olm,distance=..1.5] run return run function mg:ombre/cl/meteo_end'], 40, 'particle minecraft:small_flame ~ ~ ~ 0 0 0 0 1')
w('cl/meteo_end', ['execute align xyz positioned ~0.5 ~ ~0.5 run summon minecraft:marker ~ ~ ~ {Tags:["mg.ol","mg.olmeteor","mg.olnn"]}',
                   'scoreboard players set @e[tag=mg.olnn] mg.olst 30', 'scoreboard players operation @e[tag=mg.olnn] mg.olo = $own mg.st',
                   'execute store result score @e[tag=mg.olnn] mg.olpw run scoreboard players get $d mg.st', 'tag @e[tag=mg.olnn] remove mg.olnn'])
w('cl/meteor', ['# @s (météore, chaque tick) : chute puis impact', 'scoreboard players remove @s mg.olst 1',
                'execute if score @s mg.olst matches 1.. run particle minecraft:flame ~ ~10 ~ 0.4 3 0.4 0.05 12 force',
                'execute if score @s mg.olst matches 1.. run particle minecraft:dust{color:[1.0,0.3,0.1],scale:2} ~ ~0.2 ~ 3 0 3 0 10 force',
                'execute if score @s mg.olst matches 1.. run return 0',
                'particle minecraft:explosion_emitter ~ ~1 ~ 0 0 0 0 1 force', 'particle minecraft:lava ~ ~1 ~ 3 1 3 0 60 force',
                'playsound minecraft:entity.generic.explode player @a ~ ~ ~ 2 0.6',
                'scoreboard players operation $own mg.st = @s mg.olo', 'tag @a remove mg.olcast', 'execute as @a[tag=mg.olw] if score @s mg.olpid = $own mg.st run tag @s add mg.olcast',
                'execute store result storage mg:ombre s.d int 1 run scoreboard players get @s mg.olpw',
                'execute as @e[tag=mg.olm,distance=..6] at @s run function mg:ombre/cl/fire_hit with storage mg:ombre s', 'tag @a remove mg.olcast', 'kill @s'])
# ---- Clerc
w('cl/a41', ['# Lumière guérisseuse', 'playsound minecraft:block.amethyst_block.chime player @a ~ ~ ~ 1 1.2', 'particle minecraft:happy_villager ~ ~1 ~ 3 1 3 0 40',
             'particle minecraft:end_rod ~ ~1 ~ 2 1 2 0.05 30',
             'effect give @a[tag=mg.olw,distance=..8] minecraft:instant_health 1 1 true', 'effect give @a[tag=mg.olw,distance=..8] minecraft:regeneration 4 1 true',
             'execute if score @s mg.ols4 matches 8.. run effect give @a[tag=mg.olw,distance=..8] minecraft:regeneration 6 2 true', f'function mg:{P}/cl/end'])
w('cl/a42', ['# Châtiment sacré'] + dclean(dmg_set(10, '$pw')) +
  ['playsound minecraft:block.beacon.power_select player @a ~ ~ ~ 1 1.6', 'scoreboard players set $olr mg.st 0',
   'execute anchored eyes positioned ^ ^ ^0.6 run function mg:ombre/cl/smite', f'function mg:{P}/cl/end'])
ray('smite', ['execute positioned ~-0.6 ~-0.6 ~-0.6 as @e[tag=mg.olm,dx=0.2,dy=0.2,dz=0.2,limit=1] positioned ~0.6 ~0.6 ~0.6 run return run function mg:ombre/cl/smite_hit with storage mg:ombre s'],
    24, 'particle minecraft:end_rod ~ ~ ~ 0 0 0 0 1 force')
w('cl/smite_hit', ['execute if entity @s[tag=mg.olund] run function mg:ombre/cl/hit2', '$execute unless entity @s[tag=mg.olund] run function mg:ombre/cl/hit {d:$(d)}',
                   'particle minecraft:flash{color:[1.0,1.0,0.7,1.0]} ~ ~1 ~ 0 0 0 0 1 force', 'scoreboard players set $olr mg.st 999'])
w('cl/smite_end', ['particle minecraft:end_rod ~ ~ ~ 0.2 0.2 0.2 0.05 8'])
w('cl/a43', ['# Bénédiction', 'playsound minecraft:block.beacon.activate player @a ~ ~ ~ 1 1.4', 'particle minecraft:totem_of_undying ~ ~1 ~ 2 1 2 0.2 40',
             'effect give @a[tag=mg.olw,distance=..10] minecraft:absorption 20 1', 'effect give @a[tag=mg.olw,distance=..10] minecraft:resistance 15 0',
             f'function mg:{P}/cl/end'])
w('cl/a44', ['# Aube sacrée'] + dclean(dmg_set(20, '$pw')) +
  ['playsound minecraft:ui.toast.challenge_complete player @a ~ ~ ~ 1 0.7', 'particle minecraft:flash{color:[1.0,0.9,0.5,1.0]} ~ ~1 ~ 0 0 0 0 1 force',
   'particle minecraft:end_rod ~ ~1 ~ 6 2 6 0.1 200 force',
   'effect give @a[tag=mg.olw,distance=..16] minecraft:instant_health 1 2 true', 'effect give @a[tag=mg.olw,distance=..16] minecraft:regeneration 10 1 true',
   'execute as @e[tag=mg.olm,distance=..10] at @s run function mg:ombre/cl/smite_hit with storage mg:ombre s', f'function mg:{P}/cl/end'])

# ================================================================ boucles des classes
w('cl/tick', ['# Chaque tick : recharges des compétences, pièges, météores'] +
  [f'scoreboard players remove @a[tag=mg.olw,scores={{mg.olc{i}=1..}}] mg.olc{i} 1' for i in range(0, 5)] +
  ['execute as @e[type=minecraft:marker,tag=mg.oltrap] at @s if entity @e[tag=mg.olm,distance=..1.4] run function mg:ombre/cl/trap_fire',
   'execute as @e[type=minecraft:marker,tag=mg.olmeteor] at @s run function mg:ombre/cl/meteor', f'function mg:{P}/dmg_tick'])
w('cl/second', ['# Chaque seconde : mana, pluies de flèches, marques, aura du clerc',
                f'execute as @a[tag=mg.olw] run function mg:{P}/mana_tick',
                'execute as @e[type=minecraft:marker,tag=mg.olrain] at @s run function mg:ombre/cl/rain',
                'scoreboard players remove @e[tag=mg.olm,scores={mg.olmk=1..}] mg.olmk 1', 'execute as @e[tag=mg.olm,scores={mg.olmk=..0}] run function mg:ombre/cl/unmark',
                'execute if score $olq100 mg.st matches 0 as @a[tag=mg.olw,scores={mg.olcl=4}] at @s run effect give @a[tag=mg.olw,distance=..6] minecraft:regeneration 3 0 true'])

# ================================================================ caractéristiques (journal)
for n, obj, name, col, eff in STATS:
    w(f'st/add_{n}', [f'# @s met un point en {name}', 'execute unless score @s mg.olsp matches 1.. run return run tellraw @s {"text":"Aucun point à répartir.","color":"gray"}',
                      'scoreboard players remove @s mg.olsp 1', f'scoreboard players add @s {obj} 1', f'function mg:{P}/stats',
                      f'tellraw @s [{{"text":"{name} ","color":"{col}","bold":true}},{{"score":{{"name":"@s","objective":"{obj}"}},"color":"white"}},{{"text":"  ({eff})","color":"gray"}}]',
                      'execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.7 1.4', f'function mg:{P}/sheet'])
w('st/reset', ['# @s : redistribue ses points (300 💰, maître d\'armes)', 'execute unless score @s mg.olg matches 300.. run return run tellraw @s {"text":"Il faut 300 💰.","color":"red"}',
               'scoreboard players remove @s mg.olg 300'] + [f'scoreboard players operation @s mg.olsp += @s {o}' for _, o, *_r in STATS] +
  [f'scoreboard players set @s {o} 0' for _, o, *_r in STATS] + [f'function mg:{P}/stats', 'tellraw @s {"text":"♻ Points redistribuables.","color":"yellow"}'])
