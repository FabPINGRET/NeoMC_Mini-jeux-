execute positioned 10077 187 1275 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if block 10081 187 1278 air positioned 10077 187 1275 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glimlet Pennysack","color":"yellow"},{"text":"> It's crazy seeing the empty plot where the ","color":"white"},{"text":"Shrunken Temple","color":"green"},{"text":" used to be. It was just ripped straight out of the ground.","color":"white"}]
execute unless block 10081 187 1278 air positioned 10077 187 1275 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glimlet Pennysack","color":"yellow"},{"text":"> A Big One put the ","color":"white"},{"text":"Shrunken Temple","color":"green"},{"text":" back where used to be! Was that you?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
