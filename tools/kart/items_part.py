
# ================================================================== OBJETS MARIO KART (v3)
# Les fonctions ci-dessous remplacent celles du même nom définies plus haut (la dernière écriture l'emporte).
ITEMS = {1: ('🍌 Banane', 'yellow'), 2: ('🟢 Carapace verte', 'green'), 3: ('🔴 Carapace rouge', 'red'),
         4: ('🍄 Champignon', 'gold'), 5: ('⭐ Étoile', 'yellow'), 6: ('⚡ Éclair', 'aqua'), 7: ('🔵 Carapace bleue', 'blue'),
         8: ('🍌 Triple bananes', 'yellow'), 9: ('🟢 Triple carapaces vertes', 'green'), 10: ('🔴 Triple carapaces rouges', 'red'),
         11: ('🍄 Triple champignons', 'gold'), 12: ('🌟 Champignon doré', 'gold'), 13: ('💣 Bob-omb', 'dark_gray'),
         14: ('🚀 Bill Balle', 'dark_red'), 15: ('🦑 Bloups', 'dark_purple'), 16: ('📯 Super klaxon', 'gold'),
         17: ('👻 Boo', 'white'), 18: ('❓ Fausse boîte', 'yellow'), 19: ('🍄 Méga champignon', 'red')}
MODEL = {1: 'minecraft:yellow_dye', 2: 'minecraft:turtle_scute', 3: 'minecraft:red_dye', 4: 'minecraft:red_mushroom',
         5: 'minecraft:nether_star', 6: 'minecraft:lightning_rod', 7: 'minecraft:heart_of_the_sea', 8: 'minecraft:yellow_dye',
         9: 'minecraft:turtle_scute', 10: 'minecraft:red_dye', 11: 'minecraft:red_mushroom', 12: 'minecraft:gold_nugget',
         13: 'minecraft:fire_charge', 14: 'minecraft:firework_rocket', 15: 'minecraft:ink_sac', 16: 'minecraft:goat_horn',
         17: 'minecraft:ghast_tear', 18: 'minecraft:yellow_stained_glass', 19: 'minecraft:red_mushroom_block'}
CHARGES = {8: 3, 9: 3, 10: 3, 11: 3}

# --- tirage : (seuil cumulé sur 100, objet) par tranche de classement
TIERS = {'tete': [(28, 1), (36, 8), (60, 2), (70, 18), (80, 4), (86, 16), (92, 13), (100, 3)],
         'milieu': [(8, 1), (22, 3), (32, 9), (42, 10), (54, 4), (64, 11), (72, 13), (82, 15), (89, 17), (94, 16), (100, 5)],
         'queue': [(15, 11), (30, 12), (45, 5), (60, 14), (70, 10), (80, 19), (87, 6), (92, 7), (96, 17), (100, 15)]}
roll = ['# Tirage selon la position (0 = premier, 100 = dernier) : la tête reçoit des objets de défense, la queue des objets puissants',
        'execute store result score $kr1 mg.st run random value 1..100',
        'scoreboard players operation $kf1 mg.st = @s mg.krk', 'scoreboard players remove $kf1 mg.st 1',
        'scoreboard players operation $kf1 mg.st *= #k100 mg.st', 'scoreboard players operation $kn1 mg.st = $kn mg.st',
        'scoreboard players remove $kn1 mg.st 1', 'execute if score $kn1 mg.st matches ..0 run scoreboard players set $kf1 mg.st 50',
        'execute if score $kn1 mg.st matches 1.. run scoreboard players operation $kf1 mg.st /= $kn1 mg.st']
for tier, rng in (('tete', '..33'), ('milieu', '34..66'), ('queue', '67..')):
    lo = 1
    for hi, item in TIERS[tier]:
        roll.append(f'execute if score $kf1 mg.st matches {rng} if score $kr1 mg.st matches {lo}..{hi} run scoreboard players set $kgv mg.st {item}')
        lo = hi + 1
roll += ['scoreboard players operation @s mg.kit = $kgv mg.st', 'function mg:kart/item_give']
fn('item_roll', '\n'.join(roll) + '\n')

give = ['# Objet en main (case 5, au milieu de la barre) ; Ctrl (ou clic droit en 1re personne) pour l\'utiliser ; charges et animations de départ']
for k, (name, color) in ITEMS.items():
    give.append(f'execute if score @s mg.kit matches {k} run item replace entity @s hotbar.4 with minecraft:warped_fungus_on_a_stick'
                f'[item_model="{MODEL[k]}",custom_name=[{{"text":"{name}","color":"{color}","bold":true,"italic":false}}],'
                f'lore=[[{{"text":"Clic droit pour l\'utiliser","color":"gray","italic":false}}]],unbreakable={{}}]')
    give.append(f'execute if score @s mg.kit matches {k} run title @s subtitle [{{"text":"{name}","color":"{color}","bold":true}}]')
give.append('scoreboard players set @s mg.kic 1')
for k, n in CHARGES.items():
    give.append(f'execute if score @s mg.kit matches {k} run scoreboard players set @s mg.kic {n}')
