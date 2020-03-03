from mido import MidiFile

class rawNote:
    def __init__(self, channel, pitch, velocity, time):
        self.channel = channel
        self.pitch = pitch
        self.velocity = velocity
        self.time = time

class fingering:
    def __init__(self, notes):
        self.notes = notes

class fingeringCollection:
    def __init__(self, possibleFingeringss):
        self.possibleFingeringss = possibleFingeringss

class noteArray:
    def __init__(self, notes):
        self.notes = notes

class note:
    def __init__(self, pitch, string, fret):
        self.pitch = pitch
        self.string = string
        self.fret = fret



class rawChord:
    def __init__(self, pitchArray):
        self.pitchArray = pitchArray

def fretToPitch(string, fret):
    return stringOffsetSwitcher(string) + fret

def stringOffsetSwitcher(string): #standard tuning, converts string # to midi pitch of open note
    switcher = {
        0: 40,
        1: 45,
        2: 50,
        3: 55,
        4: 59,
        5: 64
    }
    return switcher.get(string,"Invalid string")

def findNotePositions(rawNote):
    pitch = rawNote.pitch
    if pitch < 45:
        newNote = note(pitch, 0, pitch - 40)
        noteCollection = []
        noteCollection.append(newNote)
        a = fingeringCollection(noteCollection)
        return a
    if 44 < pitch < 50:
        newNote = note(pitch, 0, pitch - 40)
        newNote2 = note(pitch, 1, pitch - 45)
        noteCollection = []
        noteCollection.append(newNote)
        noteCollection.append(newNote2)
        a = fingeringCollection(noteCollection)
        return a
    if 49 < pitch < 55:
        newNote = note(pitch, 0, pitch - 40)
        newNote2 = note(pitch, 1, pitch - 45)
        newNote3 = note(pitch, 2, pitch - 50)
        noteCollection = []
        noteCollection.append(newNote)
        noteCollection.append(newNote2)
        noteCollection.append(newNote3)
        a = fingeringCollection(noteCollection)
        return a
    if 54 < pitch < 59:
        newNote = note(pitch, 0, pitch - 40)
        newNote2 = note(pitch, 1, pitch - 45)
        newNote3 = note(pitch, 2, pitch - 50)
        newNote4 = note(pitch, 3, pitch - 55)
        noteCollection = []
        noteCollection.append(newNote)
        noteCollection.append(newNote2)
        noteCollection.append(newNote3)
        noteCollection.append(newNote4)
        a = fingeringCollection(noteCollection)
        return a
    if 58 < pitch < 64:
        newNote = note(pitch, 0, pitch - 40)
        newNote2 = note(pitch, 1, pitch - 45)
        newNote3 = note(pitch, 2, pitch - 50)
        newNote4 = note(pitch, 3, pitch - 55)
        newNote5 = note(pitch, 4, pitch - 59)
        noteCollection = []
        noteCollection.append(newNote)
        noteCollection.append(newNote2)
        noteCollection.append(newNote3)
        noteCollection.append(newNote4)
        noteCollection.append(newNote5)
        a = fingeringCollection(noteCollection)
        return a
    if pitch == 64:
        newNote = note(pitch, 0, pitch - 40)
        newNote2 = note(pitch, 1, pitch - 45)
        newNote3 = note(pitch, 2, pitch - 50)
        newNote4 = note(pitch, 3, pitch - 55)
        newNote5 = note(pitch, 4, pitch - 59)
        newNote6 = note(pitch, 5, pitch - 64)
        noteCollection = []
        noteCollection.append(newNote)
        noteCollection.append(newNote2)
        noteCollection.append(newNote3)
        noteCollection.append(newNote4)
        noteCollection.append(newNote5)
        noteCollection.append(newNote6)
        a = fingeringCollection(noteCollection)
        return a
    if 64 < pitch < 70:
        newNote2 = note(pitch, 1, pitch - 45)
        newNote3 = note(pitch, 2, pitch - 50)
        newNote4 = note(pitch, 3, pitch - 55)
        newNote5 = note(pitch, 4, pitch - 59)
        newNote6 = note(pitch, 5, pitch - 64)
        noteCollection = []
        noteCollection.append(newNote2)
        noteCollection.append(newNote3)
        noteCollection.append(newNote4)
        noteCollection.append(newNote5)
        noteCollection.append(newNote6)
        a = fingeringCollection(noteCollection)
        return a
    if 69 < pitch < 75:
        newNote3 = note(pitch, 2, pitch - 50)
        newNote4 = note(pitch, 3, pitch - 55)
        newNote5 = note(pitch, 4, pitch - 59)
        newNote6 = note(pitch, 5, pitch - 64)
        noteCollection = []
        noteCollection.append(newNote3)
        noteCollection.append(newNote4)
        noteCollection.append(newNote5)
        noteCollection.append(newNote6)
        a = fingeringCollection(noteCollection)
        return a
    if 74 < pitch < 80:
        newNote4 = note(pitch, 3, pitch - 55)
        newNote5 = note(pitch, 4, pitch - 59)
        newNote6 = note(pitch, 5, pitch - 64)
        noteCollection = []
        noteCollection.append(newNote4)
        noteCollection.append(newNote5)
        noteCollection.append(newNote6)
        a = fingeringCollection(noteCollection)
        return a
    if 79 < pitch < 84:
        newNote5 = note(pitch, 4, pitch - 59)
        newNote6 = note(pitch, 5, pitch - 64)
        noteCollection = []
        noteCollection.append(newNote5)
        noteCollection.append(newNote6)
        a = fingeringCollection(noteCollection)
        return a
    if 83 < pitch < 89:
        newNote6 = note(pitch, 5, pitch - 64)
        noteCollection = []
        noteCollection.append(newNote6)
        a = fingeringCollection(noteCollection)
        return a

