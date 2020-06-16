def same_by(characteristic, objects):
    objects = list(map(characteristic, objects))
    return [objects[0]] * len(objects) == objects if len(objects) > 0 else True
