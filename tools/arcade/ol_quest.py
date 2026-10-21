"""📜 Ombrelune : campagne (prologue, 8 chapitres, épilogue), PNJ et dialogues, quêtes secondaires, contrats, boutiques et forge,
pierres d'appel (voyage), lieux, pages du grimoire, coffres cachés, succès, journal, accès aux régions et dangers régionaux.
Module importé par gen_ombrelune.py.

Scores : mg.olch étape de la campagne, mg.olqp progression de l'étape (compteur ou bits), mg.olsa / mg.olsd quêtes secondaires
acceptées / rendues (bits), mg.olq1..16 progression des quêtes secondaires, mg.olct / mg.olcn / mg.olcp contrat (espèce + 1, objectif,
progression), mg.olws pierres d'appel (bits), mg.olpo lieux (bits), mg.olpg pages (bits), mg.oltc coffres (bits), mg.olac succès (bits),
mg.olfur cape de fourrure, mg.olfire talisman ignifuge, mg.olbless bénédiction de l'Aube, mg.olhorse destrier.
"""
import math
import random

import ol_world as W
import ol_structs as S
import ol_mobs as M
import ol_class as CL
from ol_core import w, js, P, TEXT, nm, lo, dlg, show, bit_test, bit_set, say, tdisp, DIM

SP = S.SPOTS
REG_IDX = {'hub': 0, **{r: i + 1 for i, r in enumerate(W.ORDER)}}

# ================================================================ PNJ : clé -> (nom, couleur, lieu, profession, type de village, région)
NPCS = {
    'liora': ('🔮 Archimagesse Liora', 'light_purple', SP['liora'], 'librarian', 'plains', 'hub'),
    'liora_t': ('🔮 Archimagesse Liora', 'light_purple', SP['liora_t'], 'cleric', 'plains', 'hub'),
    'orren': ('⚔ Orren, maître d\'armes', 'gold', SP['orren'], 'weaponsmith', 'plains', 'hub'),
    'aldric': ('🛡 Capitaine Aldric', 'aqua', SP['aldric'], 'armorer', 'plains', 'hub'),
    'isolde': ('👑 Régente Isolde', 'gold', SP['regent'], 'cartographer', 'plains', 'hub'),
    'bram': ('⚒ Bram, forgeron', 'red', SP['blacksmith'], 'toolsmith', 'plains', 'hub'),
    'elsa': ('🧺 Elsa, marchande', 'yellow', SP['merchant'], 'farmer', 'plains', 'hub'),
    'fenna': ('⚗ Fenna, alchimiste', 'dark_green', SP['alchemist'], 'cleric', 'swamp', 'hub'),
    'joss': ('🐴 Joss, palefrenier', 'gold', SP['stablemaster'], 'leatherworker', 'plains', 'hub'),
    'marthe': ('🍺 Marthe, aubergiste', 'gold', SP['innkeeper'], 'butcher', 'plains', 'hub'),
    'tessa': ('🌾 Tessa, maire de Brumecombe', 'green', SP['tessa'], 'farmer', 'plains', 'w'),
    'gaspard': ('🐑 Gaspard, berger', 'green', SP['farmer'], 'shepherd', 'plains', 'w'),
    'elyndra': ('🌿 Reine Elyndra', 'green', SP['elyndra'], 'librarian', 'jungle', 'nw'),
    'thalion': ('🏹 Thalion, archer elfe', 'green', SP['elf_ground'], 'fletcher', 'jungle', 'nw'),
    'bjorn': ('🪓 Jarl Bjorn', 'aqua', SP['bjorn'], 'weaponsmith', 'snow', 'n'),
    'sigrun': ('🧵 Sigrun, fourreuse', 'aqua', SP['furrier'], 'leatherworker', 'snow', 'n'),
    'maelle': ('✝ Sœur Maëlle', 'dark_aqua', SP['maelle'], 'cleric', 'swamp', 'ne'),
    'odo': ('🌱 Odo, herboriste', 'dark_green', SP['herbalist'], 'farmer', 'swamp', 'ne'),
    'kassim': ('🐪 Kassim, caravanier', 'yellow', SP['kassim'], 'cartographer', 'desert', 'e'),
    'zahra': ('💍 Zahra, joaillière', 'yellow', SP['sandmerchant'], 'mason', 'desert', 'e'),
    'durgan': ('🔥 Durgan, forgeron nain', 'red', SP['durgan'], 'armorer', 'savanna', 'se'),
    'thrain': ('👑 Roi Thrain', 'gray', SP['thrain'], 'mason', 'taiga', 's'),
    'aldric_sw': ('🛡 Capitaine Aldric', 'aqua', SP['aldric_sw'], 'armorer', 'plains', 'sw'),
}
NPC_ID = {k: i + 1 for i, k in enumerate(NPCS)}

# points à ramasser / à activer (générés ici, hors constructions)
rq = random.Random(888)


def pts_near(c, n, rmin, rmax, reg):
    out = []
    for _ in range(4000):
        if len(out) >= n:
            break
        a = rq.uniform(0, 2 * math.pi)
        d = rq.uniform(rmin, rmax)
        x, z = round(c[0] + d * math.cos(a)), round(c[1] + d * math.sin(a))
        if (x, z) not in W.H or W.region_at(x, z) != reg or W.COL[(x, z)][2]:
            continue
        if any(math.hypot(x - a_, z - b_) < 14 for a_, y_, b_ in out):
            continue
        out.append((x, W.ground(x, z), z))
    return out


SACKS = pts_near(W.P['bandit_fort'], 3, 26, 46, 'w')
COCOONS = pts_near(W.P['spider_nest'], 3, 12, 40, 'nw')
SCARABS = [(W.P['obelisks'][0] + 2, W.ground(W.P['obelisks'][0] + 2, W.P['obelisks'][1] + 2), W.P['obelisks'][1] + 2)] + pts_near(W.P['tombs'], 2, 10, 40, 'e')

# ================================================================ campagne
CH_NAMES = ['Prologue · L\'Aube éteinte', 'I · Les brigands de Valdor', 'II · Le chant de Sylvanor', 'III · Le cœur de l\'hiver', 'IV · La brume maudite',
            'V · Les sables du pharaon', 'VI · Les ailes de feu', 'VII · La porte des rois', 'VIII · La Lune Noire', 'Épilogue · L\'Aube retrouvée']
STEPS = []


def st(kind, ch, obj, **k):
    d = dict(kind=kind, ch=ch, obj=obj, **k)
    STEPS.append(d)
    return len(STEPS) - 1


def tgt(name):
    s = NPCS[name][2] if name in NPCS else SP[name]
    return (int(s[0]), int(s[1]), int(s[2]))


T = lambda x, y, z: (int(x), int(y), int(z))
LIORA, ALDRIC = tgt('liora'), tgt('aldric')
# ---- prologue
st('talk', 0, 'Rejoins l\'archimagesse Liora dans la tour des mages (nord-ouest de la cité)', npc='liora', at=LIORA, rw=(60, 30),
   text='Te voilà enfin, Porteur de l\'Aube. Il y a cent ans, l\'archimage Malveth a brisé la Pierre-Lune qui protégeait Ombrelune. '
        'Le ciel s\'est assombri, les morts se sont relevés, et ses huit éclats ont été dispersés aux quatre vents. Havreclair est la dernière cité libre. '
        'La prophétie annonçait ta venue : toi seul peux réunir les éclats. Mais d\'abord, apprends à te battre.', btn='Je suis prêt')
st('class', 0, 'Choisis ta voie auprès d\'Orren, le maître d\'armes (guilde, ouest de la place)', at=tgt('orren'))
st('talk', 0, 'Présente-toi au capitaine Aldric (cour du château, au nord)', npc='aldric', at=ALDRIC, rw=(80, 40),
   text='Alors c\'est toi, l\'élu de Liora ? Les routes de Valdor sont infestées de loups et de brigands. Avant de te confier quoi que ce soit, '
        'montre-moi ce que tu vaux : passe la porte ouest et abats-en quatre.', btn='J\'y vais', unlock='w')
st('kill', 0, 'Abats 4 loups ou brigands dans les plaines de Valdor (porte ouest)', kinds=['loup', 'bandit', 'archer', 'goule', 'squelette'], n=4, at=T(-100, 66, 6))
st('talk', 0, 'Retourne voir le capitaine Aldric', npc='aldric', at=ALDRIC, rw=(150, 80),
   text='Pas mal du tout. La maire de Brumecombe, Tessa, réclame de l\'aide depuis des semaines. Le village est à l\'ouest, au bout de la route. '
        'Prends ces potions, tu en auras besoin.', btn='Récompense : 150 XP, 80 💰, potions', give='pots')
# ---- I · Valdor
st('talk', 1, 'Rejoins Tessa, la maire de Brumecombe (ouest de Valdor)', npc='tessa', at=tgt('tessa'), rw=(80, 40),
   text='Un envoyé de Havreclair ! Les brigands de Brennic pillent nos récoltes. Ils ont caché trois sacs de grain volé autour de leur fort, à l\'ouest. '
        'Rapporte-les et le village mangera cet hiver.', btn='Je les retrouve')
st('collect', 1, 'Retrouve les 3 sacs de grain cachés autour du fort des brigands (accroupi à côté)', pts=SACKS, label='🌾 Sac de grain', item='hay_block')
st('talk', 1, 'Rapporte le grain à Tessa', npc='tessa', at=tgt('tessa'), rw=(200, 120),
   text='Merci ! Mais Brennic reviendra. On dit qu\'il porte au cou un éclat qui brille comme la lune : c\'est lui qui le rend si fort. '
        'Son fort est au nord-ouest de Valdor. Mets fin à son règne.', btn='Je m\'occupe de Brennic')
st('boss', 1, 'Abats Brennic, seigneur des brigands, dans la cour de son fort', boss='brennic', at=T(*S.ARENAS['brennic']['c']))
st('talk', 1, 'Retourne voir Tessa à Brumecombe', npc='tessa', at=tgt('tessa'), rw=(300, 200),
   text='Brennic est tombé ! Et voici l\'éclat qu\'il portait. Il pulse d\'une lumière froide. Porte-le à l\'archimagesse, elle saura quoi en faire.',
   btn='Récompense : 300 XP, 200 💰', shard=1)
st('talk', 1, 'Rapporte le premier éclat à Liora (tour des mages)', npc='liora', at=LIORA, rw=(200, 100),
   text='Le premier éclat ! Je sens les autres… l\'un d\'eux appelle depuis la forêt de Sylvanor, au nord de Valdor. Les elfes y vivent cachés, '
        'mais quelque chose empoisonne leurs bois. Le col nord de Valdor est ouvert.', btn='En route pour Sylvanor', unlock='nw')
# ---- II · Sylvanor
st('talk', 2, 'Trouve la reine Elyndra à Aelindor, la cité des arbres (Sylvanor)', npc='elyndra', at=tgt('elyndra'), rw=(150, 80),
   text='Un humain, à Aelindor… La reine-araignée Ysh\'tar a pondu ses cocons dans toute la forêt. Ses rejetons dévorent nos gardiens. '
        'Brûle trois nids de cocons, au sud-ouest de la cité.', btn='Je détruis les nids')
st('interact', 2, 'Détruis les 3 nids de cocons (clic droit dessus)', pts=COCOONS, label='🕸 Nid de cocons', item='cobweb', done='Le nid part en fumée !')
st('talk', 2, 'Retourne voir la reine Elyndra', npc='elyndra', at=tgt('elyndra'), rw=(300, 180),
   text='La forêt respire mieux. Mais Ysh\'tar elle-même se terre dans son antre, un cratère tapissé de toiles au sud-ouest. Elle a avalé un éclat de la Pierre-Lune.',
   btn='J\'affronte Ysh\'tar')
