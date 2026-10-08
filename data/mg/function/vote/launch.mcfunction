# Admin (@s) : lance le jeu le plus voté (égalité : tirage au sort entre les ex æquo)
function mg:vote/refresh
execute if score $vn mg.st matches 0 run return run tellraw @s [{"text":"⚠ Aucun vote pour le moment.","color":"red"}]
execute unless score $state mg.st matches 0 run return run tellraw @s [{"text":"⚠ Une partie est déjà en cours.","color":"red"}]
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
scoreboard players set $vc mg.st 0
execute if score Spleef mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score TNT-Run mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score PvP mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score PvP-classes mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Bedwars mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Sheep-War mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Mob-Arena mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Splegg mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Sumo mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Dropper mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score TNT-Tag mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Block-Party mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Enclumes mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Turf-Wars mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Quakecraft mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Paintball mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score One-in-Chamber mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Course-glace mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Build-mots mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Build-maitre mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute if score Elytra mg.vb = $vmax mg.st run scoreboard players add $vc mg.st 1
execute store result score $vk mg.st run random value 0..9999
scoreboard players operation $vk mg.st %= $vc mg.st
scoreboard players add $vk mg.st 1
scoreboard players set $vwin mg.st 0
execute if score Spleef mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Spleef mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 1
execute if score TNT-Run mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score TNT-Run mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 2
execute if score PvP mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score PvP mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 3
execute if score PvP-classes mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score PvP-classes mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 4
execute if score Bedwars mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Bedwars mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 5
execute if score Sheep-War mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Sheep-War mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 6
execute if score Mob-Arena mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Mob-Arena mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 7
execute if score Splegg mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Splegg mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 8
execute if score Sumo mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Sumo mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 9
execute if score Dropper mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Dropper mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 10
execute if score TNT-Tag mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score TNT-Tag mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 11
execute if score Block-Party mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Block-Party mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 12
execute if score Enclumes mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Enclumes mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 13
execute if score Turf-Wars mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Turf-Wars mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 14
execute if score Quakecraft mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Quakecraft mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 15
execute if score Paintball mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Paintball mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 16
execute if score One-in-Chamber mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score One-in-Chamber mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 17
execute if score Course-glace mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Course-glace mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 18
execute if score Build-mots mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Build-mots mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 19
execute if score Build-maitre mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Build-maitre mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 20
execute if score Elytra mg.vb = $vmax mg.st run scoreboard players remove $vk mg.st 1
execute if score Elytra mg.vb = $vmax mg.st if score $vk mg.st matches 0 run scoreboard players set $vwin mg.st 21
execute if score $vwin mg.st matches 1 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"❄ Spleef","color":"aqua","bold":true},{"text":" ("},{"score":{"name":"Spleef","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 1 run scoreboard players set @s mg.go 1
execute if score $vwin mg.st matches 2 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"✷ TNT Run","color":"red","bold":true},{"text":" ("},{"score":{"name":"TNT-Run","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 2 run scoreboard players set @s mg.go 2
execute if score $vwin mg.st matches 3 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"⚔ Arène PvP","color":"yellow","bold":true},{"text":" ("},{"score":{"name":"PvP","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 3 run scoreboard players set @s mg.go 3
execute if score $vwin mg.st matches 4 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"⚔ PvP classes","color":"gold","bold":true},{"text":" ("},{"score":{"name":"PvP-classes","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 4 run scoreboard players set @s mg.go 13
execute if score $vwin mg.st matches 5 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"⚑ Bedwars","color":"light_purple","bold":true},{"text":" ("},{"score":{"name":"Bedwars","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 5 run scoreboard players set @s mg.go 4
execute if score $vwin mg.st matches 6 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"☁ Sheep War","color":"white","bold":true},{"text":" ("},{"score":{"name":"Sheep-War","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 6 run scoreboard players set @s mg.go 5
execute if score $vwin mg.st matches 7 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"☠ Mob Arena","color":"dark_green","bold":true},{"text":" ("},{"score":{"name":"Mob-Arena","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 7 run scoreboard players set @s mg.go 6
execute if score $vwin mg.st matches 8 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"❍ Splegg","color":"yellow","bold":true},{"text":" ("},{"score":{"name":"Splegg","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 8 run scoreboard players set @s mg.go 20
execute if score $vwin mg.st matches 9 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"✊ Sumo","color":"gold","bold":true},{"text":" ("},{"score":{"name":"Sumo","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 9 run scoreboard players set @s mg.go 22
execute if score $vwin mg.st matches 10 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"⬇ The Dropper","color":"aqua","bold":true},{"text":" ("},{"score":{"name":"Dropper","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 10 run scoreboard players set @s mg.go 23
execute if score $vwin mg.st matches 11 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"✹ TNT Tag","color":"red","bold":true},{"text":" ("},{"score":{"name":"TNT-Tag","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 11 run scoreboard players set @s mg.go 27
execute if score $vwin mg.st matches 12 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"▦ Block Party","color":"light_purple","bold":true},{"text":" ("},{"score":{"name":"Block-Party","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 12 run scoreboard players set @s mg.go 28
execute if score $vwin mg.st matches 13 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"⚓ Pluie d'Enclumes","color":"gray","bold":true},{"text":" ("},{"score":{"name":"Enclumes","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 13 run scoreboard players set @s mg.go 29
execute if score $vwin mg.st matches 14 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"▮ Turf Wars","color":"gold","bold":true},{"text":" ("},{"score":{"name":"Turf-Wars","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 14 run scoreboard players set @s mg.go 30
execute if score $vwin mg.st matches 15 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"⚡ Quakecraft","color":"aqua","bold":true},{"text":" ("},{"score":{"name":"Quakecraft","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 15 run scoreboard players set @s mg.go 31
execute if score $vwin mg.st matches 16 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"▓ Paintball","color":"gold","bold":true},{"text":" ("},{"score":{"name":"Paintball","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 16 run scoreboard players set @s mg.go 36
execute if score $vwin mg.st matches 17 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"➶ One in the Chamber","color":"gold","bold":true},{"text":" ("},{"score":{"name":"One-in-Chamber","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 17 run scoreboard players set @s mg.go 26
execute if score $vwin mg.st matches 18 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"⛵ Course de bateaux (glace)","color":"aqua","bold":true},{"text":" ("},{"score":{"name":"Course-glace","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 18 run scoreboard players set @s mg.go 56
execute if score $vwin mg.st matches 19 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"✎ Build Battle (thème aléatoire)","color":"green","bold":true},{"text":" ("},{"score":{"name":"Build-mots","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 19 run scoreboard players set @s mg.go 57
execute if score $vwin mg.st matches 20 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"✎ Build Battle (Maître du mot)","color":"dark_aqua","bold":true},{"text":" ("},{"score":{"name":"Build-maitre","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 20 run scoreboard players set @s mg.go 58
execute if score $vwin mg.st matches 21 run tellraw @a [{"text":"☑ Le vote désigne ","color":"gray"},{"text":"🪽 Élytra (mode au hasard)","color":"aqua","bold":true},{"text":" ("},{"score":{"name":"Elytra","objective":"mg.vb"},"color":"gold"},{"text":" vote(s)) !","color":"gray"}]
execute if score $vwin mg.st matches 21 run scoreboard players set @s mg.go 78
function mg:core/go
