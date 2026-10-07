# @s = ballon : crevé si c'est celui du rang $kbs
execute if score $kbs mg.st matches 1 unless entity @s[tag=mg.kbal1] run return 0
execute if score $kbs mg.st matches 2 unless entity @s[tag=mg.kbal2] run return 0
execute if score $kbs mg.st matches 3 unless entity @s[tag=mg.kbal3] run return 0
execute at @s run particle minecraft:poof ~ ~1.4 ~ 0.2 0.2 0.2 0.05 12
execute at @s run playsound minecraft:entity.firework_rocket.blast master @a[tag=mg.play,distance=..30] ~ ~ ~ 1 1.8
kill @s
