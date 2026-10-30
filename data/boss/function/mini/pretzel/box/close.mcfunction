setblock -10340 89 446 minecraft:barrel[facing=up,open=false]{Items:[],components:{},lock:{components:{"minecraft:custom_name":'"Ximglie"'}}}
kill @n[tag=pretzel_item,distance=0..]
playsound minecraft:block.barrel.close block @a[tag=mg.flw] -10340 89 446 1 1

execute if score pretzel_selected Value matches 1 run function boss:mini/pretzel/attack/potion
execute if score pretzel_selected Value matches 2 run function boss:mini/pretzel/attack/shotgun
execute if score pretzel_selected Value matches 3 run function boss:mini/pretzel/attack/sword
execute if score pretzel_selected Value matches 4 run function boss:mini/pretzel/attack/carrot
execute if score pretzel_selected Value matches 5 run function boss:mini/pretzel/attack/pufferfish
execute if score pretzel_selected Value matches 6 run function boss:mini/pretzel/attack/string
execute if score pretzel_selected Value matches 7 run function boss:mini/pretzel/attack/turtle
execute if score pretzel_selected Value matches 8 run function boss:mini/pretzel/attack/book
execute if score pretzel_selected Value matches 9 run function boss:mini/pretzel/attack/brick
execute if score pretzel_selected Value matches 10 run function boss:mini/pretzel/attack/emerald
