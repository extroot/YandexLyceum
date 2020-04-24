import wave
import struct


def pitch_and_toss():
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")
    dest.setparams(source.getparams())
    frames_count = source.getnframes()

    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    newdata = [data[:len(data) // 4], data[len(data) // 4: len(data) // 4 * 2],
               data[len(data) // 4 * 2: len(data) // 4 * 3], data[len(data) // 4 * 3:]]
    newdata = list(newdata[2]) + list(newdata[3]) + list(newdata[0]) + list(newdata[1])
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    dest.writeframes(newframes)
    source.close()
    dest.close()
