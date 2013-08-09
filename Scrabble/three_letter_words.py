#this game pops up random combox and we have to guess if it's a three-letter word
import itertools
import random


def scrabble_threes():

    print "\nAre these two-letter combinations valid Scrabble words?\n\
    - Type 'quit' to quit\n\
    - Type 'y' for yes\n\
    - Type 'n' for no\n---"

    consonant_combos = ['BH', 'BL', 'BR', 'BY', 'CH', 'CL', 'CR', 'CT', 'CV', 'CY', 'DH', 'DL', 'DR', 'DY', 'FL', 'FR', 'FT', 'GH', 'GL', 'GN', 'GR', 'GT', 'GY', 'HY', 'LY', 'MY', 'PH', 'PL', 'PR', 'PS', 'RN', 'RT', 'SH', 'SM', 'SN', 'SP', 'ST', 'SY', 'TH', 'TR', 'WH']

    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    vowels = ['A', 'E', 'I', 'O', 'U']

#valid words
    words = ['AAH', 'AAL', 'AAS', 'ABA', 'ABO', 'ABS', 'ABY', 'ACE', 'ACT', 'ADD', 'ADO',
             'ADS', 'ADZ', 'AFF', 'AFT', 'AGA', 'AGE', 'AGO', 'AGS', 'AHA', 'AHI', 'AHS',
             'AID', 'AIL', 'AIM', 'AIN', 'AIR', 'AIS', 'AIT', 'ALA', 'ALB', 'ALE', 'ALL',
             'ALP', 'ALS', 'ALT', 'AMA', 'AMI', 'AMP', 'AMU', 'ANA', 'AND', 'ANE', 'ANI',
             'ANT', 'ANY', 'APE', 'APO', 'APP', 'APT', 'ARB', 'ARC', 'ARE', 'ARF', 'ARK',
             'ARM', 'ARS', 'ART', 'ASH', 'ASK', 'ASP', 'ASS', 'ATE', 'ATT', 'AUK', 'AVA',
             'AVE', 'AVO', 'AWA', 'AWE', 'AWL', 'AWN', 'AXE', 'AYE', 'AYS', 'AZO', 'BAA',
             'BAD', 'BAG', 'BAH', 'BAL', 'BAM', 'BAN', 'BAP', 'BAR', 'BAS', 'BAT', 'BAY',
             'BED', 'BEE', 'BEG', 'BEL', 'BEN', 'BES', 'BET', 'BEY', 'BIB', 'BID', 'BIG',
             'BIN', 'BIO', 'BIS', 'BIT', 'BIZ', 'BOA', 'BOB', 'BOD', 'BOG', 'BOO', 'BOP',
             'BOS', 'BOT', 'BOW', 'BOX', 'BOY', 'BRA', 'BRO', 'BRR', 'BUB', 'BUD', 'BUG',
             'BUM', 'BUN', 'BUR', 'BUS', 'BUT', 'BUY', 'BYE', 'BYS', 'CAB', 'CAD', 'CAM',
             'CAN', 'CAP', 'CAR', 'CAT', 'CAW', 'CAY', 'CEE', 'CEL', 'CEP', 'CHI', 'CIG',
             'CIS', 'COB', 'COD', 'COG', 'COL', 'CON', 'COO', 'COP', 'COR', 'COS', 'COT',
             'COW', 'COX', 'COY', 'COZ', 'CRU', 'CRY', 'CUB', 'CUD', 'CUE', 'CUM', 'CUP',
             'CUR', 'CUT', 'CWM', 'DAB', 'DAD', 'DAG', 'DAH', 'DAK', 'DAL', 'DAM', 'DAN',
             'DAP', 'DAW', 'DAY', 'DEB', 'DEE', 'DEF', 'DEL', 'DEN', 'DEV', 'DEW', 'DEX',
             'DEY', 'DIB', 'DID', 'DIE', 'DIF', 'DIG', 'DIM', 'DIN', 'DIP', 'DIS', 'DIT',
             'DOC', 'DOE', 'DOG', 'DOL', 'DOM', 'DON', 'DOR', 'DOS', 'DOT', 'DOW', 'DRY',
             'DUB', 'DUD', 'DUE', 'DUG', 'DUH', 'DUI', 'DUN', 'DUO', 'DUP', 'DYE', 'EAR',
             'EAT', 'EAU', 'EBB', 'ECU', 'EDH', 'EDS', 'EEK', 'EEL', 'EFF', 'EFS', 'EFT',
             'EGG', 'EGO', 'EKE', 'ELD', 'ELF', 'ELK', 'ELL', 'ELM', 'ELS', 'EME', 'EMS',
             'EMU', 'END', 'ENG', 'ENS', 'EON', 'ERA', 'ERE', 'ERG', 'ERN', 'ERR', 'ERS',
             'ESS', 'ETA', 'ETH', 'EVE', 'EWE', 'EYE', 'FAB', 'FAD', 'FAG', 'FAN', 'FAR',
             'FAS', 'FAT', 'FAX', 'FAY', 'FED', 'FEE', 'FEH', 'FEM', 'FEN', 'FER', 'FES',
             'FET', 'FEU', 'FEW', 'FEY', 'FEZ', 'FIB', 'FID', 'FIE', 'FIG', 'FIL', 'FIN',
             'FIR', 'FIT', 'FIX', 'FIZ', 'FLU', 'FLY', 'FOB', 'FOE', 'FOG', 'FOH', 'FON',
             'FOP', 'FOR', 'FOU', 'FOX', 'FOY', 'FRO', 'FRY', 'FUB', 'FUD', 'FUG', 'FUN',
             'FUR', 'GAB', 'GAD', 'GAE', 'GAG', 'GAL', 'GAM', 'GAN', 'GAP', 'GAR', 'GAS',
             'GAT', 'GAY', 'GED', 'GEE', 'GEL', 'GEM', 'GEN', 'GET', 'GEY', 'GHI', 'GIB',
             'GID', 'GIE', 'GIG', 'GIN', 'GIP', 'GIT', 'GNU', 'GOA', 'GOB', 'GOD', 'GOO',
             'GOR', 'GOS', 'GOT', 'GOX', 'GOY', 'GUL', 'GUM', 'GUN', 'GUT', 'GUV', 'GUY',
             'GYM', 'GYP', 'HAD', 'HAE', 'HAG', 'HAH', 'HAJ', 'HAM', 'HAO', 'HAP', 'HAS',
             'HAT', 'HAW', 'HAY', 'HEH', 'HEM', 'HEN', 'HEP', 'HER', 'HES', 'HET', 'HEW',
             'HEX', 'HEY', 'HIC', 'HID', 'HIE', 'HIM', 'HIN', 'HIP', 'HIS', 'HIT', 'HMM',
             'HOB', 'HOD', 'HOE', 'HOG', 'HON', 'HOP', 'HOS', 'HOT', 'HOW', 'HOY', 'HUB',
             'HUE', 'HUG', 'HUH', 'HUM', 'HUN', 'HUP', 'HUT', 'HYP', 'ICE', 'ICH', 'ICK',
             'ICY', 'IDS', 'IFF', 'IFS', 'IGG', 'ILK', 'ILL', 'IMP', 'INK', 'INN', 'INS',
             'ION', 'IRE', 'IRK', 'ISM', 'ITS', 'IVY', 'JAB', 'JAG', 'JAM', 'JAR', 'JAW',
             'JAY', 'JEE', 'JET', 'JEU', 'JEW', 'JIB', 'JIG', 'JIN', 'JOB', 'JOE', 'JOG',
             'JOT', 'JOW', 'JOY', 'JUG', 'JUN', 'JUS', 'JUT', 'KAB', 'KAE', 'KAF', 'KAS',
             'KAT', 'KAY', 'KEA', 'KEF', 'KEG', 'KEN', 'KEP', 'KEX', 'KEY', 'KHI', 'KID',
             'KIF', 'KIN', 'KIP', 'KIR', 'KIS', 'KIT', 'KOA', 'KOB', 'KOI', 'KOP', 'KOR',
             'KOS', 'KUE', 'KYE', 'LAB', 'LAC', 'LAD', 'LAG', 'LAM', 'LAP', 'LAR', 'LAS',
             'LAT', 'LAV', 'LAW', 'LAX', 'LAY', 'LEA', 'LED', 'LEE', 'LEG', 'LEI', 'LEK',
             'LES', 'LET', 'LEU', 'LEV', 'LEX', 'LEY', 'LEZ', 'LIB', 'LID', 'LIE', 'LIN',
             'LIP', 'LIS', 'LIT', 'LOB', 'LOG', 'LOO', 'LOP', 'LOT', 'LOW', 'LOX', 'LUG',
             'LUM', 'LUV', 'LUX', 'LYE', 'MAC', 'MAD', 'MAE', 'MAG', 'MAN', 'MAP', 'MAR',
             'MAS', 'MAT', 'MAW', 'MAX', 'MAY', 'MED', 'MEG', 'MEL', 'MEM', 'MEN', 'MET',
             'MEW', 'MHO', 'MIB', 'MIC', 'MID', 'MIG', 'MIL', 'MIM', 'MIR', 'MIS', 'MIX',
             'MOA', 'MOB', 'MOC', 'MOD', 'MOG', 'MOL', 'MOM', 'MON', 'MOO', 'MOP', 'MOR',
             'MOS', 'MOT', 'MOW', 'MUD', 'MUG', 'MUM', 'MUN', 'MUS', 'MUT', 'MYC', 'NAB',
             'NAE', 'NAG', 'NAH', 'NAM', 'NAN', 'NAP', 'NAW', 'NAY', 'NEB', 'NEE', 'NEG',
             'NET', 'NEW', 'NIB', 'NIL', 'NIM', 'NIP', 'NIT', 'NIX', 'NOB', 'NOD', 'NOG',
             'NOH', 'NOM', 'NOO', 'NOR', 'NOS', 'NOT', 'NOW', 'NTH', 'NUB', 'NUN', 'NUS',
             'NUT', 'OAF', 'OAK', 'OAR', 'OAT', 'OBA', 'OBE', 'OBI', 'OCA', 'ODA', 'ODD',
             'ODE', 'ODS', 'OES', 'OFF', 'OFT', 'OHM', 'OHO', 'OHS', 'OIL', 'OKA', 'OKE',
             'OLD', 'OLE', 'OMS', 'ONE', 'ONO', 'ONS', 'OOH', 'OOT', 'OPE', 'OPS', 'OPT',
             'ORA', 'ORB', 'ORC', 'ORE', 'ORS', 'ORT', 'OSE', 'OUD', 'OUR', 'OUT', 'OVA',
             'OWE', 'OWL', 'OWN', 'OXO', 'OXY', 'PAC', 'PAD', 'PAH', 'PAL', 'PAM', 'PAN',
             'PAP', 'PAR', 'PAS', 'PAT', 'PAW', 'PAX', 'PAY', 'PEA', 'PEC', 'PED', 'PEE',
             'PEG', 'PEH', 'PEN', 'PEP', 'PER', 'PES', 'PET', 'PEW', 'PHI', 'PHT', 'PIA',
             'PIC', 'PIE', 'PIG', 'PIN', 'PIP', 'PIS', 'PIT', 'PIU', 'PIX', 'PLY', 'POD',
             'POH', 'POI', 'POL', 'POM', 'POO', 'POP', 'POT', 'POW', 'POX', 'PRO', 'PRY',
             'PSI', 'PST', 'PUB', 'PUD', 'PUG', 'PUL', 'PUN', 'PUP', 'PUR', 'PUS', 'PUT',
             'PYA', 'PYE', 'PYX', 'QAT', 'QIS', 'QUA', 'RAD', 'RAG', 'RAH', 'RAI', 'RAJ',
             'RAM', 'RAN', 'RAP', 'RAS', 'RAT', 'RAW', 'RAX', 'RAY', 'REB', 'REC', 'RED',
             'REE', 'REF', 'REG', 'REI', 'REM', 'REP', 'RES', 'RET', 'REV', 'REX', 'RHO',
             'RIA', 'RIB', 'RID', 'RIF', 'RIG', 'RIM', 'RIN', 'RIP', 'ROB', 'ROC', 'ROD',
             'ROE', 'ROM', 'ROT', 'ROW', 'RUB', 'RUE', 'RUG', 'RUM', 'RUN', 'RUT', 'RYA',
             'RYE', 'SAB', 'SAC', 'SAD', 'SAE', 'SAG', 'SAL', 'SAP', 'SAT', 'SAU', 'SAW',
             'SAX', 'SAY', 'SEA', 'SEC', 'SEE', 'SEG', 'SEI', 'SEL', 'SEN', 'SER', 'SET',
             'SEW', 'SEX', 'SHA', 'SHE', 'SHH', 'SHY', 'SIB', 'SIC', 'SIM', 'SIN', 'SIP',
             'SIR', 'SIS', 'SIT', 'SIX', 'SKA', 'SKI', 'SKY', 'SLY', 'SOB', 'SOD', 'SOL',
             'SOM', 'SON', 'SOP', 'SOS', 'SOT', 'SOU', 'SOW', 'SOX', 'SOY', 'SPA', 'SPY',
             'SRI', 'STY', 'SUB', 'SUE', 'SUK', 'SUM', 'SUN', 'SUP', 'SUQ', 'SYN', 'TAB',
             'TAD', 'TAE', 'TAG', 'TAJ', 'TAM', 'TAN', 'TAO', 'TAP', 'TAR', 'TAS', 'TAT',
             'TAU', 'TAV', 'TAW', 'TAX', 'TEA', 'TED', 'TEE', 'TEG', 'TEL', 'TEN', 'TET',
             'TEW', 'THE', 'THO', 'THY', 'TIC', 'TIE', 'TIL', 'TIN', 'TIP', 'TIS', 'TIT',
             'TOD', 'TOE', 'TOG', 'TOM', 'TON', 'TOO', 'TOP', 'TOR', 'TOT', 'TOW', 'TOY',
             'TRY', 'TSK', 'TUB', 'TUG', 'TUI', 'TUN', 'TUP', 'TUT', 'TUX', 'TWA', 'TWO',
             'TYE', 'UDO', 'UGH', 'UKE', 'ULU', 'UMM', 'UMP', 'UNS', 'UPO', 'UPS', 'URB',
             'URD', 'URN', 'URP', 'USE', 'UTA', 'UTE', 'UTS', 'VAC', 'VAN', 'VAR', 'VAS',
             'VAT', 'VAU', 'VAV', 'VAW', 'VEE', 'VEG', 'VET', 'VEX', 'VIA', 'VID', 'VIE',
             'VIG', 'VIM', 'VIS', 'VOE', 'VOW', 'VOX', 'VUG', 'VUM', 'WAB', 'WAD', 'WAE',
             'WAG', 'WAN', 'WAP', 'WAR', 'WAS', 'WAT', 'WAW', 'WAX', 'WAY', 'WEB', 'WED',
             'WEE', 'WEN', 'WET', 'WHA', 'WHO', 'WHY', 'WIG', 'WIN', 'WIS', 'WIT', 'WIZ',
             'WOE', 'WOG', 'WOK', 'WON', 'WOO', 'WOP', 'WOS', 'WOT', 'WOW', 'WRY', 'WUD',
             'WYE', 'WYN', 'XIS', 'YAG', 'YAH', 'YAK', 'YAM', 'YAP', 'YAR', 'YAW', 'YAY',
             'YEA', 'YEH', 'YEN', 'YEP', 'YES', 'YET', 'YEW', 'YID', 'YIN', 'YIP', 'YOB',
             'YOD', 'YOK', 'YOM', 'YON', 'YOU', 'YOW', 'YUK', 'YUM', 'YUP', 'ZAG', 'ZAP',
             'ZAS', 'ZAX', 'ZED', 'ZEE', 'ZEK', 'ZEP', 'ZIG', 'ZIN', 'ZIP', 'ZIT', 'ZOA',
             'ZOO', 'ZUZ', 'ZZZ']

