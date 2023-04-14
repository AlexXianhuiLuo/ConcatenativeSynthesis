import wave
import eng_to_ipa as ipa

pathToBank = "ConcatenativeSynthesis/PhoneBank/"

test = "arm"
phonetic = ipa.convert(test)

data = []
for phone in phonetic:
    audioPath = pathToBank + phone + ".wav"
    w = wave.open(audioPath, "rb")
    data.append([w.getparams(), w.readframes(w.getnframes())])
    w.close()

output = wave.open("ConcatenativeSynthesis/output.wav", "wb")
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()

print(phonetic)

class Concatenater:
    def __init__(self, audioFiles):
        self.files = audioFiles

    def append(self, item):
        self.files.append(item)
    
    def concatenate(self):
        data = []
        for x in self.files:
            w = wave.open(x, "rb")
            data.append([w.getparams(), w.readframes(w.getnframes())])
            w.close()
        output = wave.open("ConcatenativeSynthesis/output.wav", "wb")
        output.setparams(data[0][0])
        for i in range(len(data)):
            output.writeframes(data[i][1])
        output.close()