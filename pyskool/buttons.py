# -*- coding: utf-8 -*-
# Copyright 2010, 2012 Richard Dymond (rjdymond@gmail.com)
#
# This file is part of Pyskool.
#
# Pyskool is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Pyskool is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Pyskool. If not, see <http://www.gnu.org/licenses/>.
#
# This part is specific to the controller implementation for RPI
#

"""
The controller buttons to be mapped
"""

#//////////////////////////////////////////////////////////////////////////////
#  These are the joystick buttons to be used - to be changed via .ini file
#//////////////////////////////////////////////////////////////////////////////

JOYSTICK_NUMBER = 0

X_AXIS = 0
Y_AXIS = 1
N_HAT = 0
DPAD_UP = -1
DPAD_DOWN = -1
DPAD_LEFT = -1
DPAD_RIGHT = -1

WEST_BUTTON = 0
SOUTH_BUTTON = 1
EAST_BUTTON = 2
NORTH_BUTTON = 3

LEFT_SHOULDER = 4
RIGHT_SHOULDER = 5
SELECT_BUTTON = 8
START_BUTTON = 9

#//////////////////////////////////////////////////////////////////////////////
#  These are the equates needed for the control_object
#//////////////////////////////////////////////////////////////////////////////
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
FIRE_CATAPULT = 5
