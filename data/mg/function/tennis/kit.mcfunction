# @s : raquette + tenue de son camp
give @s minecraft:warped_fungus_on_a_stick[minecraft:custom_data={mg_racket:1b},minecraft:unbreakable={},minecraft:custom_name={"text":"🎾 Raquette","color":"yellow","italic":false},minecraft:lore=[{"text":"Clic droit près de la balle : renvoyer","color":"gray","italic":false},{"text":"Accroupi : lob — clic droit au service : lancer","color":"gray","italic":false}]]
execute if score @s mg.tns matches 1 run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=3381759,unbreakable={}]
execute if score @s mg.tns matches 2 run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16733525,unbreakable={}]
effect give @s minecraft:saturation infinite 0 true
scoreboard players set @s mg.tnt 0
