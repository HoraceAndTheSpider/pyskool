# -*- coding: utf-8 -*-
# Copyright 2008, 2010 Richard Dymond (rjdymond@gmail.com)
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
# Joypad control... attempt 2!
# 
"""
Collect input from the keyboard.
"""

import pygame
from . import keys
from . import buttons

# controller 'structure'
# value of 0 - not pressed, 1 - pressed (keydown) , 2 - held
class controller_as_keyboard:
  def __init__(self):
            self.LEFT               = 0
            self.RIGHT              = 0           
            self.UP                 = 0
            self.DOWN               = 0
            self.SIT_STAND          = 0
            self.OPEN_DESK          = 0
            self.FIRE_CATAPULT      = 0            
            self.FIRE_WATER_PISTOL  = 0
            self.DROP_STINKBOMB     = 0
            self.HIT                = 0
            self.JUMP               = 0
            self.AUTOWRITE          = 0
            self.WRITE              = 0
            self.CATCH              = 0
            self.UNDERSTOOD         = 0
            self.MOUNT_BIKE         = 0            
            self.DUMP_WATER_PISTOL  = 0
            self.RELEASE_MICE       = 0
            self.KISS               = 0
            self.MENU_EXEC          = 0
            self.MENU               = 0
            self.PAUSE              = 0
            
class Keyboard:
    """Collects input from the keyboard."""
    def __init__(self):

        self.writing = False

        global control_object
        control_object = controller_as_keyboard()
        control_array = []
        self.setup_joystick()
        self.pump()
     
    def pump(self):
        """Process the input event queue."""
        self.key_down_events = []
        self.quit = False
        
        if not hasattr(self, 'moved_joystick'):
            self.setup_joystick()
        
        # get our fake key presses
        if self.moved_joystick != None:
            self.joy_action = self.get_joystick(control_object)
            self.convert_joystick()
            
            for fake_key in joystick_buttons:
                    myevent = pygame.event.Event(pygame.KEYDOWN, key=fake_key)                   
                    self.key_down_events.append(myevent)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                self.key_down_events.append(event)
                         
        # It's important to collect pressed_keys AFTER clearing the event queue,
        # otherwise keys may appear to "stick"
        self.pressed_keys = list(pygame.key.get_pressed())
        
    def got_quit(self):
        """Return whether the window close button was clicked."""
        return self.quit

    def start_writing(self):
        """Prepare the keyboard for Eric writing on a blackboard, during which
        time keypresses are echoed on the blackboard instead of making Eric
        move.
        """
        self.writing = True

    def finish_writing(self):
        """Return the keyboard to normal operation after Eric has finished
        writing on a blackboard.
        """
        self.writing = False

    def is_pressed(self, keys):
        """Return whether any one of a set of keys is being pressed, or
        `False` if Eric is writing on a blackboard at the moment.

        :param keys: A list of keys to check.
        """
        pressed = False
        if not self.writing:
            for key in keys:
                if self.pressed_keys[key]:
                    self.pressed_keys[key] = 0
                    pressed = True
        return pressed

    def was_pressed(self, keys, force_check=False):
        """Return whether any one of a set of keys was pressed since the last
        keyboard check.

        :param keys: A list of keys to check.
        :param force_check: If `True`, check keys even if Eric is writing on a
                            blackboard.
        """
        pressed = False
        if not self.writing or force_check:
            for event in self.key_down_events:
                if event.key in keys:
                    self.key_down_events.remove(event)
                    pressed = True
        return pressed

    def pressed(self, keys):
        """Return whether any one of a set of keys either is being pressed or
        was pressed since the last keyboard check.

        :param keys: A list of keys to check.
        """
        return self.was_pressed(keys) or self.is_pressed(keys)

    def get_joystick(self, control_object):
 #       if control_object.LEFT == 1:
 #            control_object.LEFT = 2
