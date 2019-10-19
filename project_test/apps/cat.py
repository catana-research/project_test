# -*- coding: utf-8 -*-
"""Cat emulation module.

This module emulates the behaviours and actions of a cat.
"""


class Cat(object):
    """A :class:`Cat` is the classiest of classes.

    """

    def __init__(self):
        self.purr_sound = 'PURRRRR'
        pass

    def meow(self, volume, duration, style=None):
        """Perform a meow action.

        Args:
            volume (int): Volume of the meow in decibels, changes behaviour if the ``volume`` is above 50 dB.
            duration (float): Duration of the meow in seconds.
            style (Optional[str]): Style of the meow, defaults to `cute`.

        A cat must meow regularly to remain healthy. It also helps to get the attention of the owner so it can get pet.

        .. math::

            n_{\mathrm{happiness}} = \sum_{k=0}^{N-1} hug_k meow_k

        Note:
            :class:`Cat` needs to meow regularly.
        """  # noqa: W605
        meow_str = 'Me' + duration*'o' + 'w'
        if volume > 50:
            meow_str = meow_str.upper()
        if style == 'cute':
            meow_str += ' ^_^'

        return meow_str

    def purr(self):
        """Purr like a cat"""
        return self.purr_sound