give += ['execute if score @s mg.kit matches 12 run scoreboard players set @s mg.kgd 150',
         'execute if score @s mg.kit matches 8..10 run function mg:kart/orb_make',
         'title @s title ""', 'execute at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.4']
fn('item_give', '\n'.join(give) + '\n')

fn('use_item', '''# Objet utilisé par @s (son kart porte mg.kk)
execute if score @s mg.kit matches 0 run return 0
scoreboard players operation $kuse mg.st = @s mg.kit
# objets à charges : on en consomme une, l'objet reste tant qu'il en reste
execute if score $kuse mg.st matches 8..11 run function mg:kart/use_charge
execute if score $kuse mg.st matches 12 run return run function mg:kart/use_golden
execute unless score $kuse mg.st matches 8..11 run scoreboard players set @s mg.kit 0
execute if score @s mg.kit matches 0 run clear @s minecraft:warped_fungus_on_a_stick
execute if score $kuse mg.st matches 1 run function mg:kart/use_banana
execute if score $kuse mg.st matches 2 run function mg:kart/use_shell {t:"mg.kgreen",c:3381555}
execute if score $kuse mg.st matches 3 run function mg:kart/use_shell {t:"mg.kred",c:13382451}
execute if score $kuse mg.st matches 4 run function mg:kart/use_mushroom
execute if score $kuse mg.st matches 5 run function mg:kart/use_star
execute if score $kuse mg.st matches 6 run function mg:kart/use_lightning
execute if score $kuse mg.st matches 7 run function mg:kart/use_blue
execute if score $kuse mg.st matches 8 run function mg:kart/use_banana
execute if score $kuse mg.st matches 9 run function mg:kart/use_shell {t:"mg.kgreen",c:3381555}
execute if score $kuse mg.st matches 10 run function mg:kart/use_shell {t:"mg.kred",c:13382451}
execute if score $kuse mg.st matches 11 run function mg:kart/use_mushroom
execute if score $kuse mg.st matches 13 run function mg:kart/use_bomb
execute if score $kuse mg.st matches 14 run function mg:kart/use_bill
execute if score $kuse mg.st matches 15 run function mg:kart/use_blooper
execute if score $kuse mg.st matches 16 run function mg:kart/use_horn
execute if score $kuse mg.st matches 17 run function mg:kart/use_boo
execute if score $kuse mg.st matches 18 run function mg:kart/use_fake
execute if score $kuse mg.st matches 19 run function mg:kart/use_mega
''')
fn('use_charge', f'''# Une charge en moins ; la dernière vide la main ; une banane ou une carapace en orbite disparaît
scoreboard players remove @s mg.kic 1
scoreboard players operation $kix mg.st = @s mg.kic
scoreboard players operation $me mg.st = @s mg.ri
execute as @e[type=minecraft:item_display,tag=mg.korb] if score @s mg.ri = $me mg.st if score @s mg.kdd = $kix mg.st run kill @s
execute if score @s mg.kic matches ..0 run scoreboard players set @s mg.kit 0
''')
fn('use_golden', '''# Champignon doré : un turbo à chaque appui tant que le chrono tourne
scoreboard players set @s mg.kbo 26
execute at @s run playsound minecraft:entity.firework_rocket.launch master @a[tag=mg.play,distance=..24] ~ ~ ~ 1 1.2
''')

