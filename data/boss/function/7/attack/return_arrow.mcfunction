tag @s remove throwing_arrow
execute unless entity @s[tag=attacking] run function boss:7/hand_frame/idle
execute unless entity @s[tag=attacking] run summon arrow