#        if control_object.RIGHT == 1:
#            control_object.RIGHT = 2
#        if control_object.UP == 1:
#            control_object.UP = 2
#        if control_object.DOWN == 1:
 #           control_object.DOWN = 2    
        if control_object.SIT_STAND == 1:
            control_object.SIT_STAND = 2
        if control_object.OPEN_DESK == 1:
            control_object.OPEN_DESK = 2
        if control_object.FIRE_CATAPULT == 1:
            control_object.FIRE_CATAPULT = 2
        if control_object.FIRE_WATER_PISTOL == 1:
            control_object.FIRE_WATER_PISTOL = 2
        if control_object.DROP_STINKBOMB == 1:
            control_object.DROP_STINKBOMB = 2
        if control_object.HIT == 1:
            control_object.HIT = 2
        if control_object.JUMP == 1:
            control_object.JUMP = 2
        if control_object.AUTOWRITE == 1:
            control_object.AUTOWRITE = 2
        if control_object.WRITE == 1:
            control_object.WRITE = 2
        if control_object.CATCH == 1:
            control_object.CATCH = 2           
        if control_object.UNDERSTOOD == 1:
            control_object.UNDERSTOOD = 2
        if control_object.MOUNT_BIKE == 1:
            control_object.MOUNT_BIKE = 2
        if control_object.DUMP_WATER_PISTOL == 1:
            control_object.DUMP_WATER_PISTOL = 2
        if control_object.RELEASE_MICE == 1:
            control_object.RELEASE_MICE = 2
        if control_object.KISS == 1:
            control_object.KISS = 2 
        if control_object.MENU_EXEC == 1:
            control_object.MENU_EXEC = 2
        if control_object.MENU == 1:
            control_object.MENU = 2
        if control_object.PAUSE == 1:
            control_object.PAUSE = 2

        
        # LEFT (AXIS/HATS)
        this_axis = self.moved_joystick.get_axis(buttons.X_AXIS)
        this_hat = self.moved_joystick.get_hat(buttons.N_HAT)
        if this_axis < -0.2 or this_hat[0]<-0.5:
            control_object.LEFT = 1
        else:
            control_object.LEFT = 0

        # RIGHT (AXIS/HATS)         
        if this_axis > 0.2 or this_hat[0]>0.5:
            control_object.RIGHT = 1
        else:
            control_object.RIGHT = 0

        # UP (AXIS/HATS)
        this_axis = self.moved_joystick.get_axis(buttons.Y_AXIS)
        this_hat = self.moved_joystick.get_hat(buttons.N_HAT)
        
        if this_axis < -0.2 or this_hat[1]>0.5:
            control_object.UP = 1
        else:
            control_object.UP = 0

        # DOWN (AXIS/HATS)         
        if this_axis > 0.2 or this_hat[1]<-0.5:
            control_object.DOWN = 1
        else:
            control_object.DOWN = 0

        # DOWN (BIKE)
        if (this_axis > 0.2 or this_hat[1]<-0.5) and control_object.MOUNT_BIKE ==0:
            control_object.MOUNT_BIKE = 1
        else:
            control_object.MOUNT_BIKE = 0


        # 'Plain' Buttons (no L/R Shoulder modifier)
        if (self.moved_joystick.get_button(buttons.LEFT_SHOULDER) == False and self.moved_joystick.get_button(buttons.RIGHT_SHOULDER) == False):

            control_object.HIT = self.check_button(buttons.WEST_BUTTON,control_object.HIT)        
            # 'Fire' is used for multiple items                 
            control_object.FIRE_CATAPULT = self.check_button(buttons.SOUTH_BUTTON,control_object.FIRE_CATAPULT)
            control_object.UNDERSTOOD = self.check_button(buttons.SOUTH_BUTTON,control_object.UNDERSTOOD)
            control_object.MENU_EXEC = self.check_button(buttons.SOUTH_BUTTON,control_object.MENU_EXEC)
            control_object.SIT_STAND = self.check_button(buttons.EAST_BUTTON,control_object.SIT_STAND)
            control_object.JUMP = self.check_button(buttons.NORTH_BUTTON,control_object.JUMP)
            control_object.MENU = self.check_button(buttons.SELECT_BUTTON,control_object.MENU) 
            control_object.PAUSE = self.check_button(buttons.START_BUTTON,control_object.PAUSE)
            
        # LEFT Shoulder held down 
        elif (self.moved_joystick.get_button(buttons.LEFT_SHOULDER) == True and self.moved_joystick.get_button(buttons.RIGHT_SHOULDER) == False):                           
            control_object.FIRE_WATER_PISTOL = self.check_button(buttons.WEST_BUTTON,control_object.FIRE_WATER_PISTOL)
            control_object.KISS = self.check_button(buttons.SOUTH_BUTTON,control_object.KISS)
            control_object.WRITE = self.check_button(buttons.EAST_BUTTON,control_object.WRITE)
            control_object.CATCH = self.check_button(buttons.NORTH_BUTTON,control_object.CATCH)
            
        # RIGHT Shoulder held down
        elif (self.moved_joystick.get_button(buttons.LEFT_SHOULDER) == False and self.moved_joystick.get_button(buttons.RIGHT_SHOULDER) == True): 
            control_object.DUMP_WATER_PISTOL = self.check_button(buttons.WEST_BUTTON,control_object.DUMP_WATER_PISTOL)
            control_object.AUTOWRITE = self.check_button(buttons.SOUTH_BUTTON,control_object.AUTOWRITE)
            control_object.DROP_STINKBOMB = self.check_button(buttons.EAST_BUTTON,control_object.DROP_STINKBOMB)
            control_object.RELEASE_MICE = self.check_button(buttons.NORTH_BUTTON,control_object.RELEASE_MICE)
        
        return (control_object)


    def check_button(self, in_button, control_variable):
        """Return whether any one of a set of joystick buttons was pressed since the last
         check, but only if previously released.

        :param in_button: the joystick button number
        :param control_variable: button press variable (0 == released, 1 == pressed, 2 == held)
        """
        if (self.moved_joystick.get_button(in_button) == True) and control_variable == 0:
                 return(1)
        elif self.moved_joystick.get_button(in_button) == False:
                 return(0)

        return(control_variable)


    def convert_joystick(self):
        global joystick_buttons
        joystick_buttons = []

        if self.writing == True:
          if self.joy_action.AUTOWRITE == 1:
              joystick_buttons.append(keys.ENTER[0])
          if self.joy_action.WRITE == 1:
              joystick_buttons.append(keys.ENTER[0])

        else:          
          if self.joy_action.LEFT == 1:
              joystick_buttons.append(keys.LEFT[1])
          if self.joy_action.RIGHT == 1:
              joystick_buttons.append(keys.RIGHT[0])
          if self.joy_action.UP == 1:
              joystick_buttons.append(keys.UP[0])
          if self.joy_action.DOWN == 1:
              joystick_buttons.append(keys.DOWN[0])            
          if self.joy_action.SIT_STAND == 1:
              joystick_buttons.append(keys.SIT_STAND[0])
          if self.joy_action.OPEN_DESK == 1:
              joystick_buttons.append(pygame.K_i)
          if self.joy_action.FIRE_CATAPULT == 1:
              joystick_buttons.append(keys.FIRE_CATAPULT[0])
          if self.joy_action.FIRE_WATER_PISTOL == 1:
              joystick_buttons.append(keys.FIRE_WATER_PISTOL[0])
          if self.joy_action.DROP_STINKBOMB == 1:
              joystick_buttons.append(keys.DROP_STINKBOMB[0])
          if self.joy_action.HIT == 1:
              joystick_buttons.append(keys.HIT[0])
          if self.joy_action.JUMP == 1:
              joystick_buttons.append(keys.JUMP[0])
          if self.joy_action.WRITE == 1:
             joystick_buttons.append(keys.WRITE[0])
          if self.joy_action.AUTOWRITE == 1:
             joystick_buttons.append(keys.AUTOWRITE[0])
          if self.joy_action.CATCH == 1:
              joystick_buttons.append(keys.CATCH[0])
          if self.joy_action.UNDERSTOOD == 1:
              joystick_buttons.append(keys.UNDERSTOOD[0])
          if self.joy_action.MOUNT_BIKE == 1:
              joystick_buttons.append(keys.MOUNT_BIKE[0])
          if self.joy_action.DUMP_WATER_PISTOL == 1:
              joystick_buttons.append(keys.DUMP_WATER_PISTOL[0])
          if self.joy_action.RELEASE_MICE == 1:
              joystick_buttons.append(keys.RELEASE_MICE[0])
          if self.joy_action.KISS == 1:
              joystick_buttons.append(keys.KISS[0])
          if self.joy_action.MENU_EXEC == 1:
              joystick_buttons.append(keys.MENU_EXEC[0])  
          if self.joy_action.MENU == 1:
              joystick_buttons.append(keys.MENU[0])
          if self.joy_action.PAUSE == 1:
              joystick_buttons.append(keys.PAUSE[0])

            
        return(joystick_buttons)
    
    def setup_joystick(self):
        if pygame.joystick.get_count() >= buttons.JOYSTICK_NUMBER + 1:
            if not hasattr(self, 'moved_joystick'):
                self.moved_joystick = pygame.joystick.Joystick(buttons.JOYSTICK_NUMBER)
                self.moved_joystick.init()
                
                self.joy_action = self.get_joystick(control_object)
                self.convert_joystick()
            elif hasattr(self, 'moved_joystick') and self.moved_joystick == None:
                self.moved_joystick = pygame.joystick.Joystick(buttons.JOYSTICK_NUMBER)
                self.moved_joystick.init()
                
                self.joy_action = self.get_joystick(control_object)
                self.convert_joystick()
                
            else:
                self.moved_joystick = None
        else:
            self.moved_joystick = None
        return