# --- orbite des carapaces / bananes qui traînent
fn('orb_make', f'''# 3 objets autour du kart : carapaces en orbite (9, 10) ou bananes en file derrière (8)
scoreboard players operation $me mg.st = @s mg.ri
execute as @e[type=minecraft:item_display,tag=mg.korb] if score @s mg.ri = $me mg.st run kill @s
execute if score @s mg.kit matches 8 run function mg:kart/orb_summon {{i:0,t:"mg.korbb",item:'{{id:"minecraft:yellow_dye"}}',s:1.1f}}
execute if score @s mg.kit matches 8 run function mg:kart/orb_summon {{i:1,t:"mg.korbb",item:'{{id:"minecraft:yellow_dye"}}',s:1.1f}}
execute if score @s mg.kit matches 8 run function mg:kart/orb_summon {{i:2,t:"mg.korbb",item:'{{id:"minecraft:yellow_dye"}}',s:1.1f}}
execute if score @s mg.kit matches 9 run function mg:kart/orb_summon {{i:0,t:"mg.korbs",item:'{{id:"minecraft:leather_helmet",components:{{"minecraft:dyed_color":3381555}}}}',s:0.6f}}
execute if score @s mg.kit matches 9 run function mg:kart/orb_summon {{i:1,t:"mg.korbs",item:'{{id:"minecraft:leather_helmet",components:{{"minecraft:dyed_color":3381555}}}}',s:0.6f}}
execute if score @s mg.kit matches 9 run function mg:kart/orb_summon {{i:2,t:"mg.korbs",item:'{{id:"minecraft:leather_helmet",components:{{"minecraft:dyed_color":3381555}}}}',s:0.6f}}
execute if score @s mg.kit matches 10 run function mg:kart/orb_summon {{i:0,t:"mg.korbs",item:'{{id:"minecraft:leather_helmet",components:{{"minecraft:dyed_color":13382451}}}}',s:0.6f}}
execute if score @s mg.kit matches 10 run function mg:kart/orb_summon {{i:1,t:"mg.korbs",item:'{{id:"minecraft:leather_helmet",components:{{"minecraft:dyed_color":13382451}}}}',s:0.6f}}
execute if score @s mg.kit matches 10 run function mg:kart/orb_summon {{i:2,t:"mg.korbs",item:'{{id:"minecraft:leather_helmet",components:{{"minecraft:dyed_color":13382451}}}}',s:0.6f}}
''')
fn('orb_summon', f'''$execute at @s run summon minecraft:item_display ~ ~ ~ {{Tags:["mg.korb","$(t)","mg.korbn","mg.fx"],teleport_duration:2,item:$(item),transformation:{{translation:[0f,0f,0f],{T0},scale:[$(s),$(s),$(s)]}}}}
scoreboard players operation @e[type=minecraft:item_display,tag=mg.korbn] mg.ri = @s mg.ri
$scoreboard players set @e[type=minecraft:item_display,tag=mg.korbn] mg.kdd $(i)
tag @e[tag=mg.korbn] remove mg.korbn
''')
fn('orbs', '''# Place les objets en orbite / en file du pilote @s autour de son kart (mg.kk)
scoreboard players operation $kob mg.st = $ktime mg.st
scoreboard players operation $kob mg.st *= #k12 mg.st
execute as @e[type=minecraft:item_display,tag=mg.korb] if score @s mg.ri = $me mg.st run function mg:kart/orb_place
''')
fn('orb_place', '''scoreboard players operation $ka2 mg.st = @s mg.kdd
scoreboard players operation $ka2 mg.st *= #k120 mg.st
scoreboard players operation $ka2 mg.st += $kob mg.st
execute store result storage mg:kart o.a int 1 run scoreboard players get $ka2 mg.st
scoreboard players operation $kb2 mg.st = @s mg.kdd
scoreboard players operation $kb2 mg.st *= #k65 mg.st
scoreboard players add $kb2 mg.st 120
execute store result storage mg:kart o.b double 0.01 run scoreboard players get $kb2 mg.st
execute if entity @s[tag=mg.korbs] run function mg:kart/orb_spin with storage mg:kart o
execute if entity @s[tag=mg.korbb] run function mg:kart/orb_trail with storage mg:kart o
''')
fn('orb_spin', '$execute at @e[type=minecraft:block_display,tag=mg.kk,limit=1] rotated $(a) 0 positioned ^ ^0.45 ^1.25 run tp @s ~ ~ ~ ~ 0\n')
fn('orb_trail', '$execute at @e[type=minecraft:block_display,tag=mg.kk,limit=1] rotated ~ 0 positioned ^ ^0.25 ^-$(b) run tp @s ~ ~ ~\n')
fn('orb_block', '''# Carapace stoppée par un objet en orbite (@s = orbite la plus proche) : les deux disparaissent, le pilote perd une charge
scoreboard players operation $ko mg.st = @s mg.ri
execute as @a[tag=mg.play] if score @s mg.ri = $ko mg.st run function mg:kart/orb_lost
kill @s
kill @e[type=minecraft:item_display,tag=mg.kcur]
''')
fn('orb_lost', '''scoreboard players remove @s mg.kic 1
execute if score @s mg.kic matches ..0 run scoreboard players set @s mg.kit 0
execute if score @s mg.kit matches 0 run clear @s minecraft:warped_fungus_on_a_stick
''')

# --- Bob-omb
fn('use_bomb', f'''execute as {KK} at @s rotated ~ 0 positioned ^ ^1 ^1.8 run summon minecraft:item_display ~ ~ ~ {{Tags:["mg.kbomb","mg.knew","mg.fx"],teleport_duration:1,item:{{id:"minecraft:black_concrete"}},transformation:{{translation:[0f,0f,0f],{T0},scale:[0.6f,0.6f,0.6f]}}}}
execute as {KK} at @s rotated ~ 0 positioned ^ ^1 ^1.8 as @e[type=minecraft:item_display,tag=mg.knew] run tp @s ~ ~ ~ ~ 0
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.t 60
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.kvy 5
tag @e[type=minecraft:item_display,tag=mg.knew] remove mg.knew
execute at @s run playsound minecraft:entity.snowball.throw master @a[tag=mg.play,distance=..16] ~ ~ ~ 1 0.5
''')
fn('bomb_tick', f'''# Bob-omb (@s) : vol en cloche, se pose, clignote, explose au contact ou à la fin de la mèche
scoreboard players remove @s mg.t 1
execute if score @s mg.t matches ..0 run return run function mg:kart/bomb_boom
execute if score @s mg.kvy matches 1.. run scoreboard players remove @s mg.kvy 1
execute unless entity @s[tag=mg.kland] if score @s mg.kvy matches 1.. run tp @s ^ ^0.35 ^1.0
execute unless entity @s[tag=mg.kland] if score @s mg.kvy matches 0 run tp @s ^ ^-0.45 ^0.8
execute unless entity @s[tag=mg.kland] at @s unless block ~ ~-0.3 ~ #mg:kart_pass run tag @s add mg.kland
particle minecraft:small_flame ~ ~0.45 ~ 0.03 0.03 0.03 0 1
scoreboard players operation $kbl mg.st = @s mg.t
scoreboard players operation $kbl mg.st %= #k8 mg.st
execute if score $kbl mg.st matches 0 run item replace entity @s contents with minecraft:red_concrete
execute if score $kbl mg.st matches 4 run item replace entity @s contents with minecraft:black_concrete
execute if score @s mg.t matches ..50 if entity {KART},distance=..1.8] run function mg:kart/bomb_boom
''')
fn('bomb_boom', f'''particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1
playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..40] ~ ~ ~ 1 0.9
execute as {KART},distance=..4.5] run function mg:kart/owner_hit
kill @s
''')

