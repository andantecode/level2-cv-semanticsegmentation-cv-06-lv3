from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()
class XRayCropDataset(BaseSegDataset):
    METAINFO = dict(
        classes=('finger-1', 'finger-2', 'finger-3', 'finger-4', 'finger-5',
                'finger-6', 'finger-7', 'finger-8', 'finger-9', 'finger-10',
                'finger-11', 'finger-12', 'finger-13', 'finger-14', 'finger-15',
                'finger-16', 'finger-17', 'finger-18', 'finger-19', 'Trapezium',
                'Trapezoid', 'Capitate', 'Hamate', 'Scaphoid', 'Lunate',
                'Triquetrum', 'Pisiform', 'Radius', 'Ulna',),
        palette=[
            (220, 20, 60), (119, 11, 32), (0, 0, 142), (0, 0, 230), (106, 0, 228),
            (0, 60, 100), (0, 80, 100), (0, 0, 70), (0, 0, 192), (250, 170, 30),
            (100, 170, 30), (220, 220, 0), (175, 116, 175), (250, 0, 30), (165, 42, 42),
            (255, 77, 255), (0, 226, 252), (182, 182, 255), (0, 82, 0), (120, 166, 157),
            (110, 76, 0), (174, 57, 255), (199, 100, 0), (72, 0, 118), (255, 179, 240),
            (0, 125, 92), (209, 0, 151), (188, 208, 182), (0, 220, 176),])
    def __init__(self,
                 img_suffix='.png',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