st('boss', 2, 'Abats Ysh\'tar, la reine-araignée, dans son antre', boss='ystar', at=T(*S.ARENAS['ystar']['c']))
st('talk', 2, 'Retourne voir la reine Elyndra', npc='elyndra', at=tgt('elyndra'), rw=(450, 300),
   text='Le deuxième éclat, arraché au ventre de la bête. Sylvanor te doit sa survie. Au nord-est, les pics de Givrecroc : le jarl Bjorn de Hrafnheim '
        'nous a envoyé un corbeau. Le géant du givre est sorti de son sommeil.', btn='Récompense : 450 XP, 300 💰', shard=2, unlock='n')
# ---- III · Givrecroc
st('talk', 3, 'Rejoins le jarl Bjorn à Hrafnheim (Givrecroc)', npc='bjorn', at=tgt('bjorn'), rw=(150, 100),
   text='Ha ! Un sudiste. Sans fourrure, le froid te tuera avant les loups. Va voir Sigrun : avec 5 peaux de bête, elle te coudra une cape.',
   btn='Je vais voir Sigrun')
st('mat', 3, 'Apporte 5 peaux de bête à Sigrun la fourreuse (Hrafnheim)', npc='sigrun', at=tgt('sigrun'), mat=1, n=5, rw=(150, 0), give='fur',
   text='Cinq belles peaux. Voilà ta cape : tu ne gèleras plus dans les pics.', btn='Recevoir la cape de fourrure')
st('talk', 3, 'Retourne voir le jarl Bjorn', npc='bjorn', at=tgt('bjorn'), rw=(100, 60),
   text='L\'armée de Hrimgar descend des sommets : vagabonds gelés, yétis, loups des neiges. Fais-en tomber six pour que nos chasseurs respirent.',
   btn='À la chasse')
st('kill', 3, 'Abats 6 créatures du givre (vagabonds, yétis, loups des neiges)', kinds=['vagabond', 'yeti', 'loupneige', 'ours'], n=6, at=T(20, 90, -160))
st('talk', 3, 'Retourne voir le jarl Bjorn', npc='bjorn', at=tgt('bjorn'), rw=(300, 200),
   text='Bien. Il est temps. Hrimgar trône dans sa forteresse de glace, sur le plus haut plateau au nord-est. Il garde l\'éclat dans son poing.',
   btn='J\'escalade le pic')
st('boss', 3, 'Abats Hrimgar, le géant du givre, dans sa forteresse', boss='hrimgar', at=T(*S.ARENAS['hrimgar']['c']))
st('talk', 3, 'Retourne voir le jarl Bjorn', npc='bjorn', at=tgt('bjorn'), rw=(600, 400),
   text='Le géant est mort ! Les skaldes chanteront ton nom. Voici le troisième éclat. À l\'est, les marais de Fangebrume : une sœur guerrière, Maëlle, '
        'y chasse les sorcières de Morvaine. Le col de l\'est est dégagé.', btn='Récompense : 600 XP, 400 💰', shard=3, unlock='ne')
# ---- IV · Fangebrume
st('talk', 4, 'Rejoins Sœur Maëlle au village sur pilotis (Fangebrume)', npc='maelle', at=tgt('maelle'), rw=(150, 100),
   text='Que l\'Aube te garde. Une peste ronge le village : la fièvre noire de Morvaine. Odo, l\'herboriste, peut préparer un antidote avec 4 fioles de venin.',
   btn='Je trouve le venin')
st('mat', 4, 'Apporte 4 fioles de venin à Odo l\'herboriste', npc='odo', at=tgt('odo'), mat=4, n=4, rw=(250, 0),
   text='Quatre fioles ! Je distille… voilà l\'antidote. Le village est sauvé, et tu es désormais protégé contre la fièvre.', btn='Recevoir l\'antidote')
st('talk', 4, 'Retourne voir Sœur Maëlle', npc='maelle', at=tgt('maelle'), rw=(150, 100),
   text='Morvaine se cache sur son île, au nord-est, protégée par trois totems maudits plantés sur la rive. Brise-les, et sa magie faiblira.',
   btn='Je brise les totems')
st('interact', 4, 'Brise les 3 totems maudits autour de l\'île de Morvaine (clic droit)', pts=SP['totems'], label='💀 Totem maudit', done='Le totem se fend !')
st('boss', 4, 'Abats Morvaine, la mère-sorcière, sur son île', boss='morvaine', at=T(*S.ARENAS['morvaine']['c']))
st('talk', 4, 'Retourne voir Sœur Maëlle', npc='maelle', at=tgt('maelle'), rw=(800, 500),
   text='La mère-sorcière n\'est plus. Prends ce quatrième éclat. Au sud, le désert d\'Azhar : Kassim, un caravanier, cherche une escorte pour la pyramide de Sethkar.',
   btn='Récompense : 800 XP, 500 💰', shard=4, unlock='e')
# ---- V · Azhar
st('talk', 5, 'Rejoins Kassim le caravanier à l\'oasis d\'Azhar', npc='kassim', at=tgt('kassim'), rw=(150, 120),
   text='La pyramide de Sethkar est scellée. Pour ouvrir la chambre du pharaon, il faut trois scarabées d\'or : un près des obélisques, '
        'deux dans les ruines autour des tombeaux.', btn='Je trouve les scarabées')
st('collect', 5, 'Retrouve les 3 scarabées d\'or (obélisques et ruines, accroupi à côté)', pts=SCARABS, label='🪲 Scarabée d\'or', item='gold_block')
st('talk', 5, 'Retourne voir Kassim', npc='kassim', at=tgt('kassim'), rw=(200, 150),
   text='Les trois scarabées ! Entre dans la pyramide par le nord et pose-les sur les trois socles de la salle des scarabées. La porte s\'ouvrira.',
   btn='J\'entre dans la pyramide')
st('interact', 5, 'Pose les 3 scarabées sur les socles de la pyramide (clic droit)', pts=SP['scarab_sockets'], label='🪲 Socle', done='Le scarabée s\'emboîte.',
   door='pyramid')
st('boss', 5, 'Abats Sethkar, le pharaon-liche, dans la chambre funéraire', boss='sethkar', at=T(*S.ARENAS['sethkar']['c']))
st('talk', 5, 'Retourne voir Kassim', npc='kassim', at=tgt('kassim'), rw=(1000, 600),
   text='Tu es revenu de la pyramide ! Voici le cinquième éclat, arraché au sarcophage. Au sud, Pyrecendre : un forgeron nain, Durgan, '
        'combat le dragon Ignarok depuis le Bastion des Braises.', btn='Récompense : 1000 XP, 600 💰', shard=5, unlock='se')
# ---- VI · Pyrecendre
st('talk', 6, 'Rejoins Durgan au Bastion des Braises (Pyrecendre)', npc='durgan', at=tgt('durgan'), rw=(150, 120),
   text='Le souffle d\'Ignarok fond l\'acier. Apporte-moi 6 écailles de drake : je forgerai un talisman qui te protégera du feu.', btn='Je chasse les drakes')
st('mat', 6, 'Apporte 6 écailles de drake à Durgan', npc='durgan', at=tgt('durgan'), mat=6, n=6, rw=(300, 0), give='fire',
   text='Six écailles… Le talisman est prêt. Avec lui, la chaleur du volcan ne t\'atteindra plus.', btn='Recevoir le talisman ignifuge')
st('go', 6, 'Gravis le volcan par la rampe nord jusqu\'à la caldeira', at=tgt('cald_in'), r=10)
st('boss', 6, 'Abats Ignarok, le dragon de feu', boss='ignarok', at=T(*S.ARENAS['ignarok']['c']))
st('talk', 6, 'Retourne voir Durgan au Bastion', npc='durgan', at=tgt('durgan'), rw=(1200, 800),
   text='Le dragon est mort ! Mon roi doit l\'apprendre : Thrain campe devant Khazgarde, notre cité perdue, à l\'ouest du volcan. '
        'Voici le sixième éclat, il était dans le nid.', btn='Récompense : 1200 XP, 800 💰', shard=6, unlock='s')
# ---- VII · Khazgarde
st('talk', 7, 'Rejoins le roi Thrain au camp nain (Khazgarde)', npc='thrain', at=tgt('thrain'), rw=(150, 150),
   text='La porte de Khazgarde est scellée par quatre pierres runiques. Réveille-les et nous reprendrons notre cité. Prends garde : '
        'un colosse de runes garde le grand hall.', btn='Je réveille les runes')
st('interact', 7, 'Réveille les 4 pierres runiques devant la porte (clic droit)', pts=SP['runes'], label='ᚱ Pierre runique', done='La rune s\'illumine !', door='kgate')
st('kill', 7, 'Purge le grand hall : abats 8 ennemis à Khazgarde', kinds=['nain', 'arbaletrier', 'gardien', 'troggo', 'rampant'], n=8, at=tgt('kgate_in'))
st('boss', 7, 'Abats le Colosse de runes au fond du grand hall', boss='colosse', at=T(*S.ARENAS['colosse']['c']))
st('talk', 7, 'Retourne voir le roi Thrain', npc='thrain', at=tgt('thrain'), rw=(1500, 1000),
   text='Khazgarde est à nous ! Voici le septième éclat. Sept éclats… Il ne manque que celui de Malveth lui-même. Retourne à Havreclair : Liora t\'attend.',
   btn='Récompense : 1500 XP, 1000 💰', shard=7)
st('talk', 7, 'Rapporte les sept éclats à Liora (tour des mages)', npc='liora', at=LIORA, rw=(800, 0), give='dawn', unlock='sw',
   text='Sept éclats… Je les fonds dans l\'acier : voici la Lame de l\'Aube, et la bénédiction qui te protégera des ténèbres. Aldric a rejoint '
        'la résistance aux Terres d\'Ombre, au sud-ouest. La Citadelle de Malveth t\'attend.', btn='Recevoir la Lame de l\'Aube')
# ---- VIII · Ombre
st('talk', 8, 'Rejoins le capitaine Aldric au camp rebelle (Terres d\'Ombre)', npc='aldric_sw', at=tgt('aldric_sw'), rw=(200, 200),
   text='Te voilà ! Trois pylônes noirs alimentent le bouclier de la Citadelle. Détruis-les et la grille tombera.', btn='Je détruis les pylônes')
st('interact', 8, 'Détruis les 3 pylônes noirs dans la cour de la Citadelle (clic droit)', pts=SP['pylons'], label='🜏 Pylône noir', done='Le pylône se brise !', door='citadel')
st('boss', 8, 'Abats l\'archimage Malveth dans la salle du trône', boss='malveth', at=T(*S.ARENAS['malveth']['c']))
st('go', 8, 'Monte au sommet de la Citadelle (escalier du donjon)', at=T(*S.ARENAS['nyxar']['c']), r=12)
st('boss', 8, 'Abats Nyxar, le dragon de la Lune Noire', boss='nyxar', at=T(*S.ARENAS['nyxar']['c']))
# ---- épilogue
st('talk', 9, 'Retourne à Havreclair : la régente Isolde t\'attend dans la salle du trône', npc='isolde', at=tgt('regent'), rw=(3000, 3000), give='finale',
   text='La Pierre-Lune est reformée et l\'Aube se lève enfin sur Ombrelune. Au nom de tout le royaume : merci, Porteur de l\'Aube. Ton nom sera gravé '
        'au-dessus de la porte de la cité.', btn='Recevoir les honneurs')
END = st('end', 9, 'Héros d\'Ombrelune : contrats, donjons, boss à revaincre, grimoire et trésors cachés')
UNLOCK = {}
for i, s_ in enumerate(STEPS):
    if s_.get('unlock'):
        UNLOCK[s_['unlock']] = i + 1
BOSS_STEP = {s_['boss']: i for i, s_ in enumerate(STEPS) if s_['kind'] == 'boss'}

