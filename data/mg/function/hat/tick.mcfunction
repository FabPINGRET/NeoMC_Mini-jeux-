# 🎩 Chapeaux (généré par tools/cosmetics/gen_hats.py) : chapeau choisi toujours sur la tête, galerie sous le Hall
execute if score $rp mg.st matches 1 as @a[scores={mg.hat=1..}] at @s run function mg:hat/guard
scoreboard players add $hatt mg.st 1
execute if score $hatt mg.st matches 20.. run function mg:hat/second
execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,gamemode=adventure,x=-20,y=64,z=8,dx=0.99,dy=1.5,dz=0.99] run function mg:hat/enter
execute as @a[x=-26,y=45,z=26,dx=2.99,dy=1.5,dz=0.99] run function mg:hat/leave
execute if entity @a[x=-34,y=45,z=8,dx=18,dy=6,dz=18] run function mg:hat/gallery_tick
