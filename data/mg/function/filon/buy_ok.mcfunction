# Achat payé (#c) : niveau suivant ou objet
scoreboard players operation @s mg.fnp -= #c mg.st
execute if score @s mg.fnt matches 1 run scoreboard players add @s mg.fnpk 1
execute if score @s mg.fnt matches 2 run scoreboard players add @s mg.fnef 1
execute if score @s mg.fnt matches 3 run scoreboard players add @s mg.fnfo 1
execute if score @s mg.fnt matches 4 run scoreboard players add @s mg.fnha 1
execute if score @s mg.fnt matches 5 run scoreboard players add @s mg.fnsw 1
execute if score @s mg.fnt matches 6 run scoreboard players add @s mg.fnar 1
execute if score @s mg.fnt matches 7 run give @s minecraft:cooked_beef 8
execute if score @s mg.fnt matches 8 run give @s minecraft:golden_apple 1
execute if score @s mg.fnt matches 9 run give @s minecraft:warped_fungus_on_a_stick[!max_damage,max_stack_size=16,custom_data={fn:1b,fn_dyn:1b},item_model="minecraft:tnt",item_name={"text":"🧨 Dynamite","color":"red"},lore=[{"text":"Clic droit dans la mine (sous la surface) : explose 2 s plus tard","color":"gray","italic":false}]] 1
execute if score @s mg.fnt matches 10 run give @s minecraft:warped_fungus_on_a_stick[!max_damage,max_stack_size=16,custom_data={fn:1b,fn_dyn:1b},item_model="minecraft:tnt",item_name={"text":"🧨 Dynamite","color":"red"},lore=[{"text":"Clic droit dans la mine (sous la surface) : explose 2 s plus tard","color":"gray","italic":false}]] 5
execute if score @s mg.fnt matches 1..6 run function mg:filon/kit
function mg:filon/effects
execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 0.8
tellraw @s [{"text":"🛒 Acheté ! Solde : ","color":"aqua"},{"score":{"name":"@s","objective":"mg.fnp"},"color":"yellow"},{"text":" pts","color":"aqua"}]
# la fenêtre se rouvre après chaque achat (enchaîner les achats)
execute if score @s mg.fnt matches 1..10 run function mg:filon/shop
