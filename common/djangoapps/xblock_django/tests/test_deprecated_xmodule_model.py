"""
Tests for deprecated xblocks in XBlockDisableConfig.
"""

from mock import patch
from django.test import TestCase
from xblock_django.models import XBlockDisableConfig


class XBlockDisableConfigTestCase(TestCase):
    """
    Tests for the DjangoXBlockUserService.
    """
    def setUp(self):
        super(XBlockDisableConfigTestCase, self).setUp()

        # Initialize the deprecated modules settings with empty list
        XBlockDisableConfig.objects.create(
            disabled_blocks='', enabled=True
        )

    @patch('django.conf.settings.DEPRECATED_ADVANCED_COMPONENT_TYPES', ['poll', 'survey'])
    def test_deprecated_blocks_file(self):
        """
        Tests that deprecated modules contain entries from settings file DEPRECATED_ADVANCED_COMPONENT_TYPES
        """
        self.assertEqual(XBlockDisableConfig.deprecated_block_types(), ['poll', 'survey'])

    @patch('django.conf.settings.DEPRECATED_ADVANCED_COMPONENT_TYPES', ['poll', 'survey'])
    def test_deprecated_blocks_file_and_config(self):
        """
        Tests for the merger of deprecated blocks defined both i settings and admin conf
        """
        XBlockDisableConfig.objects.create(
            deprecated_blocks='annotatable', enabled=True
        )

        self.assertEqual(XBlockDisableConfig.deprecated_block_types(), ['annotatable', 'poll', 'survey'])
