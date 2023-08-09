from pathlib import Path
import json

from pascal import PascalVOC

ds = Path("/home/nhan/Downloads/img_facemask_all/archive")
annotations = ds / "annotations"
img_path = ds / "images"
out = ds / "images"

if __name__ == '__main__':
    for file in annotations.glob("*.xml"):
        ann = PascalVOC.from_xml(file)
        lbl_me = ann.to_labelme(img_path, save_img_data=False)
        with open(out / f"{file.stem}.json", "w") as f:
            json.dump(lbl_me, f)
