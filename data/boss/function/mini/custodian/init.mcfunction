bossbar set boss:custodian value 100
bossbar set boss:custodian color green
bossbar set boss:custodian players

function boss:mini/custodian/time/day

kill @n[tag=custodian_boss,distance=0..]

#Stop Tick
setblock -10449 67 423 air

setblock -10451 68 423 air

fill -10445 68 425 -10443 68 425 air

tp @n[tag=custodian_stand,distance=0..] -10441 84 439 -180 0

scoreboard players set custodian_phase Value 1
