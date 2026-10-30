#execute positioned 10180 40 -237 at @e[sort=nearest,limit=1,tag=npc] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a ~ ~ ~ 1 1.2


execute positioned 10180 40 -237 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:item.chorus_fruit.teleport neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute positioned 10180 40 -237 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run particle minecraft:sneeze ~ ~ ~ 0.1 0.1 0.1 0.05 100 force @a[tag=mg.flw]

tp @n[tag=slime_man,distance=0..] 10181 35 -235

#slime man to valor tower
setblock -9765 240 416 minecraft:redstone_block
