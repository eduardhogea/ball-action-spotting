from src.frame_fetchers.abstract import AbstractFrameFetcher
from src.frame_fetchers.opencv import OpencvFrameFetcher

try:
    from src.frame_fetchers.nvdec import NvDecFrameFetcher
except Exception:
    NvDecFrameFetcher = None
