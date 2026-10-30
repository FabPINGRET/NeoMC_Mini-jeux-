function boss:10/face_attack_disable

function boss:10/kill_tornado

function boss:10/faces/reset

execute as @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] at @s if block ~ ~ ~ light run tp @s -11830 245 330 ~ -90
particle minecraft:sculk_soul -11830 245 330 2 2 2 0.1 300

playsound minecraft:entity.vex.death hostile @a[tag=mg.flw] -11830 218 330 5 0.1
playsound minecraft:entity.warden.hurt hostile @a[tag=mg.flw] -11830 218 330 5 0.7
playsound minecraft:entity.allay.death hostile @a[tag=mg.flw] -11830 218 330 5 0.1