# ---------------------------------------------------------------- moteur : avancer, annoncer, localiser
ADV = ['# @s passe à l\'étape suivante de la campagne', 'scoreboard players add @s mg.olch 1', 'scoreboard players set @s mg.olqp 0',
       f'function mg:{P}/q/start', f'function mg:{P}/q/say', f'function mg:{P}/qloc',
       'execute at @s run playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.8 0.9']
w('q/adv', ADV)
SAY = ['# @s : annonce de l\'objectif']
QL = ['# @s : 📍 localisateur et indicateur vers l\'objectif de la campagne (sauf contrat suivi)', 'execute if score @s mg.olcf matches 1 run return 0']
HUD = ['# @s : objectif de la campagne dans la barre d\'action']
START = ['# @s vient d\'arriver à l\'étape (titres de chapitre, déblocages, cinématiques)']
for i, s_ in enumerate(STEPS):
    ch = CH_NAMES[s_['ch']]
    SAY.append(f'execute if score @s mg.olch matches {i} run return run tellraw @s ' +
               js([TEXT('📜 ', 'gold'), TEXT(ch, 'gold', bold=True), TEXT(' : ', 'dark_gray'), TEXT(s_['obj'], 'yellow')]))
    at = s_.get('at')
    if s_['kind'] in ('collect', 'interact') and not at:
        at = T(*s_['pts'][0])
    if at:
        QL.append(f'execute if score @s mg.olch matches {i} run return run function mg:{P}/loc {{x:{at[0]},y:{at[1]},z:{at[2]}}}')
    s_['at'] = at
    if i > 0 and STEPS[i - 1]['ch'] != s_['ch']:
        START.append(f'execute if score @s mg.olch matches {i} run function mg:{P}/q/chapter {{t:"{CH_NAMES[s_["ch"]]}"}}')
QL += [f'function mg:{P}/loc {{x:6,y:65,z:6}}', 'scoreboard players set @s mg.olon 0']
SAY.append('tellraw @s {"text":"📜 Aucune étape.","color":"gray"}')
w('q/say', SAY)
w('qloc', QL)
w('q/chapter', ['# @s : titre du nouveau chapitre', 'title @s times 15 70 20', '$title @s title {"text":"$(t)","color":"gold","bold":true}',
                'title @s subtitle {"text":"Nouveau chapitre","color":"gray"}', 'execute at @s run playsound minecraft:event.mob_effect.raid_omen player @s ~ ~ ~ 0.6 1.2'])
for r, n in UNLOCK.items():
    START.append(f'execute if score @s mg.olch matches {n} run function mg:{P}/cs/open_{r}')
START.append(f'execute if score @s mg.olch matches {END} run function mg:{P}/cs/finale')
w('q/start', START)

# ---------------------------------------------------------------- dialogues de campagne (étapes « parler à » et « matériaux »)
GIVE = {'pots': [f'give @s {CL.HEAL_POT} 3', f'give @s {CL.MANA_POT} 3', 'tellraw @s {"text":"  +3 potions de soin, +3 potions de mana","color":"red"}'],
        'fur': ['scoreboard players set @s mg.olfur 1', 'tellraw @s {"text":"🧥 Cape de fourrure : tu ne crains plus le froid de Givrecroc.","color":"aqua"}'],
        'fire': ['scoreboard players set @s mg.olfire 1', 'tellraw @s {"text":"🔥 Talisman ignifuge : la chaleur de Pyrecendre ne t\'atteint plus.","color":"gold"}'],
        'dawn': ['scoreboard players set @s mg.olwt 9', 'scoreboard players set @s mg.olbless 1', f'function mg:{P}/kit',
                 'title @s times 10 60 20', 'title @s title {"text":"LAME DE L\'AUBE","color":"gold","bold":true}',
                 'title @s subtitle {"text":"Arme de palier 9 · bénédiction contre les ténèbres","color":"yellow"}',
                 'execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.5 1 0.5 0.4 80'],
        'finale': ['scoreboard players set @s mg.olat 9', f'function mg:{P}/kit',
                   'tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" a sauvé Ombrelune !","color":"gold"}]',
                   'tellraw @s {"text":"🛡 Armure de l\'Aube reçue (palier 9).","color":"gold"}']}
TALK_TK = []
for i, s_ in enumerate(STEPS):
    if s_['kind'] not in ('talk', 'mat'):
        continue
    nm_, col = NPCS[s_['npc']][0], NPCS[s_['npc']][1]
    xp, gold = s_['rw']
    D = dlg(nm_, col, s_['text'], [(s_['btn'], 'green', CH_NAMES[s_['ch']], 1000 + i)])
    w(f'q/d{i}', [f'# Étape {i} : dialogue de {s_["npc"]}'] + show(D))
    DONE = [f'# Étape {i} validée ({s_["npc"]})']
    if s_['kind'] == 'mat':
        mo, mn, mc = M.MATS[s_['mat']]
        DONE += [f'execute unless score @s {mo} matches {s_["n"]}.. run return run tellraw @s ' +
                 js([TEXT(f'Il te faut {s_["n"]} × {mn} (tu en as ', 'red'), {'score': {'name': '@s', 'objective': mo}, 'color': 'yellow'}, TEXT(').', 'red')]),
                 f'scoreboard players remove @s {mo} {s_["n"]}']
    if gold:
        DONE.append(f'scoreboard players add @s mg.olg {gold}')
        DONE.append(f'tellraw @s {{"text":"  +{gold} 💰","color":"gold"}}')
    if xp:
        DONE.append(f'function mg:{P}/xp {{n:{xp}}}')
    if s_.get('shard'):
        DONE += [f'scoreboard players set @s mg.olsh {s_["shard"]}', 'title @s times 10 50 15',
                 f'title @s title {js(TEXT("✦ ÉCLAT DE LUNE " + str(s_["shard"]) + " / 8", "light_purple", bold=True))}',
                 'execute at @s run playsound minecraft:block.amethyst_block.resonate player @s ~ ~ ~ 1 0.8']
    DONE += GIVE.get(s_.get('give'), [])
    DONE += [f'function mg:{P}/q/adv', 'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1']
    w(f'q/ok{i}', DONE)
    TALK_TK.append(f'execute if score $tk mg.st matches {1000 + i} if score @s mg.olch matches {i} run function mg:{P}/q/ok{i}')

# ---------------------------------------------------------------- étapes « vaincre N monstres »
KH = ['# @s a vaincu l\'espèce n° $kk : campagne, quêtes secondaires, contrat']
for i, s_ in enumerate(STEPS):
    if s_['kind'] == 'kill':
        for k in s_['kinds']:
            KH.append(f'execute if score @s mg.olch matches {i} if score $kk mg.st matches {M.KIDX[k]} run function mg:{P}/q/kp {{n:{s_["n"]}}}')
w('q/kp', ['# @s : un monstre de plus pour l\'étape (objectif $(n))', 'scoreboard players add @s mg.olqp 1',
           '$execute if score @s mg.olqp matches $(n).. run return run function mg:ombre/q/adv',
           '$tellraw @s [{"text":"⚔ Progression : ","color":"gold"},{"score":{"name":"@s","objective":"mg.olqp"},"color":"yellow","bold":true},{"text":" / $(n)","color":"yellow"}]'])

# ---------------------------------------------------------------- étapes « ramasser » (accroupi 1,5 s) et « activer » (clic droit)
COL_TICK = ['# Toutes les 5 ticks : ramassage (accroupi près d\'un objet de l\'étape en cours)']
SETUP_Q = ['# Session : objets de quête (sacs, cocons, scarabées, totems, runes, socles, pylônes)']
INT_FN = ['# @s (joueur) a cliqué l\'objet de quête n° $qid (étape × 10 + n°)']
for i, s_ in enumerate(STEPS):
    if s_['kind'] not in ('collect', 'interact'):
        continue
    n = len(s_['pts'])
    full = 2 ** n - 1
    for j, (x, y, z) in enumerate(s_['pts']):
        qid = i * 10 + j
        x, y, z = int(math.floor(x)), int(y), int(math.floor(z))
        if s_['kind'] == 'collect':
            SETUP_Q += [f'summon minecraft:item_display {x + 0.5} {y + 0.4} {z + 0.5} {{Tags:["mg.ol","mg.olspin"],item:{{id:"minecraft:{s_["item"]}",count:1}},'
                        'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]},Glowing:1b}',
                        tdisp(x + 0.5, y + 1.3, z + 0.5, TEXT(s_['label'], 'yellow', bold=True), 0.6)]
            COL_TICK.append(f'execute positioned {x + 0.5} {y} {z + 0.5} as @a[tag=mg.olw,scores={{mg.olch={i}}},distance=..2.2] if predicate mg:sneak run function mg:{P}/q/col {{q:{qid},b:{j},f:{full}}}')
        else:
            if s_['item'] if 'item' in s_ else False:
                SETUP_Q.append(f'summon minecraft:item_display {x + 0.5} {y + 0.8} {z + 0.5} {{Tags:["mg.ol"],item:{{id:"minecraft:{s_["item"]}",count:1}},'
                               'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.6f,1.6f,1.6f]}}')
            SETUP_Q += [f'summon minecraft:interaction {x + 0.5} {y} {z + 0.5} {{Tags:["mg.ol","mg.olint","mg.olnn"],width:1.6f,height:2.6f,response:1b}}',
                        f'scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid {qid}', 'tag @e[tag=mg.olnn] remove mg.olnn',
                        tdisp(x + 0.5, y + 2.9, z + 0.5, [TEXT(s_['label'] + '\n', 'gold', bold=True), TEXT('clic droit', 'gray', bold=False)], 0.6)]
            INT_FN.append(f'execute if score $qid mg.st matches {qid} if score @s mg.olch matches {i} run function mg:{P}/q/act {{b:{j},f:{full},x:{x},y:{y},z:{z}}}')
    if s_['kind'] == 'interact':
        door = s_.get('door')
        w(f'q/actdone{i}', [f'# Étape {i} : tous les objets activés'] + ([f'execute in {DIM} run function mg:{P}/door/{door}_open'] if door else []) +
          [f'function mg:{P}/q/adv'])
w('q/coltick', COL_TICK)
w('q/col', ['# @s ramasse un objet n° $(b) de son étape (1,5 s accroupi)', 'scoreboard players set @s mg.olal 10',
            '$function mg:ombre/q/colbit {b:$(b),f:$(f)}'])
w('q/colbit', ['# bit $(b) déjà pris ?', '$execute store result score $m mg.st run function mg:ombre/q/pow2 {b:$(b)}',
               'scoreboard players operation $t mg.st = @s mg.olqp', 'scoreboard players operation $t mg.st /= $m mg.st', 'scoreboard players operation $t mg.st %= #2 mg.st',
               'execute if score $t mg.st matches 1 run return run title @s actionbar {"text":"✔ Déjà ramassé","color":"gray"}',
               'scoreboard players add @s mg.olpk 1',
               'execute if score @s mg.olpk matches ..5 run title @s actionbar {"text":"✋ Ramassage…","color":"yellow"}',
               'execute if score @s mg.olpk matches ..5 run return 0', 'scoreboard players set @s mg.olpk 0',
               'scoreboard players operation @s mg.olqp += $m mg.st', 'title @s actionbar {"text":"✔ Ramassé !","color":"green","bold":true}',
               'execute at @s run playsound minecraft:entity.item.pickup player @s ~ ~ ~ 1 0.8', f'function mg:{P}/xp {{n:40}}',
               '$execute if score @s mg.olqp matches $(f).. run function mg:ombre/q/adv'])
