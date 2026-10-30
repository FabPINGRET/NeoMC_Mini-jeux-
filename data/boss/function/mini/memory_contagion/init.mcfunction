function boss:mini/memory_contagion/clear_ground
bossbar set boss:memory_contagion value 150
bossbar set boss:memory_contagion color green
bossbar set boss:memory_contagion players

fill -9964 85 363 -9964 85 360 air
setblock -9948 84 357 air
setblock -9957 84 357 air
setblock -9946 85 357 air

function boss:mini/memory_contagion/stand_reveal
tp @n[tag=mem_nexus_stand,distance=0..] -9960 100 370 180 0
