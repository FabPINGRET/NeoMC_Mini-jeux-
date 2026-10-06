# Quakecraft — donne une grenade (@s)
give @s minecraft:snowball[item_model="minecraft:tnt",custom_name=[{"text":"✹ Grenade","color":"red","bold":true,"italic":false}],lore=[{"text":"Clic droit : lance une grenade (explose à l'impact)","color":"gray","italic":false},{"text":"Rayon 4,5 blocs — un kill pour chaque joueur touché","color":"gray","italic":false}],enchantment_glint_override=true] 1
tellraw @s [{"text":"✹ ","color":"red"},{"text":"Grenade obtenue ! ","color":"gold","bold":true},{"text":"Clic droit pour la lancer.","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 0.6
