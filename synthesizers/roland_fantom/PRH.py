﻿####################################################################################################
# Copyright 2013 John Crawford
#
# This file is part of SynthServer.
#
# SynthServer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SynthServer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SynthServer.  If not, see <http://www.gnu.org/licenses/>.
####################################################################################################

## @file
#  Module Information.
#  @date 3/10/2013 Created file.  -jc
#  @author John Crawford

from synthesizers.MIDIDevice import MIDIVoice



NAME = 'PR-H'

PATCHES = [
  MIDIVoice('Minor Thirds', 87, 71, 0, 'PULSATING', 'PR-H 001'),
  MIDIVoice('Strobe X', 87, 71, 1, 'PULSATING', 'PR-H 002'),
  MIDIVoice('Orbiting', 87, 71, 2, 'PULSATING', 'PR-H 003'),
  MIDIVoice('FX World', 87, 71, 3, 'PULSATING', 'PR-H 004'),
  MIDIVoice('Mr. Fourier', 87, 71, 4, 'PULSATING', 'PR-H 005'),
  MIDIVoice('Nu Trance X', 87, 71, 5, 'PULSATING', 'PR-H 006'),
  MIDIVoice('eXisDance', 87, 71, 6, 'PULSATING', 'PR-H 007'),
  MIDIVoice('Are U ready?', 87, 71, 7, 'PULSATING', 'PR-H 008'),
  MIDIVoice('Minty Fresh', 87, 71, 8, 'PULSATING', 'PR-H 009'),
  MIDIVoice('Spectrums', 87, 71, 9, 'PULSATING', 'PR-H 010'),
  MIDIVoice('Shape of X', 87, 71, 10, 'PULSATING', 'PR-H 011'),
  MIDIVoice('Auto 5thSaws', 87, 71, 11, 'PULSATING', 'PR-H 012'),
  MIDIVoice('Strobot', 87, 71, 12, 'PULSATING', 'PR-H 013'),
  MIDIVoice('Dreamswirl', 87, 71, 13, 'PULSATING', 'PR-H 014'),
  MIDIVoice('Galaxadin', 87, 71, 14, 'PULSATING', 'PR-H 015'),
  MIDIVoice('Welcome2X', 87, 71, 15, 'PULSATING', 'PR-H 016'),
  MIDIVoice('Space & Time', 87, 71, 16, 'PULSATING', 'PR-H 017'),
  MIDIVoice('Cross Talk', 87, 71, 17, 'PULSATING', 'PR-H 018'),
  MIDIVoice('Lava Flows', 87, 71, 18, 'PULSATING', 'PR-H 019'),
  MIDIVoice('Steppin Faze', 87, 71, 19, 'PULSATING', 'PR-H 020'),
  MIDIVoice('Reanimation', 87, 71, 20, 'PULSATING', 'PR-H 021'),
  MIDIVoice('VoX Chopper', 87, 71, 21, 'PULSATING', 'PR-H 022'),
  MIDIVoice('SquareSphere', 87, 71, 22, 'PULSATING', 'PR-H 023'),
  MIDIVoice('Auto Sync', 87, 71, 23, 'PULSATING', 'PR-H 024'),
  MIDIVoice('Vocastic', 87, 71, 24, 'PULSATING', 'PR-H 025'),
  MIDIVoice('Bending Logo', 87, 71, 25, 'SYNTH FX', 'PR-H 026'),
  MIDIVoice('SolarPleXus', 87, 71, 26, 'SYNTH FX', 'PR-H 027'),
  MIDIVoice('Scare', 87, 71, 27, 'SYNTH FX', 'PR-H 028'),
  MIDIVoice('Chaoism', 87, 71, 28, 'SYNTH FX', 'PR-H 029'),
  MIDIVoice('Hillside', 87, 71, 29, 'SYNTH FX', 'PR-H 030'),
  MIDIVoice('Alien Voice', 87, 71, 30, 'SYNTH FX', 'PR-H 031'),
  MIDIVoice('What What?', 87, 71, 31, 'SYNTH FX', 'PR-H 032'),
  MIDIVoice('Beyond Here', 87, 71, 32, 'SYNTH FX', 'PR-H 033'),
  MIDIVoice('Mod Scanner', 87, 71, 33, 'SYNTH FX', 'PR-H 034'),
  MIDIVoice('Gasp', 87, 71, 34, 'SYNTH FX', 'PR-H 035'),
  MIDIVoice('Neverville', 87, 71, 35, 'SYNTH FX', 'PR-H 036'),
  MIDIVoice('Landing Pad', 87, 71, 36, 'SYNTH FX', 'PR-H 037'),
  MIDIVoice('Celebrated', 87, 71, 37, 'SYNTH FX', 'PR-H 038'),
  MIDIVoice('ResoSweep Up', 87, 71, 38, 'SYNTH FX', 'PR-H 039'),
  MIDIVoice('The VorteX', 87, 71, 39, 'SYNTH FX', 'PR-H 040'),
  MIDIVoice('Magic Wave', 87, 71, 40, 'SYNTH FX', 'PR-H 041'),
  MIDIVoice('Shangri-La', 87, 71, 41, 'SYNTH FX', 'PR-H 042'),
  MIDIVoice('CerealKiller', 87, 71, 42, 'SYNTH FX', 'PR-H 043'),
  MIDIVoice('DigimaX', 87, 71, 43, 'OTHER SYNTH', 'PR-H 044'),
  MIDIVoice('Trancy X', 87, 71, 44, 'OTHER SYNTH', 'PR-H 045'),
  MIDIVoice('X Sweep Saws', 87, 71, 45, 'OTHER SYNTH', 'PR-H 046'),
  MIDIVoice('X-Trance', 87, 71, 46, 'OTHER SYNTH', 'PR-H 047'),
  MIDIVoice('JP-8000 Saws', 87, 71, 47, 'OTHER SYNTH', 'PR-H 048'),
  MIDIVoice('X Super Saws', 87, 71, 48, 'OTHER SYNTH', 'PR-H 049'),
  MIDIVoice('Exhale', 87, 71, 49, 'OTHER SYNTH', 'PR-H 050'),
  MIDIVoice('SBF Voices', 87, 71, 50, 'OTHER SYNTH', 'PR-H 051'),
  MIDIVoice('Stadium SBF', 87, 71, 51, 'OTHER SYNTH', 'PR-H 052'),
  MIDIVoice('Master X', 87, 71, 52, 'OTHER SYNTH', 'PR-H 053'),
  MIDIVoice('X-panda', 87, 71, 53, 'OTHER SYNTH', 'PR-H 054'),
  MIDIVoice('TDreamTouch', 87, 71, 54, 'OTHER SYNTH', 'PR-H 055'),
  MIDIVoice('Smooth Synth', 87, 71, 55, 'OTHER SYNTH', 'PR-H 056'),
  MIDIVoice('Stereotype', 87, 71, 56, 'OTHER SYNTH', 'PR-H 057'),
  MIDIVoice('Saw Keystep', 87, 71, 57, 'OTHER SYNTH', 'PR-H 058'),
  MIDIVoice('4mant Cycle', 87, 71, 58, 'OTHER SYNTH', 'PR-H 059'),
  MIDIVoice('Trance Sweep', 87, 71, 59, 'OTHER SYNTH', 'PR-H 060'),
  MIDIVoice('Modular', 87, 71, 60, 'OTHER SYNTH', 'PR-H 061'),
  MIDIVoice('Triple X', 87, 71, 61, 'OTHER SYNTH', 'PR-H 062'),
  MIDIVoice('Angel Pipes', 87, 71, 62, 'OTHER SYNTH', 'PR-H 063'),
  MIDIVoice('Vint Clavier', 87, 71, 63, 'OTHER SYNTH', 'PR-H 064'),
  MIDIVoice('Wired Synth', 87, 71, 64, 'OTHER SYNTH', 'PR-H 065'),
  MIDIVoice('Nu Romance', 87, 71, 65, 'OTHER SYNTH', 'PR-H 066'),
  MIDIVoice('Survivoz', 87, 71, 66, 'BRIGHT PAD', 'PR-H 067'),
  MIDIVoice('Ring Worldz', 87, 71, 67, 'BRIGHT PAD', 'PR-H 068'),
  MIDIVoice('Mashed!? :0)', 87, 71, 68, 'BRIGHT PAD', 'PR-H 069'),
  MIDIVoice('Saturn Siren', 87, 71, 69, 'BRIGHT PAD', 'PR-H 070'),
  MIDIVoice('Side Band X', 87, 71, 70, 'BRIGHT PAD', 'PR-H 071'),
  MIDIVoice('Mashy Scene', 87, 71, 71, 'BRIGHT PAD', 'PR-H 072'),
  MIDIVoice('Spr SideBand', 87, 71, 72, 'BRIGHT PAD', 'PR-H 073'),
  MIDIVoice('Digitvox', 87, 71, 73, 'BRIGHT PAD', 'PR-H 074'),
  MIDIVoice('Oral eXam', 87, 71, 74, 'BRIGHT PAD', 'PR-H 075'),
  MIDIVoice('Timeline', 87, 71, 75, 'BRIGHT PAD', 'PR-H 076'),
  MIDIVoice('Whisper Pad', 87, 71, 76, 'BRIGHT PAD', 'PR-H 077'),
  MIDIVoice('Orchipad', 87, 71, 77, 'BRIGHT PAD', 'PR-H 078'),
  MIDIVoice('Visionary', 87, 71, 78, 'BRIGHT PAD', 'PR-H 079'),
  MIDIVoice('Rave Stringy', 87, 71, 79, 'BRIGHT PAD', 'PR-H 080'),
  MIDIVoice('InfinitePhsr', 87, 71, 80, 'BRIGHT PAD', 'PR-H 081'),
  MIDIVoice('Jupiter 2004', 87, 71, 81, 'BRIGHT PAD', 'PR-H 082'),
  MIDIVoice('Light Phaser', 87, 71, 82, 'BRIGHT PAD', 'PR-H 083'),
  MIDIVoice('Life-on', 87, 71, 83, 'BRIGHT PAD', 'PR-H 084'),
  MIDIVoice('Polar Morn', 87, 71, 84, 'BRIGHT PAD', 'PR-H 085'),
  MIDIVoice('Saturn Rings', 87, 71, 85, 'BRIGHT PAD', 'PR-H 086'),
  MIDIVoice('Ooh La La', 87, 71, 86, 'BRIGHT PAD', 'PR-H 087'),
  MIDIVoice('Flying X', 87, 71, 87, 'BRIGHT PAD', 'PR-H 088'),
  MIDIVoice('Motion Pad', 87, 71, 88, 'SOFT PAD', 'PR-H 089'),
  MIDIVoice('Mash Pad', 87, 71, 89, 'BRIGHT PAD', 'PR-H 090'),
  MIDIVoice('Xtragalactic', 87, 71, 90, 'SOFT PAD', 'PR-H 091'),
  MIDIVoice('Morph Filter', 87, 71, 91, 'SOFT PAD', 'PR-H 092'),
  MIDIVoice('TrnsSweepPad', 87, 71, 92, 'SOFT PAD', 'PR-H 093'),
  MIDIVoice('Follow', 87, 71, 93, 'SOFT PAD', 'PR-H 094'),
  MIDIVoice('Jupiter-X', 87, 71, 94, 'SOFT PAD', 'PR-H 095'),
  MIDIVoice('Riven Pad', 87, 71, 95, 'SOFT PAD', 'PR-H 096'),
  MIDIVoice('Consolament', 87, 71, 96, 'SOFT PAD', 'PR-H 097'),
  MIDIVoice('Spacious Pad', 87, 71, 97, 'SOFT PAD', 'PR-H 098'),
  MIDIVoice('JD Pop Pad', 87, 71, 98, 'SOFT PAD', 'PR-H 099'),
  MIDIVoice('Silhouette', 87, 71, 99, 'SOFT PAD', 'PR-H 100'),
  MIDIVoice('JP-8 Phase', 87, 71, 100, 'SOFT PAD', 'PR-H 101'),
  MIDIVoice('Nu Epic Pad', 87, 71, 101, 'SOFT PAD', 'PR-H 102'),
  MIDIVoice('Forever', 87, 71, 102, 'SOFT PAD', 'PR-H 103'),
  MIDIVoice('Flange Dream', 87, 71, 103, 'SOFT PAD', 'PR-H 104'),
  MIDIVoice('Guild Vox', 87, 71, 104, 'SOFT PAD', 'PR-H 105'),
  MIDIVoice('5th Pad X', 87, 71, 105, 'SOFT PAD', 'PR-H 106'),
  MIDIVoice('Evolution X', 87, 71, 106, 'SOFT PAD', 'PR-H 107'),
  MIDIVoice('Chariots', 87, 71, 107, 'SOFT PAD', 'PR-H 108'),
  MIDIVoice('Trevor\'s Pad', 87, 71, 108, 'PULSATING', 'PR-H 109'),
  MIDIVoice('Nu Pad', 87, 71, 109, 'PULSATING', 'PR-H 110'),
  MIDIVoice('Fantomas Pad', 87, 71, 110, 'PULSATING', 'PR-H 111'),
  MIDIVoice('Film Cue', 87, 71, 111, 'VOX', 'PR-H 112'),
  MIDIVoice('Choral Sweep', 87, 71, 112, 'VOX', 'PR-H 113'),
  MIDIVoice('Paradise', 87, 71, 113, 'VOX', 'PR-H 114'),
  MIDIVoice('Sad ceremony', 87, 71, 114, 'VOX', 'PR-H 115'),
  MIDIVoice('Lost Voices', 87, 71, 115, 'VOX', 'PR-H 116'),
  MIDIVoice('Talk 2 Me', 87, 71, 116, 'VOX', 'PR-H 117'),
  MIDIVoice('Pearly Harp', 87, 71, 117, 'PLUCKED', 'PR-H 118'),
  MIDIVoice('Nylon Harp', 87, 71, 118, 'PLUCKED', 'PR-H 119'),
  MIDIVoice('Skydiver', 87, 71, 119, 'PLUCKED', 'PR-H 120'),
  MIDIVoice('Unpluck\'d', 87, 71, 120, 'PLUCKED', 'PR-H 121'),
  MIDIVoice('Ethno Plucks', 87, 71, 121, 'PLUCKED', 'PR-H 122'),
  MIDIVoice('SaraswatiRvr', 87, 71, 122, 'PLUCKED', 'PR-H 123'),
  MIDIVoice('Drone X', 87, 71, 123, 'PLUCKED', 'PR-H 124'),
  MIDIVoice('Lounge Kit', 87, 71, 124, 'COMBINATION', 'PR-H 125'),
  MIDIVoice('Gospel Trio', 87, 71, 125, 'COMBINATION', 'PR-H 126'),
  MIDIVoice('xcultural', 87, 71, 126, 'COMBINATION', 'PR-H 127'),
  MIDIVoice('When I\'m 64', 87, 71, 127, 'COMBINATION', 'PR-H 128'),
]