w('q/pow2', ['$return run scoreboard players get #p$(b) mg.st'])
w('q/act', ['# @s active l\'objet $(b) de son étape', '$execute store result score $m mg.st run function mg:ombre/q/pow2 {b:$(b)}',
            'scoreboard players operation $t mg.st = @s mg.olqp', 'scoreboard players operation $t mg.st /= $m mg.st', 'scoreboard players operation $t mg.st %= #2 mg.st',
            'execute if score $t mg.st matches 1 run return run title @s actionbar {"text":"✔ Déjà fait","color":"gray"}',
            'scoreboard players operation @s mg.olqp += $m mg.st', f'function mg:{P}/xp {{n:60}}',
            '$execute positioned $(x) $(y) $(z) run particle minecraft:explosion ~0.5 ~1 ~0.5 0.4 0.6 0.4 0 3 force',
            '$execute positioned $(x) $(y) $(z) run particle minecraft:end_rod ~0.5 ~1.5 ~0.5 0.3 1 0.3 0.1 40 force',
            'execute at @s run playsound minecraft:block.respawn_anchor.deplete player @a ~ ~ ~ 1 1.2',
            'title @s actionbar {"text":"✦ Fait !","color":"gold","bold":true}', 'scoreboard players set @s mg.olal 30',
            '$execute if score @s mg.olqp matches $(f).. run function mg:ombre/q/actdone_any'])
ACT_ANY = ['# @s a tout activé : fin de l\'étape']
for i, s_ in enumerate(STEPS):
    if s_['kind'] == 'interact':
        ACT_ANY.append(f'execute if score @s mg.olch matches {i} run return run function mg:{P}/q/actdone{i}')
w('q/actdone_any', ACT_ANY)
w('q/int', ['# @s (interaction d\'objet de quête) : le joueur qui a cliqué', 'scoreboard players operation $qid mg.st = @s mg.olnid',
            f'execute on target if entity @s[tag=mg.olw] run function mg:{P}/q/int_p', 'data remove entity @s interaction', 'data remove entity @s attack'])
w('q/int_p', INT_FN)
GO = ['# Chaque seconde, @s : étapes « aller à »']
for i, s_ in enumerate(STEPS):
    if s_['kind'] == 'go':
        x, y, z = s_['at']
        GO.append(f'execute if score @s mg.olch matches {i} positioned {x} {y} {z} if entity @s[distance=..{s_["r"]}] run function mg:{P}/q/adv')
w('q/gotick', GO)

# portes (ouvertes quand l'étape est finie par un joueur, refermées à chaque session)
x1, y1, z1, x2, y2, z2 = SP['kgate_door']
cx1, cy1, cz1, cx2, cy2, cz2 = SP['cit_gate']
px, py, pz = SP['pyr_door']
DOORS = {'kgate': ([f'fill {x1} {y1} {z1} {x2} {y2} {z2} minecraft:air'], [f'fill {x1} {y1} {z1} {x2} {y2} {z2} minecraft:deepslate_tiles']),
         'citadel': ([f'fill {cx1} {cy1} {cz1} {cx2} {cy2} {cz2} minecraft:air'], [f'fill {cx1} {cy1} {cz1} {cx2} {cy2} {cz2} minecraft:iron_bars']),
         'pyramid': ([f'fill {px - 1} {py} {pz} {px + 1} {py + 2} {pz} minecraft:air'], [f'fill {px - 1} {py} {pz} {px + 1} {py + 2} {pz} minecraft:chiseled_sandstone'])}
for k, (op, _) in DOORS.items():
    w(f'door/{k}_open', [f'# Porte {k} : ouverte', 'playsound minecraft:block.iron_door.open master @a ~ ~ ~ 1 0.5'] + op)

# ================================================================ quêtes secondaires
SIDE = {  # n° : (PNJ, titre, texte, type, cible, quantité, (xp, or, bonus))
    1: ('gaspard', 'Les loups du berger', 'Les loups déciment mon troupeau. Abats-en 6 et je te paierai de ma poche.', 'kill', ['loup'], 6, (200, 150, None)),
    2: ('marthe', 'Le cidre des cryptes', 'Des goules ont emporté mon meilleur tonneau dans les cryptes sous la chapelle de Valdor. Vide les cryptes !', 'dungeon', 'crypt', 1, (400, 250, 'gem')),
    3: ('thalion', 'Cordes d\'arc', 'Nos arcs manquent de cordes. Rapporte-moi 8 soies d\'araignée.', 'mat', 2, 8, (350, 250, 'gem')),
    4: ('thalion', 'Le nid des tisseuses', 'Un nid de tisseuses grouille dans une caverne à l\'ouest. Purge-le jusqu\'à son alpha.', 'dungeon', 'nest', 1, (600, 350, 'gem')),
    5: ('sigrun', 'Fourrures d\'ours', 'Les ours des glaces rôdent près du village. Abats-en 4.', 'kill', ['ours'], 4, (500, 300, None)),
    6: ('bjorn', 'La grotte de givre', 'Un wendigo hante la grotte de givre à l\'ouest du lac gelé. Débarrasse-nous de lui.', 'dungeon', 'ice', 1, (800, 450, 'gem')),
    7: ('odo', 'Sangsues géantes', 'Les sangsues géantes infestent les mares. Abats-en 6.', 'kill', ['sangsue'], 6, (700, 400, None)),
    8: ('maelle', 'Le temple englouti', 'Un ancien temple de l\'Aube a sombré dans le marais. Libère-le du gardien noyé.', 'dungeon', 'sunken', 1, (1000, 600, 'gem')),
    9: ('zahra', 'Ambre du désert', 'Je taille des bijoux dans l\'ambre solaire. Apporte-m\'en 6.', 'mat', 5, 6, (900, 500, 'gem')),
    10: ('kassim', 'Les tombeaux d\'Azhar', 'Des pillards ont réveillé une momie royale dans les tombeaux au sud-est. Arrête-la.', 'dungeon', 'tomb', 1, (1200, 700, 'gem')),
    11: ('durgan', 'Élémentaires de feu', 'Les élémentaires de feu harcèlent le bastion. Éteins-en 6.', 'kill', ['feu'], 6, (1100, 600, None)),
    12: ('durgan', 'La forge écarlate', 'Mon ancien maître, devenu un forgeron calciné, hante la forge écarlate à l\'est. Libère son âme.', 'dungeon', 'forge', 1, (1400, 800, 'gem')),
    13: ('thrain', 'Runite pour la forge', 'Il nous faut de la runite pour reforger nos armes. Rapporte-m\'en 8.', 'mat', 7, 8, (1300, 800, 'gem')),
    14: ('thrain', 'Les mines profondes', 'Un contremaître maudit tient encore les mines profondes. Reprends-les.', 'dungeon', 'mine', 1, (1700, 1000, 'gem')),
    15: ('aldric_sw', 'Chevaliers noirs', 'Les chevaliers noirs patrouillent autour du camp. Abats-en 6.', 'kill', ['chevnoir'], 6, (1600, 900, None)),
    16: ('aldric_sw', 'Le puits des âmes', 'Le puits des âmes, à l\'ouest, nourrit l\'armée de Malveth. Tue son gardien.', 'dungeon', 'souls', 1, (2000, 1200, 'gem')),
}
SIDE_BY_NPC = {}
for q, (npc, *r_) in SIDE.items():
    SIDE_BY_NPC.setdefault(npc, []).append(q)
DUN_IDX = {k: i for i, k in enumerate(S.DUNGEONS)}
SQ_TK = []
for q, (npc, title, text, typ, target, n, (xp, gold, bonus)) in SIDE.items():
    b = q - 1
    rew = f'{xp} XP, {gold} 💰' + (', 1 gemme (+1 point)' if bonus == 'gem' else '')
    if typ == 'kill':
        cond_txt = f'{n} victoires'
    elif typ == 'mat':
        cond_txt = f'{n} × {M.MATS[target][1]}'
    else:
        cond_txt = 'donjon terminé'
    ACC = [f'# @s accepte « {title} »'] + bit_test('mg.olsd', b) + ['execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà terminée.","color":"gray"}'] + \
        bit_test('mg.olsa', b) + ['execute if score $b mg.st matches 1 run return run tellraw @s {"text":"Quête déjà en cours.","color":"gray"}',
                                  f'scoreboard players operation @s mg.olsa += #p{b} mg.st', f'scoreboard players set @s mg.olq{q} 0',
                                  'tellraw @s ' + js([TEXT('❗ Quête secondaire : ', 'yellow', bold=True), TEXT(title + ' : ' + text, 'gray')])]
    w(f'sq/{q}_acc', ACC)
    TURN = [f'# @s rend « {title} »'] + bit_test('mg.olsa', b) + ['execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d\'abord la quête.","color":"gray"}']
    if typ == 'kill':
        TURN.append(f'execute unless score @s mg.olq{q} matches {n}.. run return run tellraw @s [{{"text":"Progression : ","color":"red"}},{{"score":{{"name":"@s","objective":"mg.olq{q}"}},"color":"yellow"}},{{"text":" / {n}","color":"yellow"}}]')
    elif typ == 'mat':
        mo = M.MATS[target][0]
        TURN += [f'execute unless score @s {mo} matches {n}.. run return run tellraw @s {js(TEXT(f"Il en faut {n}.", "red"))}', f'scoreboard players remove @s {mo} {n}']
    else:
        TURN += bit_test('mg.oldg', DUN_IDX[target]) + ['execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Le donjon n\'est pas encore terminé.","color":"red"}']
    TURN += [f'scoreboard players operation @s mg.olsa -= #p{b} mg.st', f'scoreboard players operation @s mg.olsd += #p{b} mg.st',
             f'scoreboard players add @s mg.olg {gold}', f'function mg:{P}/xp {{n:{xp}}}', 'title @s times 5 40 10',
             f'title @s title {js(TEXT("✔ " + title, "yellow", bold=True))}', f'title @s subtitle {js(TEXT(rew, "gray"))}',
             'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1']
    if bonus == 'gem':
        TURN.append('scoreboard players add @s mg.olsp 1')
    w(f'sq/{q}_turn', TURN)
    SQ_TK += [f'execute if score $tk mg.st matches {400 + q * 2} run function mg:{P}/sq/{q}_acc',
              f'execute if score $tk mg.st matches {401 + q * 2} run function mg:{P}/sq/{q}_turn']
    if typ == 'kill':
        for k in target:
            KH.append(f'execute if score $kk mg.st matches {M.KIDX[k]} if function mg:{P}/sq/{q}_on run scoreboard players add @s mg.olq{q} 1')
        w(f'sq/{q}_on', bit_test('mg.olsa', b) + ['return run scoreboard players get $b mg.st'])
# contrat : espèce suivie (mg.olct = n° + 1)
KH += ['scoreboard players operation $kc mg.st = $kk mg.st', 'scoreboard players add $kc mg.st 1',
       'execute if score @s mg.olct = $kc mg.st run function mg:ombre/ct/prog']
w('khook', KH)

