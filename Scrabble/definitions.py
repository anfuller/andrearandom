#In this quiz, a definition will pop up and you'll have to guess which three-letter word it matches.
import random


def scrabble_threes():

    print "\nMatch the definition to the word. Type the correct letter.\n"
    words = ['AAH', 'AAL', 'AAS', 'ABA', 'ABO', 'ABS', 'ABY', 'ACE', 'ACT',
             'ADD', 'ADO', 'ADS', 'ADZ', 'AFF', 'AFT', 'AGA', 'AGE', 'AGO',
             'AGS', 'AHA', 'AHI', 'AHS', 'AID', 'AIL', 'AIM', 'AIN', 'AIR',
             'AIS', 'AIT', 'ALA', 'ALB', 'ALE', 'ALL', 'ALP', 'ALS', 'ALT',
             'AMA', 'AMI', 'AMP', 'AMU', 'ANA', 'AND', 'ANE', 'ANI', 'ANT',
             'ANY', 'APE', 'APO', 'APP', 'APT', 'ARB', 'ARC', 'ARE', 'ARF',
             'ARK', 'ARM', 'ARS', 'ART', 'ASH', 'ASK', 'ASP', 'ASS', 'ATE',
             'ATT', 'AUK', 'AVA', 'AVE', 'AVO', 'AWA', 'AWE', 'AWL', 'AWN',
             'AXE', 'AYE', 'AYS', 'AZO', 'BAA', 'BAD', 'BAG', 'BAH', 'BAL',
             'BAM', 'BAN', 'BAP', 'BAR', 'BAS', 'BAT', 'BAY', 'BED', 'BEE',
             'BEG', 'BEL', 'BEN', 'BES', 'BET', 'BEY', 'BIB', 'BID', 'BIG',
             'BIN', 'BIO', 'BIS', 'BIT', 'BIZ', 'BOA', 'BOB', 'BOD', 'BOG',
             'BOO', 'BOP', 'BOS', 'BOT', 'BOW', 'BOX', 'BOY', 'BRA', 'BRO',
             'BRR', 'BUB', 'BUD', 'BUG', 'BUM', 'BUN', 'BUR', 'BUS', 'BUT',
             'BUY', 'BYE', 'BYS', 'CAB', 'CAD', 'CAM', 'CAN', 'CAP', 'CAR',
             'CAT', 'CAW', 'CAY', 'CEE', 'CEL', 'CEP', 'CHI', 'CIG', 'CIS',
             'COB', 'COD', 'COG', 'COL', 'CON', 'COO', 'COP', 'COR', 'COS',
             'COT', 'COW', 'COX', 'COY', 'COZ', 'CRU', 'CRY', 'CUB', 'CUD',
             'CUE', 'CUM', 'CUP', 'CUR', 'CUT', 'CWM', 'DAB', 'DAD', 'DAG',
             'DAH', 'DAK', 'DAL', 'DAM', 'DAN', 'DAP', 'DAW', 'DAY', 'DEB',
             'DEE', 'DEF', 'DEL', 'DEN', 'DEV', 'DEW', 'DEX', 'DEY', 'DIB',
             'DID', 'DIE', 'DIF', 'DIG', 'DIM', 'DIN', 'DIP', 'DIS', 'DIT',
             'DOC', 'DOE', 'DOG', 'DOL', 'DOM', 'DON', 'DOR', 'DOS', 'DOT',
             'DOW', 'DRY', 'DUB', 'DUD', 'DUE', 'DUG', 'DUH', 'DUI', 'DUN',
             'DUO', 'DUP', 'DYE', 'EAR', 'EAT', 'EAU', 'EBB', 'ECU', 'EDH',
             'EDS', 'EEK', 'EEL', 'EFF', 'EFS', 'EFT', 'EGG', 'EGO', 'EKE',
             'ELD', 'ELF', 'ELK', 'ELL', 'ELM', 'ELS', 'EME', 'EMS', 'EMU',
             'END', 'ENG', 'ENS', 'EON', 'ERA', 'ERE', 'ERG', 'ERN', 'ERR',
             'ERS', 'ESS', 'ETA', 'ETH', 'EVE', 'EWE', 'EYE', 'FAB', 'FAD',
             'FAG', 'FAN', 'FAR', 'FAS', 'FAT', 'FAX', 'FAY', 'FED', 'FEE',
             'FEH', 'FEM', 'FEN', 'FER', 'FES', 'FET', 'FEU', 'FEW', 'FEY',
             'FEZ', 'FIB', 'FID', 'FIE', 'FIG', 'FIL', 'FIN', 'FIR', 'FIT',
             'FIX', 'FIZ', 'FLU', 'FLY', 'FOB', 'FOE', 'FOG', 'FOH', 'FON',
             'FOP', 'FOR', 'FOU', 'FOX', 'FOY', 'FRO', 'FRY', 'FUB', 'FUD',
             'FUG', 'FUN', 'FUR', 'GAB', 'GAD', 'GAE', 'GAG', 'GAL', 'GAM',
             'GAN', 'GAP', 'GAR', 'GAS', 'GAT', 'GAY', 'GED', 'GEE', 'GEL',
             'GEM', 'GEN', 'GET', 'GEY', 'GHI', 'GIB', 'GID', 'GIE', 'GIG',
             'GIN', 'GIP', 'GIT', 'GNU', 'GOA', 'GOB', 'GOD', 'GOO', 'GOR',
             'GOS', 'GOT', 'GOX', 'GOY', 'GUL', 'GUM', 'GUN', 'GUT', 'GUV',
             'GUY', 'GYM', 'GYP', 'HAD', 'HAE', 'HAG', 'HAH', 'HAJ', 'HAM',
             'HAO', 'HAP', 'HAS', 'HAT', 'HAW', 'HAY', 'HEH', 'HEM', 'HEN',
             'HEP', 'HER', 'HES', 'HET', 'HEW', 'HEX', 'HEY', 'HIC', 'HID',
             'HIE', 'HIM', 'HIN', 'HIP', 'HIS', 'HIT', 'HMM', 'HOB', 'HOD',
             'HOE', 'HOG', 'HON', 'HOP', 'HOS', 'HOT', 'HOW', 'HOY', 'HUB',
             'HUE', 'HUG', 'HUH', 'HUM', 'HUN', 'HUP', 'HUT', 'HYP', 'ICE',
             'ICH', 'ICK', 'ICY', 'IDS', 'IFF', 'IFS', 'IGG', 'ILK', 'ILL',
             'IMP', 'INK', 'INN', 'INS', 'ION', 'IRE', 'IRK', 'ISM', 'ITS',
             'IVY', 'JAB', 'JAG', 'JAM', 'JAR', 'JAW', 'JAY', 'JEE', 'JET',
             'JEU', 'JEW', 'JIB', 'JIG', 'JIN', 'JOB', 'JOE', 'JOG', 'JOT',
             'JOW', 'JOY', 'JUG', 'JUN', 'JUS', 'JUT', 'KAB', 'KAE', 'KAF',
             'KAS', 'KAT', 'KAY', 'KEA', 'KEF', 'KEG', 'KEN', 'KEP', 'KEX',
             'KEY', 'KHI', 'KID', 'KIF', 'KIN', 'KIP', 'KIR', 'KIS', 'KIT',
             'KOA', 'KOB', 'KOI', 'KOP', 'KOR', 'KOS', 'KUE', 'KYE', 'LAB',
             'LAC', 'LAD', 'LAG', 'LAM', 'LAP', 'LAR', 'LAS', 'LAT', 'LAV',
             'LAW', 'LAX', 'LAY', 'LEA', 'LED', 'LEE', 'LEG', 'LEI', 'LEK',
             'LES', 'LET', 'LEU', 'LEV', 'LEX', 'LEY', 'LEZ', 'LIB', 'LID',
             'LIE', 'LIN', 'LIP', 'LIS', 'LIT', 'LOB', 'LOG', 'LOO', 'LOP',
             'LOT', 'LOW', 'LOX', 'LUG', 'LUM', 'LUV', 'LUX', 'LYE', 'MAC',
             'MAD', 'MAE', 'MAG', 'MAN', 'MAP', 'MAR', 'MAS', 'MAT', 'MAW',
             'MAX', 'MAY', 'MED', 'MEG', 'MEL', 'MEM', 'MEN', 'MET', 'MEW',
             'MHO', 'MIB', 'MIC', 'MID', 'MIG', 'MIL', 'MIM', 'MIR', 'MIS',
             'MIX', 'MOA', 'MOB', 'MOC', 'MOD', 'MOG', 'MOL', 'MOM', 'MON',
             'MOO', 'MOP', 'MOR', 'MOS', 'MOT', 'MOW', 'MUD', 'MUG', 'MUM',
             'MUN', 'MUS', 'MUT', 'MYC', 'NAB', 'NAE', 'NAG', 'NAH', 'NAM',
             'NAN', 'NAP', 'NAW', 'NAY', 'NEB', 'NEE', 'NEG', 'NET', 'NEW',
             'NIB', 'NIL', 'NIM', 'NIP', 'NIT', 'NIX', 'NOB', 'NOD', 'NOG',
             'NOH', 'NOM', 'NOO', 'NOR', 'NOS', 'NOT', 'NOW', 'NTH', 'NUB',
             'NUN', 'NUS', 'NUT', 'OAF', 'OAK', 'OAR', 'OAT', 'OBA', 'OBE',
             'OBI', 'OCA', 'ODA', 'ODD', 'ODE', 'ODS', 'OES', 'OFF', 'OFT',
             'OHM', 'OHO', 'OHS', 'OIL', 'OKA', 'OKE', 'OLD', 'OLE', 'OMS',
             'ONE', 'ONO', 'ONS', 'OOH', 'OOT', 'OPE', 'OPS', 'OPT', 'ORA',
             'ORB', 'ORC', 'ORE', 'ORS', 'ORT', 'OSE', 'OUD', 'OUR', 'OUT',
             'OVA', 'OWE', 'OWL', 'OWN', 'OXO', 'OXY', 'PAC', 'PAD', 'PAH',
             'PAL', 'PAM', 'PAN', 'PAP', 'PAR', 'PAS', 'PAT', 'PAW', 'PAX',
             'PAY', 'PEA', 'PEC', 'PED', 'PEE', 'PEG', 'PEH', 'PEN', 'PEP',
             'PER', 'PES', 'PET', 'PEW', 'PHI', 'PHT', 'PIA', 'PIC', 'PIE',
             'PIG', 'PIN', 'PIP', 'PIS', 'PIT', 'PIU', 'PIX', 'PLY', 'POD',
             'POH', 'POI', 'POL', 'POM', 'POO', 'POP', 'POT', 'POW', 'POX',
             'PRO', 'PRY', 'PSI', 'PST', 'PUB', 'PUD', 'PUG', 'PUL', 'PUN',
             'PUP', 'PUR', 'PUS', 'PUT', 'PYA', 'PYE', 'PYX', 'QAT', 'QIS',
             'QUA', 'RAD', 'RAG', 'RAH', 'RAI', 'RAJ', 'RAM', 'RAN', 'RAP',
             'RAS', 'RAT', 'RAW', 'RAX', 'RAY', 'REB', 'REC', 'RED', 'REE',
             'REF', 'REG', 'REI', 'REM', 'REP', 'RES', 'RET', 'REV', 'REX',
             'RHO', 'RIA', 'RIB', 'RID', 'RIF', 'RIG', 'RIM', 'RIN', 'RIP',
             'ROB', 'ROC', 'ROD', 'ROE', 'ROM', 'ROT', 'ROW', 'RUB', 'RUE',
             'RUG', 'RUM', 'RUN', 'RUT', 'RYA', 'RYE', 'SAB', 'SAC', 'SAD',
             'SAE', 'SAG', 'SAL', 'SAP', 'SAT', 'SAU', 'SAW', 'SAX', 'SAY',
             'SEA', 'SEC', 'SEE', 'SEG', 'SEI', 'SEL', 'SEN', 'SER', 'SET',
             'SEW', 'SEX', 'SHA', 'SHE', 'SHH', 'SHY', 'SIB', 'SIC', 'SIM',
             'SIN', 'SIP', 'SIR', 'SIS', 'SIT', 'SIX', 'SKA', 'SKI', 'SKY',
             'SLY', 'SOB', 'SOD', 'SOL', 'SOM', 'SON', 'SOP', 'SOS', 'SOT',
             'SOU', 'SOW', 'SOX', 'SOY', 'SPA', 'SPY', 'SRI', 'STY', 'SUB',
             'SUE', 'SUK', 'SUM', 'SUN', 'SUP', 'SUQ', 'SYN', 'TAB', 'TAD',
             'TAE', 'TAG', 'TAJ', 'TAM', 'TAN', 'TAO', 'TAP', 'TAR', 'TAS',
             'TAT', 'TAU', 'TAV', 'TAW', 'TAX', 'TEA', 'TED', 'TEE', 'TEG',
             'TEL', 'TEN', 'TET', 'TEW', 'THE', 'THO', 'THY', 'TIC', 'TIE',
             'TIL', 'TIN', 'TIP', 'TIS', 'TIT', 'TOD', 'TOE', 'TOG', 'TOM',
             'TON', 'TOO', 'TOP', 'TOR', 'TOT', 'TOW', 'TOY', 'TRY', 'TSK',
             'TUB', 'TUG', 'TUI', 'TUN', 'TUP', 'TUT', 'TUX', 'TWA', 'TWO',
             'TYE', 'UDO', 'UGH', 'UKE', 'ULU', 'UMM', 'UMP', 'UNS', 'UPO',
             'UPS', 'URB', 'URD', 'URN', 'URP', 'USE', 'UTA', 'UTE', 'UTS',
             'VAC', 'VAN', 'VAR', 'VAS', 'VAT', 'VAU', 'VAV', 'VAW', 'VEE',
             'VEG', 'VET', 'VEX', 'VIA', 'VID', 'VIE', 'VIG', 'VIM', 'VIS',
             'VOE', 'VOW', 'VOX', 'VUG', 'VUM', 'WAB', 'WAD', 'WAE', 'WAG',
             'WAN', 'WAP', 'WAR', 'WAS', 'WAT', 'WAW', 'WAX', 'WAY', 'WEB',
             'WED', 'WEE', 'WEN', 'WET', 'WHA', 'WHO', 'WHY', 'WIG', 'WIN',
             'WIS', 'WIT', 'WIZ', 'WOE', 'WOG', 'WOK', 'WON', 'WOO', 'WOP',
             'WOS', 'WOT', 'WOW', 'WRY', 'WUD', 'WYE', 'WYN', 'XIS', 'YAG',
             'YAH', 'YAK', 'YAM', 'YAP', 'YAR', 'YAW', 'YAY', 'YEA', 'YEH',
             'YEN', 'YEP', 'YES', 'YET', 'YEW', 'YID', 'YIN', 'YIP', 'YOB',
             'YOD', 'YOK', 'YOM', 'YON', 'YOU', 'YOW', 'YUK', 'YUM', 'YUP',
             'ZAG', 'ZAP', 'ZAS', 'ZAX', 'ZED', 'ZEE', 'ZEK', 'ZEP', 'ZIG',
             'ZIN', 'ZIP', 'ZIT', 'ZOA', 'ZOO', 'ZUZ', 'ZZZ']

    definitions = ['to exclaim in delight', 'East Indian shrub', 'aa rough, cindery lava', 'sleeveless garment', 'aborigine offensive', 'ab abdominal muscle', 'to pay the penalty for abye', 'to make a perfect shot', 'to perform by action', 'to perform addition', 'bustle', 'ad advertisement', 'cutting tool adze', 'off', 'toward the stern', 'Turkish military officer', 'to grow old', 'in the past', 'ag agriculture', 'intj. expressing sudden realization', 'tuna', 'ah to exclaim in amazement', 'to help', 'to suffer pain', 'to point in a direction', 'Hebrew letter ayin', 'to broadcast', 'ai three-toed sloth', 'small island', 'wing', 'long-sleeved vestment', 'alcoholic beverage', 'everything one has', 'high mountain', 'al East Indian tree', 'high-pitched note', 'Oriental nurse amah', 'friend', 'unit of electric current strength ampere', 'atomic mass unit', 'collection of information on a subject', 'added condition', 'one', 'tropical American black cuckoo', 'small insect', 'one or another', 'to mimic', 'type of protein', 'computer program application', 'appropriate', 'stock trader', 'to travel a curved course', 'unit of surface measure/conj. of be', 'dog''s bark', 'large boat', 'to supply with weapons', 'ar letter ''r''', 'skill acquired by experience', 'tree/to burn into ashes', 'to question', 'venemous snake', 'donkey', 'reckless impulse driving one to ruin', 'Laotian monetary unit', 'diving seabird', 'at all', 'expression of greeting', 'monetary unit of Macau', 'away', 'to inspire with awe', 'pointed punching tool', 'bristlelike appendage of certain grasses', 'to cut with an axe', 'affirmative vote', 'ay affirmative vote', 'containing nitrogen', 'baa to bleat', 'something bad', 'to put into a bag', 'intj. expressing disgust', 'type of shoe balmoral', 'to strike with a dull sound', 'to prohibit/Rumanian coin', 'small roll', 'to exclude', 'ba eternal soul in Egyptian mythology', 'to hit a baseball', 'to howl', 'to provide with a bed', 'winged insect', 'to plead', 'unit of power', 'inner room', 'Hebrew letter beth', 'to wager', 'Turkish ruler', 'to drink alcohol', 'to make a bid', 'large', 'to store in a bin', 'biography', 'bi bisexual', 'to restrain with a bit', 'business', 'large snake', 'to move up and down', 'body', 'to impede', 'to deride', 'to hit', 'bo pal', 'botfly larva', 'to bend forward at the waist', 'to put into a box', 'male child', 'brassiere', 'brother', 'intj. used to indicate coldness brrr', 'young fellow', 'to grow buds', 'to annoy', 'to live idly', 'small bread roll', 'to remove a rough edge from burr', 'to transport by bus', 'flatfish', 'to purchase', 'free advance to next tournament round', 'by side issue', 'to drive a taxi', 'ungentlemanly man', 'rotating machine part', 'to be able/to put into a can', 'to put a cover onto', 'automobile', 'to anchor to a cathead', 'to caw like a crow', 'small low island', 'letter ''c''', 'drawn frame of animation', 'large mushroom cepe', 'Greek letter', 'cigarette', 'having certain atoms on same side of molecule', 'corncob', 'to fool', 'to cheat at dice', 'depression between two mountains', 'to swindle', 'to make the sound of a dove', 'to steal', 'intj. expressing surprise', 'lettuce variety', 'lightweight bed', 'to intimidate', 'to direct a racing boat coxswain', 'shy/to caress', 'cousin', 'French wine classification', 'to weep', 'young of certain animals', 'food portion to be chewed again', 'to signal a start', 'together with', 'to place into a cup', 'mongrel dog', 'to make an incision', 'circular basin with steep walls cirque', 'to touch lightly', 'father', 'hanging shred', 'dash in Morse code', 'transportion by relay', 'lentil dish', 'to build a dam', 'skill level in martial arts', 'to dip into water', 'to dawn', '24 hours', 'debutante', 'letter ''d''', 'excellent', 'differential calculus operator', 'to live in a lair', 'Hindu god deva', 'to wet with dew', 'sulfate used as stimulant', 'former North African ruler', 'to fish', 'do-conj to execute', 'to cease living/to make a die', 'difference', 'to scoop earth from the ground', 'obscure/to make obscure', 'to make a loud noise', 'to immerse briefly', 'to disrespect', 'dot in Morse code', 'doctor', 'female deer', 'to follow after like a dog', 'unit of pain intensity', 'title given to certain monks', 'to put on', 'black European beetle', 'do first tone of diatonic musical scale', 'to cover with dots', 'to prosper', 'having no moisture/prohibitionist/to make dry', 'to confer knighthood upon', 'bomb that fails to explode', 'something owed', 'teat, udder', 'intj. expressing patent obviousness of a preceding statement', 'duo-pl instrumental duet', 'of a dull brown color/to demand payment', 'instrumental duet', 'to open', 'to color', 'hearing organ', 'to consume', 'water', 'to recede', 'old French coin', 'Old English letter', 'ed education', 'intj. expressing fright', 'snakelike fish', 'letter ''f'' ef', 'ef letter ''f''', 'newt', 'to throw eggs at', 'conscious self', 'to get with great difficulty', 'old age', 'small, often mischievous fairy', 'large deer', 'letter ''l''', 'deciduous tree', 'el letter ''l''', 'uncle', 'em printer''s measurement', 'large, flightless bird', 'to terminate', 'phonetic symbol', 'entity', 'long period of time aeon', 'chronological period epoch', 'previous to; before', 'unit of work or energy', 'erne', 'to make a mistake', 'European climbing plant ervil', 'letter ''s'' es', 'Greek letter', 'Old English letter edh', 'evening', 'female sheep', 'organ of sight/to watch closely', 'fabulous/something fabricated', 'passing fancy', 'to make weary by hard work', 'to use a fan to cool', 'at or to a great distance', 'fa fourth tone of diatonic musical scale', 'obese/to make fat', 'to reproduce by electronic means', 'to join closely', 'federal agent', 'to pay a fee to', 'Hebrew letter pe', 'passive homosexual', 'marsh', 'for', 'fe Hebrew letter-feh', 'to fetch', 'to grant land to under Scottish feudal law', 'amounting to or consisting of a small number', 'crazy', 'brimless cap worn by men in the Near East', 'to tell a white lie', 'topmast support bar', 'intj. expressing disapproval', 'to adorn', 'coin of Iraq, Jordan', 'to equip with fins', 'evergreen tree', 'healthy/to be suitable for', 'to repair', 'hissing or sputtering sound', 'virus disease', 'clever/to hit a ball high into the air in baseball/to move through the air', 'to deceive', 'enemy', 'to cover with fog', 'intj. faugh', 'warm, dry wind foehn', 'to deceive', 'directed or sent to', 'drunk', 'to outwit', 'farewell feast or gift', 'away', 'to cook over direct heat in hot fat or oil', 'to fob', 'old-fashioned person', 'to make stuffy', 'to act playfully', 'to cover with fur', 'to chatter', 'to roam about restlessly', 'to go', 'to prevent from talking', 'girl', 'to visit socially', 'gin-conj to begin', 'to make an opening in', 'to compel', 'to supply with gas', 'pistol', 'merry/homosexual', 'food fish', 'to turn right', 'to become like jelly', 'to adorn with gemstones', 'knowledge obtained by investigation', 'to obtain', 'very', 'liquid butter made in India ghee', 'to fasten with a wedge', 'disease of sheep', 'to give', 'to catch fish with a pronged spear', 'to begin/to remove seeds from cotton', 'to gyp', 'intj. used as an order of dismissal', 'large antelope', 'Asian gazelle', 'to fill a pit with waste', 'to treat as a god a supernatural being', 'slimy stuff', 'intj. used as a mild oath', 'go Japanese board game', 'get-conj to obtain', 'gaseous oxygen', 'non-Jewish person', 'design in oriental carpets', 'to chew without teeth', 'to shoot with a gun', 'to remove the guts of', 'governor', 'to ridicule', 'large room for sports activities', 'to swindle', 'have-conj to possess', 'to have', 'to hack', 'ha', 'pilgrimage to Mecca hadj', 'to overact', 'Vietnamese monetary unit', 'to happen', 'ha sound expressing triumph', 'to provide with a hat', 'to turn left', 'to make into hay', 'Hebrew letter heth', 'to add an edge to', 'female chicken', 'hip', 'objective or possessive case of the pronoun she', 'he male person', 'Hebrew letter heth', 'to cut with an ax', 'to cast an evil spell upon', 'intj. used to attract attention', 'intj. used to represent a hiccup', 'hide-conj to conceal', 'to hurry', 'objective case of the pronoun he', 'Hebrew unit of liquid measure', 'aware of the most current styles and trends/to build a type of roof', 'possessive form of the pronoun he', 'to strike', 'intj. expressing thought', 'to provide with hobnails', 'portable trough', 'to use a hoe', 'to take more than one''s share', 'honeybun', 'to move by jumping on one foot', 'trivalent metallic element of the rare earth group', 'having a high temperature/to heat', 'method of doing something', 'heavy barge', 'center of a wheel', 'color', 'to grasp with both arms', 'intj. expressing surprise', 'to sing without words', 'barbarian', 'intj. used to mark a marching cadence', 'to live in a hut', 'hypochondria', 'to cover with ice', 'fish disease', 'intj. expressing distaste', 'covered with ice', 'id part of psyche', 'if and only if', 'if possible condition', 'to ignore', 'kind', 'evil', 'to graft feathers onto a bird''s wing', 'to apply ink to', 'to house at an inn', 'in influence', 'electrically charged atom', 'to anger', 'to annoy', 'doctrine', 'possesive form of it', 'climbing vine', 'to poke', 'to cut unevenly', 'to force together tightly', 'to cause to shake', 'to jabber', 'corvine bird', 'to turn right gee', 'to fly in a jet', 'game', 'to bargain with offensive', 'to refuse to proceed further', 'to bob', 'Muslim supernatural being jinn', 'to work by the piece', 'fellow', 'to run slowly', 'to write down quickly', 'to toll', 'to rejoice', 'to put into a jug', 'coin of North Korea', 'legal right', 'to protrude', 'ancient Hebrew unit of measure', 'crow-like bird', 'Hebrew letter kaph', 'large cupboard/pl. of ka', 'evergreen shrub', 'letter ''k''', 'parrot', 'marijuana', 'small barrel', 'to know', 'to catch', 'dry, hollow stalk', 'to provide with a key', 'Greek letter chi', 'to tease', 'marijuana kef', 'group of related people', 'to sleep', 'alcoholic beverage', 'ki vital life-sustaining energy force', 'to equip', 'timber tree', 'reddish brown antelope', 'large Japanese carp', 'hill', 'Hebrew unit of measure', 'land measure in India', 'letter ''q''', 'private Korean-American banking club', 'laboratory', 'resinous substance secreted by insects', 'boy', 'to fall behind', 'to flee', 'to drink with the tongue', 'Roman tutelary god', 'la sixth tone of diatonic musical scale', 'former Latvian monetary unit', 'lavatory', 'to sue', 'not strict or stringent', 'to place', 'meadow', 'lead-conj to show the way', 'shelter from the wind', 'to walk hurriedly', 'flower necklace', 'Albanian monetary unit', 'chronic inflammatory collagen disease affecting connective tissue skin or joints', 'to rent', 'monetary unit of Rumania', 'Bulgarian monetary unit', 'law', 'lea', 'lesbian', 'liberation', 'to provide with a lid', 'to become horizontal/to tell untruths', 'waterfall linn', 'to touch with the lips', 'li Chinese unit of distance', 'light to illuminate/former Lithuanian monetary unit litas', 'to throw in a high arc', 'to cut down trees for timber', 'to subject to a forfeit at the card game loo', 'to chop off', 'to distribute proportionately', 'close to the ground/to make the sound of cattle', 'to supply with lox liquid oxygen', 'to pull with effort', 'chimney', 'sweetheart', 'unit of illumination', 'solution used to make soap', 'raincoat', 'insane/to madden', 'more', 'magazine', 'adult human male/to supply with men', 'to draw a map', 'to destroy the perfection of', 'ma mother', 'to pack into a dense mass', 'to mow', 'maximum', 'to have permission/to gather flowers during Spring', 'medical', 'megabyte', 'honey', 'Hebrew letter', 'man adult human male', 'meet-conj to make the acquaintance of', 'to meow', 'unit of electrical conductance', 'playing marble', 'microphone', 'middle', 'playing marble', 'unit of length', 'primly demure', 'Russian peasant commune', 'mi third tone of diatonic musical scale', 'to combine', 'extinct flightless bird', 'to crowd about', 'soft leather heelless shoe moccasin', 'one who wears boldly stylish clothes', 'to move away', 'unit of quantity in chemistry mole', 'mother', 'man', 'to make the sound of a cow', 'to wipe with a mop', 'forest humus', 'mo moment', 'witty saying', 'to cut down grass', 'to cover with mud', 'to assault with intent to rob', 'to act in disguise', 'man', 'mu Greek letter', 'mutt', 'gene that regulates other genes', 'to capture', 'no; not', 'to find fault incessantly', 'no', 'nim-conj to steal', 'Indian flat round leavened bread', 'to sleep briefly', 'no', 'negative vote', 'bird beak', 'born with the name of', 'photographic negative', 'to catch in a net', 'existing only a short time/something that is new', 'to provide with a penpoint', 'nothing', 'to steal', 'to bite quickly', 'insect egg', 'to veto/water sprite', 'wealthy person', 'to move the head downward', 'strong ale/to fill space with bricks', 'classical drama of Japan', 'name', 'now', 'and not', 'no negative reply', 'in no way', 'present time', 'pert. to item number n', 'protuberance', 'woman belonging to a religious order', 'nu Greek letter', 'to gather nuts', 'clumsy person', 'hardwood tree', 'to row with oars', 'cereal grass', 'hereditary African chief', 'African sorcery obeah', 'African sorcery obeah', 'South American herb', 'harem room', 'one that is odd/unusual', 'lyric poem', 'od hypothetical force of natural power', 'oe Faroean wind', 'to kill', 'often', 'unit of electrical resistance', 'intj. expressing surprise', 'oh to exclaim "oh"', 'to supply with oil', 'Turkish unit of weight', 'Turkish unit of weight oka', 'individual of a specified age/living or existing for a relatively long time', 'shout of approval', 'om mantra used in meditation', 'number 1', 'large mackerel', 'on side of wicket in cricket', 'to exclaim in amazement', 'out', 'to open', 'op style of abstract art', 'to choose', 'os-pl orifice', 'to form into a sphere', 'marine mammal orca', 'mineral or rock containing valuable metal', 'or heraldic color gold', 'table scrap', 'ridge of sand esker', 'stringed instrument of northern Africa', 'belonging to us', 'to be revealed', 'ovum-pl female reproductive cell', 'to be under obligation to pay', 'nocturnal bird', 'to possess', 'containing oxygen', 'containing oxygen', 'shoe patterned after a moccasin', 'to line with padding', 'intj. used as an exclamation of disgust', 'to hang around with as friends', 'jack of clubs', 'to criticize harshly', 'soft food for infants', 'to shoot par on a hole', 'pa father', 'to touch lightly', 'to scrape at with a paw', 'ceremonial embrace given to signify Christian love and unity', 'to give money in order to buy something', 'edible seed of an annual herb', 'pectoral muscle', 'natural soil aggregate', 'to urinate offensive', 'to nail a wooden pin', 'Hebrew letter pe', 'to write', 'to fill with energy', 'for each', 'foot/pl. of pe Hebrew letter', 'to caress with the hand', 'bench for seating people in church', 'Greek letter', 'intj. used as an expression of mild anger or annoyance', 'brain membrane', 'photograph', 'to pi', 'to bear pigs cloven-hoofed mammals', 'to fasten with a pin', 'to break through the shell of an egg', 'pi Greek letter', 'to mark with cavities or depressions', 'more used as a musical direction', 'container for the Eucharist pyx', 'to supply with or offer repeatedly', 'to produce seed vessels', 'intj. expressing disgust', 'Hawaiian food', 'politician', 'English immigrant in Australia offensive', 'poop', 'to make a sharp, explosive sound', 'to put into a pot', 'explosive sound', 'to infect with syphilis', 'argument or vote in favor of something', 'to inquire impertinently into private matters', 'Greek letter', 'intj. used to attract attention psst', 'tavern', 'pudding', 'to fill in with clay or mortar', 'coin of Afghanistan', 'to make a pun a play on words', 'to give birth to puppies', 'to purr', 'viscous fluid formed in infected tissue', 'to place in a particular position', 'copper coin of Burma', 'book of ecclesiastical rules in the pre reformation english church', 'container for the Eucharist', 'evergreen shrub kat', 'qi vital life-sustaining energy force', 'in the capacity of', 'to fear', 'to scold', 'intj. used to cheer on a team or player', 'style of popular Algerian music', 'dominion; sovereignty', 'to strike with great force', 'run-conj to move by rapid steps', 'to strike sharply', 'Ethiopian prince', 'to hunt rats long-tailed rodents', 'uncooked/sore or irritated spot', 'to stretch out', 'to emit rays', 'Confederate soldier', 'recreation', 'of the color red/to put into order', 'female Eurasian sandpiper', 'to referee', 'regulation', 'erroneous form of former Portuguese coin', 'quantity of ionizing radiation', 'cross-ribbed fabric', 'thing or matter', 'to soak in order to loosen the fiber from the woody tissue', 'to increase the speed of', 'animal with a single wavy layer of hair/king', 'Greek letter', 'long, narrow inlet', 'to poke fun at', 'to free from something objectionable', 'to lay off from employment', 'to put in proper condition for use', 'to provide with a rim an outer edge', 'to run or melt', 'to tear or cut apart roughly', 'to take property from illegally', 'lengendary bird of prey', 'to provide with a rod', 'mass of eggs within a female fish', 'male gypsy', 'to decompose', 'to propel by means of oars', 'to move along the surface of a body with pressure', 'to feel sorrow or remorse for', 'to tear roughly', 'alcoholic liquor/odd', 'to move by rapid steps', 'to make ruts grooves in', 'Scandinavian handwoven rug', 'cereal grass', 'to sob', 'pouchlike structure in an animal or plant', 'unhappy', 'so', 'to bend or sink downward from weight or pressure', 'salt', 'to weaken gradually', 'sit-conj to rest on the buttocks', 'xu', 'to cut or divide with a saw', 'saxophone', 'to utter', 'ocean', 'secant', 'to perceive with the eyes', 'advocate of racial segregation', 'large whale rorqual', 'self', 'monetary unit of Japan', 'unit of weight of India', 'to put in a particular position', 'to mend or fasten with a needle and thread', 'to determine the sex of', 'intj. used to urge silence shh', 'female person', 'intj. used to urge silence', 'timid/to move suddenly back in fear', 'sibling', 'to urge to attack', 'simulation', 'to commit a sin', 'to drink in small quantities', 'respectful form of address used to a man', 'sister', 'to rest on the buttocks', 'number 6', 'Jamaican music', 'to travel on skis', 'to hit or throw toward the sky', 'crafty', 'to cry with a convulsive catching of the breath', 'to cover with sod turf', 'fifth tone of diatonic musical scale so', 'Kyrgyzstan monetary unit', 'male child', 'to dip or soak in a liquid', 'so fifth tone of diatonic musical scale', 'habitual drunkard', 'former French coin', 'to scatter over land for growth, as seed', 'sock-pl knitted or woven covering for the foot', 'soybean', 'mineral spring', 'to watch secretly', 'mister; sir used as a Hindu title of respect', 'to keep in a pigpen', 'to act as a substitute', 'to institute legal proceedings against', 'marketplace souk', 'to add into one total', 'to expose to the sun', 'to eat supper', 'marketplace souk', 'syne', 'to name or designate', 'small boy', 'to', 'to provide with a tag', 'tall, conical cap worn in Muslim countries', 'tight-fitting Scottish cap', 'brown from the sun''s rays/to convert hide into leather by soaking in chemicals', 'path of virtuous conduct according to a Chinese philosophy', 'to strike gently', 'to cover with tar', 'ta thanks', 'to make tatting', 'greek letter', 'Hebrew letter', 'to convert into white leather by the application of minerals', 'to place a tax on', 'beverage made by infusing dried leaves in boiling water', 'to spread for drying', 'to place a golf ball on a small peg', 'yearling sheep', 'ancient mound in the Middle East', 'number 10', 'Hebrew letter teth', 'to work hard', 'article used to specify or make particular', 'though', 'possessive form of the pronoun thou', 'involuntary muscular contraction', 'to fasten with a cord or rope', 'sesame plant', 'to coat with tin', 'to tilt', 'ti seventh tone of diatonic musical scale', 'small bird', 'British unit of weight', 'to touch with the toe', 'to clothe', 'male of various animals', 'unit of weight', 'in addition', 'to cut off the top', 'high, craggy hill', 'to total', 'to pull by means of a rope or chain', 'to amuse oneself as if with a toy', 'to attempt', 'to utter a scolding exclamation', 'to wash in a tub', 'to pull with force', 'bird of New Zealand', 'to store in a large cask', 'to copulate with a ewe', 'to utter an exclamation of impatience', 'tuxedo', 'two', 'number 2', 'chain on a ship', 'Japanese herb', 'sound of a cough or grunt', 'ukulele', 'Eskimo knife', 'intj. expressing hesitation um', 'to umpire', 'un one', 'upon', 'up to raise', 'urban area', 'annual bean grown in India', 'type of vase', 'to vomit', 'to put into service', 'large lizard', 'utility vehicle', 'ut musical tone', 'vacuum cleaner', 'large motor vehicle', 'unit of reactive power', 'anatomical duct', 'to put into a vat', 'Hebrew letter vav', 'Hebrew letter', 'Hebrew letter vav', 'letter ''v''', 'vegetable', 'to treat animals medically', 'to annoy', 'by way of', 'video', 'to strive for superiority', 'charge paid to a bookie on a bet vigorish', 'energy', 'force or power', 'small bay, creek, or inlet', 'to make a vow', 'voice', 'small cavity in a rock or lode', 'intj. expressing surprise', 'web', 'to form into a wad', 'woe', 'to move briskly up and down or to and fro', 'to become wan/unnaturally pale', 'to wrap', 'to engage in war', 'be-conj to exist', 'hare/wet', 'Hebrew letter vav', 'to coat with wax', 'method of doing something', 'to provide with a web', 'to marry', 'short time/very small', 'benign skin tumor', 'soaked with a liquid/to make wet', 'who', 'what or which person or persons', 'reason or cause of something', 'to provide with a wig', 'to be victorious/to winnow', 'to know', 'intelligence/to know', 'wizard', 'tremendous grief', 'dark-skinned foreigner', 'cooking utensil', 'to dwell', 'to seek the affection of', 'Italian offensive', 'wo woe', 'to know', 'to excite to enthusiastic approval', 'contorted/to contort', 'insane', 'letter ''y''', 'rune for ''W'' wynn', 'xi Greek letter', 'synthetic garnet', 'intj. used as an exclamation of disgust', 'to chatter', 'plant having an edible root', 'to bark shrilly', 'yare', 'to deviate from an intended course', 'to this extent', 'affirmative vote', 'yeah', 'to yearn', 'yes', 'to give an affirmative reply to', 'up to now', 'evergreen tree or shrub', 'Jew offensive', 'feminine passive principle Chinese', 'to yelp', 'hoodlum', 'Hebrew letter', 'boisterous laugh', 'day', 'yonder', '2d person sing. or pl. pronoun', 'to yowl', 'to laugh loudly', 'intj. expressing tasteful pleasure', 'yep', 'to turn sharply', 'to kill or destroy', 'za pizza', 'tool for cutting roof slates', 'letter ''z''', 'letter ''z''', 'inmate in a Soviet labor camp', 'long sandwich', 'to turn sharply', 'zinfandel', 'to move rapidly', 'pimple', 'zoon-pl whole product of a fertilized egg', 'place where animals are kept for public exhibition', 'ancient Hebrew silver coin', 'intj. representing the sound of snoring']

    correct_answers = 0
    incorrect_answers = 0

