"""Anneau de vent (prototype, WIND = False : rien n'est genere). Un anneau de vent est un detour bonus (comme un anneau
d'or) : en le traversant, le joueur est pousse vers l'avant par une charge de vent (wind_charge) sans proprietaire,
invoquee 1 bloc derriere lui et lancee vers lui a 3 fois sa vitesse ; elle explose a son contact. Option A du plan :
l'effet reel (la vitesse de Motion lue cote serveur, la poussee) ne se mesure qu'en jeu ; l'option B de secours serait un
modificateur de l'attribut minecraft:gravity. Le pilote automatique ignore les anneaux de vent (jamais necessaires).
Exige explosion_knockback_resistance a 0 : core/attr_reset (reset_player) le remet a 0 au retour au lobby.
Pour essayer : WIND = True, regenerer, tester en jeu (9 essais sur 10 doivent pousser le joueur).
Python stdlib uniquement (compatible 3.8).
"""
import sweep as SW

WIND = False
TAG = 'mg.xwc'
KILL = 'kill @e[type=minecraft:wind_charge,tag=%s]' % TAG
OBJECTIVE = ('xv', 'anneaux de vent pris (ne fait qu\'augmenter)', None)


def active(spec):
    """Anneaux de vent du parcours : [(x, decalage lateral)] ; vide si WIND est faux."""
    return list(spec.WINDS) if WIND else []


def objectives():
    return [OBJECTIVE] if WIND else []


def tags():
    return [TAG] if WIND else []


def cleanup_lines():
    """Tue les charges de vent restantes (nettoyage, desinstallation, debut de tick)."""
    return [KILL] if WIND else []


def detect_lines(c):
    """Lignes de la fonction `rings` : franchissement balaye (sweep.py) d'un anneau de vent (trou de 7 x 7), une fois chacun (mg.xv)."""
    out = []
    if c.winds:
        out.append('# Anneaux de vent (trou de 7 x 7) : une poussee chacun, mg.xv ne fait qu\'augmenter')
    for k, (x, cy, cz) in enumerate(c.winds, 1):
        out += SW.ring_lines(x, cy, cz, SW.GOLD_R, 'if score @s mg.xv matches ..%d' % (k - 1),
                             ['function mg:elyrace/wind', 'scoreboard players set @s mg.xv %d' % k])
    return out


def functions():
    """Fonctions generees : wind (@s = joueur) et wind_at (macro) ; rien si WIND est faux."""
    if not WIND:
        return {}
    return {
        'wind': ['# @s = joueur qui traverse un anneau de vent : charge de vent derriere lui, lancee vers lui a 3 fois sa vitesse',
                 '# (Motion x 1000 puis x 0,003 = vitesse x 3 ; derriere = - vitesse x 0,4, soit environ 1 bloc a 2,5 blocs/tick)',
                 'execute store result storage mg:c dx double 0.003 run data get entity @s Motion[0] 1000',
                 'execute store result storage mg:c dy double 0.003 run data get entity @s Motion[1] 1000',
                 'execute store result storage mg:c dz double 0.003 run data get entity @s Motion[2] 1000',
                 'execute store result storage mg:c bx double -0.0004 run data get entity @s Motion[0] 1000',
                 'execute store result storage mg:c by double -0.0004 run data get entity @s Motion[1] 1000',
                 'execute store result storage mg:c bz double -0.0004 run data get entity @s Motion[2] 1000',
                 'execute at @s run function mg:elyrace/wind_at with storage mg:c',
                 'execute at @s run playsound minecraft:entity.breeze.wind_burst master @s ~ ~ ~ 1 1',
                 'execute at @s run particle minecraft:cloud ~ ~1 ~ 0.5 0.5 0.5 0.2 30',
                 'title @s actionbar [{"text":"≋ Anneau de vent !","color":"aqua","bold":true}]'],
        'wind_at': ['# macro : $(bx..bz) = decalage derriere le joueur, $(dx..dz) = vitesse de la charge ; etiquette %s (tuee au tick suivant)' % TAG,
                    '$summon minecraft:wind_charge ~$(bx) ~$(by) ~$(bz) {Motion:[$(dx),$(dy),$(dz)],Tags:["%s"]}' % TAG],
    }