# ================================================================ dialogues génériques des PNJ (services, quêtes secondaires)
SERV = {  # PNJ -> boutons de service (étiquette, couleur, infobulle, n°)
    'liora': [('📜 Rappel de l\'objectif', 'yellow', 'Objectif en cours', 9)],
    'liora_t': [('📜 Rappel de l\'objectif', 'yellow', 'Objectif en cours', 9)],
    'orren': [('🎖 Choisir / changer de classe', 'gold', 'Chevalier, Rôdeur, Mage, Clerc', 500), ('📋 Contrats de la guilde', 'yellow', 'Chasses répétables', 850),
              ('♻ Redistribuer mes points (300 💰)', 'gray', 'Tous tes points de caractéristique', 709)],
    'aldric': [('📜 Rappel de l\'objectif', 'yellow', 'Objectif en cours', 9)],
    'isolde': [('📜 Rappel de l\'objectif', 'yellow', 'Objectif en cours', 9)],
    'bram': [('⚔ Améliorer mon arme', 'red', 'Palier suivant (or + matériaux)', 801), ('🛡 Améliorer mon armure', 'red', 'Palier suivant (or + matériaux)', 802)],
    'elsa': [('✚ 3 potions de soin : 60 💰', 'red', 'Soin instantané', 651), ('✦ 3 potions de mana : 60 💰', 'aqua', '+60 mana chacune', 652)],
    'fenna': [('💪 Élixir de force : 80 💰 + 2 venins', 'dark_green', 'Force I pendant 3 min', 653), ('🪨 Élixir de pierre : 120 💰 + 2 runites', 'gray', 'Résistance I pendant 3 min', 654),
              ('💨 Élixir de vent : 60 💰 + 2 soies', 'green', 'Vitesse I pendant 3 min', 655), ('✦ 3 potions de mana : 60 💰', 'aqua', '+60 mana chacune', 652)],
    'joss': [('🐴 Acheter un destrier : 400 💰', 'gold', 'Sifflet en case 7 : il accourt et tu le montes', 656)],
    'marthe': [('🍺 Se reposer (soins)', 'gold', 'Tu récupères toute ta vie et ta mana', 657), ('💬 Les rumeurs', 'gray', 'Ce qu\'on raconte à l\'auberge', 658)],
    'sigrun': [('🧥 Cape de fourrure : 5 peaux', 'aqua', 'Protège du froid de Givrecroc', 659)],
    'odo': [('✚ 3 potions de soin : 60 💰', 'red', 'Soin instantané', 651)],
    'kassim': [('✦ 3 potions de mana : 60 💰', 'aqua', '+60 mana chacune', 652)],
    'durgan': [('⚔ Améliorer mon arme', 'red', 'Palier suivant', 801), ('🛡 Améliorer mon armure', 'red', 'Palier suivant', 802)],
    'thrain': [('📜 Rappel de l\'objectif', 'yellow', 'Objectif en cours', 9)],
    'aldric_sw': [('✚ 3 potions de soin : 60 💰', 'red', 'Soin instantané', 651)],
    'tessa': [('📜 Rappel de l\'objectif', 'yellow', 'Objectif en cours', 9)], 'gaspard': [], 'elyndra': [('📜 Rappel de l\'objectif', 'yellow', 'Objectif en cours', 9)],
    'thalion': [], 'bjorn': [], 'maelle': [], 'zahra': [],
}
GREET = {
    'liora': 'La Pierre-Lune attend d\'être reformée. Chaque éclat retrouvé rallume un peu l\'Aube.',
    'liora_t': 'Le temple de l\'Aube garde l\'autel de la Pierre-Lune. Prie, si tu le souhaites.',
    'orren': 'Un bon guerrier choisit sa voie… et l\'affûte chaque jour. Les contrats de la guilde paient bien.',
    'aldric': 'La garde tient les murs, mais pas les routes. Reviens me voir quand tu as du nouveau.',
    'isolde': 'Havreclair a survécu cent ans dans l\'ombre. Tant que je serai régente, elle tiendra.',
    'bram': 'Apporte-moi de l\'or et des matériaux des régions : je forge du solide. Chaque région te fournit son matériau.',
    'elsa': 'Potions fraîches, à prix d\'ami !', 'fenna': 'Mes élixirs ont besoin d\'ingrédients rares : venin, runite, soie.',
    'joss': 'Un destrier rapide, ça change une vie d\'aventurier.', 'marthe': 'Assieds-toi, voyageur. Un bon lit, une bonne soupe, et les meilleures rumeurs du royaume.',
    'tessa': 'Brumecombe se relève grâce à toi.', 'gaspard': 'Mes moutons, mes pauvres moutons…', 'elyndra': 'La forêt se souvient de ceux qui la protègent.',
    'thalion': 'Mon arc ne rate jamais sa cible. Enfin, presque jamais.', 'bjorn': 'Une corne d\'hydromel pour le héros ! Plus tard. D\'abord, le travail.',
    'sigrun': 'Le froid ne pardonne pas. Une bonne fourrure, si.', 'maelle': 'Que l\'Aube éclaire ton chemin dans la brume.',
    'odo': 'Chaque plante du marais soigne… ou tue.', 'kassim': 'Le désert appartient à ceux qui savent lire les étoiles.',
    'zahra': 'L\'ambre solaire capture la lumière d\'un millier de jours.', 'durgan': 'Par ma barbe ! Encore un qui veut affronter le dragon ?',
    'thrain': 'Khazgarde, mon foyer… Je la reverrai.', 'aldric_sw': 'La Citadelle est imprenable, disent-ils. On verra bien.',
}
for npc, (name, col, pos, prof, typ, reg) in NPCS.items():
    L = [f'# @s parle à {npc}']
    for i, s_ in enumerate(STEPS):
        if s_['kind'] in ('talk', 'mat') and s_['npc'] == npc:
            L.append(f'execute if score @s mg.olch matches {i} run return run function mg:{P}/q/d{i}')
    btn = list(SERV.get(npc, []))
    for q in SIDE_BY_NPC.get(npc, []):
        _, title, text, typ_, tg, n_, (xp, gold, bonus) = SIDE[q]
        btn.append((f'❗ {title}', 'yellow', text, 400 + q * 2))
        btn.append((f'✔ Rendre : {title}', 'green', f'Récompense : {xp} XP, {gold} 💰', 401 + q * 2))
    D = dlg(name, col, GREET.get(npc, '…'), btn)
    w(f'npc/{npc}_gen', show(D))
    L.append(f'function mg:{P}/npc/{npc}_gen')
    w(f'npc/{npc}', L)
w('npc/any', ['# @s parle au PNJ n° $npc'] + [f'execute if score $npc mg.st matches {i} run return run function mg:{P}/npc/{k}' for k, i in NPC_ID.items()])
w('npc/int', ['# @s (interaction d\'un PNJ) : le joueur qui a cliqué lui parle', 'scoreboard players operation $npc mg.st = @s mg.olnid',
              f'execute on target if entity @s[tag=mg.olw] run function mg:{P}/npc/any', 'data remove entity @s interaction'])
VTYPE = {'plains': 'plains', 'jungle': 'jungle', 'snow': 'snow', 'swamp': 'swamp', 'desert': 'desert', 'savanna': 'savanna', 'taiga': 'taiga'}
SETUP_NPC = ['# Session : PNJ (villageois immobiles + zone de clic)']
for npc, (name, col, (x, y, z), prof, typ, reg) in NPCS.items():
    SETUP_NPC += [f'summon minecraft:villager {x} {y} {z} {{Tags:["mg.ol","mg.olnpcv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,'
                  f'VillagerData:{{profession:"minecraft:{prof}",level:5,type:"minecraft:{VTYPE[typ]}"}},Offers:{{Recipes:[]}},CustomName:{js(TEXT(name, col))},CustomNameVisible:1b}}',
                  f'summon minecraft:interaction {x} {y} {z} {{Tags:["mg.ol","mg.olnpc","mg.olnn"],width:1.1f,height:2.2f,response:1b}}',
                  f'scoreboard players set @e[tag=mg.olnn,limit=1] mg.olnid {NPC_ID[npc]}', 'tag @e[tag=mg.olnn] remove mg.olnn',
                  tdisp(x, y + 2.35, z, TEXT('💬 clic droit', 'gray'), 0.6)]
# marqueur « ! » au-dessus des PNJ qui ont quelque chose pour le joueur : affiché dans le chat à l'approche (léger)

# ================================================================ boutiques, forge, auberge, écurie
def buy(price, lines, what):
    return [f'execute unless score @s mg.olg matches {price}.. run return run function mg:{P}/sh/poor', f'scoreboard players remove @s mg.olg {price}'] + lines + \
        ['scoreboard players set @s mg.olal 40', f'title @s actionbar {js([TEXT("✔ " + what + " ", "green", bold=True), TEXT(f"(-{price} 💰)", "gold")])}',
         'execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1']


w('sh/poor', say('Pas assez d\'or 💰', 'red') + ['execute at @s run playsound minecraft:entity.villager.no player @s ~ ~ ~ 0.8 1'])
w('sh/651', buy(60, [f'give @s {CL.HEAL_POT} 3'], '3 potions de soin'))
w('sh/652', buy(60, [f'give @s {CL.MANA_POT} 3'], '3 potions de mana'))


def elixir(n, price, mat, q, eff, what):
    mo = M.MATS[mat][0]
    w(f'sh/{n}', [f'execute unless score @s {mo} matches {q}.. run return run tellraw @s {js(TEXT(f"Il faut {q} × {M.MATS[mat][1]}.", "red"))}'] +
      buy(price, [f'scoreboard players remove @s {mo} {q}', f'effect give @s minecraft:{eff} 180 0'], what))


elixir(653, 80, 4, 2, 'strength', 'Élixir de force')
elixir(654, 120, 7, 2, 'resistance', 'Élixir de pierre')
elixir(655, 60, 2, 2, 'speed', 'Élixir de vent')
w('sh/656', ['execute if score @s mg.olhorse matches 1.. run return run tellraw @s {"text":"Tu as déjà un destrier : siffle-le (case 7) !","color":"yellow"}'] +
  buy(400, ['scoreboard players set @s mg.olhorse 1', f'item replace entity @s hotbar.6 with {CL.WHISTLE}'], 'Destrier'))
w('sh/657', ['function mg:core/heal', 'scoreboard players operation @s mg.olmp = @s mg.olmm', f'function mg:{P}/mana_bar',
             'tellraw @s {"text":"🍺 Tu te reposes un moment près du feu. Vie et mana restaurées.","color":"gold"}'])
RUMORS = ['On dit que trois coffres sont cachés dans chaque région, marqués d\'un fanion rouge.',
          'Les pages du grimoire de Malveth racontent son histoire. Il en reste une dans presque chaque lieu important.',
          'Les élites brillent d\'un contour doré. Elles lâchent parfois des gemmes de lune.',
          'Le maître d\'armes paie bien pour chaque chasse inscrite au tableau de la guilde.',
          'Les pierres d\'appel permettent de voyager d\'une région à l\'autre en un clin d\'œil.']
R_ = ['execute store result score $r mg.st run random value 0..4'] + [f'execute if score $r mg.st matches {i} run tellraw @s {js(TEXT("🍺 « " + t + " »", "gray"))}'
                                                                      for i, t in enumerate(RUMORS)]
w('sh/658', R_)
w('sh/659', ['execute if score @s mg.olfur matches 1.. run return run tellraw @s {"text":"Tu as déjà une cape de fourrure.","color":"yellow"}',
             'execute unless score @s mg.olm1 matches 5.. run return run tellraw @s {"text":"Il faut 5 peaux de bête.","color":"red"}',
             'scoreboard players remove @s mg.olm1 5'] + GIVE['fur'])
# forge
FW = ['# @s : améliorer son arme (palier suivant)', 'execute if score @s mg.olwt matches 8.. run return run tellraw @s {"text":"⚒ « Au-delà, seule la magie de l\'Aube peut forger mieux. »","color":"yellow"}',
      'execute if score @s mg.olcl matches 0 run return run tellraw @s {"text":"⚒ « Choisis d\'abord ta voie à la guilde. »","color":"red"}']
for t, (gold, mat, q, lv) in CL.FORGE_W.items():
    FW.append(f'execute if score @s mg.olwt matches {t - 1} run return run function mg:{P}/sh/fw{t}')
    mo, mn, mc = M.MATS[mat]
    w(f'sh/fw{t}', [f'# arme palier {t}', f'execute unless score @s mg.ollv matches {lv}.. run return run tellraw @s {js(TEXT(f"⚒ « Reviens au niveau {lv}. »", "red"))}',
                    f'execute unless score @s {mo} matches {q}.. run return run tellraw @s {js(TEXT(f"⚒ « Il me faut {q} × {mn} et {gold} 💰. »", "red"))}'] +
      buy(gold, [f'scoreboard players remove @s {mo} {q}', f'scoreboard players set @s mg.olwt {t}', f'function mg:{P}/kit',
                 'execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1', 'execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12'],
          f'Arme {CL.TIER[t][0]}'))