def scoringFunc(fret1, fret2):
    if fret1 == 0 or fret2 == 0:
        return 0
    return abs(fret1 - fret2)

def findAveragePosition(fret1, fret2):
    if fret1 == 0:
        if fret2 == 0:
            return 0
        else:
            return fret2
    elif fret2 == 0:
        return fret1
    else:
        return (fret1 + fret2) / 2

mid = MidiFile('sor_study_in_c.mid')

msgArray = []
#j = 0
#for i, track in enumerate(mid.tracks):
    #print('Track {}: {}'.format(i, track.name))
track = mid.tracks[1]
for msg in track:
        if msg.type == 'note_on': #assuming no note_off msgs are used
            #j = j + 1
            msgArray.append(rawNote(msg.channel, msg.note, msg.velocity, msg.time))
            # print('channel ' + str(msg.channel) + '; ' + 'pitch ' + str(msg.note) + '; ' + 'velocity ' + str(msg.velocity) + '; ' + 'time ' + str(msg.time))
# print(len(msgArray))
msgArray2 = []
timeDelta = 0
i=0
while i<len(msgArray):
    msg = msgArray[i]
    if msg.velocity == 0:
        timeDelta = timeDelta + msg.time
    else:
        msgArray2.append(rawNote(msg.channel, msg.pitch, msg.velocity, msg.time + timeDelta))
        timeDelta = 0
    i = i + 1
# for msg in msgArray2:
    # print('channel ' + str(msg.channel) + '; ' + 'pitch ' + str(msg.pitch) + '; ' + 'velocity ' + str(msg.velocity) + '; ' + 'time ' + str(msg.time))
msgArray = []
msgArray3 = []
i = 0
noteOrChordArray = []
while i<len(msgArray2):
    msg = msgArray2[i]
    if msg.time == 0:
        noteOrChordArray.append(rawNote(msg.channel, msg.pitch, msg.velocity, msg.time))
    else: #note potentially part of new chord or is a singlet
        if len(noteOrChordArray) > 0: #previous chord needs to be recorded
            msgArray3.append(noteArray(noteOrChordArray))
            noteOrChordArray = []
            noteOrChordArray.append(rawNote(msg.channel, msg.pitch, msg.velocity, msg.time))
        else:
            noteOrChordArray.append(rawNote(msg.channel, msg.pitch, msg.velocity, msg.time))      
    i = i + 1
