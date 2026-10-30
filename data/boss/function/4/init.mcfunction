scoreboard players set boss:ed BossHealth 6
bossbar set boss:ed value 6
bossbar set boss:ed color green
bossbar set boss:ed players

#ATTACK BUFFER RESET
setblock -10061 95 -374 stone

#PHASE RESET
setblock -10061 95 -367 air
fill -10061 98 -362 -10061 98 -365 air

#LATCH RESET
setblock -10074 95 -378 air

#ATTACK QUEUE RESET
fill -10052 95 -352 -10055 95 -349 air replace stone
setblock -10053 95 -349 air
setblock -10052 95 -352 stone
setblock -10055 95 -352 stone
setblock -10052 95 -349 stone

#RESET BARRIER
fill -10063 116 -338 -10063 140 -372 barrier

#RESET FELLA SPEED
clone -10071 98 -377 -10071 98 -372 -10071 95 -377
