particle minecraft:explosion ~ ~ ~ 0.5 0.5 0.5 0 5
playsound minecraft:entity.dragon_fireball.explode master @a[tag=mg.flw] ~ ~ ~ 3 1
playsound minecraft:block.respawn_anchor.set_spawn master @a[tag=mg.flw] ~ ~ ~ 3 2
playsound minecraft:entity.wither.hurt master @a[tag=mg.flw] ~ ~ ~ 3 0.7

fill ~-1.6 ~-0.6 ~-1.6 ~1.6 ~0.6 ~1.6 air replace copper_ore
fill ~-1.6 ~-1.6 ~-0.6 ~1.6 ~1.6 ~0.6 air replace copper_ore
fill ~-0.6 ~-1.6 ~-1.6 ~0.6 ~1.6 ~1.6 air replace copper_ore
fill ~-2 ~-0.3 ~-2 ~2 ~0.3 ~2 air replace copper_ore
fill ~-0.3 ~-2 ~-2 ~0.3 ~2 ~2 air replace copper_ore
fill ~-2 ~-2 ~-0.3 ~2 ~2 ~0.3 air replace copper_ore


fill ~-1.6 ~-0.6 ~-1.6 ~1.6 ~0.6 ~1.6 air replace deepslate_copper_ore
fill ~-1.6 ~-1.6 ~-0.6 ~1.6 ~1.6 ~0.6 air replace deepslate_copper_ore
fill ~-0.6 ~-1.6 ~-1.6 ~0.6 ~1.6 ~1.6 air replace deepslate_copper_ore
fill ~-2 ~-0.3 ~-2 ~2 ~0.3 ~2 air replace deepslate_copper_ore
fill ~-0.3 ~-2 ~-2 ~0.3 ~2 ~2 air replace deepslate_copper_ore
fill ~-2 ~-2 ~-0.3 ~2 ~2 ~0.3 air replace deepslate_copper_ore

kill @e[tag=wv_model_flamesword,distance=0..]
kill @e[tag=wv_model_forestsword,distance=0..]
kill @e[tag=wv_model_sporessword,distance=0..]
kill @e[tag=wv_model_stonesword,distance=0..]
kill @e[tag=wv_model_icesword,distance=0..]
kill @e[tag=wv_model_watersword,distance=0..]
kill @e[tag=wv_model_valorsword,distance=0..]

execute as @e[tag=m_caster,distance=..3] run damage @s 30 minecraft:dragon_breath

function boss:final/virus/check_health
scoreboard players set lordsword_mode bool 0

scoreboard players set wv_lord_timer Value 60
execute as @a[gamemode=!spectator,tag=mg.flw] run scoreboard players add wv_lord_timer Value 20
