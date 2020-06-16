import wave
import struct


def chip_and_dale(number):
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")
    dest.setparams(source.getparams())
    frames_count = source.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    newdata = data[:: number]
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    dest.writeframes(newframes)
    source.close()
    dest.close()
