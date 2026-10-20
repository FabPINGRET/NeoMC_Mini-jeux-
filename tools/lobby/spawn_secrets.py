# Spawn : succès cachés du spawn, détection et terrier secret ; exécuté par gen_lobby.py (exec) après le mode kart libre.
# Utilise : F, PIPES, POND, R, SEC_BTN, X1, X2, os, rx1, rx2, ry1, ry2, rz1, rz2, sz_, tdisp, wr

# ------------------------------------------------------------------ SECRETS : succès cachés (onglet « Secrets du spawn ») et leur détection
import json
ADV = os.path.join(R, 'data', 'mg', 'advancement', 'secrets')
os.makedirs(ADV, exist_ok=True)
for f in os.listdir(ADV): os.remove(os.path.join(ADV, f))
SECRETS = [  # id, titre, indice, icône, cadre
    ('terrier', 'Le terrier', 'Certaines trappes mènent plus loin qu\'on ne croit', 'spruce_trapdoor', 'task'),
    ('tuyau', 'Tuyau de distorsion', 'Accroupi, on voyage plus vite', 'green_concrete', 'task'),
    ('couronne', 'Roi du château', 'Personne ne regarde jamais les toits', 'golden_helmet', 'task'),
    ('etoiles', 'La tête dans les étoiles', 'Au cœur doré, lève les yeux', 'nether_star', 'task'),
    ('ile', 'Île céleste', 'Le ciel n\'est pas réservé aux oiseaux', 'grass_block', 'challenge'),
    ('plongeon', 'Petit plongeon', 'Les poissons aussi aiment la visite', 'tropical_fish_bucket', 'task'),
    ('vide', 'Ouf !', 'Le vide ne veut pas de toi', 'feather', 'task'),
    ('arsenal', 'Arsenal complet', 'Un de chaque, pas moins', 'blaze_rod', 'task'),
    ('mille', 'Dans le mille', 'Vise le cœur', 'target', 'task'),
    ('lynx', 'Œil de lynx', 'Vingt fois en plein cœur', 'spyglass', 'challenge'),
    ('sommet', 'Au sommet', 'Tout en haut, la lumière verte', 'diamond', 'task'),
    ('ecureuil', 'Écureuil volant', 'Tout en haut en moins d\'une minute', 'elytra', 'challenge'),
    ('pilote', 'Pilote du dimanche', 'Un tour, rien qu\'un', 'minecart', 'task'),
    ('volant', 'Fou du volant', 'Un tour en moins de 40 secondes', 'blaze_powder', 'challenge'),
    ('danse', 'Danse de la victoire', 'Sur la place, montre tes plus beaux pas', 'jukebox', 'task'),
    ('bouton', 'Appuie, pour voir', 'Un bouton discret, près des champions', 'polished_blackstone_button', 'task'),
    ('visite', 'Visite guidée', 'Cinq lieux à voir absolument', 'filled_map', 'task'),
]
def adv(name, d):
    with open(os.path.join(ADV, name + '.json'), 'w', encoding='utf-8', newline='\n') as f: json.dump(d, f, indent=2, ensure_ascii=False); f.write('\n')
adv('root', {'criteria': {'tick': {'trigger': 'minecraft:tick'}},
             'display': {'icon': {'id': 'minecraft:ender_eye'}, 'title': {'text': 'Secrets du spawn', 'color': 'gold'},
                         'description': {'text': f'Le spawn cache {len(SECRETS)} secrets... ouvre l\'œil !', 'color': 'gray'},
                         'background': 'minecraft:block/amethyst_block', 'show_toast': False, 'announce_to_chat': False}})
for sid, title, hint, icon, frame in SECRETS:
    adv(sid, {'parent': 'mg:secrets/root', 'criteria': {'found': {'trigger': 'minecraft:impossible'}},
              'display': {'icon': {'id': f'minecraft:{icon}'}, 'title': {'text': title}, 'description': {'text': hint, 'color': 'gray'}, 'frame': frame,
                          'show_toast': True, 'announce_to_chat': False, 'hidden': True},
              'rewards': {'function': f'mg:secrets/found/{sid}'}})
adv('maitre', {'parent': 'mg:secrets/visite', 'criteria': {'found': {'trigger': 'minecraft:impossible'}},
               'display': {'icon': {'id': 'minecraft:dragon_egg'}, 'title': {'text': 'Maître des secrets', 'color': 'light_purple'},
                           'description': {'text': 'Tous les secrets du spawn', 'color': 'gray'}, 'frame': 'challenge',
                           'show_toast': True, 'announce_to_chat': False, 'hidden': True},
               'rewards': {'function': 'mg:secrets/found/maitre'}})