w('sh/801', FW)
FA = ['# @s : améliorer son armure', 'execute if score @s mg.olat matches 8.. run return run tellraw @s {"text":"⚒ « Je ne peux pas faire mieux. »","color":"yellow"}']
for t, (gold, mat, q, lv) in CL.FORGE_A.items():
    FA.append(f'execute if score @s mg.olat matches {t - 1} run return run function mg:{P}/sh/fa{t}')
    mo, mn, mc = M.MATS[mat]
    w(f'sh/fa{t}', [f'# armure palier {t}', f'execute unless score @s mg.ollv matches {lv}.. run return run tellraw @s {js(TEXT(f"⚒ « Reviens au niveau {lv}. »", "red"))}',
                    f'execute unless score @s {mo} matches {q}.. run return run tellraw @s {js(TEXT(f"⚒ « Il me faut {q} × {mn} et {gold} 💰. »", "red"))}'] +
      buy(gold, [f'scoreboard players remove @s {mo} {q}', f'scoreboard players set @s mg.olat {t}', f'function mg:{P}/kit',
                 'execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 0.8'], CL.ARM_NAME[t]))
w('sh/802', FA)

# ================================================================ contrats de la guilde (chasses répétables)
CT_KINDS = [k for r in W.ORDER for k in M.REG_KINDS[r]]
CT = ['# @s : contrat de la guilde (prendre, suivre, rendre)', 'execute if score @s mg.olct matches 1.. if score @s mg.olcp >= @s mg.olcn run return run function mg:ombre/ct/done',
      'execute if score @s mg.olct matches 1.. run return run function mg:ombre/ct/status', 'function mg:ombre/ct/new']
w('ct/menu', CT)
NEW = ['# @s : nouveau contrat : une espèce d\'une région débloquée', 'scoreboard players set $max mg.st 0']
for r in W.ORDER:
    NEW.append(f'execute if score @s mg.olch matches {UNLOCK[r]}.. run scoreboard players set $max mg.st {sum(len(M.REG_KINDS[x]) for x in W.ORDER[:W.ORDER.index(r) + 1])}')
NEW += ['execute if score $max mg.st matches 0 run return run tellraw @s {"text":"📋 « Reviens quand le capitaine t\'aura ouvert les routes. »","color":"gray"}',
        'scoreboard players remove $max mg.st 1', 'execute store result storage mg:ombre ct.m int 1 run scoreboard players get $max mg.st',
        'function mg:ombre/ct/rand with storage mg:ombre ct']
w('ct/new', NEW)
w('ct/rand', ['$execute store result score $r mg.st run random value 0..$(m)'] +
  [f'execute if score $r mg.st matches {i} run function mg:{P}/ct/set {{k:{M.KIDX[k] + 1},n:{6 + 2 * W.ORDER.index(M.K[k]["reg"]) // 2}}}' for i, k in enumerate(CT_KINDS)])
w('ct/set', ['$scoreboard players set @s mg.olct $(k)', '$scoreboard players set @s mg.olcn $(n)', 'scoreboard players set @s mg.olcp 0', 'function mg:ombre/ct/status'])
ST_ = ['# @s : état du contrat']
for k in CT_KINDS:
    d = M.K[k]
    ST_.append(f'execute if score @s mg.olct matches {M.KIDX[k] + 1} run tellraw @s ' + js([TEXT('📋 Contrat : ', 'yellow', bold=True), TEXT(f'{d["name"]} ', d['col'], bold=True),
                                                                                         TEXT(f'({W.REGIONS[d["reg"]][1]}) : ', 'gray'),
                                                                                         {'score': {'name': '@s', 'objective': 'mg.olcp'}, 'color': 'yellow'}, TEXT(' / ', 'gray'),
                                                                                         {'score': {'name': '@s', 'objective': 'mg.olcn'}, 'color': 'yellow'}]))
w('ct/status', ST_)
w('ct/prog', ['scoreboard players add @s mg.olcp 1', 'execute if score @s mg.olcp = @s mg.olcn run tellraw @s {"text":"📋 Contrat rempli : retourne voir Orren à la guilde !","color":"green","bold":true}'])
DONE_ = ['# @s rend son contrat : récompense selon la région de l\'espèce', 'scoreboard players set $g mg.st 0']
for k in CT_KINDS:
    ri = W.ORDER.index(M.K[k]['reg']) + 1
    DONE_.append(f'execute if score @s mg.olct matches {M.KIDX[k] + 1} run scoreboard players set $g mg.st {ri}')
DONE_ += ['scoreboard players operation $c mg.st = $g mg.st', 'scoreboard players operation $c mg.st *= #100 mg.st', 'scoreboard players add $c mg.st 60',
          'scoreboard players operation @s mg.olg += $c mg.st', 'scoreboard players operation $x mg.st = $c mg.st', 'scoreboard players operation $x mg.st *= #2 mg.st',
          'execute store result storage mg:ombre s.n int 1 run scoreboard players get $x mg.st', f'function mg:{P}/xpm with storage mg:ombre s',
          'tellraw @s [{"text":"📋 Contrat rempli : +","color":"green"},{"score":{"name":"$c","objective":"mg.st"},"color":"gold","bold":true},{"text":" 💰","color":"gold"}]',
          'scoreboard players set @s mg.olct 0', 'scoreboard players add @s mg.olcd 1', 'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.2']
w('ct/done', DONE_)

# ================================================================ pierres d'appel (voyage, réapparition)
WAYS = [('hub', 'Havreclair'), ('w', 'Brumecombe'), ('nw', 'Aelindor'), ('n', 'Hrafnheim'), ('ne', 'Village des pilotis'), ('e', 'Oasis d\'Azhar'),
        ('se', 'Bastion des Braises'), ('s', 'Camp nain'), ('sw', 'Camp rebelle')]
WPOS = {k: SP['waystone_' + k] for k, _ in WAYS}
TRAVEL = dlg('🌀 Pierres d\'appel', 'light_purple', 'Les pierres que tu as touchées te permettent d\'y voyager. Tu réapparais à la dernière pierre touchée.',
             [(f'🌀 {name}', 'light_purple', 'Voyager ici', 300 + i) for i, (k, name) in enumerate(WAYS)] +
             [('⌂ Quitter Ombrelune (lobby)', 'gray', 'Retour au monde des mini-jeux', 399)])
w('travel', ['# @s : fenêtre de voyage'] + show(TRAVEL) + ['execute at @s run playsound minecraft:block.beacon.ambient player @s ~ ~ ~ 0.6 1.5'])
WS_TICK = ['# Chaque seconde : pierres d\'appel touchées (5 blocs)']
SETUP_WS = ['# Session : pierres d\'appel']
for i, (k, name) in enumerate(WAYS):
    x, y, z = WPOS[k]
    WS_TICK.append(f'execute positioned {x} {y} {z} as @a[tag=mg.olw,distance=..5] run function mg:{P}/ws/{i}')
    w(f'ws/{i}', [f'# @s touche la pierre « {name} »', f'execute in {DIM} run spawnpoint @s {int(x) + 1} {int(y)} {int(z)}'] + bit_test('mg.olws', i) +
      ['execute if score $b mg.st matches 1 run return 0', f'scoreboard players operation @s mg.olws += #p{i} mg.st',
       'tellraw @s ' + js([TEXT('🌀 Pierre d\'appel éveillée : ', 'light_purple'), TEXT(name, 'yellow', bold=True), TEXT(' (voyage et réapparition)', 'gray')]),
       'execute at @s run playsound minecraft:block.respawn_anchor.charge player @s ~ ~ ~ 1 1.2'])
    w(f'ws/go{i}', [f'# @s voyage vers {name}'] + bit_test('mg.olws', i) +
      ['execute if score $b mg.st matches 0 run return run tellraw @s ' + js(TEXT(f'🌀 La pierre « {name} » n\'est pas encore éveillée : va la toucher.', 'red')),
       'execute if entity @s[tag=mg.olboss_in] run return run tellraw @s {"text":"Impossible pendant un combat de boss.","color":"red"}',
       f'execute in {DIM} run tp @s {x + 1} {y} {z}', f'execute in {DIM} run spawnpoint @s {int(x) + 1} {int(y)} {int(z)}',
       'execute at @s run playsound minecraft:entity.enderman.teleport player @a ~ ~ ~ 0.7 1.2', 'execute at @s run particle minecraft:reverse_portal ~ ~1 ~ 0.4 0.9 0.4 0.05 60'])
    SETUP_WS += [f'summon minecraft:interaction {x} {y} {z} {{Tags:["mg.ol","mg.olway"],width:1.4f,height:2.4f,response:1b}}',
                 tdisp(x, y + 2.5, z, [TEXT('🌀 Pierre d\'appel\n', 'light_purple', bold=True), TEXT(name, 'yellow', bold=False)], 0.7)]
w('ws_tick', WS_TICK)
w('way_int', ['execute on target if entity @s[tag=mg.olw] run function mg:ombre/travel', 'data remove entity @s interaction'])

# ================================================================ lieux à découvrir
POIS = [('Havreclair', 'hub', (0, 65, 0), 50, 0), ('Brumecombe', 'w', W.P['brumecombe'], 20, 40), ('Fort de Brennic', 'w', W.P['bandit_fort'], 22, 40),
        ('Chapelle de Valdor', 'w', W.P['crypt'], 14, 30), ('Moulin de Valdor', 'w', W.P['mill'], 12, 20), ('Aelindor', 'nw', W.P['aelindor'], 24, 60),
        ('Antre d\'Ysh\'tar', 'nw', W.P['spider_lair'], 20, 60), ('Sanctuaire elfique', 'nw', W.P['shrine_nw'], 12, 40), ('Nid des tisseuses', 'nw', W.P['spider_nest'], 12, 40),
        ('Hrafnheim', 'n', W.P['hrafnheim'], 22, 80), ('Forteresse du géant', 'n', W.P['giant_hold'], 20, 80), ('Lac gelé', 'n', W.P['ice_lake'], 22, 50),
        ('Grotte de givre', 'n', W.P['ice_cave'], 12, 50), ('Village des pilotis', 'ne', W.P['stilts'], 22, 100), ('Île de la sorcière', 'ne', W.P['witch_isle'], 30, 100),
        ('Temple englouti', 'ne', W.P['sunken'], 14, 70), ('Oasis d\'Azhar', 'e', W.P['oasis'], 22, 120), ('Pyramide de Sethkar', 'e', W.P['pyramid'], 30, 120),
        ('Obélisques', 'e', W.P['obelisks'], 12, 80), ('Tombeaux d\'Azhar', 'e', W.P['tombs'], 12, 80), ('Bastion des Braises', 'se', W.P['bastion'], 20, 140),
        ('Caldeira', 'se', (W.VX, W.VZ), 20, 140), ('Forge écarlate', 'se', W.P['forge_r'], 14, 100), ('Camp nain', 's', W.P['dwarf_camp'], 20, 160),
        ('Porte de Khazgarde', 's', W.P['kgate'], 18, 160), ('Mines profondes', 's', (W.P['mines'][0], 126), 10, 120), ('Camp rebelle', 'sw', W.P['rebels'], 18, 180),
        ('Citadelle de Malveth', 'sw', W.P['citadel'], 40, 200), ('Puits des âmes', 'sw', W.P['soul_well'], 12, 150)]
