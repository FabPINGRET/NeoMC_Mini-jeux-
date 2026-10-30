execute positioned -316 57 -77 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -316 57 -77 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ramdak","color":"dark_aqua"},{"text":"> LET ME OUT LET ME OUT!!! THERE'S","color":"white"},{"text":" *cough*","color":"gray","italic":true},{"text":" BUGS ON ME!!! THERE'S SO MANY BUGS IN HERE!!!","color":"white","italic":false}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
