# Bombe atomique : une seule, l'objet disparaît
item replace entity @s weapon.mainhand with minecraft:air
function mg:bomber/drop {t:5,cd:"bc4",cdv:0,sp:0.0004}
tellraw @a[tag=mg.play] [{"text":"☢ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" a largué la bombe atomique !","color":"green"}]
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.6 1.4