# --- Bill Balle (la fusée) : le kart se pilote seul le long des points de passage
fn('use_bill', f'''scoreboard players set @s mg.kbill 100
scoreboard players set @s mg.kdr 0
execute at {KK} run summon minecraft:block_display ~ ~ ~ {{Tags:["mg.kbillm","mg.kbilln","mg.kpart","mg.fx"],teleport_duration:2,block_state:{{Name:"minecraft:coal_block"}},transformation:{{translation:[-0.75f,0.1f,-1.3f],{T0},scale:[1.5f,1.3f,2.6f]}}}}
ride @e[type=minecraft:block_display,tag=mg.kbilln,limit=1] mount {KK}
execute as {KK} at @s on passengers run rotate @s ~ 0
tag @e[tag=mg.kbilln] remove mg.kbilln
title @s actionbar [{{"text":"🚀 BILL BALLE !","color":"dark_red","bold":true}}]
execute at @s run playsound minecraft:entity.firework_rocket.large_blast master @a[tag=mg.play,distance=..30] ~ ~ ~ 1 0.6
''')
fn('bill_move', f'''# Bill Balle : vers le prochain point de passage, vite, sans gravité ; renverse les karts touchés
scoreboard players operation $ki mg.st = @s mg.kcp
execute as {KK} at @s run function mg:kart/bill_step
execute as {KK} at @s on passengers unless entity @s[type=minecraft:player] run rotate @s ~ 0
execute as {KK} at @s rotated ~ 0 positioned ^ ^2.6 ^-5.5 rotated ~ 16 run tp @e[type=minecraft:item_display,tag=mg.kcamc,limit=1] ~ ~ ~ ~ ~
execute as {KK} at @s rotated ~ 0 positioned ^ ^0.6 ^-1.6 run particle minecraft:flame ~ ~ ~ 0.2 0.2 0.2 0.05 8
execute as {KK} at @s rotated ~ 0 positioned ^ ^0.6 ^-2 run particle minecraft:large_smoke ~ ~ ~ 0.2 0.2 0.2 0.02 3
execute as {KK} at @s as {KART},tag=!mg.kk,distance=..2.4] run function mg:kart/owner_hit
execute store result score @s mg.khd run data get entity {KK} Rotation[0] 10
scoreboard players set @s mg.ksp 100
scoreboard players set @s mg.kvy 0
''')
fn('bill_end', f'''scoreboard players operation $me mg.st = @s mg.ri
execute as {KK} on passengers if entity @s[tag=mg.kbillm] run kill @s
title @s actionbar [{{"text":"Fin du Bill Balle","color":"gray"}}]
''')

