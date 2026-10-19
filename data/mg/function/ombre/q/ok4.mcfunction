# Étape 4 validée (aldric)
scoreboard players add @s mg.olg 80
tellraw @s {"text":"  +80 💰","color":"gold"}
function mg:ombre/xp {n:150}
give @s minecraft:potion[potion_contents={potion:"minecraft:strong_healing"},custom_name={"text":"✚ Potion de soin","color":"red","italic":false,"bold":true}] 3
give @s minecraft:honey_bottle[custom_data={olmana:1b},item_model="minecraft:potion",custom_name={"text":"✦ Potion de mana","color":"aqua","italic":false,"bold":true},lore=[{"text":"Boire : +60 mana","color":"gray","italic":false}]] 3
tellraw @s {"text":"  +3 potions de soin, +3 potions de mana","color":"red"}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
