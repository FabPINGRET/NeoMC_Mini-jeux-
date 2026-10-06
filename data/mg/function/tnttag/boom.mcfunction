# @s = porteur qui explose
particle minecraft:explosion_emitter ~ ~1 ~ 0 0 0 0 1
particle minecraft:flame ~ ~1 ~ 0.6 0.8 0.6 0.15 80
playsound minecraft:entity.generic.explode master @a ~ ~ ~ 2 0.9
tellraw @a [{"text":"✹ BOUM ! ","color":"red","bold":true},{"selector":"@s","color":"gold"},{"text":" a explosé avec la bombe !","color":"gray"}]
function mg:tnttag/unequip
function mg:core/eliminate