# --- Bloups, Super klaxon, Boo, fausse boîte, méga champignon
fn('use_blooper', '''# Bloups : encre sur tous les pilotes devant soi
scoreboard players operation $kme mg.st = @s mg.krk
execute as @a[tag=mg.play] if score @s mg.krk < $kme mg.st run function mg:kart/inked
tellraw @a[tag=mg.play] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" envoie Bloups 🦑 sur les premiers !","color":"dark_purple"}]
''')
fn('inked', f'''effect give @s minecraft:blindness 3 0 true
title @s title [{{"text":"🦑","color":"dark_purple"}}]
title @s subtitle [{{"text":"De l'encre partout !","color":"dark_purple"}}]
scoreboard players operation $kh mg.st = @s mg.ri
execute as {KART}] if score @s mg.ri = $kh mg.st at @s run particle minecraft:squid_ink ~ ~1 ~ 0.5 0.5 0.5 0.1 40
execute at @s run playsound minecraft:entity.squid.squirt master @s ~ ~ ~ 1 1
''')
fn('use_horn', f'''# Super klaxon : onde de choc, détruit les objets proches (même la carapace bleue), renverse les karts proches
execute as {KK} at @s run particle minecraft:sonic_boom ~ ~0.8 ~ 0 0 0 0 1
execute as {KK} at @s run particle minecraft:cloud ~ ~0.5 ~ 2.5 0.3 2.5 0.15 60
execute at {KK} run playsound minecraft:item.goat_horn.sound.0 master @a[tag=mg.play,distance=..40] ~ ~ ~ 1 1
execute at {KK} run kill @e[type=minecraft:item_display,tag=mg.kshell,distance=..5.5]
execute at {KK} run kill @e[type=minecraft:item_display,tag=mg.kban,distance=..5.5]
execute at {KK} run kill @e[type=minecraft:item_display,tag=mg.kbomb,distance=..5.5]
execute at {KK} run kill @e[type=minecraft:item_display,tag=mg.kblue,distance=..6]
execute at {KK} run kill @e[type=minecraft:item_display,tag=mg.kfake,distance=..5.5]
execute as {KK} at @s as {KART},tag=!mg.kk,distance=..5] run function mg:kart/owner_hit
''')
fn('use_boo', '''# Boo : vole l'objet d'un adversaire au hasard et rend intouchable 4 s
scoreboard players set @s mg.kboo 80
tag @s add mg.kme
execute as @a[tag=mg.play,tag=!mg.kme,scores={mg.kit=1..},sort=random,limit=1] run tag @s add mg.kvic
tag @s remove mg.kme
execute if entity @a[tag=mg.kvic] run scoreboard players operation @s mg.kit = @a[tag=mg.kvic,limit=1] mg.kit
execute if entity @a[tag=mg.kvic] run function mg:kart/item_give
execute if entity @a[tag=mg.kvic] run tellraw @a[tag=mg.play] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" vole l'objet de ","color":"gray"},{"selector":"@a[tag=mg.kvic]","color":"yellow"},{"text":" 👻","color":"white"}]
execute as @a[tag=mg.kvic] run function mg:kart/robbed
tag @a remove mg.kvic
title @s actionbar [{"text":"👻 Intouchable !","color":"white","bold":true}]
execute at @s run playsound minecraft:entity.vex.ambient master @a[tag=mg.play,distance=..24] ~ ~ ~ 1 0.6
''')
fn('robbed', '''scoreboard players set @s mg.kit 0
scoreboard players set @s mg.kic 0
scoreboard players operation $me mg.st = @s mg.ri
execute as @e[type=minecraft:item_display,tag=mg.korb] if score @s mg.ri = $me mg.st run kill @s
clear @s minecraft:warped_fungus_on_a_stick
title @s actionbar [{"text":"👻 Boo t'a volé ton objet !","color":"white"}]
''')
fn('use_fake', f'''execute as {KK} at @s rotated ~ 0 positioned ^ ^1 ^-2.6 run summon minecraft:item_display ~ ~ ~ {{Tags:["mg.kfake","mg.kspin","mg.fx"],item:{{id:"minecraft:yellow_stained_glass"}},transformation:{{translation:[0f,0f,0f],{T0},scale:[1.1f,1.1f,1.1f]}},interpolation_duration:4}}
execute as {KK} at @s rotated ~ 0 positioned ^ ^0.7 ^-2.6 run summon minecraft:text_display ~ ~ ~ {{Tags:["mg.kfakeq","mg.fx"],billboard:"center",text:[{{"text":"?","color":"gold","bold":true}}],background:0,transformation:{{translation:[0f,0f,0f],{T0},scale:[1.5f,1.5f,1.5f]}}}}
execute at @s run playsound minecraft:block.glass.place master @a[tag=mg.play,distance=..16] ~ ~ ~ 1 1
''')
fn('fake_tick', f'''execute if score @s mg.t matches 1.. run return run scoreboard players remove @s mg.t 1
tag @s add mg.kcur
execute as {KART},distance=..1.8,limit=1,sort=nearest] run function mg:kart/fake_hit
tag @s remove mg.kcur
''')
fn('fake_hit', '''function mg:kart/owner_hit
execute at @e[type=minecraft:item_display,tag=mg.kcur,limit=1] run kill @e[type=minecraft:text_display,tag=mg.kfakeq,distance=..1.5]
execute at @e[type=minecraft:item_display,tag=mg.kcur,limit=1] run particle minecraft:wax_off ~ ~0.5 ~ 0.4 0.4 0.4 0 15
kill @e[type=minecraft:item_display,tag=mg.kcur]
''')
MEGA = 1.7
def tf(tr, sc, f):
    return 'translation:[%sf,%sf,%sf],%s,scale:[%sf,%sf,%sf]' % (*[ks(v * f) for v in tr], T0, *[ks(v * f) for v in sc])
mega_on = ['# Méga champignon : le kart grossit (animation de 8 ticks), invincible, écrase les karts touchés',
           'scoreboard players set @s mg.kmg 160',
           f'data merge entity {KK} {{start_interpolation:0,interpolation_duration:8,transformation:{{{tf(*ROOT, MEGA)}}}}}']
mega_off = ['# Fin du méga champignon : retour à la taille normale (animation)',
            f'data merge entity {KK} {{start_interpolation:0,interpolation_duration:8,transformation:{{{tf(*ROOT, 1)}}}}}']
