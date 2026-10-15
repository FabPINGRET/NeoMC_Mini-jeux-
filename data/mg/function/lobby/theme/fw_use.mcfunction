# 🎄 Étoile de feu d'artifice consommée (advancement mg:theme_fw ; @s = joueur) : fusée à 4 explosions de Noël, tirée au hasard
advancement revoke @s only mg:theme_fw
# budget épuisé (étoile de coffre ou ramassée) : consommée sans effet
execute unless score @s mg.thfw matches 1.. run return run title @s actionbar {"text":"🎄 Plus de feu d'artifice à lancer.","color":"gray"}
execute store success score $thf mg.st if block ~ ~2 ~ #mg:sky_clear if block ~ ~3 ~ #mg:sky_clear if block ~ ~4 ~ #mg:sky_clear if block ~ ~5 ~ #mg:sky_clear if block ~ ~6 ~ #mg:sky_clear if block ~ ~7 ~ #mg:sky_clear if block ~ ~8 ~ #mg:sky_clear if block ~ ~9 ~ #mg:sky_clear if block ~ ~10 ~ #mg:sky_clear if block ~ ~11 ~ #mg:sky_clear if block ~ ~12 ~ #mg:sky_clear if block ~ ~13 ~ #mg:sky_clear if block ~ ~14 ~ #mg:sky_clear
execute if score $thf mg.st matches 0 run title @s actionbar {"text":"🎄 À ciel ouvert !","color":"red"}
execute if score $thf mg.st matches 0 run return run function mg:lobby/theme/fw_back
# l'explosion (~10 blocs plus haut, rayon de dégâts 5) ne doit blesser personne
execute store success score $thf mg.st positioned ~ ~10 ~ if entity @a[distance=..6]
execute if score $thf mg.st matches 1 run title @s actionbar {"text":"🎄 Trop de monde autour !","color":"red"}
execute if score $thf mg.st matches 1 run return run function mg:lobby/theme/fw_back
scoreboard players remove @s mg.thfw 1
execute store result score $thr mg.st run random value 1..4
execute if score $thr mg.st matches 1 at @s run summon minecraft:firework_rocket ~ ~2 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"star",colors:[I;11743532],fade_colors:[I;16777215],has_trail:true}]}}}}
execute if score $thr mg.st matches 2 at @s run summon minecraft:firework_rocket ~ ~2 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"large_ball",colors:[I;3887386],fade_colors:[I;15790320],has_twinkle:true}]}}}}
execute if score $thr mg.st matches 3 at @s run summon minecraft:firework_rocket ~ ~2 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"burst",colors:[I;15790320],fade_colors:[I;12040119],has_twinkle:true}]}}}}
execute if score $thr mg.st matches 4 at @s run summon minecraft:firework_rocket ~ ~2 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"star",colors:[I;15435844],fade_colors:[I;11743532],has_trail:true,has_twinkle:true}]}}}}
