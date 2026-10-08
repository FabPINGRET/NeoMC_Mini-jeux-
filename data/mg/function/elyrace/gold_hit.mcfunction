# @s = joueur qui traverse un anneau d'or : une fusée
give @s minecraft:firework_rocket[minecraft:custom_data={mg_elyr:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée d'or","color":"gold","italic":false}] 1
execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.4
execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.4 0.4 0.4 0.3 25
tellraw @s [{"text":"★ Anneau d'or ! ","color":"gold","bold":true},{"text":"+1 fusée (clic droit en vol pour accélérer).","color":"gray"}]