for block, tr, sc, tag in PARTS:
    mega_on.append(f'execute as {KK} on passengers if entity @s[tag={tag}] run data merge entity @s {{start_interpolation:0,interpolation_duration:8,transformation:{{{tf(tr, sc, MEGA)}}}}}')
    mega_off.append(f'execute as {KK} on passengers if entity @s[tag={tag}] run data merge entity @s {{start_interpolation:0,interpolation_duration:8,transformation:{{{tf(tr, sc, 1)}}}}}')
mega_on += [f'execute as {KK} on passengers if entity @s[tag=mg.khead] run data merge entity @s {{start_interpolation:0,interpolation_duration:8,transformation:{{translation:[0f,1.05f,-0.15f],{T0},scale:[1.25f,1.25f,1.25f]}}}}',
            'title @s actionbar [{"text":"🍄 MÉGA !","color":"red","bold":true}]',
            'execute at @s run playsound minecraft:entity.player.levelup master @a[tag=mg.play,distance=..30] ~ ~ ~ 1 0.5']
mega_off += [f'execute as {KK} on passengers if entity @s[tag=mg.khead] run data merge entity @s {{start_interpolation:0,interpolation_duration:8,transformation:{{translation:[0f,0.62f,-0.1f],{T0},scale:[0.75f,0.75f,0.75f]}}}}',
             'execute at @s run playsound minecraft:entity.player.levelup master @a[tag=mg.play,distance=..30] ~ ~ ~ 0.7 1.6']
fn('use_mega', '\n'.join(mega_on) + '\n')
fn('mega_end', '\n'.join(mega_off) + '\n')
fn('mega_touch', f'''execute as {KK} at @s as {KART},tag=!mg.kk,distance=..2.6] run function mg:kart/owner_hit
''')

# --- touché : immunités (étoile, méga, Bill Balle, Boo)
fn('hit', f'''# @s touché : tête-à-queue (2 tours), sauf en étoile, méga, Bill Balle ou Boo
execute if score @s mg.kst matches 1.. run return 0
execute if score @s mg.kmg matches 1.. run return 0
execute if score @s mg.kbill matches 1.. run return 0
execute if score @s mg.kboo matches 1.. run return 0
scoreboard players set @s mg.khi 20
scoreboard players set @s mg.kbo 0
scoreboard players set @s mg.kdr 0
scoreboard players set @s mg.krc 0
title @s actionbar [{{"text":"💥 Touché !","color":"red","bold":true}}]
scoreboard players operation $kh mg.st = @s mg.ri
execute as {KART}] if score @s mg.ri = $kh mg.st at @s run particle minecraft:explosion ~ ~0.5 ~ 0.3 0.3 0.3 0 2
execute as {KART}] if score @s mg.ri = $kh mg.st at @s run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..24] ~ ~ ~ 0.4 1.6
''')

# --- vitesse : méga champignon un peu plus rapide
fn('speed', '''# Vitesse (centièmes de bloc par tick) : 100 sur la route, 45 dans l'herbe, 115 en méga, 125 en étoile, 150 en boost
scoreboard players set $kmx mg.st 100
execute if score $kro mg.st matches 0 if score $kg mg.st matches 1 run scoreboard players set $kmx mg.st 45
execute if score @s mg.kmg matches 1.. run scoreboard players set $kmx mg.st 115
execute if score @s mg.kst matches 1.. run scoreboard players set $kmx mg.st 125
execute if score @s mg.kbo matches 1.. run scoreboard players set $kmx mg.st 150
execute if score @s mg.khi matches 1.. run return run function mg:kart/speed_hit

execute if score $kf mg.st matches 1 if score $kb mg.st matches 0 run scoreboard players add @s mg.ksp 5
execute if score $kb mg.st matches 1 if score $kf mg.st matches 0 if score @s mg.ksp matches 1.. run scoreboard players remove @s mg.ksp 10
execute if score $kb mg.st matches 1 if score $kf mg.st matches 0 if score @s mg.ksp matches ..0 run scoreboard players remove @s mg.ksp 3
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches 3.. run scoreboard players remove @s mg.ksp 2
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches ..-3 run scoreboard players add @s mg.ksp 2
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches -2..2 run scoreboard players set @s mg.ksp 0
execute if score @s mg.kbo matches 1.. if score @s mg.ksp < $kmx mg.st run scoreboard players operation @s mg.ksp = $kmx mg.st
execute if score @s mg.ksp > $kmx mg.st run scoreboard players remove @s mg.ksp 6
execute if score @s mg.ksp matches ..-36 run scoreboard players set @s mg.ksp -35
''')

