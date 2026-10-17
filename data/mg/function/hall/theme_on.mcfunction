# Décor saisonnier de l'allée des champions selon $theme (1 🎃 Halloween, 2 🎄 Noël) — généré par tools/hall/gen_hall.py
execute if score $theme mg.st matches 1 run function mg:hall/theme_h
execute if score $theme mg.st matches 2 run function mg:hall/theme_n
