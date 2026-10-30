execute positioned -291 41 -61 run playsound minecraft:entity.donkey.eat master @a[tag=mg.flw] ~ ~ ~ 1 0.2
execute positioned -291 41 -61 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Homunculus","color":"aqua"},{"text":"> Hey you, I'm trying to smoke a ciggy in here in peace. I put boxes in front of the door specifically so I wouldn't be bothered. If Grudgrumlin asks why all the food smells like smoke I'm blaming it on you. Life's hard when you're a homunculus.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
