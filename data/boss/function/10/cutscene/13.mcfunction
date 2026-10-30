playsound minecraft:entity.vex.ambient neutral @a[tag=mg.flw] -11830 216 330 3 0.7
playsound minecraft:entity.vex.charge neutral @a[tag=mg.flw] -11830 216 330 3 0.1
playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] -11830 216 330 3 0.1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Smoke","color":"yellow"},{"text":"> The Bell will fall."}]

particle sculk_soul -11830 219 330 1 2 1 0.2 300
particle minecraft:large_smoke -11830 219 330 1 2 1 0.1 300
playsound minecraft:entity.warden.sonic_boom master @a[tag=mg.flw] -11830 219 330 3 0.4

kill @n[tag=boss_ta_cutscene_stand,distance=0..]
setblock -11798 203 360 air

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds

#","color":"white"},{"text":"
