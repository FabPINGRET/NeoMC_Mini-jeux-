execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.hoglin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Slackwit","color":"green"},{"text":"> Gruhhhhhhhhhhh GRAH! Ook grud guhh. Guh buhhhh buh buh buh buh grud! GUH!","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Slackwit","color":"green"},{"text":"> My Cao chose me when I was still but an infant, and we have travelled together since. She is a most devoted companion. I do feel sorry for those who have no Cao to call their own, such as the","color":"white"},{"text":" peculiar merchant","color":"red"},{"text":" residing beneath the library.","color":"white"}]

# ","color":"white"},{"text":"
#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
