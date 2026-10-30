#No Moon, Altar On, No Moon for anyone (Start moon following player again)

execute as @p[tag=mg.flw] unless entity @e[tag=mlc_tag,distance=0..] if score mlc_altar Value matches 5 at @s run tellraw @s [{"text":"<"},{"text":"Moonlight Nexus","color":"aqua"},{"text":"> This land is so warm! And the people here seem to really appreciate me and my lycanthropic curse!","color":"white"}]
execute as @p[tag=mg.flw] unless entity @e[tag=mlc_tag,distance=0..] if score mlc_altar Value matches 5 at @s run playsound minecraft:block.amethyst_block.fall neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

#No Moon, Altar Off (Tell that it's an altar)

execute as @p[tag=mg.flw] unless entity @e[tag=mlc_tag,distance=0..] unless score mlc_altar Value matches 5 positioned ~ ~2 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"It's an altar to the Sun...","color":"gray","italic":true}]

#Yes Moon, Altar Off (Turn the altar on)

execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] unless score mlc_altar Value matches 5 run setblock ~ ~2 ~ minecraft:soul_fire strict
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 5 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Moonlight Nexus","color":"aqua"},{"text":"> Hey, this is a beautiful ","color":"white"},{"text":"altar","color":"red"},{"text":"! And this place is so nice and warm... I'll stop cursing the","color":"white"},{"text":" Botsicles","color":"aqua"},{"text":" and start cursing","color":"white"},{"text":" whoever lives here","color":"red"},{"text":" instead. I'm so excited to change them into something different at night! Actually, I think I'll make the moon rise ","color":"white"},{"text":"right now","color":"light_purple"},{"text":". Thanks for your help!","color":"white"}]
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 5 run playsound minecraft:block.amethyst_block.fall neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 5 run scoreboard players set moonlight_contagion bool 1
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 5 run data merge block -440 57 77 {front_text:{color:"cyan",messages:["","Great Altar","of Moonfire",""]}}
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 5 run function main_quest:mlc/change_supplicants
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 5 run summon armor_stand -443 56 77 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["mlc_display"],DisabledSlots:4144959,equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{id:[I;-1531356392,10633216,-2053431415,1006290370],properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjJkNWQ5ZDQxZDE5MTdmODZkODIyZDEzZDI2YWEwN2VlNmRlZmVjY2RhMWM5ODg1MDVhYjg2NGFmZTk4YTYwNSJ9fX0="}]}}}}}
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 5 run kill @e[tag=mlc_moon,type=armor_stand,limit=2,distance=0..]
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 5 run setblock -9766 273 431 minecraft:air
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 5 run playsound minecraft:zelda.secret master @a[tag=mg.flw] -443 54 77 1 1 1
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 5 run setblock -9768 272 431 air
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] positioned ~ ~2 ~ unless score mlc_altar Value matches 5 run setblock -442 51 76 minecraft:redstone_block
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] run scoreboard players set mlc_altar Value 5
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] run advancement grant @a[tag=mg.flw] only main_quest:quest_8
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] run scoreboard players set $fla29 mg.fla 1
execute as @p[tag=mg.flw] if entity @s[tag=mlc_tag] run tag @a[tag=mg.flw] remove mlc_tag
