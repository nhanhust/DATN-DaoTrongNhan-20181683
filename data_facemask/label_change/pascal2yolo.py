from pathlib import Path

from pascal import PascalVOC
 
ds = input("Duong dan tro toi folder chua cac file xml can chuyen doi:  ").strip()
ds = Path(ds)
outfile = input("Duong dan tro toi folder label can chuyen doi:  ").strip()
#ds = Path("/home/nhan/Downloads/data_facemask/new_data/mask_label.v5i.voc/train")

label_map = {
    "without_mask": 0,
    "with_mask": 1,
    "mask_weared_incorrect": 2,
    "without": 0,
    "correct": 1,
    "uncorrect": 2,
    "Face: No Mask": 0,
    "Face: Mask": 1,
    "Face: Incorrect Mask": 2,
#    "No Mask": 0,
#    "Mask": 1,
}

if __name__ == '__main__':
    for file in ds.glob("*.xml"):
        ann = PascalVOC.from_xml(file)
        yolo = ann.to_yolo(label_map)
        out_name = f"{file.stem}.txt"
        with open(outfile +'/' + out_name, "w") as f:
            f.write(yolo)
