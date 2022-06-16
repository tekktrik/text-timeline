# SPDX-FileCopyrightText: 2022 Alec Delaney
#
# SPDX-License-Identifier: MIT

"""
text_timeline
=============

Main entry for making timelines from formatted text files
"""

from typing import Optional
import os


class TextTimeline:
    """Main entry point for creating timelines from files"""

    def __init__(self, filename: str, *, name: Optional[str] = None, **kwargs) -> None:

        self._filename = filename
        self.nodes = []
        """The list of timeline nodes"""
        self.name = name if name else os.path.basename(os.path.splitext(filename))
        self._kwargs = kwargs

        self._parse_file(filename)

    @property
    def filename(self):
        """The filename of the text file"""
        return self._filename

    def _parse_file(self, filename: str):
        """Parses a file to create the timeline"""

    def generate_timeline(self, filename: str) -> None:
        """Generate a timeline from the data"""
