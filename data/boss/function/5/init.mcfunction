function boss:5/clear
kill @n[tag=boss_skt_cutscene,distance=0..]

tag @a[tag=mg.flw] remove bossroom

#Reset start latch
setblock -10205 55 405 air

#Reset particles
setblock -10203 55 411 air

#Reset bossfight tick
setblock -10197 55 405 air

#Reset cutscene dreadwarden facing player or serpent
setblock -10197 55 407 air
setblock -10197 55 409 air

bossbar set boss:skt value 6
bossbar set boss:skt players
bossbar set boss:skt color green
scoreboard players set boss:skt BossHealth 6
scoreboard players set boss:skt_lastattack Value 0
setblock -10203 55 418 minecraft:black_wool
setblock -10204 55 418 minecraft:blue_wool
kill @e[tag=r_soul,distance=0..]
kill @e[tag=cuauhtli,distance=0..]
kill @e[tag=boss_5_debris,distance=0..]

#Reset attack pick next attack flag
setblock -10196 55 411 air

#Stop giving darkness effect
setblock -10196 56 413 air

#Reset win cutscene
setblock -10215 55 405 air

fill -10222 93 463 -10222 94 464 air
setblock -10222 92 464 minecraft:mossy_cobblestone

fill -10193 94 434 -10192 93 434 air
setblock -10192 92 434 minecraft:mossy_cobblestone

fill -10251 94 434 -10252 93 434 air
setblock -10252 92 434 minecraft:mossy_cobblestone
