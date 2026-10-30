execute positioned 10328 28 -69 run playsound minecraft:entity.strider.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute positioned 10328 28 -69 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Scleemotius","color":"green"},{"text":"> You stand in my ","color":"white"},{"text":"Thorn Forge","color":"green"},{"text":", tiny Orc. Use it at your leisure to enhance your armor. With a frame so small, I'd want all the protection I could find. I mean no offense.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