PO = ['# Toutes les 2 s : lieux découverts']
for i, (name, reg, c, r, xp) in enumerate(POIS):
    x, z = c[0], c[-1]
    PO.append(f'execute positioned {x} 100 {z} as @a[tag=mg.olw,distance=..{r + 40}] at @s if entity @s[x={x - r},y=0,z={z - r},dx={2 * r},dy=300,dz={2 * r}] run function mg:{P}/poi/{i}')
    L = [f'# @s découvre « {name} »'] + bit_test('mg.olpo', i) + ['execute if score $b mg.st matches 1 run return 0', f'scoreboard players operation @s mg.olpo += #p{i} mg.st']
    if xp:
        L += ['title @s times 10 50 15', f'title @s title {js(TEXT(name, "yellow", bold=True))}', f'title @s subtitle {js(TEXT("✦ Lieu découvert", "gold"))}',
              'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.5 1.6', f'function mg:{P}/xp {{n:{xp}}}']
    w(f'poi/{i}', L)
w('pois', PO)

# ================================================================ pages du grimoire de Malveth (lore)
PAGES = [
    'Page I : J\'étais l\'apprenti le plus doué de l\'Académie de Havreclair. Ils disaient que mon talent était une bénédiction.',
    'Page II : La Pierre-Lune protège le royaume depuis mille ans. Pourquoi la garder sous verre, quand on pourrait en boire la lumière ?',
    'Page III : Les elfes de Sylvanor m\'ont chassé de leurs bois. Ils ont senti l\'ombre en moi avant moi-même.',
    'Page IV : Dans les pics, j\'ai réveillé un géant endormi sous la glace. Il m\'obéit comme un chien.',
    'Page V : La sorcière Morvaine m\'a enseigné le langage des morts. En échange, je lui ai promis le marais.',
    'Page VI : Sous la pyramide dort Sethkar. Je lui ai rendu la vie. Il me doit l\'éternité.',
    'Page VII : Le dragon Ignarok a accepté un éclat comme trésor. Les dragons aiment ce qui brille.',
    'Page VIII : J\'ai brisé la Pierre. Le ciel est devenu noir. Je n\'ai jamais rien vu d\'aussi beau.',
    'Page IX : Les nains de Khazgarde ont scellé leur porte. Mon colosse de runes gardera leurs trésors pour moi.',
    'Page X : Nyxar est né de l\'éclat que j\'ai gardé. Un dragon fait de nuit. Mon enfant.',
    'Page XI : On parle d\'un Porteur de l\'Aube. Une prophétie de vieille femme. Qu\'il vienne.',
    'Page XII : Si quelqu\'un lit ces lignes, c\'est que je suis tombé. Pardonne-moi, Liora. Tu avais raison.',
    'Page XIII : La lumière ne disparaît jamais tout à fait. Elle attend.',
    'Page XIV : Trois coffres par région, avait dit le vieux roi, pour que les braves ne manquent jamais de rien.',
]
LORE = S.LORE[:len(PAGES)]
LO = ['# Toutes les 5 ticks : pages du grimoire (accroupi près d\'une page)']
SETUP_LORE = ['# Session : pages du grimoire (livres posés)']
for i, (reg, x, y, z) in enumerate(LORE):
    LO.append(f'execute positioned {x + 0.5} {y} {z + 0.5} as @a[tag=mg.olw,distance=..2] if predicate mg:sneak run function mg:{P}/pg/{i}')
    SETUP_LORE.append(f'summon minecraft:item_display {x + 0.5} {y + 0.4} {z + 0.5} {{Tags:["mg.ol","mg.olspin"],item:{{id:"minecraft:written_book",count:1}},'
                      'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}')
    w(f'pg/{i}', [f'# @s lit la page {i + 1} du grimoire'] + bit_test('mg.olpg', i) + ['execute if score $b mg.st matches 1 run return 0',
                                                                                 f'scoreboard players operation @s mg.olpg += #p{i} mg.st',
                                                                                 'tellraw @s ' + js([TEXT('📕 Grimoire de Malveth, ', 'dark_purple', bold=True), TEXT(PAGES[i], 'gray', italic=True)]),
                                                                                 f'function mg:{P}/xp {{n:{80 + 20 * i}}}',
                                                                                 'execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 1 0.8'])
LO += [f'execute positioned {x + 0.5} {y + 0.9} {z + 0.5} run particle minecraft:enchant ~ ~ ~ 0.3 0.3 0.3 0.4 2' for (reg, x, y, z) in LORE]
w('pg_tick', LO)

# ================================================================ coffres cachés (3 par région)
CHESTS = []
for r in W.ORDER:
    c_ = []
    for _ in range(5000):
        if len(c_) >= 3:
            break
        x0, z0, x1, z1 = W.rect(r)
        x, z = rq.randrange(x0 + 14, x1 - 14), rq.randrange(z0 + 14, z1 - 14)
        if W.COL[(x, z)][2] or (W.flat_at(x, z) or (0, 0))[1] > 0 or (x, z) in W.ROAD:
            continue
        if any(math.hypot(x - a, z - b) < 40 for a, y_, b in c_):
            continue
        c_.append((x, W.ground(x, z), z))
    CHESTS += [(r, x, y, z) for (x, y, z) in c_]
TC = ['# Toutes les 5 ticks : coffres cachés (accroupi à côté)']
DECO = ['# Session : décor des coffres cachés (coffre, fanion rouge)']
for i, (r, x, y, z) in enumerate(CHESTS):
    ri = W.ORDER.index(r) + 1
    TC.append(f'execute positioned {x + 0.5} {y} {z + 0.5} as @a[tag=mg.olw,distance=..2.2] if predicate mg:sneak run function mg:{P}/tc/{i}')
    DECO += [f'setblock {x} {y} {z} minecraft:chest[facing=south]', f'setblock {x + 1} {y} {z} minecraft:spruce_fence',
             f'setblock {x + 1} {y + 1} {z} minecraft:spruce_fence', f'setblock {x + 1} {y + 2} {z} minecraft:red_wool']
    mo = M.MATS[M.REG_MAT[r]][0]
    w(f'tc/{i}', [f'# @s ouvre le coffre caché n° {i + 1} ({r})'] + bit_test('mg.oltc', i) +
      ['execute if score $b mg.st matches 1 run return run title @s actionbar {"text":"🗝 Déjà fouillé","color":"gray"}',
       f'scoreboard players operation @s mg.oltc += #p{i} mg.st', f'scoreboard players add @s mg.olg {80 * ri}', f'scoreboard players add @s {mo} {2 + ri // 3}',
       f'function mg:{P}/xp {{n:{60 * ri}}}', 'execute store result score $r mg.st run random value 1..3', 'execute if score $r mg.st matches 1 run scoreboard players add @s mg.olsp 1',
       'title @s times 5 40 10', 'title @s title {"text":"🗝 COFFRE CACHÉ","color":"gold","bold":true}',
       f'title @s subtitle {js(TEXT(f"+{80 * ri} 💰 et des matériaux", "yellow"))}',
       'execute if score $r mg.st matches 1 run tellraw @s {"text":"  💎 et une gemme de lune : +1 point de caractéristique !","color":"light_purple"}',
       'execute at @s run playsound minecraft:block.chest.open player @s ~ ~ ~ 1 0.8', 'execute at @s run particle minecraft:happy_villager ~ ~1 ~ 0.6 0.6 0.6 0 20'])
TC += [f'execute positioned {x + 0.5} {y + 1.2} {z + 0.5} run particle minecraft:end_rod ~ ~ ~ 0.15 0.3 0.15 0.01 1' for (r, x, y, z) in CHESTS]
w('tc_tick', TC)

# ================================================================ succès
ACH = [(0, 'Premier sang', 'Vaincre un premier monstre', 'score @s mg.olkt matches 1..', 50),
       (1, 'Chasseur', 'Vaincre 100 monstres', 'score @s mg.olkt matches 100..', 300),
       (2, 'Fléau des ténèbres', 'Vaincre 500 monstres', 'score @s mg.olkt matches 500..', 1000),
       (3, 'Chasseur d\'élites', 'Vaincre 15 élites', 'score @s mg.olel matches 15..', 500),
       (4, 'Explorateur', 'Découvrir 15 lieux', f'function mg:{P}/ach/c_po15', 300),
       (5, 'Cartographe', 'Découvrir tous les lieux', f'score @s mg.olpo matches {2 ** len(POIS) - 1}', 800),
       (6, 'Érudit', 'Lire toutes les pages du grimoire', f'score @s mg.olpg matches {2 ** len(LORE) - 1}', 800),
       (7, 'Pilleur de trésors', 'Ouvrir les 24 coffres cachés', f'score @s mg.oltc matches {2 ** len(CHESTS) - 1}', 1000),
       (8, 'Maître des donjons', 'Terminer les 8 donjons', 'score @s mg.oldg matches 255', 1200),
       (9, 'Tueur de dragons', 'Vaincre Ignarok', f'score @s mg.olch matches {BOSS_STEP["ignarok"] + 1}..', 600),
       (10, 'Porteur de l\'Aube', 'Terminer la campagne', f'score @s mg.olch matches {END}..', 2000),
       (11, 'Légende', 'Atteindre le niveau 35', 'score @s mg.ollv matches 35..', 2000),
       (12, 'Fortuné', 'Posséder 10 000 💰', 'score @s mg.olg matches 10000..', 500),
       (13, 'Mercenaire', 'Remplir 10 contrats', 'score @s mg.olcd matches 10..', 600),
       (14, 'Bon samaritain', 'Rendre 8 quêtes secondaires', f'function mg:{P}/ach/c_sq8', 800),
       (15, 'Forgé dans l\'acier', 'Arme de palier 8', 'score @s mg.olwt matches 8..', 600),
       (16, 'Cavalier', 'Acheter un destrier', 'score @s mg.olhorse matches 1..', 100),
       (17, 'Encyclopédiste', 'Compléter le bestiaire', f'function mg:{P}/ach/c_best', 1500)]
w('ach/c_po15', ['# 15 lieux découverts ?', 'scoreboard players set $n mg.st 0'] + sum([bit_test('mg.olpo', i) + ['scoreboard players operation $n mg.st += $b mg.st']
                                                                                     for i in range(len(POIS))], []) + ['execute if score $n mg.st matches 15.. run return 1', 'return 0'])
w('ach/c_sq8', ['scoreboard players set $n mg.st 0'] + sum([bit_test('mg.olsd', i) + ['scoreboard players operation $n mg.st += $b mg.st'] for i in range(16)], []) +
  ['execute if score $n mg.st matches 8.. run return 1', 'return 0'])
B1 = sum(1 << M.bitobj(i)[1] for i, k in enumerate(M.KINDS) if not M.K[k].get('minion') and M.bitobj(i)[0] == 'mg.olbs')
B2 = sum(1 << M.bitobj(i)[1] for i, k in enumerate(M.KINDS) if not M.K[k].get('minion') and M.bitobj(i)[0] == 'mg.olbs2')
w('ach/c_best', [f'execute if score @s mg.olbs matches {B1} if score @s mg.olbs2 matches {B2}.. run return 1', 'return 0'])
AC = ['# Toutes les 5 s, @s : succès']
for n, title, desc, cond, xp in ACH:
    w(f'ach/{n}', [f'# Succès : {title}'] + bit_test('mg.olac', n) + ['execute if score $b mg.st matches 1 run return 0', f'scoreboard players operation @s mg.olac += #p{n} mg.st',
                                                                      f'function mg:{P}/xp {{n:{xp}}}',
                                                                      'tellraw @a[tag=mg.olw] ' + js([TEXT('🏆 ', 'gold'), {'selector': '@s', 'color': 'yellow'}, TEXT(' obtient le titre ', 'gray'),
                                                                                                       TEXT('« ' + title + ' »', 'gold', bold=True), TEXT(' (' + desc + ')', 'dark_gray')]),
                                                                      'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.3'])
    AC.append(f'execute if {cond} run function mg:{P}/ach/{n}')
