import InvertSM64Recolor

recolor_value = """
8107EC40 0000
8107EC42 FF00
8107EC38 0000
8107EC3A FF00
8107ECA0 7306
8107ECA2 0000
8107EC98 3903
8107EC9A 0000
8107EC88 FEC1
8107EC8A 7900
8107EC80 7F60
8107EC82 3C00
8107EC58 FFFF
8107EC5A FF00
8107EC50 7F7F
8107EC52 7F00
8107EC28 0000
8107EC2A 0000
8107EC68 2F0E
8107EC6A 0700
8107EC20 0000
8107EC22 0000
8107EC70 721C
8107EC72 0E00"""

# Insert your color code into recolor_value(make sure it's still with """ on both sides a.k.a 3 ") - default one is SMG3's Color Code - must be a complete color code with all the hat information, etc. not an uncomplete one(so yes, it needs values, that you wouldn't use normally.)

InvertSM64Recolor.RecolorInverter(recolor_value)