msgArray2 = []

# i = 0
# while i<len(msgArray3):
#     j = 0
#     while j < len(msgArray3[i].notes):
#         print('pitch ' + str(msgArray3[i].notes[j].pitch) + ' timeDelta ' + str(msgArray3[i].notes[j].time))
#         j += 1
#     print('\n')
#     i+=1

possibleFingeringsArray = [] #3d array, top level is chord, next is array of individual notes, next is possible fingerings for particular notes in each chord
i = 0
while i < len(msgArray3):
    j = 0
    rawChord = msgArray3[i]
    positionsArray = []
    while j < len(msgArray3[i].notes):
        temp = findNotePositions(msgArray3[i].notes[j])
        positionsArray.append(temp)
        j += 1
    possibleFingeringsArray.append(noteArray(positionsArray))
    i += 1

msgArray3 = []

i = 0
while i < len(possibleFingeringsArray):
    j = 0
    while j < len(possibleFingeringsArray[i].notes):
        k = 0
        while k < len(possibleFingeringsArray[i].notes[j].possibleFingeringss):
            temp = possibleFingeringsArray[i].notes[j].possibleFingeringss[k]
            print('string ' + str(temp.string) + ' fret ' + str(temp.fret))
            k += 1
        print('\n')
        j += 1
    print('\n')
    i += 1

# possibleFingeringsArray2 = []
# i = 0
# while i < len(possibleFingeringsArray):
#     j = 0
#     if len(possibleFingeringsArray[i].notes) == 2:
#         while j < len(possibleFingeringsArray[i].notes[0].possibleFingeringss):
#             possibleFingeringsArray3 = []
#             k = 0
#             while k < len((possibleFingeringsArray[i].notes[1].possibleFingeringss)):
#                 if scoringFunc(possibleFingeringsArray[i].notes[0].possibleFingeringss[j].fret, possibleFingeringsArray[i].notes[1].possibleFingeringss[k].fret) < 5 or possibleFingeringsArray[i].notes[0].possibleFingeringss[j].fret == 0 or possibleFingeringsArray[i].notes[1].possibleFingeringss[k].fret == 0:
#                     if possibleFingeringsArray[i].notes[0].possibleFingeringss[j].string != possibleFingeringsArray[i].notes[1].possibleFingeringss[k].string:
#                         fingeringArray = []
#                         fingeringArray.append(possibleFingeringsArray[i].notes[0].possibleFingeringss[j])
#                         fingeringArray.append(possibleFingeringsArray[i].notes[1].possibleFingeringss[k])
#                         temp = fingering(fingeringArray)
#                         possibleFingeringsArray3.append(temp)
#                 k += 1
#             j += 1
#     else: #single note
#         fingeringArray = []
#         fingeringArray.append(possibleFingeringsArray[i].notes[0].possibleFingeringss[0])
#         temp = fingering(fingeringArray)
#         possibleFingeringsArray3.append(temp)
#     possibleFingeringsArray2.append(fingering(possibleFingeringsArray3))
#     i += 1

# # i = 0
# # while i < len(possibleFingeringsArray2):
# #     j = 0
# #     while j < len(possibleFingeringsArray2[i].notes):
# #         k = 0
# #         while k < len(possibleFingeringsArray2[i].notes[j].notes):
# #             print(str(possibleFingeringsArray2[i].notes[j].notes[k].string) + ' ' + str(possibleFingeringsArray2[i].notes[j].notes[k].fret))
# #             k += 1
# #         print('\n')
# #         j += 1
# #     print('\n')
# #     i += 1

