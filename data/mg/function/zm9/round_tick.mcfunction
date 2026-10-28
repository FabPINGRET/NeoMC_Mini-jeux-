# Manche en cours : apparitions, fin de manche
scoreboard players add $zsc mg.st 1
execute store result score $zal mg.st if entity @e[tag=mg.zz,x=-34,y=-64,z=42460,dx=68,dy=384,dz=76]
execute if score $zsc mg.st >= $zsj mg.st if score $zleft mg.st matches 1.. if score $zal mg.st < $zmx mg.st run function mg:zm9/spawn
execute if score $zleft mg.st matches ..0 if score $zal mg.st matches 0 run function mg:zm9/round_end
