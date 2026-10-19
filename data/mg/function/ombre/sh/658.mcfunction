execute store result score $r mg.st run random value 0..4
execute if score $r mg.st matches 0 run tellraw @s {"text":"🍺 « On dit que trois coffres sont cachés dans chaque région, marqués d'un fanion rouge. »","color":"gray"}
execute if score $r mg.st matches 1 run tellraw @s {"text":"🍺 « Les pages du grimoire de Malveth racontent son histoire. Il en reste une dans presque chaque lieu important. »","color":"gray"}
execute if score $r mg.st matches 2 run tellraw @s {"text":"🍺 « Les élites brillent d'un contour doré. Elles lâchent parfois des gemmes de lune. »","color":"gray"}
execute if score $r mg.st matches 3 run tellraw @s {"text":"🍺 « Le maître d'armes paie bien pour chaque chasse inscrite au tableau de la guilde. »","color":"gray"}
execute if score $r mg.st matches 4 run tellraw @s {"text":"🍺 « Les pierres d'appel permettent de voyager d'une région à l'autre en un clin d'œil. »","color":"gray"}
