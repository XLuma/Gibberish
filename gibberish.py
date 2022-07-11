from ctypes import sizeof
from logging import root
from random import randrange
import googletrans
from pymsyt import Msbt
import deepl
import os
LANGUAGE = "en" #change this to your source language
API_KEY = "" #add you Deepl api key here
CYCLES = 6 #how many times text should be translated before going back to english. adjust this to taste
languages = ["BG", "CS", "DA", "DE", "ES", "ET", "FI", "FR", "HU", "ID", "IT", "JA", "LT", "LV", "NL", "PL", "PT-PT","PT-BR", "RO", "RU", "SK", "SL", "SV", "TR", "ZH"]
current_language = ""
curent_lang_index = 0
rootdir = os.getcwd()
rootdir = rootdir + "\\translate"
outdir = os.getcwd() + "\\output"

def pick_language():
    i = randrange(0, len(googletrans.LANGCODES))
    return i, googletrans.LANGCODES[i]


def main():
    translator = deepl.Translator(API_KEY)
    google_trans = googletrans.Translator()
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            outfile = outdir  + str.split(subdir, "\\translate")[1] + "\\" + file
            data = open(os.path.join(subdir, file), "rb").read()
            msbt = Msbt.from_binary(data)
            msbt_dict = msbt.to_dict()
            for entry, contents in msbt_dict["entries"].items(): # Iterate MSBT text entries
                print(entry)
                for texts in contents.values():
                    for stuff in texts:
                        if 'text' in stuff: #lmao finally got them strings
                            currentString = stuff['text']
                            #result = translator.translate_text(currentString, target_lang=LANGUAGE)
                            result = google_trans.translate(currentString, dest='en')
                            for i in range(CYCLES):
                                curent_lang_index, current_language = pick_language()
                                #result = translator.translate_text(result.text, target_lang=current_language) #have a random function to pick a language
                                result = google_trans.translate(result.text, dest=current_language)
                            #outstr = translator.translate_text(result.text, target_lang=LANGUAGE)
                            outstr = google_trans.translate(result.text, dest=LANGUAGE)
                            #print(outstr.text)
                            msbt_dict["entries"][entry] = { # Adding a new text entry
                                "contents": [{"text":outstr.text}]
                            }
            os.makedirs(outdir + str.split(subdir, "\\translate")[1], exist_ok=True)
            open(outfile, 'wb').write( Msbt.from_dict(msbt_dict).to_binary(big_endian=True))
                                

    


if __name__ == "__main__":
    main()
