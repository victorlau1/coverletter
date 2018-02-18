from unittest import TestCase
from unittest.mock import patch
from docx import Document
from coverletter.description import JobDescriptionParser
import os

class TestDescriptionParser(TestCase):

    #Read testfile within data
    def setUp(self):
      filepath = os.path.dirname(__file__) + '/data/'
      self.testfilepath = os.path.abspath(os.path.join(filepath, 'jobDescription.docx'))  
      self.test_inst = JobDescriptionParser

      with open(self.testfilepath, 'rb') as file_template:
        self.document = Document(file_template)

    #Test that it parses the job description document
    def test_parse_document(self):
      filepath = self.testfilepath
      description_parser = self.test_inst
      description_parser.parse_document(description_parser, filepath)
      self.assertIsNotNone(self.test_inst.document)
    
    #Returns output of top words associated with job
    def test_top_nouns(self):
      description_parser = self.test_inst
      test_document = self.document
      output = description_parser.top_nouns(description_parser, self.document)
      self.assertEqual('experience', output[0])
      self.assertEqual('sql', output[1])

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

    #Get aggregate counts of top words