# Gibberish
Gibberish is a simple program to "poorly translate" text from msbt files. It achieves this by using the Deepl api to translate text to foreign languages back to english.

It is currently broken, because Deepl costs WAY too much, and googletrans... simply doesnt work. Official apis like Google's or Microsoft's also requires actual cards, which I dont have so... deepl it is

Update: found a (Rather slow) library that allows to freely translate stuff, so... thats better than nothing !!!

# Dependencies
- to use this, you will need python, deepl, pymsyt.

# Usage

- Put the necessary files in the "translate" folder. then, open the program and change the source language as well as how many times it should be translated. (The lower the value, the less weird it is likely to be)
- You will also need a Deepl api key. You can signup for their free plan which allows 500k characters per month, which should be plenty(spoilers: it is not. Dont signup for Deepl, its way too expensive. Bing is the cheapest of the bunch and you get funny results). Put it in the required field in the program.
- Then simply launch the program, and wait. An "output" folder will appear with new files, having translated text. 

