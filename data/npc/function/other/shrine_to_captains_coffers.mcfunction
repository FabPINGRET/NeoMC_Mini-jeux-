execute if block -48 58 -275 candle positioned -48 57 -273 as @p[tag=mg.flw] unless entity @s[tag=brother_shrine] positioned -48 57 -275 run tellraw @a[distance=..10,tag=mg.flw] {"text":"I have a gift for anyone who pays their respects at the Shrine to the Fallen Brothers hidden well on this island... To find it, one must climb up something...","italic":true,"color":"gray"}
execute if block -48 58 -275 candle positioned -48 57 -273 as @p[tag=mg.flw] if entity @s[tag=brother_shrine] positioned -48 57 -275 run tellraw @a[distance=..10,tag=mg.flw] {"text":"You have gone out of your way to pay your respects to the Fallen Brothers... Here is the gift I promised you...","italic":true,"color":"gray"}
execute if block -48 58 -275 candle positioned -48 57 -273 as @p[tag=mg.flw] if entity @s[tag=brother_shrine] run setblock -46 53 -273 minecraft:redstone_block

execute unless block -48 58 -275 candle positioned -48 57 -275 run tellraw @a[distance=..10,tag=mg.flw] {"text":"You are a loyal friend to the Marauders, and they will be a loyal friend to you...","italic":true,"color":"gray"}





#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
