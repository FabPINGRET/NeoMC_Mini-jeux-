execute positioned -10341 89 445 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute store result score pretzel_retreat_remark Value run random value 1..11

execute if score pretzel_retreat_remark Value matches 1 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> Haha, that crud made me violent!","color":"white"}]
execute if score pretzel_retreat_remark Value matches 2 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> That was an ouchie one, two thumbs down for that crud.","color":"white"}]
execute if score pretzel_retreat_remark Value matches 3 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> That crud made me lose control, wow!","color":"white"}]
execute if score pretzel_retreat_remark Value matches 4 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> That's some powerful crud, it made me chase you haha!","color":"white"}]
execute if score pretzel_retreat_remark Value matches 5 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> That one was ok, kinda covered me in wounds though.","color":"white"}]
execute if score pretzel_retreat_remark Value matches 6 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> Ow, hoping the next crud is a band-aid or a hospital worker.","color":"white"}]
execute if score pretzel_retreat_remark Value matches 7 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> Interesting, that last one made me have a dream I was killing you.","color":"white"}]
execute if score pretzel_retreat_remark Value matches 8 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> That was a crazy sword, it made me do a horrible deed! Haha.","color":"white"}]
execute if score pretzel_retreat_remark Value matches 9 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> Hey, don't get mad at me, blame the barrel! Let's see what else is in it...","color":"white"}]
execute if score pretzel_retreat_remark Value matches 10 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> Let's both pretend we didn't just go beast mode on each other.","color":"white"}]
execute if score pretzel_retreat_remark Value matches 11 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> Um, not to be awkward, you just tried to kill me I think? I'm not ok with that.","color":"white"}]