#looping through all the words
    for word in words[0:25]:
#getting a random word
        random_word = random.choice(words)
        list_place = words.index(random_word)
#matching it with the definition
        right_answer = definitions[int(list_place)]
#getting a random definition
        possible_answers = list(random.sample(definitions, 3))
        possible_answers.append(right_answer)
        possible_answers = random.sample(possible_answers, 4)
        right_letter = ''
        answer = raw_input(random_word + '\n' +
                           'A) ' + possible_answers[0] +
                           '\nB) ' + possible_answers[1] +
                           '\nC) ' + possible_answers[2] +
                           '\nD) ' + possible_answers[3] + '\n')
#tallying our score
        if possible_answers[0] == right_answer:
            right_letter = 'a'
        else:
            pass
        if possible_answers[1] == right_answer:
            right_letter = 'b'
        else:
            pass
        if possible_answers[2] == right_answer:
            right_letter = 'c'
        else:
            pass
        if possible_answers[3] == right_answer:
            right_letter = 'd'
        else:
            pass
        if answer == right_letter:
            print "Correct!\n"
            correct_answers = correct_answers + 1
        else:
            print "Wrong! " + right_answer + " is the right answer.\n"
            incorrect_answers = incorrect_answers + 1

#printing our results
    print "Correct answers: ", correct_answers
    print "Incorrect answers: ", incorrect_answers
    pct_correct = str(int(round(100*float(correct_answers)/float(correct_answers+incorrect_answers), 0)))+"%"
    print "Percent correct: ", pct_correct + '\n'

scrabble_threes()
