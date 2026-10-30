#No Moon, Altar On, Someone has moon (Quip)

execute as @p[tag=mg.flw] unless entity @s[tag=mlc_tag] if entity @e[tag=mlc_tag,distance=0..] if score mlc_altar Value matches 3 positioned ~ ~2 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"It looks like an altar...","color":"gray","italic":true}]

#Yes Moon, Altar On (Quip)

execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] if score mlc_altar Value matches 3 positioned ~ ~2 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"It looks like an altar...","color":"gray","italic":true}]

#No Moon, Altar On, No Moon for anyone (Start moon following player again)

execute as @p[tag=mg.flw] unless entity @e[tag=mlc_tag,distance=0..] if score mlc_altar Value matches 3 at @s if block ~ ~-0.1 ~ resin_bricks run function main_quest:mlc/start
execute as @p[tag=mg.flw] unless entity @e[tag=mlc_tag,distance=0..] if score mlc_altar Value matches 3 at @s unless block ~ ~-0.1 ~ resin_bricks run tellraw @s [{"text":"<"},{"text":"Moonlight Nexus","color":"aqua"},{"text":"> Step on the bricks first!","color":"white"}]
execute as @p[tag=mg.flw] unless entity @e[tag=mlc_tag,distance=0..] if score mlc_altar Value matches 3 at @s unless block ~ ~-0.1 ~ resin_bricks run playsound minecraft:block.amethyst_block.fall neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

#No Moon, Altar Off (Tell that it's an altar)

execute as @p[tag=mg.flw] unless entity @e[tag=mlc_tag,distance=0..] unless score mlc_altar Value matches 3 positioned ~ ~2 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"It looks like an altar...","color":"gray","italic":true}]

#Yes Moon, Altar Off (Turn the altar on)

execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] unless score mlc_altar Value matches 3 run setblock ~ ~2 ~ minecraft:soul_fire strict
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 3 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Moonlight Nexus","color":"aqua"},{"text":"> Hey, this is a nice ","color":"white"},{"text":"altar","color":"aqua"},{"text":"! I think if you mess up and step off the","color":"white"},{"text":" Waxwane Brick","color":"aqua"},{"text":", I'll come back to here instead.","color":"white"}]
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 3 run playsound minecraft:block.amethyst_block.fall neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] run scoreboard players set mlc_altar Value 3
