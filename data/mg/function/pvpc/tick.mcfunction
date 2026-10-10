# ⚔ Arène PvP souterraine — tick (seulement si quelqu'un est dessous ou y est inscrit)
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.pvpc,x=8,y=55,z=7,dx=2.99,dy=1.5,dz=2.99] run function mg:pvpc/class_1
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.pvpc,x=16,y=55,z=7,dx=2.99,dy=1.5,dz=2.99] run function mg:pvpc/class_2
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.pvpc,x=8,y=55,z=15,dx=2.99,dy=1.5,dz=2.99] run function mg:pvpc/class_3
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.pvpc,x=16,y=55,z=15,dx=2.99,dy=1.5,dz=2.99] run function mg:pvpc/class_4
execute as @a[tag=!mg.play,tag=!mg.out,x=12,y=55,z=16,dx=2.99,dy=1.5,dz=2.99] run function mg:pvpc/leave
execute as @a[tag=mg.pvpc,tag=mg.play] run function mg:pvpc/cleanup
execute as @a[tag=mg.pvpc,scores={mg.pkc=1..}] run function mg:pvpc/kill
execute as @a[tag=mg.pvpc,scores={mg.deaths=1..}] run function mg:pvpc/died
execute as @a[tag=mg.pvpc,scores={mg.pshop=1..}] run function mg:pvpc/buy
execute as @a[tag=mg.pvpc,scores={mg.phc=1..}] run function mg:pvpc/home_tick
execute as @a[tag=mg.pvpc] unless entity @s[x=-12,y=40,z=-10,dx=51,dy=20,dz=45] run function mg:pvpc/cleanup
execute as @a[tag=mg.pvpc] if items entity @s container.* minecraft:gold_nugget[custom_data~{pvpc_coin:1b}] run function mg:pvpc/coins_picked
scoreboard players add $pvt mg.st 1
execute if score $pvt mg.st matches 20.. run function mg:pvpc/second
