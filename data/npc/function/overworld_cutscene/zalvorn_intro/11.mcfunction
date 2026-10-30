execute at @n[tag=zalvorn,tag=enemy,distance=0..] run playsound minecraft:block.leaf_litter.break master @a[tag=mg.flw] ~ ~ ~ 2 0.5
execute at @n[tag=zalvorn,tag=enemy,distance=0..] run playsound minecraft:entity.generic.explode master @a[tag=mg.flw] ~ ~ ~ 1 2

execute at @n[tag=zalvorn,tag=enemy,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @n[tag=zalvorn,tag=enemy,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute at @n[tag=zalvorn,tag=enemy,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pupu-Nini","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"Die, creep!","color":"white","italic":false},{"text":" *tuk-nuk*","color":"gray","italic":true},{"text":" ⇒","color":"light_purple"}]

execute at @n[tag=zalvorn,tag=enemy,distance=0..] run particle minecraft:tinted_leaves{color:[0.090,0.749,0.157,1.00]} ~ ~1.5 ~ 1 1 1 0 200
execute at @n[tag=zalvorn,tag=enemy,distance=0..] run summon armor_stand ~ ~2 ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,ShowArms:1b,Small:1b,NoBasePlate:1b,PersistenceRequired:1b,Tags:["npc","pygmy","pupufight"],Pose:{LeftArm:[150f,0f,29f],RightArm:[154f,0f,310f],LeftLeg:[348f,338f,0f],RightLeg:[28f,345f,351f],Head:[41f,0f,0f]},DisabledSlots:4144959,equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{id:[I;-127647101,874661077,-1298052956,-1297449667],properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZjk0NTAwYjMyM2EwYTVmMjZmZGJmNjViZjVlZDA0NDdmOTBlMGIxMmRmNDlkNzNlZWFhNDIxZTAyZThmZTY5OSJ9fX0="}]}}}}}
execute as @n[tag=pupufight,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ ~

schedule function floaty:sched/npc/overworld_cutscene/zalvorn_intro/12 6s

#reset things
setblock -10189 57 123 air
setblock -10193 56 120 air
fill -10196 57 116 -10194 57 116 air

function music:end

tag @a[tag=mg.flw] add cutscene

kill @n[tag=zalvorn,tag=enemy,distance=0..]
kill @n[tag=pumpkin_laser,distance=0..]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
