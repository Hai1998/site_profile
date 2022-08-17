from django.test import TestCase
import os
# Create your tests here.


def deleteimage():
    os.remove('./media/image/image_2022_05_06T03_47_35_674Z.png')

deleteimage()