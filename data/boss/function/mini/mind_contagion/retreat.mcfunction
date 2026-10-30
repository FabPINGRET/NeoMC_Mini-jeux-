execute as @n[tag=mind_boss,distance=0..] at @s run particle dust_color_transition{from_color:[0.000,0.271,0.290],to_color:[0.000,0.933,1.000],scale:2} ~ 174 ~ 0.4 0.6 0.4 0 100
execute as @n[tag=mind_boss,distance=0..] at @s run playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] ~ ~ ~ 1 1

execute as @n[tag=mind_boss,distance=0..] at @s run summon bat ~ 137 ~ {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,Tags:["mind_boss_bat"],active_effects:[{id:"minecraft:invisibility",amplifier:0,duration:-1,show_particles:0b}]}
execute as @n[tag=mind_boss,distance=0..] at @s run summon bat ~ 137 ~ {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,Tags:["mind_boss_bat"],active_effects:[{id:"minecraft:invisibility",amplifier:0,duration:-1,show_particles:0b}]}
execute as @n[tag=mind_boss,distance=0..] at @s run summon bat ~ 137 ~ {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,Tags:["mind_boss_bat"],active_effects:[{id:"minecraft:invisibility",amplifier:0,duration:-1,show_particles:0b}]}


tp @n[tag=mind_boss,distance=0..] -11760 125 -196
kill @e[tag=mind_clone,distance=0..]

setblock -11761 147 -177 minecraft:redstone_block

function boss:mini/mind_contagion/attacks/tentacle_finish
