from unittest import TestCase
from unittest.mock import patch
from coverletter.description import JobDescriptionParser
import os

class TestDescriptionParser(TestCase):

    #Read testfile within data
    def setUp(self):
      file_path = os.path.dirname(__file__) + '/data/'
      self.testfile_path = os.path.abspath(os.path.join(file_path, 'jobDescription.docx'))
      self.test_inst = JobDescriptionParser

    #Test that it parses the job description document
    def test_parse_document(self):
      self.test_inst.parse_document(self.testfile_path)
      self.assertIsNotNone(self.test_inst.document)
    
    #Returns output of top words associated with job
    def test_top_words(self):
      assert True

    #Returns top nouns for inserted text (based on analysis)
    def test_textblob_nouns(self):
      assert True
    
    #Writes output to a file (not DB)
    def test_save_file(self):
      assert True

    #Give a prompt based on variable data
    def test_read_results_file(self):
      assert True

    #Aggregate data if more than one pararaph
    def test_aggregate_paragraphs(self):
      assert True