# finalFingerings = [] 
# i = 0
# while i < len(possibleFingeringsArray2) - 1:
#     j = 0
#     bestScore = 1000
#     while j < len(possibleFingeringsArray2[i].notes):
#         k = 0
#         while k < len(possibleFingeringsArray2[i+1].notes):
#             if len(possibleFingeringsArray2[i + 1].notes[k].notes) == 2:
#                     averagePosition2 = findAveragePosition(possibleFingeringsArray2[i + 1].notes[k].notes[0].fret, possibleFingeringsArray2[i + 1].notes[k].notes[1].fret)
#             else:
#                 averagePosition2 = possibleFingeringsArray2[i + 1].notes[k].notes[0].fret
#             if i == 0:
#                 if len(possibleFingeringsArray2[i].notes[j].notes) == 2:
#                     averagePosition1 = findAveragePosition(possibleFingeringsArray2[i].notes[j].notes[0].fret, possibleFingeringsArray2[i].notes[j].notes[1].fret)
#                 else:
#                     averagePosition1 = possibleFingeringsArray2[i].notes[j].notes[0].fret
#                 temp = scoringFunc(averagePosition1, averagePosition2)
#                 if temp < bestScore:
#                     bestScore = temp
#                     tempFingering1 = possibleFingeringsArray2[i].notes[j].notes
#                     tempFingering2 = possibleFingeringsArray2[i + 1].notes[k].notes
#             else:
#                 tempFingering1 = finalFingerings[i].notes
#                 if len(tempFingering1) == 2:
#                     averagePosition1 = findAveragePosition(tempFingering1[0].fret, tempFingering1[1].fret)
#                 else:
#                     averagePosition1 = tempFingering1[0].fret
#                 temp = scoringFunc(averagePosition1, averagePosition2)
#                 if temp < bestScore:
#                     bestScore = temp
#                     tempFingering2 = possibleFingeringsArray2[i + 1].notes[k].notes

#             k += 1
#         j += 1
#     if i == 0:
#         finalFingerings.append(fingering(tempFingering1))
#         finalFingerings.append(fingering(tempFingering2))
#     else:
#         finalFingerings.append(fingering(tempFingering2))
#     i += 1

# i = 0
# while i < len(finalFingerings):
#     j = 0
#     while j < len(finalFingerings[i].notes):
#         print(str(finalFingerings[i].notes[j].string) + ' ' + str(finalFingerings[i].notes[j].fret))
#         j += 1
#     print(' ')
#     i += 1
# lineBuffer1 = ''
# lineBuffer2 = ''
# lineBuffer3 = ''
# lineBuffer4 = ''
# lineBuffer5 = ''
# lineBuffer6 = ''

# i=0

# while i < len(finalFingerings):
#     k = 0
#     line6 = 0
#     line5 = 0
#     line4 = 0
#     line3 = 0
#     line2 = 0
#     line1 = 0
#     while k < len(finalFingerings[i].notes):
#         if k == 1:
#             if finalFingerings[i].notes[k].string == 5:
#                 lineBuffer6 += str(finalFingerings[i].notes[k].fret)
#             else:
#                 if line6 == 0:
#                     lineBuffer6 += '-'
#         if finalFingerings[i].notes[k].string == 5 and k == 0:
#             lineBuffer6 += '----' + str(finalFingerings[i].notes[k].fret)
#             line6 = 1
#         elif k == 0:
#             lineBuffer6 += '----'

#         if k == 1:
#             if finalFingerings[i].notes[k].string == 4:
#                 lineBuffer5 += str(finalFingerings[i].notes[k].fret)
#             else:
#                 if line5 == 0:
#                     lineBuffer5 += '-'
#         if finalFingerings[i].notes[k].string == 4 and k == 0:
#             lineBuffer5 += '----' + str(finalFingerings[i].notes[k].fret)
#             line5 = 1
#         elif k == 0:
#             lineBuffer5 += '----'

#         if k == 1:
#             if finalFingerings[i].notes[k].string == 3:
#                 lineBuffer4 += str(finalFingerings[i].notes[k].fret)
#             else:
#                 if line4 == 0:
#                     lineBuffer4 += '-'
#         if finalFingerings[i].notes[k].string == 3 and k == 0:
#             lineBuffer4 += '----' + str(finalFingerings[i].notes[k].fret)
#             line4 = 1
#         elif k == 0:
#             lineBuffer4 += '----'

