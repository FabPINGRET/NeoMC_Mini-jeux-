# Une munition de recharge pour @s : 60 % mouton normal, 40 % mouton spécial au hasard
execute store result score $r mg.st run random value 0..99
execute if score $r mg.st matches ..59 run return run function mg:sheepwar/give_ammo {n:1}
function mg:sheepwar/give_special
