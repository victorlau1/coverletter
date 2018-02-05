from unittest import TestCase
from unittest.mock import patch
from coverletter.cli import Cli
import os

class TestCli(TestCase):

  #Test Prompt Exists
  def test_prompt_start(self):
    with patch('coverletter.cli.Cli.do_prompt', return_value='Y'):
      result = Cli().do_prompt()
      self.assertEqual(result, 'Y')

  #Integration Test 1
  def test_prompt(self):
    cli = Cli()
    file_path = os.path.dirname(__file__) + '/data/'
    testfile_path = os.path.abspath(os.path.join(file_path, 'testDoc.docx'))
    user_input = [
      testfile_path,
      1,
      'Whatever',
      'Whatever',
      'Y',
      file_path,
      'testDocOutput.docx'
    ]
    with patch('builtins.input', side_effect=user_input):
      result = cli.do_prompt()
    self.assertIsNone(result)
  