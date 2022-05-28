from fastapi import UploadFile
from numpy import save
import torch
from IPython.display import Image, clear_output
from neuro.detect import run

async def create_my_photo(file:str):
    preds, ims = run(weights = 'neuro/wildview.pt',
                     source = f'app/routers/assets/{file}', 
                     project= 'app/routers',
                     name= 'assets',
                     imgsz=(2880,2880),
                     iou_thres = 0.33,
                     conf_thres=0.2, 
                     save_txt=True,
                     exist_ok=True,
                     hide_labels=True,
                     hide_conf=True,
                     line_thickness=1,
                     max_det= 2280,
                      )
    return len(preds[0])

