# ================================================================== DÉPLACEMENT, COLLISIONS ET FILETS (exécuté à la fin de sound_part.py)
# Déplacement du kart (move : remontée, nez, montée de marche, rebond contre un mur, caméra) et rebond (bump).
# La sonde de move regarde (vitesse + 0,75) bloc devant le kart, soit 1,26 dès 51 de vitesse : un mur plus proche passe entre le kart et
# elle. move sonde donc aussi à mi-chemin (126.. = 51+ de vitesse, 176.. = 101+) un mur de 2 blocs de haut. Le plafond de vitesse est tenu
# par speed (Mini : accélération 7).
# Filets : kart enterré dans un mur (drive, course seulement) ou pilote qui appuie sur Z/S 10 s sans passer de point de passage (mg.kof) -> rescue.
CAM = '$execute at @s rotated $(h) 0 positioned ^ ^2.4 ^-5 rotated ~ 16 run tp @e[type=minecraft:item_display,tag=mg.kcamc,limit=1] ~ ~ ~ ~ ~'
WALL = 'unless block ~ ~ ~ #mg:kart_pass unless block ~ ~1 ~ #mg:kart_pass run return run function mg:kart/bump {v:$(v),h:$(h)}'
fn('move', f'''# @s = kart : remis sur la route s'il s'y est enfoncé, nez tourné, avance selon la trajectoire (rebond si mur), caméra
execute at @s unless block ~ ~ ~ #mg:kart_pass align y run tp @s ~ ~1 ~
$execute at @s run tp @s ~ ~ ~ ~$(t) 0
execute at @s on passengers unless entity @s[type=minecraft:player] run rotate @s ~ 0
$execute if score $kg mg.st matches 1 at @s rotated $(h) 0 positioned ^ ^0.5 ^$(c) unless block ~ ~ ~ #mg:kart_pass if block ~ ~1 ~ #mg:kart_pass at @s if block ~ ~1.5 ~ #mg:kart_pass run tp @s ~ ~1 ~
$execute at @s rotated $(h) 0 positioned ^ ^0.5 ^$(c) unless block ~ ~ ~ #mg:kart_pass run return run function mg:kart/bump {{v:$(v),h:$(h)}}
$execute if score $kc mg.st matches 126.. at @s rotated $(h) 0 positioned ^ ^0.5 ^$(c) positioned ^ ^ ^-0.5 {WALL}
$execute if score $kc mg.st matches 176.. at @s rotated $(h) 0 positioned ^ ^0.5 ^$(c) positioned ^ ^ ^-1 {WALL}
$execute at @s rotated $(h) 0 run tp @s ^ ^$(v) ^$(d)
{CAM}
''')
fn('bump', f'''$execute at @s run tp @s ~ ~$(v) ~
{CAM}
function mg:kart/bumped_owner
''')

# speed : l'accélération s'arrête au plafond $kmx (sans plafond, un kart dont l'accélération dépasse la décroissance de 6 accélérait sans fin)
patch_fn('speed', 'execute if score $kf mg.st matches 1 if score $kb mg.st matches 0 run scoreboard players operation @s mg.ksp += $kac mg.st\n',
         'scoreboard players set $kup mg.st 0\n'
         'execute if score $kf mg.st matches 1 if score $kb mg.st matches 0 if score @s mg.ksp < $kmx mg.st store success score $kup mg.st run scoreboard players operation @s mg.ksp += $kac mg.st\n'
         'execute if score $kup mg.st matches 1 run scoreboard players operation @s mg.ksp < $kmx mg.st\n')
# au-dessus du plafond (boost fini) : traîne de 6 par tick, ou de 6 - accélération si Z est tenu seul (l'ancien bilan, au moins 1 : le Mini
# ne doit plus accélérer au-dessus du plafond)
patch_fn('speed', 'execute if score @s mg.ksp > $kmx mg.st run scoreboard players remove @s mg.ksp 6\n',
         'scoreboard players set $kdc mg.st 6\n'
         'execute if score $kf mg.st matches 1 if score $kb mg.st matches 0 run scoreboard players operation $kdc mg.st -= $kac mg.st\n'
         'execute if score $kdc mg.st matches ..0 run scoreboard players set $kdc mg.st 1\n'
         'execute if score @s mg.ksp > $kmx mg.st run scoreboard players operation @s mg.ksp -= $kdc mg.st\n'
         'execute if score @s mg.ksp matches 151.. run scoreboard players set @s mg.ksp 150\n')

# drive : compteur mg.kof (ticks de Z ou S tenu depuis le dernier point de passage, course seulement), puis filets vers rescue
patch_fn('drive', 'execute unless entity @s[tag=mg.kfin] run function mg:kart/inputs\n',
         'execute unless entity @s[tag=mg.kfin] run function mg:kart/inputs\n'
         'execute if score $klob mg.st matches 0 if score $kbat mg.st matches 0 if score $kf mg.st matches 1 run scoreboard players add @s mg.kof 1\n'
         'execute if score $klob mg.st matches 0 if score $kbat mg.st matches 0 if score $kb mg.st matches 1 if score $kf mg.st matches 0 run scoreboard players add @s mg.kof 1\n')
patch_fn('drive', 'execute if score $kyy mg.st matches ..6000 run return run function mg:kart/rescue\n',
         'execute if score $kyy mg.st matches ..6000 run return run function mg:kart/rescue\n'
         'execute if score $kbat mg.st matches 0 if score $klob mg.st matches 0 at @e[type=minecraft:block_display,tag=mg.kk,limit=1] unless block ~ ~ ~ #mg:kart_pass unless block ~ ~1 ~ #mg:kart_pass run return run function mg:kart/rescue\n'
         'execute if score @s mg.kof matches 200.. run return run function mg:kart/rescue\n')
# remise à 0 de mg.kof : secours, point de passage franchi, préparation de la course
patch_fn('rescue', 'scoreboard players set @s mg.khi 0\n', 'scoreboard players set @s mg.khi 0\nscoreboard players set @s mg.kof 0\n')
patch_fn('cp_pass', 'scoreboard players add @s mg.kcp 1\n', 'scoreboard players add @s mg.kcp 1\nscoreboard players set @s mg.kof 0\n')
patch_fn('prepare', 'scoreboard players set @a[tag=mg.play] mg.kvm 1\n', 'scoreboard players set @a[tag=mg.play] mg.kvm 1\nscoreboard players set @a[tag=mg.play] mg.kof 0\n')