#combining possible letters
    combos = list(itertools.product(consonants, vowels, consonants)) + list(itertools.product(vowels, consonants, vowels))\
        + list(itertools.product(vowels, vowels, consonants)) + list(itertools.product(consonants, vowels, vowels))\
        + list(itertools.product(consonant_combos, vowels)) + words
    correct_answers = 0
    incorrect_answers = 0
    are_words = ''
    not_words = ''
    words_found = ''

#picking random combox
    for c in combos[0:25]:
        random_item = random.choice(combos)
        text = ''.join(random_item)
        answer = raw_input(text + '\n')

#if the combo is a valid word
        if answer == 'y' and any(text in w for w in words):
            print "Correct, " + text + " is a word! \n---"
            correct_answers = correct_answers + 1
            words_found = words_found + text + '\n'
        elif answer == 'n' and any(text in w for w in words):
            print "Nope, " + text + " is a word! \n---"
            incorrect_answers = incorrect_answers + 1
            are_words = are_words + text + '\n'
        elif answer == 'n' and any(text not in w for w in words):
            print "Correct, " + text + " is not a word! \n---"
            correct_answers = correct_answers + 1
        elif answer == 'y' and any(text not in w for w in words):
            print "Nope, " + text + " is not a word! \n---"
            incorrect_answers = incorrect_answers + 1
            not_words = not_words + text + '\n'
        elif answer == "quit":
            print "---\nCorrect: ", correct_answers
            print "Incorrect: ", incorrect_answers
            pct_correct = str(int(round(100*float(correct_answers)/float(correct_answers+incorrect_answers), 0)))+"%"
            print "Percent correct: ", pct_correct
            if words_found != '':
                print "\nYou correctly found:\n", words_found
            else:
                pass
            if are_words != '':
                print "Are words:\n", are_words
            else:
                pass
            if not_words != '':
                print "Not words:\n", not_words
            else:
                pass
            quit()
        else:
            print "Invalid answer!\n---"

#getting our results
    print "\nCorrect answers: ", correct_answers
    print "Incorrect answers: ", incorrect_answers
    pct_correct = str(int(round(100*float(correct_answers)/float(correct_answers+incorrect_answers), 0)))+"%"
    print "Percent correct: ", pct_correct
    if words_found != '':
        print "\nYou correctly found:\n", words_found
    else:
        pass
    if are_words != '':
        print "These are words:\n", are_words
    else:
        pass
    if not_words != '':
        print "These are not words:\n", not_words
    else:
        pass

scrabble_threes()

#make answer a separate function, pass the answer to the function
#if function returns correct or not, if correct, do something
#tkinter
