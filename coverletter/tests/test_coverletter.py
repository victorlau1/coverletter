from unittest import TestCase
from unittest.mock import patch
from coverletter.coverletter import CoverLetterParser
from docx import Document
import os

class TestCoverLetter(TestCase):

  def setUp(self):
    self.coverletter = CoverLetterParser()
    self.fakeText = 'Phasellus ipsum ipsum, [efficitur] vitae ligula non'
    document = Document()
    self.fakeDocument = document

  #Test insert overwrite
  def test_insert_overwrite(self):
    assert True

  #Test placeholder returns right plaec
  def test_get_placeholder(self):
    result = self.coverletter.get_placeholder(self.fakeText, 24, ']')
    self.assertEqual(result, 'efficitur')
  
  #Tests Save Document Given Inputs
  def test_save_document(self):
    test_fileName = 'test_savedata.docx'
    file_path = os.path.dirname(__file__) + '/data/'
    testfile_savepath = os.path.abspath(os.path.join(file_path, test_fileName))
    print(testfile_savepath)
    if os.path.exists(testfile_savepath):
      os.remove(testfile_savepath)

    user_input = [
      file_path,
      test_fileName
    ]

    with patch('builtins.input', side_effect=user_input):
      result = self.coverletter.save_document(self.fakeDocument)  
    self.assertTrue(os.path.exists(testfile_savepath))

  #Test separator will take options

  #Test separator will accept custom separator

  #Test separator will error out 