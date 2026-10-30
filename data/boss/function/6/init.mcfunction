function boss:6/clear

kill @n[tag=boss_sh_cutscene,distance=0..]

tag @a[tag=mg.flw] remove bossroom
tag @a[tag=mg.flw] remove sh_targeted

function game:blue_light_off
schedule clear floaty:sched/boss/6/select_cycle
tp @n[tag=boss_sh_slimeman,distance=0..] -10506 71 -70
fill -10502 79 -86 -10470 79 -54 minecraft:iron_bars replace minecraft:honey_block
fill -10502 79 -86 -10470 79 -54 minecraft:iron_bars replace minecraft:iron_bars
kill @n[tag=boss_sh_cutscene,distance=0..]
kill @n[tag=boss_sh_loc,distance=0..]
kill @n[tag=boss_sh_superslimebeam,distance=0..]
kill @e[tag=fungloom,distance=0..]
summon armor_stand -10490 63 -70 {CustomNameVisible:0b,NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_sh_loc","x2","z3","east"],DisabledSlots:4144959,Rotation:[270F,0F],CustomName:'{"bold":true,"color":"light_purple","text":"Slubwart the Yucky"}'}

bossbar set boss:sh value 10
bossbar set boss:sh players
bossbar set boss:sh color green
scoreboard players set boss:sh BossHealth 10
scoreboard players set boss:sh_lastattack Value 0
scoreboard players set boss:sh_state Value 0

scoreboard players set boss:sh_ceiling bool 0
scoreboard players set boss:sh_protected bool 0

fill -10504 74 -69 -10468 71 -71 air replace minecraft:honey_block
fill -10487 74 -88 -10485 71 -52 air replace minecraft:honey_block

#Reset Start latch
setblock -10462 42 -46 air

#Reset dreadwarden particles
setblock -10462 42 -55 air

#Reset hanging slubwart
clone -10534 62 -64 -10530 67 -60 -10493 73 -72

#Reset falling block command blocks
fill -10489 103 -69 -10493 107 -71 stone

#Reset attack wool counters
fill -10478 42 -70 -10478 42 -72 minecraft:black_wool

#Reset mid-cutscene shell hardening
setblock -10471 42 -96 stone

#Reset slime man facing direction
fill -10462 43 -61 -10462 43 -59 air

#Reset super slime beam particles
setblock -10462 43 -63 air

#Reset final cutscene
setblock -10504 42 -46 air
