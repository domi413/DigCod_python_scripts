# DigCod Python Scripts for TI-Nspire

This repository contains a collection of Python scripts designed for use with the TI-Nspire calculator.

**Note:** You may have to use a TI-nspire CX II, the older version TI-nspire CX may not support python scripts. It requires OS 5.20 or greater, the older TI-nspire CX can only be updated up to version ~ 4.5

The reason I don't upload these scripts to the _Studentenportal_ is that they are likely to be removed. The _Studentenportal_ is monitored by lecturers who delete not allowed stuff. These scripts aren't currently illegal, but they could become because they make the exam much easier.

## Usage

To use these scripts on your TI-Nspire calculator:

1. Connect your Handheld to the computer.
2. Open the TI-Nspire Student Software.
3. Create a new Python script within the software.
4. Copy and paste the content of each `.py` script into the new Python script you created.
5. Use the "File -> Save to Handheld" function to transfer the script to your calculator.

Cracked version of Students-software can be found [here](https://filecr.com/windows/ti-nspire-cx-cas-student-software/?id=494300560000).

### Alternatively:

1. Open Chrome (it's required to use Chrome for this method).\*1
2. Navigate to [TI-Nspire Navigator](https://nspireconnect.ti.com/nsc/).
3. Choose the option to transfer files. \*2

\*1 This method doesn't work for linux. The only option for linux is AFAIK through a VM.

\*2 Apparently you have to rename the `.py` to `.tns` to create a supported file type, but then you receive another error message when opening the file. So you prolly have to use the Students Software.

## Running Scripts

To execute a script on the TI-Nspire:

1. Navigate to the script on your handheld.
2. Press `ctrl+r` to run the script.
3. Follow the on-screen prompts to input numbers and observe the output.

## TODO

- [ ] Implement an option to abort the running script e.g. with `ctrl+c`
- [ ] Make the main-loops consistent, so every script has the same structure
- [ ] Rewrite the scripts in Lua, so they can also be used on the older CX-Version
- [ ] Would be cool if all scripts are combined in a single script. E.g. a menu in which you can select a script and a script and if the script has run through, you jump back to the menu.

### Additional scripts TODO

- [ ] Make a RSA script based on the `multiplicative_inverse.py` that takes the given keys as input and calculates everything else
- [ ] Enhance the `binary_decimal.py` so it solves the exercise in the exam 1:1

#### Informationstheorie:

- [ ] Entscheidungsgehalt
- [ ] Informationsgehalt
- [ ] Entropie
- [ ] Redundanz der Quelle
- [ ] Mittlere Codewortlänge
- [ ] Redundanz des Codes
- [ ] Maximierung Entropie

#### Kanalmatrix:

- [ ] Berechnung der Kanalmatrix
- [ ] Berechnung der Eingangswahrscheinlichkeiten
- [ ] Berechnung der Ausgangswahrscheinlichkeiten
- [ ] Entropie am Kanaleingang H(X)
- [ ] Entropie am Kanalausgang H(Y)
- [ ] Transinformation
- [ ] Maximale Symbolrate

#### Blockcodes:

- [ ] Hammingdistanz
- [ ] Anzahl möglicher/gültiger Codewörter
- [ ] Dichtgepacktheit eines Codes
- [ ] Schnelle Mehrfachaddition
