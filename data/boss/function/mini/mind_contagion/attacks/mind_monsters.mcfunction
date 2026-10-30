execute as @e[tag=mind_boss_monster_loc,distance=0..] at @s as @a[gamemode=!spectator,tag=mg.flw] positioned ~ 173.5 ~ run function summon:mind_monster_hard
execute as @e[tag=mind_boss_monster_loc,distance=0..] at @s run playsound minecraft:entity.warden.tendril_clicks hostile @a[tag=mg.flw] ~ 174 ~ 2 0.1
execute as @e[tag=mind_boss_monster_loc,distance=0..] at @s run particle dust_color_transition{from_color:[0.000,0.271,0.290],to_color:[0.000,0.933,1.000],scale:2} ~ 174 ~ 0.4 0.6 0.4 0 50

kill @e[tag=mind_boss_monster_loc,distance=0..]

setblock -11759 147 -177 minecraft:redstone_block
