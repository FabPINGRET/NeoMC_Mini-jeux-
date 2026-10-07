# ================================================================== SON ET MUSIQUE (exécuté à la fin de battle_part.py)
# Musique : séquenceur (kart/music, chaque tick) qui joue une croche de kart/mus/<morceau>_<n> à chaque pilote en course
# (catégorie record : volume Juke-box du joueur) ; dernier tour = plus rapide ; étoile = thème d'invincibilité.
# Bruitages : bips du départ, roulette d'objet (1 s avant de recevoir l'objet), moteur selon la vitesse, crissement en dérapage,
# jingle du dernier tour, fanfare d'arrivée.
fn('music', '''# Séquenceur de musique du kart (chaque tick de course)
scoreboard players add $kmc mg.st 1
scoreboard players set $kmt mg.st 4
execute if score $kfl mg.st matches 1 run scoreboard players set $kmt mg.st 3
execute if score $kmc mg.st < $kmt mg.st run return 0
scoreboard players set $kmc mg.st 0
scoreboard players add $kms mg.st 1
execute if score $kms mg.st matches 128.. run scoreboard players set $kms mg.st 0
execute store result storage mg:kart mus.s int 1 run scoreboard players get $kms mg.st
execute store result storage mg:kart mus.t int 1 run scoreboard players get $ktr mg.st
function mg:kart/mus_play with storage mg:kart mus
''')
fn('mus_play', '''$execute as @a[tag=mg.play,tag=!mg.kfin] unless score @s mg.kst matches 1.. at @s run function mg:kart/mus/t$(t)_$(s)
$execute as @a[tag=mg.play,tag=!mg.kfin,scores={mg.kst=1..}] at @s run function mg:kart/mus/star_$(s)
''')
patch_fn('tick', 'function mg:kart/track_tick\n', 'function mg:kart/track_tick\nfunction mg:kart/music\n')
patch_fn('prepare', 'tag @a remove mg.kok\n', 'tag @a remove mg.kok\nscoreboard players set $kfl mg.st 0\nscoreboard players set $kms mg.st -1\n'
         'scoreboard players set $kmc mg.st 0\nscoreboard players set @a[tag=mg.play] mg.krl 0\nscoreboard players set #k2 mg.st 2\n')

# départ : bips 3-2-1 graves puis GO aigu
patch_fn('hold', "# Compte à rebours du kart retenu (vrai) tant que tous les pilotes n'ont pas choisi leur kart, 1 minute au plus\n",
         "# Compte à rebours du kart retenu (vrai) tant que tous les pilotes n'ont pas choisi leur kart, 1 minute au plus\n" +
         ''.join(f'execute if score $timer mg.st matches {t} as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bit master @s ~ ~ ~ 1 0.7\n' for t in (61, 41, 21)))
patch_fn('go', '# Départ : portillon ouvert\n', '# Départ : portillon ouvert\n'
         'execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bit master @s ~ ~ ~ 1 1.4\n'
         'execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 0.8 1.4\n'
         'title @a[tag=mg.play] title [{"text":"GO !","color":"green","bold":true}]\n')

# roulette d'objet : la boîte lance 20 ticks de roulette, puis l'objet tombe
patch_fn('owner_roll', 'run function mg:kart/item_roll', 'unless score @s mg.krl matches 1.. run scoreboard players set @s mg.krl 20')
fn('roulette', '''# Roulette d'objet de @s (mg.krl : ticks restants)
scoreboard players remove @s mg.krl 1
scoreboard players operation $krm mg.st = @s mg.krl
scoreboard players operation $krm mg.st %= #k2 mg.st
execute if score $krm mg.st matches 0 if score @s mg.krl matches 8.. at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.8 2
execute if score $krm mg.st matches 0 if score @s mg.krl matches 1..7 at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.8 1.6
execute if score @s mg.krl matches 0 if score @s mg.kit matches 0 run function mg:kart/item_roll
execute if score @s mg.krl matches 0 at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.5
''')
patch_fn('drive', 'execute if score @s mg.kch matches 1.. run function mg:kart/choose\n',
         'execute if score @s mg.kch matches 1.. run function mg:kart/choose\nexecute if score @s mg.krl matches 1.. run function mg:kart/roulette\n'
         'execute if score $kph mg.st matches 0 run function mg:kart/engine\n')
ROUL = ('{"text":"🎲 ","color":"gold"},{"text":"🍌 🟢 🔴 🍄 ⭐ ⚡ 💣 👻","color":"white"},{"text":"  ...","color":"gray"}')
for name in ('hud', 'bat_hud'):
    first = {'hud': '# Barre du bas : tour, position, objet (et charges), vitesse\n',
             'bat_hud': '# Barre du bas en bataille : ballons, temps restant, objet, vitesse\n'}[name]
    patch_fn(name, first, first + f'execute if score @s mg.krl matches 1.. run return run title @s actionbar [{ROUL}]\n')

