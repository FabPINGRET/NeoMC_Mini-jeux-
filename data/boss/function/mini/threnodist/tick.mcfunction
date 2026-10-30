execute if score thren_target Value matches 1 as @n[tag=threnodist_stand,distance=0..] at @s facing entity @n[tag=targeted,gamemode=!spectator,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute if score thren_target Value matches 2 as @n[tag=threnodist_stand,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ ~


execute as @e[tag=thren_stand_decoy,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ ~
