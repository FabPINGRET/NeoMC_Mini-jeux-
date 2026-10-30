execute positioned 10121 67 175 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if block 10128 64 184 air positioned 10121 67 175 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glavonok the Monk of Shh","color":"red"},{"text":"> You are the one freeing the Lords, yes? We need your help. This monastery, the Monks of Shh, the Isle of Silence, all of it is misdirection to hide a ","color":"white"},{"text":"grand secret","color":"green"},{"text":". When you are ready to learn it, ","color":"white"},{"text":"stand on the altar","color":"red"},{"text":" there and I'll pray a blessing over you.","color":"white"}]

execute unless block 10128 64 184 air positioned 10121 67 175 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glavonok the Monk of Shh","color":"red"},{"text":"> This monastery, the Monks of Shh, the Isle of Silence, all of it is misdirection to hide a ","color":"white"},{"text":"grand secret","color":"green"},{"text":". When you are ready to learn it, simply","color":"white"},{"text":" go down the stairs to the left, stand on the magic circle, and sneak","color":"red"},{"text":".","color":"white"}]


execute positioned 10121 67 175 run kill @n[tag=quest_marker,distance=..3]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