# moteur (toutes les 4 ticks, selon la vitesse) et crissement en dérapage
eng = ['# Bruit du moteur de @s selon sa vitesse (entendu par lui et les pilotes proches)']
for lo, hi, p in ((1, 29, 0.55), (30, 59, 0.65), (60, 89, 0.78), (90, 109, 0.9), (110, 139, 1.05), (140, 999, 1.25)):
    eng.append(f'execute if score @s mg.ksp matches {lo}..{hi} at @s run playsound minecraft:block.note_block.didgeridoo player @a[tag=mg.play,distance=..12] ~ ~ ~ 0.14 {p}')
eng.append('execute if score @s mg.kdr matches 1.. at @s run playsound minecraft:block.gravel.step player @a[tag=mg.play,distance=..12] ~ ~ ~ 0.5 1.4')
fn('engine', '\n'.join(eng) + '\n')

# dernier tour : jingle et musique plus rapide ; arrivée : fanfare
patch_fn('lap', 'execute if score @s mg.klp = $kLaps mg.st run title @s title [{"text":"TOUR FINAL !","color":"gold","bold":true}]\n',
         'execute if score @s mg.klp = $kLaps mg.st run title @s title [{"text":"TOUR FINAL !","color":"gold","bold":true}]\n'
         'execute if score @s mg.klp = $kLaps mg.st if score $kfl mg.st matches 0 run function mg:kart/final_lap\n')
fn('final_lap', '''# Premier pilote dans le dernier tour : jingle pour tous, la musique accélère
scoreboard players set $kfl mg.st 1
execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bit record @s ~ ~ ~ 1 1
execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bit record @s ~ ~ ~ 1 1.26
execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bit record @s ~ ~ ~ 1 1.5
execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bell record @s ~ ~ ~ 0.8 2
''')
patch_fn('finish', 'execute at @s run playsound minecraft:entity.firework_rocket.twinkle master @a[tag=mg.play] ~ ~ ~ 1 1\n',
         'execute at @s run playsound minecraft:entity.firework_rocket.twinkle master @a[tag=mg.play] ~ ~ ~ 1 1\n'
         'execute at @s run playsound minecraft:ui.toast.challenge_complete record @s ~ ~ ~ 1 1\n'
         'execute if score @s mg.kfp matches 1 at @s run playsound minecraft:block.note_block.bell record @s ~ ~ ~ 1 2\n'
         'execute if score @s mg.kfp matches 1 at @s run playsound minecraft:block.note_block.bell record @s ~ ~ ~ 1 1.5\n'
         'execute if score @s mg.kfp matches 1 at @s run playsound minecraft:block.note_block.bell record @s ~ ~ ~ 1 1.26\n')
patch_fn('bat_tick', 'execute if score $ktime mg.st matches 3000 run tellraw', 'execute if score $ktime mg.st matches 3000 run function mg:kart/final_lap\nexecute if score $ktime mg.st matches 3000 run tellraw')

# ------------------------------------------------------------------ bouton « Je suis coincé » (/trigger mg.opt set 26, branché dans core/opt)
patch_fn('drive', 'function mg:kart/seat\n', 'function mg:kart/seat\nscoreboard players remove @s[scores={mg.kstk=1..}] mg.kstk 1\n'
         'execute if entity @s[tag=mg.kstuck] run function mg:kart/stuck\n')
fn('stuck', '''# Bouton « Je suis coincé » (@s = pilote, son kart est tagué mg.kk) : remis sur la route au point de passage précédent, recharge 5 s
tag @s remove mg.kstuck
execute if entity @s[tag=mg.kfin] run return 0
execute if score @s mg.kstk matches 1.. run return run tellraw @s [{"text":"⛑ Patiente encore un peu avant de redemander (5 s).","color":"red"}]
scoreboard players set @s mg.kstk 100
function mg:kart/rescue''')
s_go = open(os.path.join(K, 'go.mcfunction'), encoding='utf-8').read()
with open(os.path.join(K, 'go.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(s_go.rstrip('\n') + '\ntellraw @a[tag=mg.play] [{"text":"Coincé dans le décor ? ","color":"gray"},{"text":"[⛑ Je suis coincé]","color":"yellow","bold":true,'
            '"click_event":{"action":"run_command","command":"trigger mg.opt set 26"},"hover_event":{"action":"show_text","value":"Te remet sur la route au dernier point de passage '
            '(ou /trigger mg.opt set 26)"}},{"text":" (T pour ouvrir le chat, puis clique)","color":"dark_gray"}]\n')
