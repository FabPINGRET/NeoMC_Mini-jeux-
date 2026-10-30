execute if score mainstory Story matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] as @p[gamemode=!spectator,tag=mg.flw] if items entity @s armor.chest minecraft:leather_chestplate if items entity @s weapon.mainhand minecraft:wooden_sword run tag @s add robbo_pass

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute if score mainstory Story matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] as @p[gamemode=!spectator,tag=mg.flw] unless entity @s[tag=robbo_pass] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Robbo","color":"aqua"},{"text":"> Hey hero, I'm stationed here to monitor the","color":"white"},{"text":" Bloom Contagion","color":"light_purple"},{"text":" and to make sure nobody wanders too close. Unfortunately I can't let you in here without both a weapon and armor, it's too dangerous. The ","color":"white"},{"text":"Bugboys","color":"green"},{"text":" in their forest make quality swords from their Blade Willow, and there's an armor shop in the castle. Come back when you're geared up and I'll let you through.","color":"white"}]
execute if score mainstory Story matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] as @p[gamemode=!spectator,tag=mg.flw] if entity @s[tag=robbo_pass] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Robbo","color":"aqua"},{"text":"> Ah, you're all ready to go I see! I'll open the gate for you. Be very careful, once you enter the","color":"white"},{"text":" Sanctum","color":"light_purple"},{"text":" you cannot return until the","color":"white"},{"text":" bloom contagion","color":"light_purple"},{"text":" is neutralized. There's no telling what you'll find inside, but something tells me it will be the first of many challenges that await you...","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] as @p[gamemode=!spectator,tag=mg.flw] if entity @s[tag=robbo_pass] if score mainstory Story matches 0 run setblock -12 52 -63 minecraft:redstone_block
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] as @p[gamemode=!spectator,tag=mg.flw] if entity @s[tag=robbo_pass] if score mainstory Story matches 0 run advancement grant @a[tag=mg.flw] only main_quest:quest_1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] as @p[gamemode=!spectator,tag=mg.flw] if entity @s[tag=robbo_pass] if score mainstory Story matches 0 run scoreboard players set $fla40 mg.fla 1
execute unless score mainstory Story matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Robbo","color":"aqua"},{"text":"> You've returned! I... I think the ","color":"white"},{"text":"contagion","color":"light_purple"},{"text":" might actually have stopped spreading! I'll remain here just in case, but you should ","color":"white"},{"text":"report news of your victory back to the King and Queen","color":"gold"},{"text":". There is still hero-ing left to be done in the Isles.","color":"white"}]

execute positioned -11 58 -64 run kill @e[tag=quest_marker,distance=..3]
execute positioned -5 58 -61 run kill @e[tag=quest_marker,distance=..3]

tag @a[tag=mg.flw] remove robbo_pass

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
