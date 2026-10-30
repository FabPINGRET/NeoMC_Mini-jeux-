execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score bubble_lake Story matches 0..3 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Betta","color":"yellow"},{"text":"> Operation ","color":"white"},{"text":"T","color":"blue"},{"text":"actical ","color":"white"},{"text":"R","color":"blue"},{"text":"eclamation of ","color":"white"},{"text":"O","color":"blue"},{"text":"verrun ","color":"white"},{"text":"U","color":"blue"},{"text":"nderwater ","color":"white"},{"text":"T","color":"blue"},{"text":"erritory is in its final phase: eliminating the ","color":"white"},{"text":"Lake Freak Supreme","color":"dark_green"},{"text":". I know monster slaying is just another Tuesday for you, but down here? We fight tooth and scale just to hold the line.","color":"white"}]

execute if score bubble_lake Story matches 4 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Betta","color":"yellow"},{"text":"> I watched you hunt some of those ","color":"white"},{"text":"Lake Freaks","color":"dark_green"},{"text":". It was a smart idea to use the sharp end of your sword, I will have to remember that!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
