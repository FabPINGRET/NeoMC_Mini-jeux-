"""Records de la Course d'elytres : meilleur temps de chaque joueur sur chaque parcours (objectif mg.xr<NUM>, en ticks), record du
serveur (faux joueur #srv du meme objectif) et son detenteur, fige dans le stockage mg:hall e.xr<NUM> par mg:hall/ely (comme les
records des parcours d'elytra). Le temps est lu dans #xrt (ticks depuis le GO) : $xt en course de groupe, mg.xst du joueur en solo.
Les objectifs mg.xr* ne sont PAS dans game.OBJECTIVES : prepare remet ceux-la a zero a chaque depart (verifie par checks_solo.py).
Fonctions generees : elyrace/time, elyrace/records, c<N>/record (a l'arrivee), c<N>/records_show (affichage).
Python stdlib uniquement (compatible 3.8).
"""
import course_common as CC

SRV = '#srv'                    # faux joueur de chaque objectif mg.xr<NUM> : le record du serveur
COMMA = '{"text":",","color":"gold"}'
ZERO = '{"text":"0","color":"gold"}'
SECONDS = '{"text":" s","color":"gold"}'


def obj(spec):
    """Nom (sans « mg. ») de l'objectif des records du parcours."""
    return 'xr%d' % spec.NUM


def objective_lines(specs):
    return ['scoreboard objectives add mg.%s dummy' % obj(s) for s in specs]


def uninstall_lines(specs):
    return (['scoreboard objectives remove mg.%s' % obj(s) for s in specs]
            + ['data remove storage mg:hall e.%s' % obj(s) for s in specs])


def score(name):
    return '{"score":{"name":"%s","objective":"mg.st"},"color":"gold"}' % name


def tell_time(cond, who, head, tail=None):
    """Deux tellraw qui affichent le temps ($es secondes, $ecs centiemes) apres `head` (composants separes par des virgules) :
    un zero de remplissage quand les centiemes sont inferieurs a 10, comme mg:elytra/finish1."""
    out = []
    for pad, test in ((True, '..9'), (False, '10..')):
        parts = [head, score('$es'), COMMA] + ([ZERO] if pad else []) + [score('$ecs'), SECONDS] + ([tail] if tail else [])
        out.append(' '.join(x for x in ['execute', cond, 'if score $ecs mg.st matches ' + test, 'run tellraw', who, '[' + ','.join(parts) + ']'] if x))
    return out


def time_lines():
    return ['# Temps #xq (ticks) -> $es (secondes) et $ecs (centiemes, par pas de 5), meme convention que mg:elytra/finish1 et mg:sky/finish ;',
            '# $es et $ecs sont partages avec ces jeux : a recalculer juste avant chaque affichage (#k5 et #k20 : mg:elyrace/objectives)',
            'scoreboard players operation $es mg.st = #xq mg.st', 'scoreboard players operation $es mg.st /= #k20 mg.st',
            'scoreboard players operation $ecs mg.st = #xq mg.st', 'scoreboard players operation $ecs mg.st %= #k20 mg.st',
            'scoreboard players operation $ecs mg.st *= #k5 mg.st']


def record_lines(spec):
    """c<N>/record : @s franchit l'arrivee, temps #xrt. Record personnel, puis (s'il en est un) record du serveur."""
    o = 'mg.' + obj(spec)
    who = '{"selector":"@s","color":"yellow","bold":true}'
    out = ['# @s = joueur qui franchit l\'arrivée du parcours %d (%s), temps #xrt (ticks, posé par finish) : record personnel, puis record du serveur' % (spec.NUM, spec.NAME),
           'scoreboard players operation #xq mg.st = #xrt mg.st',
           'function mg:elyrace/time',
           '# #rp = 1 : meilleur temps personnel (ou premier temps)',
           'scoreboard players set #rp mg.st 0',
           'execute unless score @s %s matches 1.. run scoreboard players set #rp mg.st 1' % o,
           'execute if score @s %s matches 1.. if score #xrt mg.st < @s %s run scoreboard players set #rp mg.st 1' % (o, o),
           'execute if score #rp mg.st matches 0 run return 0',
           'scoreboard players operation @s %s = #xrt mg.st' % o]
    out += tell_time('', '@s', '{"text":"★ Nouveau record personnel : ","color":"yellow","bold":true}')
    out += ['# #rs = 1 : nouveau record du serveur (un record du serveur est toujours un record personnel)',
            'scoreboard players set #rs mg.st 0',
            'execute unless score %s %s matches 1.. run scoreboard players set #rs mg.st 1' % (SRV, o),
            'execute if score %s %s matches 1.. if score #xrt mg.st < %s %s run scoreboard players set #rs mg.st 1' % (SRV, o, SRV, o),
            'execute if score #rs mg.st matches 0 run return 0',
            'scoreboard players operation %s %s = #xrt mg.st' % (SRV, o)]
    out += tell_time('', '@a', '{"text":"🏆 ","color":"gold"},%s,{"text":" bat le record du serveur sur %s : ","color":"gray"}' % (who, spec.NAME))
    out.append('function mg:hall/ely {key:"%s",lbl:"🪽 Record %s"}' % (obj(spec), spec.NAME))
    return out


def show_lines(spec):
    """c<N>/records_show : @s voit son meilleur temps et le record du serveur (le detenteur vient du stockage mg:hall)."""
    o, e = 'mg.' + obj(spec), obj(spec)
    mine = 'if score @s %s matches 1..' % o
    head = '{"text":"  ⏱ %s : ","color":"aqua"}' % spec.NAME
    out = ['# @s = joueur : son meilleur temps et le record du serveur sur le parcours %d (%s)' % (spec.NUM, spec.NAME),
           'execute unless score @s %s matches 1.. run tellraw @s [%s,{"text":"pas encore de temps","color":"gray"}]' % (o, head),
           'execute %s run scoreboard players operation #xq mg.st = @s %s' % (mine, o),
           'execute %s run function mg:elyrace/time' % mine]
    out += tell_time(mine, '@s', head + ',{"text":"ton record ","color":"gray"}')
    out += ['# record du serveur : le détenteur et le temps viennent du stockage mg:hall (composant interprété) ; repli : le temps seul',
            'execute if data storage mg:hall e.%s run tellraw @s [{"text":"    🏆 ","color":"gold"},{"nbt":"e.%s","storage":"mg:hall","interpret":true}]' % (e, e),
            'execute if score %s %s matches 1.. unless data storage mg:hall e.%s run scoreboard players operation #xq mg.st = %s %s' % (SRV, o, e, SRV, o),
            'execute if score %s %s matches 1.. unless data storage mg:hall e.%s run function mg:elyrace/time' % (SRV, o, e)]
    out += tell_time('if score %s %s matches 1.. unless data storage mg:hall e.%s' % (SRV, o, e), '@s', '{"text":"    🏆 Record du serveur : ","color":"gold"}')
    return out


def records_lines(specs):
    out = ['# @s = joueur : ses meilleurs temps et les records du serveur (mg.xs 3)',
           'tellraw @s [{"text":"\\n📊 Course d\'élytres : records","color":"aqua","bold":true}]']
    out += ['function ' + CC.fn(s, 'records_show') for s in specs]
    return out + ['tellraw @s [{"text":"Les temps de la course de groupe et du contre-la-montre solo comptent pour les mêmes records.","color":"dark_gray","italic":true}]']


def functions(specs):
    return {'time': time_lines(), 'records': records_lines(specs)}


def course_files(spec):
    return {'record': record_lines(spec), 'records_show': show_lines(spec)}
