import wave
import struct


def break_the_silence():
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")
    dest.setparams(source.getparams())
    frames_count = source.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    newdata = list(filter(lambda x: abs(x) > 5, data))
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    dest.writeframes(newframes)
    source.close()
    dest.close()