def G_(sid): return f'advancement grant @s only mg:secrets/{sid}'
def NOT(sid): return f'unless entity @s[advancements={{mg:secrets/{sid}=true}}]'
ALL = ','.join(f'mg:secrets/{s[0]}=true' for s in SECRETS)
import shutil
shutil.rmtree(os.path.join(F, 'secrets', 'found'), ignore_errors=True)
for sid, title, hint, icon, frame in SECRETS + [('maitre', 'Maître des secrets', '', '', 'challenge')]:
    col = 'light_purple' if frame == 'challenge' else 'green'
    wr(f'secrets/found/{sid}', [f'# Secret « {title} » trouvé par @s : annonce à tout le monde',
                               'function mg:secrets/count',
                               'tellraw @a [{"text":"🕵 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" a trouvé un secret du spawn : ","color":"gray"},'
                               f'{{"text":"[{title}]","color":"{col}","bold":true}},{{"text":" (","color":"gray"}},{{"score":{{"name":"$secn","objective":"mg.st"}},"color":"gold"}},'
                               f'{{"text":"/{len(SECRETS) + 1})","color":"gray"}}]',
                               'execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 0.6 1.6',
                               'function mg:secrets/reward'])
wr('secrets/count', ['# Nombre de secrets trouvés par @s → $secn'] + ['scoreboard players set $secn mg.st 0'] +
   [f'execute if entity @s[advancements={{mg:secrets/{x[0]}=true}}] run scoreboard players add $secn mg.st 1' for x in SECRETS + [('maitre',)]])
wr('secrets/reward', ['# Un secret trouvé (@s) : petite fête, et le grand final quand tout est trouvé',
                      'execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.3',
                      'execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.5 0.8 0.5 0.4 40',
                      f'execute if entity @s[advancements={{{ALL}}}] unless entity @s[advancements={{mg:secrets/maitre=true}}] run advancement grant @s only mg:secrets/maitre'])
ISL_SPOTS = [(31, 90, -31, 5), (-34, 94, 31, 5), (-31, 98, -35, 4), (37, 96, 31, 4), (-6, 104, 30, 3)]
chk = ['# Secrets du spawn : vérifications (toutes les 0,5 s, @s = joueur du spawn, à sa position)',
       f'execute {NOT("terrier")} if entity @s[x={rx1},y={ry1},z={rz1},dx={rx2 - rx1},dy={ry2 - ry1},dz={rz2 - rz1}] run {G_("terrier")}',
       f'execute {NOT("couronne")} if entity @s[x={X1 - 1},y=84,z=-0.3,dx={X2 - X1 + 2},dy=2,dz=0.6] run {G_("couronne")}',
       f'execute {NOT("plongeon")} if entity @s[x={POND[0] - 3},y=61.5,z={POND[1] - 3},dx=6,dy=1,dz=6] if block ~ ~ ~ minecraft:water run {G_("plongeon")}',
       f'execute {NOT("arsenal")} if items entity @s container.* minecraft:warped_fungus_on_a_stick if items entity @s container.* minecraft:blaze_rod '
       f'if items entity @s container.* minecraft:wind_charge if items entity @s container.* minecraft:snowball run {G_("arsenal")}']
for (cx, cy, cz, r) in ISL_SPOTS:
    chk.append(f'execute {NOT("ile")} if entity @s[x={cx - r},y={cy + 0.5},z={cz - r},dx={2 * r},dy=3,dz={2 * r}] run {G_("ile")}')
chk += [f'execute if entity @s[x=-1,y=64,z=-1,dx=2,dy=1,dz=2,x_rotation=-90..-75] run scoreboard players add @s mg.eup 10',
        f'execute unless entity @s[x=-1,y=64,z=-1,dx=2,dy=1,dz=2,x_rotation=-90..-75] run scoreboard players set @s mg.eup 0',
        f'execute {NOT("etoiles")} if score @s mg.eup matches 60.. run {G_("etoiles")}',
        'tag @s[x=-56,y=64,z=-10,dx=20,dy=6,dz=20] add mg.ev1', 'tag @s[x=64,y=63,z=-4,dx=6,dy=4,dz=8] add mg.ev2', 'tag @s[x=-6,y=63,z=-53,dx=12,dy=6,dz=12] add mg.ev3',
        'tag @s[x=-5,y=63,z=43,dx=10,dy=4,dz=10] add mg.ev4', f'tag @s[x=-4,y=63,z={round(sz_) - 4},dx=8,dy=5,dz=8] add mg.ev5',
        f'execute {NOT("visite")} if entity @s[tag=mg.ev1,tag=mg.ev2,tag=mg.ev3,tag=mg.ev4,tag=mg.ev5] run {G_("visite")}',
        'scoreboard players remove @s[scores={mg.ept=1..}] mg.ept 10']
