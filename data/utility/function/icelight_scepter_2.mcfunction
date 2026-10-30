scoreboard players set icelight_chain Value 0


execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s run summon armor_stand ^ ^ ^0.01 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,Tags:["lightning_radius"]}
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s as @e[tag=lightning_radius,sort=nearest,limit=1,distance=0..] at @s facing entity @p[tag=mg.flw] eyes run tp @s ~ ~ ~ ~180 0
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s as @e[tag=lightning_radius,sort=nearest,limit=1,distance=0..] at @s positioned ^ ^ ^5.5 run summon lightning_bolt ~ ~ ~
execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s as @e[tag=lightning_radius,sort=nearest,limit=1,distance=0..] at @s positioned ^ ^ ^5.5 run particle electric_spark ~ ~ ~ 1 0.5 1 0.1 40 force

execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s if entity @e[tag=enemy,distance=..15] run function utility:icelight_chain_start

execute as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s run kill @e[tag=lightning_radius,sort=nearest,limit=1,distance=0..]
execute if score FreeMagic bool matches 0 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.mainhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] run effect give @s minecraft:hunger 3 18 true

execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s run summon armor_stand ^ ^ ^0.01 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,Tags:["lightning_radius"]}
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s as @e[tag=lightning_radius,sort=nearest,limit=1,distance=0..] at @s facing entity @p[tag=mg.flw] eyes run tp @s ~ ~ ~ ~180 0
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s as @e[tag=lightning_radius,sort=nearest,limit=1,distance=0..] at @s positioned ^ ^ ^5.5 run summon lightning_bolt ~ ~ ~
execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s as @e[tag=lightning_radius,sort=nearest,limit=1,distance=0..] at @s positioned ^ ^ ^5.5 run particle electric_spark ~ ~ ~ 1 0.5 1 0.1 40 force

execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s if entity @e[tag=enemy,distance=..15] run function utility:icelight_chain_start

execute if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] at @s run kill @e[tag=lightning_radius,sort=nearest,limit=1,distance=0..]
execute if score FreeMagic bool matches 0 if score Ambidextrous bool matches 1 as @a[scores={CarrotStick=1..},tag=mg.flw] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_model_data={strings:['14']}] run effect give @s minecraft:hunger 3 18 true



execute as @e[tag=icelight_marked,distance=0..] at @s run summon lightning_bolt
execute as @e[tag=icelight_marked,distance=0..] at @s run damage @s 12 minecraft:lightning_bolt by @p[scores={CarrotStick=1..},tag=mg.flw]
tag @e[distance=0..] remove icelight_marked
tag @e[distance=0..] remove icelight_premarked
tag @e[distance=0..] remove icelight_nexttarget
