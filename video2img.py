import cv2
import os
import sys
import pathlib

# for i in range(len(sys.argv)):
# print("%s" % sys.argv[i])

if len(sys.argv) < 3:
    print("%s convert video into pictures of frames.\n" % sys.argv[0])
    print("Usage: %s [video] [number of frames to convert]\n" % sys.argv[0])
    sys.exit(0)

# sys.exit(0)

# fname="/data/streams/VID_20230907_094240"
fullname = sys.argv[1]
path = pathlib.Path(sys.argv[1]).parent.resolve()
file_name = pathlib.Path(sys.argv[1]).stem
file_extension = pathlib.Path(sys.argv[1]).suffix
# print("path:", path)
# print("file_name:", file_name)
# print("file_extension:", file_extension)
# sys.exit(0)

wanted_frames = int(sys.argv[2])
# print("wanted_frames:",wanted_frames)
# sys.exit(0)

vidcap = cv2.VideoCapture("%s" % fullname)

# length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
# print("total frames:", length )

interval = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT) / wanted_frames)
print("wanted frames:", wanted_frames)
print("frame interval:", interval)

# sys.exit(0)
os.makedirs("%s/%s" % (path, file_name))

success, image = vidcap.read()
# count = 0
count = 1
written = 0
while success:
    if count % interval == 0:
        print("Writing %s-%d.jpg" % (file_name, count))
        cv2.imwrite(
            "%s/%s/%s-%d.jpg" % (path, file_name, file_name, count), image
        )  # save frame as JPEG file
        written += 1
    success, image = vidcap.read()
    #   print('Read a new frame: ', success)
    count += 1
    if written >= wanted_frames:
      break
print("Total %d frames are written to files." % written)
