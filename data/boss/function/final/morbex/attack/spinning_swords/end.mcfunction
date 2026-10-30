kill @e[tag=morbex_spinning_sword_pivot,distance=0..]
kill @e[tag=morbex_spinning_sword,distance=0..]

execute as @n[tag=lord_morbex_stand,distance=0..] at @s run playsound minecraft:item.armor.equip_diamond hostile @a[tag=mg.flw] ~ ~ ~ 3 1

#stop tick
setblock -12352 43 333 air

function boss:final/morbex/equipment/sword
function boss:final/morbex/pose/neutral

schedule function floaty:sched/boss/final/morbex/appear 1s