for (a, b) in ((PIPES[0], PIPES[3]), (PIPES[1], PIPES[2])):
    for (p, q) in ((a, b), (b, a)):
        chk.append(f'execute unless score @s mg.ept matches 1.. if predicate mg:sneak positioned {p[0] + 0.5} 68 {p[1] + 0.5} if entity @s[distance=..0.9] run function mg:secrets/pipe {{x:{q[0] + 0.5},z:{q[1] + 0.5}}}')
wr('secrets/check', chk)
wr('secrets/pipe', ['# Tuyau de distorsion : @s file vers l\'autre tuyau (macro x, z)',
                    'execute at @s run particle minecraft:portal ~ ~0.5 ~ 0.3 0.6 0.3 0.6 40',
                    '$tp @s $(x) 68.2 $(z)', 'scoreboard players set @s mg.ept 40',
                    'execute at @s run playsound minecraft:entity.enderman.teleport master @a ~ ~ ~ 0.8 1.6',
                    'execute at @s run playsound minecraft:block.note_block.bit master @s ~ ~ ~ 1 0.6',
                    'execute at @s run particle minecraft:happy_villager ~ ~1 ~ 0.4 0.6 0.4 0 20', G_('tuyau')])
bx, by, bz = SEC_BTN
wr('secrets/tick', ['# Secrets du spawn (toutes les 0,5 s depuis lobby/armory_tick)',
                    'execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.lk,gamemode=!spectator,x=0,y=64,z=0,distance=..140] at @s run function mg:secrets/check',
                    'scoreboard players remove $ebt mg.st 10',
                    f'execute unless score $ebt mg.st matches 1.. if block {bx} {by} {bz} minecraft:polished_blackstone_button[powered=true] run function mg:secrets/button'])
wr('secrets/button', ['# Le bouton secret du garage : feu d\'artifice au-dessus du podium',
                      'scoreboard players set $ebt mg.st 100',
                      f'execute as @a[x={bx + 0.5},y={by},z={bz + 0.5},distance=..5] run {G_("bouton")}',
                      'execute positioned 0.5 80 48.5 run function mg:lobby/boom',
                      'execute positioned -6.5 76 48.5 run function mg:lobby/boom',
                      'execute positioned 7.5 77 48.5 run function mg:lobby/boom'])
wr('secrets/dance', ['# Danse de la victoire (@s sur la place) : 10 accroupissements en 3 s',
                     'execute store result score $sn mg.t if predicate mg:sneak',
                     'execute if score $sn mg.t matches 1 unless score @s mg.esn matches 1 run scoreboard players add @s mg.esc 1',
                     'scoreboard players operation @s mg.esn = $sn mg.t',
                     'scoreboard players add @s mg.est 1',
                     'execute if score @s mg.est matches 60.. run scoreboard players set @s mg.esc 0',
                     'execute if score @s mg.est matches 60.. run scoreboard players set @s mg.est 0',
                     f'execute if score @s mg.esc matches 10.. {NOT("danse")} run {G_("danse")}'])
# crochets dans les fonctions générées ici
for rel, anchor, add in (('lobby/laser_bull', 'title @s actionbar [{"text":"★ DANS LE MILLE ! ★"',
                          ['scoreboard players add @s mg.ebl 1', G_('mille'), 'execute if score @s mg.ebl matches 20.. run ' + G_('lynx')]),
                         ('lobkart/lap', 'execute unless score $klrec mg.st matches 1.. run function mg:lobkart/record',
                          [G_('pilote'), 'execute if score @s mg.klt matches ..799 run ' + G_('volant')])):
    p = os.path.join(F, rel + '.mcfunction')
    s = open(p, encoding='utf-8').read().rstrip('\n').split('\n')
    i = next(k for k, l in enumerate(s) if l.startswith(anchor))
    wr(rel, s[:i] + add + s[i:])
with open(os.path.join(F, 'lobby', 'armory_tick.mcfunction'), 'a', encoding='utf-8', newline='\n') as f:
    f.write('\n# Secrets du spawn\n'
            'execute if score $lfx mg.t matches 0 run function mg:secrets/tick\n'
            'execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.lk,x=0,y=64,z=0,distance=..15] run function mg:secrets/dance\n')
with open(os.path.join(F, 'lobby', 'deco_common.mcfunction'), 'a', encoding='utf-8', newline='\n') as f:
    f.write(tdisp((rx1 + rx2) / 2 + 0.5, ry1 + 3.2, rz1 + 1.5, '[{"text":"🕳 Le terrier secret","color":"light_purple","bold":true},{"text":"\\nBravo, peu de gens trouvent cet endroit...","color":"gray"}]', 1.0) + '\n')
print('secrets :', len(SECRETS) + 1)

