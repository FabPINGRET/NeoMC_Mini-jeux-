# @s : sans chapeau
scoreboard players set @s mg.hat 0
function mg:hat/strip
playsound minecraft:item.armor.equip_generic master @s ~ ~ ~ 1 0.8
tellraw @s {"text":"🎩 Chapeau rangé.","color":"gray"}