#         if k == 1:
#             if finalFingerings[i].notes[k].string == 2:
#                 lineBuffer3 += str(finalFingerings[i].notes[k].fret)
#             else:
#                 if line3 == 0:
#                     lineBuffer3 += '-'
#         if finalFingerings[i].notes[k].string == 2 and k == 0:
#             lineBuffer3 += '----' + str(finalFingerings[i].notes[k].fret)
#             line3 = 1
#         elif k == 0:
#             lineBuffer3 += '----'

#         if k == 1:
#             if finalFingerings[i].notes[k].string == 1:
#                 lineBuffer2 += str(finalFingerings[i].notes[k].fret)
#             else:
#                 if line2 == 0:
#                     lineBuffer2 += '-'
#         if finalFingerings[i].notes[k].string == 1 and k == 0:
#             lineBuffer2 += '----' + str(finalFingerings[i].notes[k].fret)
#             line2 = 1
#         elif k == 0:
#             lineBuffer2 += '----'

#         if k == 1:
#             if finalFingerings[i].notes[k].string == 0:
#                 lineBuffer1 += str(finalFingerings[i].notes[k].fret)
#             else:
#                 if line1 == 0:
#                     lineBuffer1 += '-'
#         if finalFingerings[i].notes[k].string == 0 and k == 0:
#             lineBuffer1 += '----' + str(finalFingerings[i].notes[k].fret)
#             line1 = 1
#         elif k == 0:
#             lineBuffer1 += '----'


#         # if finalFingerings[i].notes[k].string == 4:
#         #     line5 = 1
#         #     lineBuffer5 += '----' + str(finalFingerings[i].notes[k].fret)
#         # else:
#         #     lineBuffer5 += '----'
#         # if finalFingerings[i].notes[k].string == 3:
#         #     line4 = 1
#         #     lineBuffer4 += '----' + str(finalFingerings[i].notes[k].fret)
#         # else:
#         #     lineBuffer4 += '----'
#         # if finalFingerings[i].notes[k].string == 2:
#         #     line3 = 1
#         #     lineBuffer3 += '----' + str(finalFingerings[i].notes[k].fret)
#         # else:
#         #     lineBuffer3 += '----'
#         # if finalFingerings[i].notes[k].string == 1:
#         #     line2 = 1
#         #     lineBuffer2 += '----' + str(finalFingerings[i].notes[k].fret)
#         # else:
#         #     lineBuffer2 += '----'
#         # if finalFingerings[i].notes[k].string == 0:
#         #     line1 = 1
#         #     lineBuffer1 += '----' + str(finalFingerings[i].notes[k].fret)
#         # else:
#         #     lineBuffer1 += '----'
#         k += 1
#     i += 1

# print(lineBuffer6[0:120])
# print(lineBuffer5[0:120])
# print(lineBuffer4[0:120])
# print(lineBuffer3[0:120])
# print(lineBuffer2[0:120])
# print(lineBuffer1[0:120])
# print('\n')
# print(lineBuffer6[121:240])
# print(lineBuffer5[121:240])
# print(lineBuffer4[121:240])
# print(lineBuffer3[121:240])
# print(lineBuffer2[121:240])
# print(lineBuffer1[121:240])
# print('\n')
# print(lineBuffer6[241:360])
# print(lineBuffer5[241:360])
# print(lineBuffer4[241:360])
# print(lineBuffer3[241:360])
# print(lineBuffer2[241:360])
# print(lineBuffer1[241:360])
# print('\n')
# print(lineBuffer6[361:480])
# print(lineBuffer5[361:480])
# print(lineBuffer4[361:480])
# print(lineBuffer3[361:480])
# print(lineBuffer2[361:480])
# print(lineBuffer1[361:480])
# print('\n')
# print(lineBuffer6[481:600])
# print(lineBuffer5[481:600])
# print(lineBuffer4[481:600])
# print(lineBuffer3[481:600])
# print(lineBuffer2[481:600])
# print(lineBuffer1[481:600])
# print('\n')
# print(lineBuffer6[601:682])
# print(lineBuffer5[601:682])
# print(lineBuffer4[601:682])
# print(lineBuffer3[601:682])
# print(lineBuffer2[601:682])
# print(lineBuffer1[601:682])

