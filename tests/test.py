import os
import unittest
import tkinter as tk
import cv2 as cv
from app.main import global_thresholding, adaptive_mean_thresholding, otsu_binarization
from gui.main import GUI
os.chdir("..")   # go up one directory from working directory


class MyTest(unittest.TestCase):

    def test_thresh(self):
        im_path1 = 'images\image1.jpg'
        self.assertEqual(global_thresholding(im_path1)[0][0], 255)
        self.assertEqual(adaptive_mean_thresholding(im_path1, 7)[0][0], 255)

        im_path2 = 'images\image2.jpg'
        self.assertEqual(global_thresholding(im_path2)[-1][-1], 255)
        self.assertEqual(adaptive_mean_thresholding(im_path2, 7)[-1][-1], 255)

    def test_gui(self):
        window = tk.Tk()
        gui = GUI(window, 7)
        self.assertEqual(gui.block_size, 7)
        self.assertIsNone(gui.image_path)
        self.assertEqual(window.title(), 'Image-Scanner')

    def test_otsu_binarization(self):
        im_path1 = 'images\image1.jpg'
        self.assertEqual(otsu_binarization.binarization(im_path1), 155)

        im_path2 = 'images\image4.png'
        self.assertEqual(otsu_binarization.binarization(im_path2), 117)


