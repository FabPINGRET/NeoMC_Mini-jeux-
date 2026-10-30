execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.fox.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute if score banana_of_temptation bool matches 0 if block -105 37 -171 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Monky the Bum","color":"dark_green"},{"text":"> OOH OOH EEH. (Hey, sorry, I can't open this door for ya pri-mate.","color":"white"},{"text":" *cough* ","color":"gray","italic":true},{"text":"I don't have the key, you understand?)","color":"white","italic":false}]

execute if score banana_of_temptation bool matches 0 unless block -105 37 -171 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Monky the Bum","color":"dark_green"},{"text":"> AAH!! OOH OOH OOH! (Hey, look at that!","color":"white"},{"text":" *cough* ","color":"gray","italic":true},{"text":" Monky Jr. is letting ya take his secret tunnel pri-mate. I sometimes hear him painfully crying from inside it when he's had to sneak into the city. I wish ya all the best chim-pal.)","color":"white","italic":false}]

execute if score banana_of_temptation bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Monky the Bum","color":"dark_green"},{"text":"> AHH AHHHH OOH OOOH OOOH! (I know that look on your face chim-pal, it's not worth it. The banana of temptation is not worth it pri-mate. Just go home.)","color":"white","italic":false}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
