scoreboard players operation $tid mg.st = @s mg.olid
execute as @e[tag=mg.oltrapd] if score @s mg.olid = $tid mg.st run kill @s
kill @s