# print(len(lineBuffer1))





# i = 0
# while i < len(possibleFingeringsArray[0].notes[0].possibleFingeringss):
#     print(str(temp.string) + ' ' + str(temp.fret))
#     i += 1

# print(str(len(possibleFingeringsArray[2].notes[0].possibleFingeringss)))



# fingerings = []

# fretNum = 0
# while fretNum < 25: #for each fret, including open
#     stringNum = 0
#     while stringNum < 6:
#         singleNote = note(fretToPitch(stringNum, fretNum), stringNum, fretNum) #single notes
#         singleNoteContainer = []
#         singleNoteContainer.append(singleNote)
#         chordish = fingering(singleNoteContainer)
#         fingerings.append(chordish)
#         if fretNum == 0:
#             k = 0
#             stringNumSecondNote = stringNum
#             fretNumSecondNote = fretNum
#             while k < 25 * 6 - 25 * (stringNum + 1):
#                 doubleNoteFirst = note(fretToPitch(stringNum, fretNum), stringNum, fretNum)
                
#                 if stringNumSecondNote > 5:
#                     fretNumSecondNote = fretNumSecondNote + 1
#                     stringNumSecondNote = stringNum
#                 if stringNumSecondNote == stringNum:
#                     stringNumSecondNote = stringNumSecondNote + 1
                

#                 doubleNoteSecond = note(fretToPitch(stringNumSecondNote, fretNumSecondNote), stringNumSecondNote, fretNumSecondNote)

#                 doubleNoteContainer = []
#                 doubleNoteContainer.append(doubleNoteFirst)
#                 doubleNoteContainer.append(doubleNoteSecond)

#                 doubleNoteFingering = fingering(doubleNoteContainer)
#                 fingerings.append(doubleNoteFingering)
#                 stringNumSecondNote += 1



#                 k = k + 1
#         # else:
#         #     k = 0
#         stringNum = stringNum + 1
#     fretNum = fretNum + 1

# i = 0
# j = 0
# print(str(len(fingerings)))
# while i < len(fingerings):
#     j = 0
#     while j < len(fingerings[i].notes):
#         if len(fingerings[i].notes) > 1:
#             print(str(fingerings[i].notes[j].pitch) + ' ' + str(fingerings[i].notes[j].string) + ' ' + str(fingerings[i].notes[j].fret))
#         j = j + 1
#         #print('\n')
#     i = i + 1

# note1 = rawNote(0, 43, 60, 60)
# note2 = rawNote(0, 46, 60, 60)
# note3 = rawNote(0, 50, 60, 60)
# note4 = rawNote(0, 57, 60, 60)
# note5 = rawNote(0, 60, 60, 60)
# note6 = rawNote(0, 64, 60, 60)
# note7 = rawNote(0, 68, 60, 60)
# note8 = rawNote(0, 71, 60, 60)
# note9 = rawNote(0, 76, 60, 60)
# note10 = rawNote(0, 82, 60, 60)
# note11 = rawNote(0, 86, 60, 60)
# possArray = []
# possArray.append(findNotePositions(note1))
# possArray.append(findNotePositions(note2))
# possArray.append(findNotePositions(note3))
# possArray.append(findNotePositions(note4))
# possArray.append(findNotePositions(note5))
# possArray.append(findNotePositions(note6))
# possArray.append(findNotePositions(note7))
# possArray.append(findNotePositions(note8))
# possArray.append(findNotePositions(note9))
# possArray.append(findNotePositions(note10))
# possArray.append(findNotePositions(note11))

# i= 0
# while i < len(possArray):
#     j = 0
#     while j < len(possArray[i].possibleFingeringss):
#         print(str(possArray[i].possibleFingeringss[j].string) + ' ' + str(possArray[i].possibleFingeringss[j].fret))
#         j += 1
#     print('\n')
#     i +=1





        







    