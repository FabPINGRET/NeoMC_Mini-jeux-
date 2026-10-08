# Votes à la majorité (core/tick, toutes les secondes, lobby uniquement). Généré.
# Joueurs comptés : tous les joueurs connectés hors monde de survie. Il en faut 3 au moins.
execute unless score $state mg.st matches 0 run return run scoreboard players set $vat mg.st -1
execute if score $setup mg.st matches 0 run return 0
execute store result score $vnp mg.st if entity @a[tag=mg.init,tag=!mg.surv]
# recompte seulement si le nombre de joueurs a changé (un votant a pu partir) ; sinon les votes sont déjà à jour
execute unless score $vnp mg.st = $vnpo mg.st run function mg:vote/refresh
scoreboard players operation $vnpo mg.st = $vnp mg.st
scoreboard players set $vmax mg.st 0
scoreboard players operation $vmax mg.st > Spleef mg.vb
scoreboard players operation $vmax mg.st > TNT-Run mg.vb
scoreboard players operation $vmax mg.st > PvP mg.vb
scoreboard players operation $vmax mg.st > PvP-classes mg.vb
scoreboard players operation $vmax mg.st > Bedwars mg.vb
scoreboard players operation $vmax mg.st > Sheep-War mg.vb
scoreboard players operation $vmax mg.st > Mob-Arena mg.vb
scoreboard players operation $vmax mg.st > Splegg mg.vb
scoreboard players operation $vmax mg.st > Sumo mg.vb
scoreboard players operation $vmax mg.st > Dropper mg.vb
scoreboard players operation $vmax mg.st > TNT-Tag mg.vb
scoreboard players operation $vmax mg.st > Block-Party mg.vb
scoreboard players operation $vmax mg.st > Enclumes mg.vb
scoreboard players operation $vmax mg.st > Turf-Wars mg.vb
scoreboard players operation $vmax mg.st > Quakecraft mg.vb
scoreboard players operation $vmax mg.st > Paintball mg.vb
scoreboard players operation $vmax mg.st > One-in-Chamber mg.vb
scoreboard players operation $vmax mg.st > Course-glace mg.vb
scoreboard players operation $vmax mg.st > Build-mots mg.vb
scoreboard players operation $vmax mg.st > Build-maitre mg.vb
scoreboard players operation $vmax mg.st > Elytra mg.vb
scoreboard players operation $vm2 mg.st = $vmax mg.st
scoreboard players operation $vm2 mg.st += $vmax mg.st
scoreboard players set $vok mg.st 0
execute if score $vnp mg.st matches 3.. if score $vm2 mg.st > $vnp mg.st run scoreboard players set $vok mg.st 1
# Majorité perdue pendant le compte à rebours → annulé
execute if score $vok mg.st matches 0 if score $vat mg.st matches 1.. run tellraw @a[tag=!mg.surv] {"text":"☑ Plus de majorité : lancement automatique annulé.","color":"gray"}
execute if score $vok mg.st matches 0 run return run scoreboard players set $vat mg.st -1
scoreboard players set $vlead mg.st 0
execute if score Spleef mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 1
execute if score TNT-Run mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 2
execute if score PvP mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 3
execute if score PvP-classes mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 4
execute if score Bedwars mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 5
execute if score Sheep-War mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 6
execute if score Mob-Arena mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 7
execute if score Splegg mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 8
execute if score Sumo mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 9
execute if score Dropper mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 10
execute if score TNT-Tag mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 11
execute if score Block-Party mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 12
execute if score Enclumes mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 13
execute if score Turf-Wars mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 14
execute if score Quakecraft mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 15
execute if score Paintball mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 16
execute if score One-in-Chamber mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 17
execute if score Course-glace mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 18
execute if score Build-mots mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 19
execute if score Build-maitre mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 20
execute if score Elytra mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st 21
# Nouvelle majorité → compte à rebours
execute unless score $vat mg.st matches 1.. run scoreboard players set $vat mg.st 11
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 1 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"❄ Spleef","color":"aqua","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Spleef","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 2 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"✷ TNT Run","color":"red","bold":true},{"text":" (","color":"gray"},{"score":{"name":"TNT-Run","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 3 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"⚔ Arène PvP","color":"yellow","bold":true},{"text":" (","color":"gray"},{"score":{"name":"PvP","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 4 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"⚔ PvP classes","color":"gold","bold":true},{"text":" (","color":"gray"},{"score":{"name":"PvP-classes","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 5 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"⚑ Bedwars","color":"light_purple","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Bedwars","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 6 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"☁ Sheep War","color":"white","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Sheep-War","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 7 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"☠ Mob Arena","color":"dark_green","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Mob-Arena","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 8 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"❍ Splegg","color":"yellow","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Splegg","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 9 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"✊ Sumo","color":"gold","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Sumo","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 10 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"⬇ The Dropper","color":"aqua","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Dropper","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 11 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"✹ TNT Tag","color":"red","bold":true},{"text":" (","color":"gray"},{"score":{"name":"TNT-Tag","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 12 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"▦ Block Party","color":"light_purple","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Block-Party","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 13 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"⚓ Pluie d'Enclumes","color":"gray","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Enclumes","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 14 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"▮ Turf Wars","color":"gold","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Turf-Wars","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 15 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"⚡ Quakecraft","color":"aqua","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Quakecraft","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 16 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"▓ Paintball","color":"gold","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Paintball","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 17 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"➶ One in the Chamber","color":"gold","bold":true},{"text":" (","color":"gray"},{"score":{"name":"One-in-Chamber","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 18 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"⛵ Course de bateaux (glace)","color":"aqua","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Course-glace","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 19 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"✎ Build Battle (thème aléatoire)","color":"green","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Build-mots","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 20 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"✎ Build Battle (Maître du mot)","color":"dark_aqua","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Build-maitre","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
execute if score $vat mg.st matches 11 if score $vlead mg.st matches 21 run tellraw @a[tag=!mg.surv] [{"text":"☑ Majorité pour ","color":"green"},{"text":"🪽 Élytra (mode au hasard)","color":"aqua","bold":true},{"text":" (","color":"gray"},{"score":{"name":"Elytra","objective":"mg.vb"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$vnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs) : lancement dans 10 s !","color":"gray"}]
scoreboard players remove $vat mg.st 1
execute if score $vat mg.st matches 1..10 run title @a[tag=!mg.surv] actionbar [{"text":"☑ Jeu voté : lancement dans ","color":"green"},{"score":{"name":"$vat","objective":"mg.st"},"color":"gold","bold":true},{"text":" s","color":"green"}]
execute if score $vat mg.st matches 1..3 as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.5
execute if score $vat mg.st matches 0 run function mg:vote/auto_launch
