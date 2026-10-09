# @s : quilles renversées par ce lancer → score
scoreboard players set #pc mg.st 0
execute as @e[type=minecraft:block_display,tag=mg.bpin,tag=!mg.bpdn] if score @s mg.bln = #ln mg.st run scoreboard players add #pc mg.st 1
scoreboard players operation #k mg.st = @s mg.bk
scoreboard players operation #k mg.st -= #pc mg.st
execute as @e[type=minecraft:block_display,tag=mg.bpmv] if score @s mg.bln = #ln mg.st run function mg:bowl/pin_stop
function mg:bowl/result