w('achievements', AC)
AL = ['# @s : liste des succès', 'tellraw @s ' + js(TEXT('\n🏆 Succès et titres', 'gold', bold=True))]
for n, title, desc, cond, xp in ACH:
    AL += bit_test('mg.olac', n)
    AL.append('execute if score $b mg.st matches 1 run tellraw @s ' + js([TEXT(' ✔ ', 'green'), TEXT(title, 'gold', bold=True), TEXT(' : ' + desc, 'gray')]))
    AL.append('execute if score $b mg.st matches 0 run tellraw @s ' + js([TEXT(' ✖ ', 'dark_gray'), TEXT(title, 'gray'), TEXT(' : ' + desc, 'dark_gray')]))
w('ach_list', AL)

# ================================================================ journal (fiche, matériaux, quêtes)
SHEET = [TEXT('\n📖 Journal de ', 'gold', bold=True), {'selector': '@s', 'color': 'yellow'},
         TEXT('\n⭐ Niveau ', 'gold'), {'score': {'name': '@s', 'objective': 'mg.ollv'}, 'color': 'yellow', 'bold': True},
         TEXT('   XP ', 'aqua'), {'score': {'name': '@s', 'objective': 'mg.olxp'}, 'color': 'aqua'},
         TEXT('   💰 ', 'gold'), {'score': {'name': '@s', 'objective': 'mg.olg'}, 'color': 'gold'},
         TEXT('   ✦ Éclats ', 'light_purple'), {'score': {'name': '@s', 'objective': 'mg.olsh'}, 'color': 'light_purple'}, TEXT('/8', 'light_purple'),
         TEXT('\n☠ Victoires ', 'gray'), {'score': {'name': '@s', 'objective': 'mg.olkt'}, 'color': 'white'},
         TEXT('   ★ Élites ', 'gray'), {'score': {'name': '@s', 'objective': 'mg.olel'}, 'color': 'white'},
         TEXT('   ⚔ Arme ', 'gray'), {'score': {'name': '@s', 'objective': 'mg.olwt'}, 'color': 'white'},
         TEXT('   🛡 Armure ', 'gray'), {'score': {'name': '@s', 'objective': 'mg.olat'}, 'color': 'white'},
         TEXT('\n✦ Points à répartir : ', 'light_purple'), {'score': {'name': '@s', 'objective': 'mg.olsp'}, 'color': 'light_purple', 'bold': True}]
for n, obj, name, col, eff in CL.STATS:
    SHEET += [TEXT(f'\n {name} ', col), {'score': {'name': '@s', 'objective': obj}, 'color': 'white', 'bold': True}, TEXT(' ', 'gray'),
              {'text': '[+]', 'color': 'green', 'bold': True, 'click_event': {'action': 'run_command', 'command': f'/trigger mg.oltk set {700 + n}'},
               'hover_event': {'action': 'show_text', 'value': eff}}]
SHEET += [TEXT('\n'), {'text': '[📜 Quête]', 'color': 'yellow', 'click_event': {'action': 'run_command', 'command': '/trigger mg.oltk set 9'}}, TEXT(' '),
          {'text': '[❗ Secondaires]', 'color': 'yellow', 'click_event': {'action': 'run_command', 'command': '/trigger mg.oltk set 722'}}, TEXT(' '),
          {'text': '[🧺 Matériaux]', 'color': 'gold', 'click_event': {'action': 'run_command', 'command': '/trigger mg.oltk set 723'}}, TEXT(' '),
          {'text': '[📖 Bestiaire]', 'color': 'aqua', 'click_event': {'action': 'run_command', 'command': '/trigger mg.oltk set 721'}}, TEXT(' '),
          {'text': '[🏆 Succès]', 'color': 'gold', 'click_event': {'action': 'run_command', 'command': '/trigger mg.oltk set 720'}}, TEXT(' '),
          {'text': '[🌀 Voyage]', 'color': 'light_purple', 'click_event': {'action': 'run_command', 'command': '/trigger mg.oltk set 724'}}]
w('sheet', ['# @s : journal dans le chat', 'scoreboard players enable @s mg.oltk', 'tellraw @s ' + js(SHEET),
            'execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1'])
w('journal', [f'function mg:{P}/sheet', f'function mg:{P}/q/say', f'execute if score @s mg.olct matches 1.. run function mg:{P}/ct/status'])
MATL = [TEXT('\n🧺 Matériaux : ', 'gold', bold=True)]
for n, (o, name, col) in M.MATS.items():
    MATL += [TEXT('\n ' + name + ' : ', col), {'score': {'name': '@s', 'objective': o}, 'color': 'white', 'bold': True}]
w('mats', ['tellraw @s ' + js(MATL)])
SQL = ['# @s : quêtes secondaires', 'tellraw @s ' + js(TEXT('\n❗ Quêtes secondaires', 'yellow', bold=True))]
for q, (npc, title, text, typ, tg, n_, rw) in SIDE.items():
    b = q - 1
    SQL += bit_test('mg.olsd', b) + [f'execute if score $b mg.st matches 1 run tellraw @s ' + js([TEXT(' ✔ ', 'green'), TEXT(title, 'gray', strikethrough=True)])]
    SQL += [f'scoreboard players set $d mg.st 0'] + [l.replace('$b', '$d') for l in bit_test('mg.olsd', b)] + bit_test('mg.olsa', b) + \
        [f'execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s ' + js([TEXT(' ▶ ', 'yellow'), TEXT(title, 'yellow', bold=True),
                                                                                                 TEXT(f' ({NPCS[npc][0]})', 'gray')])]
w('sq_list', SQL)

# ================================================================ choix (trigger mg.oltk)
TK = ['# @s : choix dans une fenêtre (trigger mg.oltk)', 'scoreboard players operation $tk mg.st = @s mg.oltk', 'scoreboard players reset @s mg.oltk',
      'scoreboard players enable @s mg.oltk',
      f'execute if score $tk mg.st matches 9 run function mg:{P}/q/say', f'execute if score $tk mg.st matches 9 run function mg:{P}/qloc',
      f'execute if score $tk mg.st matches 500 run function mg:{P}/cl/menu'] + \
     [f'execute if score $tk mg.st matches {600 + n} run function mg:{P}/cl/pick_{n}' for n in CL.CLASSES] + \
     [f'execute if score $tk mg.st matches {700 + n} run function mg:{P}/st/add_{n}' for n in range(1, 5)] + \
     [f'execute if score $tk mg.st matches 709 run function mg:{P}/st/reset', f'execute if score $tk mg.st matches 710 run function mg:{P}/sheet',
      f'execute if score $tk mg.st matches 720 run function mg:{P}/ach_list', f'execute if score $tk mg.st matches 721 run function mg:{P}/bestiary',
      f'execute if score $tk mg.st matches 722 run function mg:{P}/sq_list', f'execute if score $tk mg.st matches 723 run function mg:{P}/mats',
      f'execute if score $tk mg.st matches 724 run function mg:{P}/travel',
      f'execute if score $tk mg.st matches 801 run function mg:{P}/sh/801', f'execute if score $tk mg.st matches 802 run function mg:{P}/sh/802',
      f'execute if score $tk mg.st matches 850 run function mg:{P}/ct/menu',
      f'execute if score $tk mg.st matches 399 in minecraft:overworld run function mg:{P}/leave'] + \
     [f'execute if score $tk mg.st matches {n} run function mg:{P}/sh/{n}' for n in range(651, 660)] + \
     [f'execute if score $tk mg.st matches {300 + i} run function mg:{P}/ws/go{i}' for i in range(len(WAYS))] + TALK_TK + SQ_TK
w('tk', TK)

# ================================================================ régions : accès selon la campagne, titre, dangers
RC = ['# Chaque seconde, @s : région (0 cité, 1..8), accès, titre', 'scoreboard players set $r mg.st 0']
for r in W.ORDER:
    x0, z0, x1, z1 = W.rect(r)
    RC.append(f'execute if entity @s[x={x0},y=-64,z={z0},dx={x1 - x0 - 1},dy=400,dz={z1 - z0 - 1}] run scoreboard players set $r mg.st {REG_IDX[r]}')
for r in W.ORDER:
    RC.append(f'execute if score $r mg.st matches {REG_IDX[r]} unless score @s mg.olch matches {UNLOCK[r]}.. unless entity @s[tag=mg.olfree] run return run function mg:{P}/deny')
RC += ['function mg:ombre/save_pos', f'execute unless score @s mg.olrg = $r mg.st run function mg:{P}/region_chg']
w('region', RC)
RG = ['# @s change de région : titre', 'scoreboard players operation @s mg.olrg = $r mg.st', 'title @s times 10 50 15']
for r, (ij, name, col, (l1, l2), b) in W.REGIONS.items():
    RG += [f'execute if score $r mg.st matches {REG_IDX[r]} run title @s title {js(TEXT(name.upper(), col, bold=True))}',
           f'execute if score $r mg.st matches {REG_IDX[r]} run title @s subtitle {js(TEXT("Cité-refuge" if r == "hub" else f"Niveaux conseillés {l1} à {l2}", "gray"))}']
RG.append('execute at @s run playsound minecraft:event.mob_effect.raid_omen ambient @s ~ ~ ~ 0.4 1.4')
w('region_chg', RG)
w('deny', ['# @s entre dans une région pas encore ouverte : retour en arrière',
           'execute store result storage mg:ombre d.x int 1 run scoreboard players get @s mg.olsx', 'execute store result storage mg:ombre d.y int 1 run scoreboard players get @s mg.olsy',
           'execute store result storage mg:ombre d.z int 1 run scoreboard players get @s mg.olsz', 'function mg:ombre/back with storage mg:ombre d',
           'tellraw @s {"text":"⛔ Cette région n\'est pas encore accessible : suis la campagne (📜 dans le journal).","color":"red"}',
           'execute at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 0.8 0.6'])
w('save_pos', ['execute store result score @s mg.olsx run data get entity @s Pos[0]', 'execute store result score @s mg.olsy run data get entity @s Pos[1]',
               'execute store result score @s mg.olsz run data get entity @s Pos[2]'])
w('back', [f'$execute in {DIM} run tp @s $(x).5 $(y) $(z).5'])
HZ = ['# Toutes les 2 s, @s : dangers des régions (froid, chaleur, ténèbres) sans protection',
      f'execute if score @s mg.olrg matches {REG_IDX["n"]} unless score @s mg.olfur matches 1.. unless entity @s[x=-24,y=60,z=-140,dx=48,dy=40,dz=40] run function mg:{P}/hz/cold',
      f'execute if score @s mg.olrg matches {REG_IDX["se"]} unless score @s mg.olfire matches 1.. unless entity @s[x=120,y=60,z=90,dx=40,dy=30,dz=40] run function mg:{P}/hz/heat',
      f'execute if score @s mg.olrg matches {REG_IDX["sw"]} unless score @s mg.olbless matches 1.. run function mg:{P}/hz/dark']
w('hazard', HZ)
w('hz/cold', ['damage @s 1 minecraft:freeze', 'effect give @s minecraft:slowness 3 0 true', 'particle minecraft:snowflake ~ ~1 ~ 0.4 0.6 0.4 0 10',
              'scoreboard players set @s mg.olal 40', 'title @s actionbar {"text":"🥶 Tu gèles ! Une cape de fourrure (Sigrun, Hrafnheim) te protégerait.","color":"aqua"}'])
w('hz/heat', ['damage @s 1 minecraft:hot_floor', 'particle minecraft:flame ~ ~1 ~ 0.4 0.6 0.4 0 6', 'scoreboard players set @s mg.olal 40',
              'title @s actionbar {"text":"🔥 La chaleur t\'écrase ! Durgan (Bastion des Braises) peut forger un talisman.","color":"gold"}'])
w('hz/dark', ['effect give @s minecraft:darkness 4 0 true', 'scoreboard players set @s mg.olal 40',
              'title @s actionbar {"text":"🌑 Les ténèbres te rongent. Seule la bénédiction de l\'Aube t\'en protège.","color":"dark_purple"}'])
