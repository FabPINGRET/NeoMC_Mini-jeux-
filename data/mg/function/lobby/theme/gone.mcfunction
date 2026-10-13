# Retire un animal du thème sans animation de mort ni butin (@s)
execute on passengers run kill @s[type=minecraft:item_display]
execute at @s run tp @s ~ -300 ~
kill @s