# --- pilotage : chronos des objets, Bill Balle, orbites, effets
fn('drive', f'''# Pilotage du kart de @s (chaque tick)
function mg:kart/kk
execute unless entity @e[tag=mg.kk] at @s run function mg:kart/kart_new
execute unless entity @e[tag=mg.kk] run function mg:kart/kk
execute if score @s mg.kv matches 1.. run function mg:kart/view_cmd
function mg:kart/seat
execute as {KK} at @s run function mg:kart/probe
execute if score $kg mg.st matches 0 if score @s mg.kvy matches ..0 as {KK} at @s unless block ~ ~-1.2 ~ #mg:kart_pass run function mg:kart/step_down

scoreboard players set $kf mg.st 0
scoreboard players set $kb mg.st 0
scoreboard players set $kl mg.st 0
scoreboard players set $kr mg.st 0
scoreboard players set $kj mg.st 0
scoreboard players set $ks mg.st 0
execute unless entity @s[tag=mg.kfin] run function mg:kart/inputs

# Objet : clic droit (vue assise) ou Ctrl (caméra de poursuite)
scoreboard players set $kuse mg.st 0
execute if score @s mg.qs matches 1.. run scoreboard players set $kuse mg.st 1
execute if score $ks mg.st matches 1 unless score @s mg.kspr matches 1 run scoreboard players set $kuse mg.st 1
scoreboard players operation @s mg.kspr = $ks mg.st
scoreboard players reset @s mg.qs
execute if score $kuse mg.st matches 1 run function mg:kart/use_item

# Chronos des objets
scoreboard players remove @s[scores={{mg.kbo=1..}}] mg.kbo 1
scoreboard players remove @s[scores={{mg.kst=1..}}] mg.kst 1
scoreboard players remove @s[scores={{mg.kboo=1..}}] mg.kboo 1
execute if score @s mg.kmg matches 1 run function mg:kart/mega_end
scoreboard players remove @s[scores={{mg.kmg=1..}}] mg.kmg 1
execute if score @s mg.kgd matches 1 run function mg:kart/golden_end
scoreboard players remove @s[scores={{mg.kgd=1..}}] mg.kgd 1
execute if score @s mg.kit matches 8..10 run function mg:kart/orbs
execute if score @s mg.kboo matches 1.. as {KK} at @s run particle minecraft:white_ash ~ ~0.8 ~ 0.6 0.5 0.6 0 6

# Bill Balle : pilote automatique
execute if score @s mg.kbill matches 1 run function mg:kart/bill_end
execute if score @s mg.kbill matches 1.. run scoreboard players remove @s mg.kbill 1
execute if score @s mg.kbill matches 1.. run function mg:kart/bill_move
execute if score @s mg.kbill matches 1.. unless entity @s[tag=mg.kfin] run return run function mg:kart/cp_check

execute if score $kwa mg.st matches 1 run return run function mg:kart/rescue
execute if score $kyy mg.st matches ..6000 run return run function mg:kart/rescue

function mg:kart/speed
function mg:kart/steer
function mg:kart/heading
function mg:kart/vertical
execute if score $kbp mg.st matches 1 if score $kg mg.st matches 1 run function mg:kart/boost_pad
execute if score @s mg.kst matches 1.. run function mg:kart/star_touch
execute if score @s mg.kmg matches 1.. run function mg:kart/mega_touch

execute store result storage mg:kart m.d double 0.01 run scoreboard players get @s mg.ksp
scoreboard players operation $kc mg.st = @s mg.ksp
execute if score @s mg.ksp matches 0.. run scoreboard players add $kc mg.st 75
execute if score @s mg.ksp matches ..-1 run scoreboard players remove $kc mg.st 75
execute store result storage mg:kart m.c double 0.01 run scoreboard players get $kc mg.st
execute store result storage mg:kart m.t double 0.1 run scoreboard players get $kt mg.st
execute store result storage mg:kart m.h double 0.1 run scoreboard players get @s mg.khd
execute store result storage mg:kart m.v double 0.01 run scoreboard players get $kv mg.st
execute as {KK} run function mg:kart/move with storage mg:kart m
function mg:kart/fx
execute unless entity @s[tag=mg.kfin] run function mg:kart/cp_check
''')
fn('golden_end', '''execute if score @s mg.kit matches 12 run clear @s minecraft:warped_fungus_on_a_stick
execute if score @s mg.kit matches 12 run scoreboard players set @s mg.kit 0
''')

