# SPDX-FileCopyrightText: 2022 Alec Delaney
#
# SPDX-License-Identifier: MIT

"""
text_timeline.node
==================

Node information

TODO: Update this
"""

from typing import Optional, Literal
from collections.abc import Sequence


class TimelineNode:
    """Base class for timeline nodes"""

    def __init__(
        self,
        pasts: Sequence["TimelineNode"],
        futures: Sequence["TimelineNode"],
        id: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:

        self._pasts = list(pasts)
        self._futures = list(futures)
        self._id = id
        self._description = description

    def __eq__(self, node: "TimelineNode") -> bool:

        if not isinstance(node, TimelineNode):
            raise TypeError("Can only compare two TimelineNodes")

        return self.id == node.id

    def __lt__(self, node: "TimelineNode") -> bool:

        if not isinstance(node, TimelineNode):
            raise TypeError("Can only compare two TimelineNodes")

        return self._is_relative_in_time(node, "_pasts")

    def __gt__(self, node: "TimelineNode") -> bool:

        if not isinstance(node, TimelineNode):
            raise TypeError("Can only compare two TimelineNodes")

        return self._is_relative_in_time(node, "_futures")

    @property
    def pasts(self) -> list["TimelineNode"]:
        return self._pasts

    @property
    def futures(self) -> list["TimelineNode"]:
        return self._futures

    @property
    def id(self) -> Optional[str]:
        return self._id

    @property
    def description(self) -> Optional[str]:
        return self._description

    def _append_checks(self, event: "TimelineNode") -> bool:

        if not isinstance(event, TimelineNode):
            raise TypeError("Only TimelineNodes can be added as pasts")

        if event == self:
            raise ValueError(f"Event {self.id} can not be a past of itself")

        return event in self._pasts

    def add_past(self, event: "TimelineNode") -> None:

        if self._append_checks(event):
            return

        if not self < event:
            self._pasts.append(event)
            event.add_future(self)

    def add_future(self, event: "TimelineNode") -> None:

        if self._append_checks(event):
            return

        if not self > event:
            self._futures.append(event)
            event.add_past(self)

    def _is_relative_in_time(
        self, node: "TimelineNode", events_name: Literal["_pasts", "_futures"]
    ) -> bool:

        events: list["TimelineNode"] = getattr(self, events_name)
        if node in events:
            return False
        if not all([event._is_relative_in_time(node, events_name) for event in events]):
            return False
        return True
