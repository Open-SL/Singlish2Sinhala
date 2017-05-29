# -*- coding: utf-8 -*-
import sys

consonants= []
consonantsUni= []
vowels= []
vowelsUni= []
vowelModifiersUni= []
specialConsonants= []
specialConsonantsUni= []
specialCharUni= []
specialChar= []

vowelsUni.extend(['ඌ','ඕ','ඕ','ආ','ආ','ඈ','ඈ','ඈ','ඊ','ඊ','ඊ','ඊ','ඒ','ඒ','ඒ','ඌ','ඌ','ඖ','ඇ'])

vowels.extend(['oo','o\\)','oe','aa','a\\)','Aa','A\\)','ae','ii','i\\)','ie','ee','ea','e\\)','ei','uu','u\\)','au','/\a'])

vowelModifiersUni.extend(['ූ','ෝ','ෝ','ා','ා','ෑ','ෑ','ෑ','ී','ී','ී','ී','ේ','ේ','ේ','ූ','ූ','ෞ','ැ'])

vowelsUni.extend(['අ','ඇ','ඉ','එ','උ','ඔ','ඓ'])

vowels.extend(['a','A','i','e','u','o','I'])

vowelModifiersUni.extend(['','ැ','ි','ෙ','ු','ො','ෛ'])

nVowels=26;

specialConsonantsUni.extend(['ං','ඃ','ඞ','ඍ'])

specialConsonants.extend(["\n","\h","\N","\R"])
# special characher Repaya
specialConsonantsUni.append('ර්'+'\u200D')
specialConsonantsUni.append('ර්'+'\u200D')

specialConsonants.append("/R")
specialConsonants.append("\r")

consonantsUni.extend(['ඬ','ඳ','ඟ','ථ','ධ','ඝ','ඡ','ඵ','භ','ශ','ෂ','ඥ','ඤ','ළු','ද','ච','ඛ','ත'])

consonants.extend(['nnd','nndh','nng','Th','Dh','gh','Ch','ph','bh','sh','Sh','GN','KN','Lu','dh','ch','kh','th'])

consonantsUni.extend(['ට','ක','ඩ','න','ප','බ','ම','‍ය','‍ය','ය','ජ','ල','ව','ව','ස','හ','ණ','ළ','ඛ','ඝ','ඨ','ඪ','ඵ','ඹ','ෆ','ඣ','ග'])

consonants.extend(['t','k','d','n','p','b','m','\\u005C' + 'y','Y','y','j','l','v','w','s','h','N','L','K','G','T','D','P','B','f','q','g'])

consonantsUni.append('ර')
consonants.append('r')

specialCharUni.append('ෲ')
specialChar.append('ruu')
specialCharUni.append('ෘ')
specialChar.append('ru')
# specialCharUni.append('්‍ර')
# specialChar.append('ra')

def Translate(text):
    # special consonents
    for i in range (0,len(specialConsonants)):
        text = text.replace(specialConsonants[i], specialConsonantsUni[i])


    # consonents + special
    for i in range (0,len(specialCharUni)):
        for j in range(0,len(consonants)):
            s = consonants[j] + specialChar[i]
            v = consonantsUni[j] + specialCharUni[i]
            r = s
            text = text.replace(r, v)



    # consonants + Rakaransha + vowel modifiers
    for j in range(0,len(consonants)):
        for i in range(0,len(vowels)):
            s = consonants[j] + "r" + vowels[i]
            v = consonantsUni[j] + "්‍ර" + vowelModifiersUni[i]
            r = s
            # r = new RegExp(s, "g")
            text = text.replace(r, v)

        s = consonants[j] + "r"
        v = consonantsUni[j] + "්‍ර"
        r = v
        text = text.replace(r, v)


    # constants with vowels modifiers
    for i in range(0,len(consonants)):
        for j in range(0,nVowels):
            s = consonants[i]+vowels[j]
            v = consonantsUni[i] + vowelModifiersUni[j]
            r = s
            text = text.replace(r, v)



    # Hal kirima
    for i in range(0, len(consonants)):
        r = consonants[i]
        text = text.replace(r, consonantsUni[i]+"්")


    # adding vowels
    for i in range(0,len(vowels)):
        r = vowels[i]
        text = text.replace(r, vowelsUni[i])

    return text

if __name__ == '__main__':
    print Translate(sys.argv[1])
