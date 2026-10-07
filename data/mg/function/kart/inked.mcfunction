effect give @s minecraft:blindness 3 0 true
title @s title [{"text":"🦑","color":"dark_purple"}]
title @s subtitle [{"text":"De l'encre partout !","color":"dark_purple"}]
scoreboard players operation $kh mg.st = @s mg.ri
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $kh mg.st at @s run particle minecraft:squid_ink ~ ~1 ~ 0.5 0.5 0.5 0.1 40
execute at @s run playsound minecraft:entity.squid.squirt master @s ~ ~ ~ 1 1