# --- tick : nouveaux objets au sol / en l'air
fn('tick', f'''# Kart (état 2, jeu 61)
scoreboard players add $ktime mg.st 1
function mg:kart/track_tick
scoreboard players enable @a[tag=mg.play] mg.kv
execute as @a[tag=mg.play] run function mg:kart/drive
tag @e[tag=mg.kk] remove mg.kk
tag @e[tag=mg.kcamc] remove mg.kcamc

execute as @e[type=minecraft:item_display,tag=mg.kbox,tag=!mg.kboff] at @s if entity {KART},distance=..2.3] run function mg:kart/box_hit
execute as @e[type=minecraft:item_display,tag=mg.kboff] run function mg:kart/box_wait
execute as @e[type=minecraft:item_display,tag=mg.kshell] at @s run function mg:kart/shell_tick
execute as @e[type=minecraft:item_display,tag=mg.kban] at @s run function mg:kart/banana_tick
execute as @e[type=minecraft:item_display,tag=mg.kblue] at @s run function mg:kart/blue_tick
execute as @e[type=minecraft:item_display,tag=mg.kbomb] at @s run function mg:kart/bomb_tick
execute as @e[type=minecraft:item_display,tag=mg.kfake] at @s run function mg:kart/fake_tick

scoreboard players add $kph mg.st 1
execute if score $kph mg.st matches 4.. run function mg:kart/every4

execute store result score $kn mg.st if entity @a[tag=mg.play]
execute store result score $kfn mg.st if entity @a[tag=mg.play,tag=mg.kfin]
execute if score $kn mg.st matches 1.. if score $kfn mg.st = $kn mg.st run return run function mg:kart/end
execute if score $kend mg.st matches 1.. if score $ktime mg.st >= $kend mg.st run return run function mg:kart/end
execute if score $ktime mg.st matches 8400.. run return run function mg:kart/end
execute unless entity @a[tag=mg.play] run function mg:core/draw
''')
fn('every4', '''scoreboard players set $kph mg.st 0
scoreboard players add $kbr mg.st 1
execute if score $kbr mg.st matches 4.. run scoreboard players set $kbr mg.st 0
execute if score $kbr mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.kspin] run data merge entity @s {start_interpolation:0,interpolation_duration:4,transformation:{left_rotation:{angle:0f,axis:[0f,1f,0f]}}}
execute if score $kbr mg.st matches 1 as @e[type=minecraft:item_display,tag=mg.kspin] run data merge entity @s {start_interpolation:0,interpolation_duration:4,transformation:{left_rotation:{angle:1.5708f,axis:[0f,1f,0f]}}}
execute if score $kbr mg.st matches 2 as @e[type=minecraft:item_display,tag=mg.kspin] run data merge entity @s {start_interpolation:0,interpolation_duration:4,transformation:{left_rotation:{angle:3.1416f,axis:[0f,1f,0f]}}}
execute if score $kbr mg.st matches 3 as @e[type=minecraft:item_display,tag=mg.kspin] run data merge entity @s {start_interpolation:0,interpolation_duration:4,transformation:{left_rotation:{angle:4.7124f,axis:[0f,1f,0f]}}}
execute as @a[tag=mg.play] run function mg:kart/progress
execute as @a[tag=mg.play] run function mg:kart/rank_one
execute as @a[tag=mg.play] run function mg:kart/hud
function mg:kart/minimap
''')
fn('shell_tick', f'''# Carapace (@s) : avance, rebondit ou éclate contre un mur, stoppée par une orbite, touche un kart
scoreboard players remove @s mg.t 1
execute if score @s mg.t matches ..0 run return run kill @s
scoreboard players remove @s[scores={{mg.kbo=1..}}] mg.kbo 1
execute if entity @s[tag=mg.kred] unless score @s mg.kdd matches -1 run function mg:kart/shell_aim
execute positioned ^ ^ ^1.4 unless block ~ ~ ~ #mg:kart_pass run return run function mg:kart/shell_wall
tp @s ^ ^ ^1.4
particle minecraft:crit ~ ~0.2 ~ 0.1 0.1 0.1 0 1
execute if score @s mg.kbo matches 1.. run return 0
tag @s add mg.kcur
execute as @e[type=minecraft:item_display,tag=mg.korbs,distance=..1.3,limit=1,sort=nearest] run function mg:kart/orb_block
execute if entity @s[tag=mg.kcur] as {KART},distance=..1.7,limit=1,sort=nearest] run function mg:kart/shell_hit
tag @s remove mg.kcur
''')

# --- barre du bas : charges pour les objets multiples
hud = ['# Barre du bas : tour, position, objet (et charges), vitesse',
       'scoreboard players operation $kmh mg.st = @s mg.ksp',
       'scoreboard players operation $kmh mg.st *= #kkmh mg.st',
       'scoreboard players operation $kmh mg.st /= #k100 mg.st',
       'execute if score $kmh mg.st matches ..-1 run scoreboard players operation $kmh mg.st *= #km1 mg.st',
       'execute store result score $kpl mg.st run scoreboard players get @s mg.klp',
       'execute if score $kpl mg.st matches ..0 run scoreboard players set $kpl mg.st 1',
       'execute if score $kpl mg.st > $kLaps mg.st run scoreboard players operation $kpl mg.st = $kLaps mg.st']
hud.append(f'execute unless score @s mg.khi matches 1.. if score @s mg.kit matches 0 run title @s actionbar [{base},{{"text":"(pas d\'objet)","color":"dark_gray"}}{tail}]')
for k, (name, color) in ITEMS.items():
    extra = ',{"text":" ×","color":"gray"},{"score":{"name":"@s","objective":"mg.kic"},"color":"white","bold":true}' if k in CHARGES else ''
    hud.append(f'execute unless score @s mg.khi matches 1.. if score @s mg.kit matches {k} run title @s actionbar [{base},{{"text":"{name}","color":"{color}","bold":true}}{extra},{{"text":" (clic droit)","color":"gray"}}{tail}]')
fn('hud', '\n'.join(hud) + '\n')

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rp_part.py'), encoding='utf-8').read())
