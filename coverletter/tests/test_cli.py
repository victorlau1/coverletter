from unittest import TestCase
from unittest.mock import patch
from coverletter.cli import Cli

class TestCli(TestCase):

  #Test that do_prompt command works
  def test_prompt(self):
    cli = Cli()
    with patch('coverletter.cli.Cli.do_prompt', side_effect='/fake/path'):
      result = cli.do_prompt()
    self.assertIsNotNone(result)
  