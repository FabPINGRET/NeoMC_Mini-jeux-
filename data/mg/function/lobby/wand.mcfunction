# Baguette feu d'artifice (@s = joueur, position = joueur)
scoreboard players reset @s mg.fw
# l'objet est consommé par le clic : on le redonne
execute unless items entity @s hotbar.* minecraft:blaze_rod run item replace entity @s hotbar.1 with minecraft:blaze_rod[custom_name=[{"text":"✦ Baguette feu d'artifice","color":"gold","bold":true,"italic":false}],lore=[{"text":"Clic droit : feu d'artifice dans le ciel","color":"gray","italic":false}],enchantment_glint_override=true,consumable={consume_seconds:0.05,animation:"none",sound:"minecraft:entity.firework_rocket.launch",has_consume_particles:false}]
playsound minecraft:entity.firework_rocket.launch master @a ~ ~ ~ 1.5 1
particle minecraft:firework ~ ~1 ~ 0.2 0.3 0.2 0.3 25
execute positioned ~ ~16 ~ run function mg:lobby/boom
