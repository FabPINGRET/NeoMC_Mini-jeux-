# $theme remis d'après sa copie mg:lobby theme s'il manque ou vaut 0 (appelé par on, off, toggle, restore)
execute unless score $theme mg.st matches 1.. store result score $theme mg.st run data get storage mg:lobby theme
