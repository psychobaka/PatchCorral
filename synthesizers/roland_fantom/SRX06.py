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



NAME = 'XP-E - SRX-06 - Complete Orchestra'

PATCHES = [
  MIDIVoice('WarmVlns SRX', 93, 7, 0, 'STRINGS', 'XP-E 001'),
  MIDIVoice('Legato Vlns', 93, 7, 1, 'STRINGS', 'XP-E 002'),
  MIDIVoice('NaturalVlnsS', 93, 7, 2, 'STRINGS', 'XP-E 003'),
  MIDIVoice('Agitato Vlns', 93, 7, 3, 'STRINGS', 'XP-E 004'),
  MIDIVoice('Vlns-Spc /', 93, 7, 4, 'STRINGS', 'XP-E 005'),
  MIDIVoice('Vl&Va Spicct', 93, 7, 5, 'STRINGS', 'XP-E 006'),
  MIDIVoice('Arco Vas SRX', 93, 7, 6, 'STRINGS', 'XP-E 007'),
  MIDIVoice('Agitato Vas', 93, 7, 7, 'STRINGS', 'XP-E 008'),
  MIDIVoice('Vlas-Spc /', 93, 7, 8, 'STRINGS', 'XP-E 009'),
  MIDIVoice('Marc Vas SRX', 93, 7, 9, 'STRINGS', 'XP-E 010'),
  MIDIVoice('Vc Sec mf', 93, 7, 10, 'STRINGS', 'XP-E 011'),
  MIDIVoice('Fast Cellos', 93, 7, 11, 'STRINGS', 'XP-E 012'),
  MIDIVoice('Vcs Legato', 93, 7, 12, 'STRINGS', 'XP-E 013'),
  MIDIVoice('3 Cellos', 93, 7, 13, 'STRINGS', 'XP-E 014'),
  MIDIVoice('Cellos', 93, 7, 14, 'STRINGS', 'XP-E 015'),
  MIDIVoice('CelloSectMrc', 93, 7, 15, 'STRINGS', 'XP-E 016'),
  MIDIVoice('Marcato Vcs', 93, 7, 16, 'STRINGS', 'XP-E 017'),
  MIDIVoice('Agitato Vcs', 93, 7, 17, 'STRINGS', 'XP-E 018'),
  MIDIVoice('Vcs+Cbs SRX', 93, 7, 18, 'STRINGS', 'XP-E 019'),
  MIDIVoice('Arco Vcs+Cbs', 93, 7, 19, 'STRINGS', 'XP-E 020'),
  MIDIVoice('Thick Basses', 93, 7, 20, 'STRINGS', 'XP-E 021'),
  MIDIVoice('Cb Sect SRX', 93, 7, 21, 'STRINGS', 'XP-E 022'),
  MIDIVoice('WideBasses S', 93, 7, 22, 'STRINGS', 'XP-E 023'),
  MIDIVoice('Agitato Cbs', 93, 7, 23, 'STRINGS', 'XP-E 024'),
  MIDIVoice('BIG StrgEns', 93, 7, 24, 'STRINGS', 'XP-E 025'),
  MIDIVoice('Big Strings2', 93, 7, 25, 'STRINGS', 'XP-E 026'),
  MIDIVoice('Orch p', 93, 7, 26, 'STRINGS', 'XP-E 027'),
  MIDIVoice('Orch p>f/Mod', 93, 7, 27, 'STRINGS', 'XP-E 028'),
  MIDIVoice('StrsArco SRX', 93, 7, 28, 'STRINGS', 'XP-E 029'),
  MIDIVoice('StrSwel/ModS', 93, 7, 29, 'STRINGS', 'XP-E 030'),
  MIDIVoice('StStrOrcp/fS', 93, 7, 30, 'STRINGS', 'XP-E 031'),
  MIDIVoice('SlowResinStr', 93, 7, 31, 'STRINGS', 'XP-E 032'),
  MIDIVoice('Adagio Strs', 93, 7, 32, 'STRINGS', 'XP-E 033'),
  MIDIVoice('LegatoStrngs', 93, 7, 33, 'STRINGS', 'XP-E 034'),
  MIDIVoice('Intim StrSec', 93, 7, 34, 'STRINGS', 'XP-E 035'),
  MIDIVoice('DramaStrsSRX', 93, 7, 35, 'STRINGS', 'XP-E 036'),
  MIDIVoice('St Str p/f', 93, 7, 36, 'STRINGS', 'XP-E 037'),
  MIDIVoice('SlowEpic Str', 93, 7, 37, 'STRINGS', 'XP-E 038'),
  MIDIVoice('Real Strings', 93, 7, 38, 'STRINGS', 'XP-E 039'),
  MIDIVoice('4Seasons SRX', 93, 7, 39, 'STRINGS', 'XP-E 040'),
  MIDIVoice('VlVaVcCb SRX', 93, 7, 40, 'STRINGS', 'XP-E 041'),
  MIDIVoice('StudioString', 93, 7, 41, 'STRINGS', 'XP-E 042'),
  MIDIVoice('Quartet SRX', 93, 7, 42, 'STRINGS', 'XP-E 043'),
  MIDIVoice('VibSwStrings', 93, 7, 43, 'STRINGS', 'XP-E 044'),
  MIDIVoice('Str Swell', 93, 7, 44, 'STRINGS', 'XP-E 045'),
  MIDIVoice('OuvertureSRX', 93, 7, 45, 'STRINGS', 'XP-E 046'),
  MIDIVoice('Cluster Sect', 93, 7, 46, 'STRINGS', 'XP-E 047'),
  MIDIVoice('Velo Str SRX', 93, 7, 47, 'STRINGS', 'XP-E 048'),
  MIDIVoice('Agitato to 0', 93, 7, 48, 'STRINGS', 'XP-E 049'),
  MIDIVoice('DynaMarc SRX', 93, 7, 49, 'STRINGS', 'XP-E 050'),
  MIDIVoice('VivaceStrSRX', 93, 7, 50, 'STRINGS', 'XP-E 051'),
  MIDIVoice('Agitato STR', 93, 7, 51, 'STRINGS', 'XP-E 052'),
  MIDIVoice('STR SpiccSRX', 93, 7, 52, 'STRINGS', 'XP-E 053'),
  MIDIVoice('StacctoSectn', 93, 7, 53, 'STRINGS', 'XP-E 054'),
  MIDIVoice('Spicc/releas', 93, 7, 54, 'STRINGS', 'XP-E 055'),
  MIDIVoice('STR Marcato', 93, 7, 55, 'STRINGS', 'XP-E 056'),
  MIDIVoice('Big Marcato!', 93, 7, 56, 'STRINGS', 'XP-E 057'),
  MIDIVoice('Spicc Sect', 93, 7, 57, 'STRINGS', 'XP-E 058'),
  MIDIVoice('Spc+Pz/rleas', 93, 7, 58, 'STRINGS', 'XP-E 059'),
  MIDIVoice('Piz-Spc /', 93, 7, 59, 'STRINGS', 'XP-E 060'),
  MIDIVoice('RoomPizz SRX', 93, 7, 60, 'STRINGS', 'XP-E 061'),
  MIDIVoice('Stage Pizz', 93, 7, 61, 'STRINGS', 'XP-E 062'),
  MIDIVoice('Nite Pizzico', 93, 7, 62, 'STRINGS', 'XP-E 063'),
  MIDIVoice('VIOLIN solo', 93, 7, 63, 'STRINGS', 'XP-E 064'),
  MIDIVoice('Solo Vln /', 93, 7, 64, 'STRINGS', 'XP-E 065'),
  MIDIVoice('Solo Violin', 93, 7, 65, 'STRINGS', 'XP-E 066'),
  MIDIVoice('Sad S.VlnSRX', 93, 7, 66, 'STRINGS', 'XP-E 067'),
  MIDIVoice('Solo Viola', 93, 7, 67, 'STRINGS', 'XP-E 068'),
  MIDIVoice('AgitatoVaSRX', 93, 7, 68, 'STRINGS', 'XP-E 069'),
  MIDIVoice('Solo Cello 1', 93, 7, 69, 'STRINGS', 'XP-E 070'),
  MIDIVoice('Solo Cello 2', 93, 7, 70, 'STRINGS', 'XP-E 071'),
  MIDIVoice('The V Cello', 93, 7, 71, 'STRINGS', 'XP-E 072'),
  MIDIVoice('Solo Vc /', 93, 7, 72, 'STRINGS', 'XP-E 073'),
  MIDIVoice('Marcato Vc', 93, 7, 73, 'STRINGS', 'XP-E 074'),
  MIDIVoice('Vln&Vcl', 93, 7, 74, 'STRINGS', 'XP-E 075'),
  MIDIVoice('Solo Cb /', 93, 7, 75, 'STRINGS', 'XP-E 076'),
  MIDIVoice('Tape Orc SRX', 93, 7, 76, 'STRINGS', 'XP-E 077'),
  MIDIVoice('Tape Str SRX', 93, 7, 77, 'STRINGS', 'XP-E 078'),
  MIDIVoice('Old Tale', 93, 7, 78, 'STRINGS', 'XP-E 079'),
  MIDIVoice('Mellow Tape', 93, 7, 79, 'STRINGS', 'XP-E 080'),
  MIDIVoice('Cystaline Pd', 93, 7, 80, 'STRINGS', 'XP-E 081'),
  MIDIVoice('SynStrings', 93, 7, 81, 'STRINGS', 'XP-E 082'),
  MIDIVoice('Full Orc SRX', 93, 7, 82, 'ORCHESTRA', 'XP-E 083'),
  MIDIVoice('St.OrcUniSRX', 93, 7, 83, 'ORCHESTRA', 'XP-E 084'),
  MIDIVoice('OrchUnif SRX', 93, 7, 84, 'ORCHESTRA', 'XP-E 085'),
  MIDIVoice('GRAND OrcSRX', 93, 7, 85, 'ORCHESTRA', 'XP-E 086'),
  MIDIVoice('WavinGoodbye', 93, 7, 86, 'ORCHESTRA', 'XP-E 087'),
  MIDIVoice('DynOrchestr1', 93, 7, 87, 'ORCHESTRA', 'XP-E 088'),
  MIDIVoice('Pathetique', 93, 7, 88, 'ORCHESTRA', 'XP-E 089'),
  MIDIVoice('Oboes & Sect', 93, 7, 89, 'ORCHESTRA', 'XP-E 090'),
  MIDIVoice('SlowEpicOrch', 93, 7, 90, 'ORCHESTRA', 'XP-E 091'),
  MIDIVoice('Grand Tutti', 93, 7, 91, 'ORCHESTRA', 'XP-E 092'),
  MIDIVoice('Ultimate Orc', 93, 7, 92, 'ORCHESTRA', 'XP-E 093'),
  MIDIVoice('SuspenceOrch', 93, 7, 93, 'ORCHESTRA', 'XP-E 094'),
  MIDIVoice('Tremolo /', 93, 7, 94, 'ORCHESTRA', 'XP-E 095'),
  MIDIVoice('TremOrc /Mod', 93, 7, 95, 'ORCHESTRA', 'XP-E 096'),
  MIDIVoice('ORC full+BD', 93, 7, 96, 'ORCHESTRA', 'XP-E 097'),
  MIDIVoice('Finally Orch', 93, 7, 97, 'ORCHESTRA', 'XP-E 098'),
  MIDIVoice('Orch & Choir', 93, 7, 98, 'ORCHESTRA', 'XP-E 099'),
  MIDIVoice('NowWeAreFree', 93, 7, 99, 'ORCHESTRA', 'XP-E 100'),
  MIDIVoice('Too Tense', 93, 7, 100, 'ORCHESTRA', 'XP-E 101'),
  MIDIVoice('OrchestrlSRX', 93, 7, 101, 'ORCHESTRA', 'XP-E 102'),
  MIDIVoice('DynOrchestr2', 93, 7, 102, 'ORCHESTRA', 'XP-E 103'),
  MIDIVoice('GiantOrchest', 93, 7, 103, 'ORCHESTRA', 'XP-E 104'),
  MIDIVoice('Strngs&Horns', 93, 7, 104, 'ORCHESTRA', 'XP-E 105'),
  MIDIVoice('Full Orch. 1', 93, 7, 105, 'ORCHESTRA', 'XP-E 106'),
  MIDIVoice('Full Orch. 2', 93, 7, 106, 'ORCHESTRA', 'XP-E 107'),
  MIDIVoice('Full Orch. 3', 93, 7, 107, 'ORCHESTRA', 'XP-E 108'),
  MIDIVoice('End Titles', 93, 7, 108, 'ORCHESTRA', 'XP-E 109'),
  MIDIVoice('HornStrs SRX', 93, 7, 109, 'ORCHESTRA', 'XP-E 110'),
  MIDIVoice('SRX Full Orc', 93, 7, 110, 'ORCHESTRA', 'XP-E 111'),
  MIDIVoice('Harp & Flute', 93, 7, 111, 'ORCHESTRA', 'XP-E 112'),
  MIDIVoice('Celesta&Flt', 93, 7, 112, 'ORCHESTRA', 'XP-E 113'),
  MIDIVoice('ProkofievSRX', 93, 7, 113, 'ORCHESTRA', 'XP-E 114'),
  MIDIVoice('MassInCeeSRX', 93, 7, 114, 'ORCHESTRA', 'XP-E 115'),
  MIDIVoice('PentatnicSRX', 93, 7, 115, 'ORCHESTRA', 'XP-E 116'),
  MIDIVoice('DawnSynphony', 93, 7, 116, 'ORCHESTRA', 'XP-E 117'),
  MIDIVoice('Bad Ending', 93, 7, 117, 'ORCHESTRA', 'XP-E 118'),
  MIDIVoice('Epic Ending', 93, 7, 118, 'ORCHESTRA', 'XP-E 119'),
  MIDIVoice('Catwalk', 93, 7, 119, 'HIT&STAB', 'XP-E 120'),
  MIDIVoice('OrchStaccato', 93, 7, 120, 'HIT&STAB', 'XP-E 121'),
  MIDIVoice('Staccato SRX', 93, 7, 121, 'HIT&STAB', 'XP-E 122'),
  MIDIVoice('OrchHitStack', 93, 7, 122, 'HIT&STAB', 'XP-E 123'),
  MIDIVoice('Dynam Hit', 93, 7, 123, 'HIT&STAB', 'XP-E 124'),
  MIDIVoice('MondoHit SRX', 93, 7, 124, 'HIT&STAB', 'XP-E 125'),
  MIDIVoice('OrchHit SRX', 93, 7, 125, 'HIT&STAB', 'XP-E 126'),
  MIDIVoice('OrcHitMajSRX', 93, 7, 126, 'HIT&STAB', 'XP-E 127'),
  MIDIVoice('OrcHitMinSRX', 93, 7, 127, 'HIT&STAB', 'XP-E 128'),
  MIDIVoice('OrcHitDimSRX', 93, 8, 0, 'HIT&STAB', 'XP-E 129'),
  MIDIVoice('Big Hit Maj1', 93, 8, 1, 'HIT&STAB', 'XP-E 130'),
  MIDIVoice('Big Hit Maj2', 93, 8, 2, 'HIT&STAB', 'XP-E 131'),
  MIDIVoice('Big Hit Min', 93, 8, 3, 'HIT&STAB', 'XP-E 132'),
  MIDIVoice('Big Hit Dim', 93, 8, 4, 'HIT&STAB', 'XP-E 133'),
  MIDIVoice('Sfz! Hit-Maj', 93, 8, 5, 'HIT&STAB', 'XP-E 134'),
  MIDIVoice('Sfz! Hit-Min', 93, 8, 6, 'HIT&STAB', 'XP-E 135'),
  MIDIVoice('Suspense', 93, 8, 7, 'HIT&STAB', 'XP-E 136'),
  MIDIVoice('Hit/Off-Maj', 93, 8, 8, 'HIT&STAB', 'XP-E 137'),
  MIDIVoice('Trem Hit-Maj', 93, 8, 9, 'HIT&STAB', 'XP-E 138'),
  MIDIVoice('Trem Hit-Min', 93, 8, 10, 'HIT&STAB', 'XP-E 139'),
  MIDIVoice('Trem Hit-Dim', 93, 8, 11, 'HIT&STAB', 'XP-E 140'),
  MIDIVoice('Orc/Prc 5-1^', 93, 8, 12, 'HIT&STAB', 'XP-E 141'),
  MIDIVoice('Drama Stab', 93, 8, 13, 'HIT&STAB', 'XP-E 142'),
  MIDIVoice('Maj Concern', 93, 8, 14, 'HIT&STAB', 'XP-E 143'),
  MIDIVoice('OrcGlsMajSRX', 93, 8, 15, 'HIT&STAB', 'XP-E 144'),
  MIDIVoice('OrcGlsMinSRX', 93, 8, 16, 'HIT&STAB', 'XP-E 145'),
  MIDIVoice('Harp Up Hit', 93, 8, 17, 'HIT&STAB', 'XP-E 146'),
  MIDIVoice('Harp Dn Hit', 93, 8, 18, 'HIT&STAB', 'XP-E 147'),
  MIDIVoice('BrassStabSRX', 93, 8, 19, 'HIT&STAB', 'XP-E 148'),
  MIDIVoice('Finale', 93, 8, 20, 'HIT&STAB', 'XP-E 149'),
  MIDIVoice('Tuned HIT', 93, 8, 21, 'HIT&STAB', 'XP-E 150'),
  MIDIVoice('YourMissionS', 93, 8, 22, 'HIT&STAB', 'XP-E 151'),
  MIDIVoice('Big Hit SRX', 93, 8, 23, 'HIT&STAB', 'XP-E 152'),
  MIDIVoice('HorrorHitSRX', 93, 8, 24, 'HIT&STAB', 'XP-E 153'),
  MIDIVoice('Perc Hit', 93, 8, 25, 'HIT&STAB', 'XP-E 154'),
  MIDIVoice('BrassFallSRX', 93, 8, 26, 'HIT&STAB', 'XP-E 155'),
  MIDIVoice('Tp Fall', 93, 8, 27, 'HIT&STAB', 'XP-E 156'),
  MIDIVoice('BrsStacc SRX', 93, 8, 28, 'HIT&STAB', 'XP-E 157'),
  MIDIVoice('Finale SRX /', 93, 8, 29, 'HIT&STAB', 'XP-E 158'),
  MIDIVoice('Orch Piccolo', 93, 8, 30, 'FLUTE', 'XP-E 159'),
  MIDIVoice('Picc Vel Tr', 93, 8, 31, 'FLUTE', 'XP-E 160'),
  MIDIVoice('Piccolo Trio', 93, 8, 32, 'FLUTE', 'XP-E 161'),
  MIDIVoice('Orch Flute', 93, 8, 33, 'FLUTE', 'XP-E 162'),
  MIDIVoice('Vibra Flute', 93, 8, 34, 'FLUTE', 'XP-E 163'),
  MIDIVoice('FluteAtm/Aft', 93, 8, 35, 'FLUTE', 'XP-E 164'),
  MIDIVoice('Picc/Fl 8va', 93, 8, 36, 'FLUTE', 'XP-E 165'),
  MIDIVoice('Double Flute', 93, 8, 37, 'FLUTE', 'XP-E 166'),
  MIDIVoice('Fl/EH Usn', 93, 8, 38, 'FLUTE', 'XP-E 167'),
  MIDIVoice('Calliope SRX', 93, 8, 39, 'FLUTE', 'XP-E 168'),
  MIDIVoice('DynoCelt SRX', 93, 8, 40, 'FLUTE', 'XP-E 169'),
  MIDIVoice('Ethnic Flute', 93, 8, 41, 'FLUTE', 'XP-E 170'),
  MIDIVoice('AmbiFluteSRX', 93, 8, 42, 'FLUTE', 'XP-E 171'),
  MIDIVoice('T.WhistleDly', 93, 8, 43, 'FLUTE', 'XP-E 172'),
  MIDIVoice('TinWhistle', 93, 8, 44, 'FLUTE', 'XP-E 173'),
  MIDIVoice('Sop Recorder', 93, 8, 45, 'FLUTE', 'XP-E 174'),
  MIDIVoice('Tnr Recorder', 93, 8, 46, 'FLUTE', 'XP-E 175'),
  MIDIVoice('Whistle SRX', 93, 8, 47, 'FLUTE', 'XP-E 176'),
  MIDIVoice('Solo Clari', 93, 8, 48, 'WIND', 'XP-E 177'),
  MIDIVoice('Unison Clari', 93, 8, 49, 'WIND', 'XP-E 178'),
  MIDIVoice('Orch Clar', 93, 8, 50, 'WIND', 'XP-E 179'),
  MIDIVoice('Bs Clairenet', 93, 8, 51, 'WIND', 'XP-E 180'),
  MIDIVoice('Orch Bs Clar', 93, 8, 52, 'WIND', 'XP-E 181'),
  MIDIVoice('Cl/Bs Cl 8va', 93, 8, 53, 'WIND', 'XP-E 182'),
  MIDIVoice('Fl/Cl Usn', 93, 8, 54, 'WIND', 'XP-E 183'),
  MIDIVoice('Fl/Cl 8va', 93, 8, 55, 'WIND', 'XP-E 184'),
  MIDIVoice('Orch Oboe', 93, 8, 56, 'WIND', 'XP-E 185'),
  MIDIVoice('Sweet Oboe', 93, 8, 57, 'WIND', 'XP-E 186'),
  MIDIVoice('Cor Oboe', 93, 8, 58, 'WIND', 'XP-E 187'),
  MIDIVoice('OBOE Solo', 93, 8, 59, 'WIND', 'XP-E 188'),
  MIDIVoice('2 Close Oboe', 93, 8, 60, 'WIND', 'XP-E 189'),
  MIDIVoice('Orch Eng Hrn', 93, 8, 61, 'WIND', 'XP-E 190'),
  MIDIVoice('Horn\'o U.K.', 93, 8, 62, 'WIND', 'XP-E 191'),
  MIDIVoice('Orch Bassoon', 93, 8, 63, 'WIND', 'XP-E 192'),
  MIDIVoice('Bassoon III', 93, 8, 64, 'WIND', 'XP-E 193'),
  MIDIVoice('BassFoons', 93, 8, 65, 'WIND', 'XP-E 194'),
  MIDIVoice('Cl/Bsn Usn', 93, 8, 66, 'WIND', 'XP-E 195'),
  MIDIVoice('Cl/Bsn 8va', 93, 8, 67, 'WIND', 'XP-E 196'),
  MIDIVoice('Fl/Ob Usn', 93, 8, 68, 'WIND', 'XP-E 197'),
  MIDIVoice('Fl/EH 8va', 93, 8, 69, 'WIND', 'XP-E 198'),
  MIDIVoice('Fl/Bsn 8va', 93, 8, 70, 'WIND', 'XP-E 199'),
  MIDIVoice('BsCl/Bsn 8vb', 93, 8, 71, 'WIND', 'XP-E 200'),
  MIDIVoice('BsCl/Bsn Usn', 93, 8, 72, 'WIND', 'XP-E 201'),
  MIDIVoice('Cl/Hrn/Bsn 1', 93, 8, 73, 'WIND', 'XP-E 202'),
  MIDIVoice('Cl/Hrn/Bsn 2', 93, 8, 74, 'WIND', 'XP-E 203'),
  MIDIVoice('Ob/Hrns/Bsns', 93, 8, 75, 'WIND', 'XP-E 204'),
  MIDIVoice('Ob/Bsn 8va', 93, 8, 76, 'WIND', 'XP-E 205'),
  MIDIVoice('Ob/EH Usn', 93, 8, 77, 'WIND', 'XP-E 206'),
  MIDIVoice('Ob/EH 8va', 93, 8, 78, 'WIND', 'XP-E 207'),
  MIDIVoice('EH/Bsn Usn', 93, 8, 79, 'WIND', 'XP-E 208'),
  MIDIVoice('EH/Bsn 8va', 93, 8, 80, 'WIND', 'XP-E 209'),
  MIDIVoice('EH/Cl Usn', 93, 8, 81, 'WIND', 'XP-E 210'),
  MIDIVoice('EH/Bs Cl 8va', 93, 8, 82, 'WIND', 'XP-E 211'),
  MIDIVoice('Ob/Cl Usn', 93, 8, 83, 'WIND', 'XP-E 212'),
  MIDIVoice('Ob/BsCl 15va', 93, 8, 84, 'WIND', 'XP-E 213'),
  MIDIVoice('Hrns/Bsns', 93, 8, 85, 'WIND', 'XP-E 214'),
  MIDIVoice('Really Reeds', 93, 8, 86, 'WIND', 'XP-E 215'),
  MIDIVoice('Reed Duet', 93, 8, 87, 'WIND', 'XP-E 216'),
  MIDIVoice('Multi Reeds', 93, 8, 88, 'WIND', 'XP-E 217'),
  MIDIVoice('Medieval Rds', 93, 8, 89, 'WIND', 'XP-E 218'),
  MIDIVoice('ScottishPIPE', 93, 8, 90, 'WIND', 'XP-E 219'),
  MIDIVoice('Hill&Sheeps', 93, 8, 91, 'ETHNIC', 'XP-E 220'),
  MIDIVoice('HilndChr SRX', 93, 8, 92, 'ETHNIC', 'XP-E 221'),
  MIDIVoice('Solo Fr.Horn', 93, 8, 93, 'AC.BRASS', 'XP-E 222'),
  MIDIVoice('SoloF.HrnSRX', 93, 8, 94, 'AC.BRASS', 'XP-E 223'),
  MIDIVoice('HrnAccompSRX', 93, 8, 95, 'AC.BRASS', 'XP-E 224'),
  MIDIVoice('Orch Hrns Sw', 93, 8, 96, 'AC.BRASS', 'XP-E 225'),
  MIDIVoice('Hornz Stereo', 93, 8, 97, 'AC.BRASS', 'XP-E 226'),
  MIDIVoice('Orch Hrns ff', 93, 8, 98, 'AC.BRASS', 'XP-E 227'),
  MIDIVoice('FizzHorns ff', 93, 8, 99, 'AC.BRASS', 'XP-E 228'),
  MIDIVoice('Fr.Horns SRX', 93, 8, 100, 'AC.BRASS', 'XP-E 229'),
  MIDIVoice('Dynamic Hrns', 93, 8, 101, 'AC.BRASS', 'XP-E 230'),
  MIDIVoice('Horn Sect /', 93, 8, 102, 'AC.BRASS', 'XP-E 231'),
  MIDIVoice('Fr.HrnSfzSRX', 93, 8, 103, 'AC.BRASS', 'XP-E 232'),
  MIDIVoice('MuteFr.Horns', 93, 8, 104, 'AC.BRASS', 'XP-E 233'),
  MIDIVoice('F.Horn Rip', 93, 8, 105, 'AC.BRASS', 'XP-E 234'),
  MIDIVoice('Trumpet Plus', 93, 8, 106, 'AC.BRASS', 'XP-E 235'),
  MIDIVoice('Natural Tmpt', 93, 8, 107, 'AC.BRASS', 'XP-E 236'),
  MIDIVoice('Real Tp SRX', 93, 8, 108, 'AC.BRASS', 'XP-E 237'),
  MIDIVoice('El Bono SRX', 93, 8, 109, 'AC.BRASS', 'XP-E 238'),
  MIDIVoice('Coronet', 93, 8, 110, 'AC.BRASS', 'XP-E 239'),
  MIDIVoice('Flugelhorn', 93, 8, 111, 'AC.BRASS', 'XP-E 240'),
  MIDIVoice('Mute Tp SRX', 93, 8, 112, 'AC.BRASS', 'XP-E 241'),
  MIDIVoice('HrmnMute SRX', 93, 8, 113, 'AC.BRASS', 'XP-E 242'),
  MIDIVoice('WahMute /Mod', 93, 8, 114, 'AC.BRASS', 'XP-E 243'),
  MIDIVoice('Trumpeters', 93, 8, 115, 'AC.BRASS', 'XP-E 244'),
  MIDIVoice('Tp Ens SRX', 93, 8, 116, 'AC.BRASS', 'XP-E 245'),
  MIDIVoice('Trumps fff!!', 93, 8, 117, 'AC.BRASS', 'XP-E 246'),
  MIDIVoice('Softy Bones', 93, 8, 118, 'AC.BRASS', 'XP-E 247'),
  MIDIVoice('Bone Fluegal', 93, 8, 119, 'AC.BRASS', 'XP-E 248'),
  MIDIVoice('Natural Tbn', 93, 8, 120, 'AC.BRASS', 'XP-E 249'),
  MIDIVoice('Trombone SRX', 93, 8, 121, 'AC.BRASS', 'XP-E 250'),
  MIDIVoice('SoloTb SRX 1', 93, 8, 122, 'AC.BRASS', 'XP-E 251'),
  MIDIVoice('SoloTb SRX 2', 93, 8, 123, 'AC.BRASS', 'XP-E 252'),
  MIDIVoice('Bs Tb', 93, 8, 124, 'AC.BRASS', 'XP-E 253'),
  MIDIVoice('Tbn One', 93, 8, 125, 'AC.BRASS', 'XP-E 254'),
  MIDIVoice('Bone Boys', 93, 8, 126, 'AC.BRASS', 'XP-E 255'),
  MIDIVoice('Bones sectn', 93, 8, 127, 'AC.BRASS', 'XP-E 256'),
  MIDIVoice('BigBones SRX', 93, 9, 0, 'AC.BRASS', 'XP-E 257'),
  MIDIVoice('BsBoneSctSRX', 93, 9, 1, 'AC.BRASS', 'XP-E 258'),
  MIDIVoice('Noblesse', 93, 9, 2, 'AC.BRASS', 'XP-E 259'),
  MIDIVoice('Brass Choral', 93, 9, 3, 'AC.BRASS', 'XP-E 260'),
  MIDIVoice('BrassEns/Mod', 93, 9, 4, 'AC.BRASS', 'XP-E 261'),
  MIDIVoice('Small Brass', 93, 9, 5, 'AC.BRASS', 'XP-E 262'),
  MIDIVoice('Brass Orche', 93, 9, 6, 'AC.BRASS', 'XP-E 263'),
  MIDIVoice('Switch Fall', 93, 9, 7, 'AC.BRASS', 'XP-E 264'),
  MIDIVoice('4-Pc Brs Scn', 93, 9, 8, 'AC.BRASS', 'XP-E 265'),
  MIDIVoice('BiggieBrsSRX', 93, 9, 9, 'AC.BRASS', 'XP-E 266'),
  MIDIVoice('SoloTuba SRX', 93, 9, 10, 'AC.BRASS', 'XP-E 267'),
  MIDIVoice('Tuba sfz/Mod', 93, 9, 11, 'AC.BRASS', 'XP-E 268'),
  MIDIVoice('Tuba SRX', 93, 9, 12, 'AC.BRASS', 'XP-E 269'),
  MIDIVoice('Medieval Brs', 93, 9, 13, 'AC.BRASS', 'XP-E 270'),
  MIDIVoice('Full Brass', 93, 9, 14, 'AC.BRASS', 'XP-E 271'),
  MIDIVoice('Brass ff', 93, 9, 15, 'AC.BRASS', 'XP-E 272'),
  MIDIVoice('Brass Sect /', 93, 9, 16, 'AC.BRASS', 'XP-E 273'),
  MIDIVoice('Multi Sax', 93, 9, 17, 'SAX', 'XP-E 274'),
  MIDIVoice('St.EuroPiano', 93, 9, 18, 'AC.PIANO', 'XP-E 275'),
  MIDIVoice('JoyoClassics', 93, 9, 19, 'AC.PIANO', 'XP-E 276'),
  MIDIVoice('Empathy', 93, 9, 20, 'AC.PIANO', 'XP-E 277'),
  MIDIVoice('Piano & Strs', 93, 9, 21, 'AC.PIANO', 'XP-E 278'),
  MIDIVoice('Pno Concerto', 93, 9, 22, 'AC.PIANO', 'XP-E 279'),
  MIDIVoice('Song Wish', 93, 9, 23, 'AC.PIANO', 'XP-E 280'),
  MIDIVoice('HpsFrntSRX 1', 93, 9, 24, 'KEYBOARDS', 'XP-E 281'),
  MIDIVoice('HpsFrntSRX 2', 93, 9, 25, 'KEYBOARDS', 'XP-E 282'),
  MIDIVoice('HpsFrntSRX 3', 93, 9, 26, 'KEYBOARDS', 'XP-E 283'),
  MIDIVoice('HpsBackSRX 1', 93, 9, 27, 'KEYBOARDS', 'XP-E 284'),
  MIDIVoice('HpsBackSRX 2', 93, 9, 28, 'KEYBOARDS', 'XP-E 285'),
  MIDIVoice('HpsBackSRX 3', 93, 9, 29, 'KEYBOARDS', 'XP-E 286'),
  MIDIVoice('Hps F/B SRX', 93, 9, 30, 'KEYBOARDS', 'XP-E 287'),
  MIDIVoice('Hps F4/B SRX', 93, 9, 31, 'KEYBOARDS', 'XP-E 288'),
  MIDIVoice('Hps F/B/B4 S', 93, 9, 32, 'KEYBOARDS', 'XP-E 289'),
  MIDIVoice('HpsLuteSRX 1', 93, 9, 33, 'KEYBOARDS', 'XP-E 290'),
  MIDIVoice('HpsLute 2', 93, 9, 34, 'KEYBOARDS', 'XP-E 291'),
  MIDIVoice('HpsLute 3', 93, 9, 35, 'KEYBOARDS', 'XP-E 292'),
  MIDIVoice('FullHarpsi 1', 93, 9, 36, 'KEYBOARDS', 'XP-E 293'),
  MIDIVoice('FullHarpsi 2', 93, 9, 37, 'KEYBOARDS', 'XP-E 294'),
  MIDIVoice('Continuo Pdl', 93, 9, 38, 'KEYBOARDS', 'XP-E 295'),
  MIDIVoice('Celesta SRX', 93, 9, 39, 'KEYBOARDS', 'XP-E 296'),
  MIDIVoice('MusicBellSRX', 93, 9, 40, 'BELL', 'XP-E 297'),
  MIDIVoice('Water Mallet', 93, 9, 41, 'BELL', 'XP-E 298'),
  MIDIVoice('Newborn', 93, 9, 42, 'BELL', 'XP-E 299'),
  MIDIVoice('Victoriana 1', 93, 9, 43, 'BELL', 'XP-E 300'),
  MIDIVoice('St.M.Box SRX', 93, 9, 44, 'BELL', 'XP-E 301'),
  MIDIVoice('Victoriana 2', 93, 9, 45, 'BELL', 'XP-E 302'),
  MIDIVoice('ChurchBellS1', 93, 9, 46, 'BELL', 'XP-E 303'),
  MIDIVoice('BlfryChm SRX', 93, 9, 47, 'BELL', 'XP-E 304'),
  MIDIVoice('ChurchBellS2', 93, 9, 48, 'BELL', 'XP-E 305'),
  MIDIVoice('Tub.Bells S1', 93, 9, 49, 'BELL', 'XP-E 306'),
  MIDIVoice('Tub.Bells S2', 93, 9, 50, 'BELL', 'XP-E 307'),
  MIDIVoice('BsMarimbSRX1', 93, 9, 51, 'MALLET', 'XP-E 308'),
  MIDIVoice('BsMarimbSRX2', 93, 9, 52, 'MALLET', 'XP-E 309'),
  MIDIVoice('MultiMallets', 93, 9, 53, 'MALLET', 'XP-E 310'),
  MIDIVoice('Glocken', 93, 9, 54, 'MALLET', 'XP-E 311'),
  MIDIVoice('Glockeneste', 93, 9, 55, 'MALLET', 'XP-E 312'),
  MIDIVoice('GlocknlstSRX', 93, 9, 56, 'MALLET', 'XP-E 313'),
  MIDIVoice('Clear Glock', 93, 9, 57, 'MALLET', 'XP-E 314'),
  MIDIVoice('Xylorimba', 93, 9, 58, 'MALLET', 'XP-E 315'),
  MIDIVoice('Xylophone S1', 93, 9, 59, 'MALLET', 'XP-E 316'),
  MIDIVoice('Xylophone S2', 93, 9, 60, 'MALLET', 'XP-E 317'),
  MIDIVoice('Mallet Stack', 93, 9, 61, 'MALLET', 'XP-E 318'),
  MIDIVoice('OrgFlutes S1', 93, 9, 62, 'ORGAN', 'XP-E 319'),
  MIDIVoice('OrgFlutes S2', 93, 9, 63, 'ORGAN', 'XP-E 320'),
  MIDIVoice('OrgFlutes S3', 93, 9, 64, 'ORGAN', 'XP-E 321'),
  MIDIVoice('OrgFlute 8\'S', 93, 9, 65, 'ORGAN', 'XP-E 322'),
  MIDIVoice('Psyche Pipes', 93, 9, 66, 'ORGAN', 'XP-E 323'),
  MIDIVoice('ChrchPipes S', 93, 9, 67, 'ORGAN', 'XP-E 324'),
  MIDIVoice('Organ&Recdr', 93, 9, 68, 'ORGAN', 'XP-E 325'),
  MIDIVoice('Early Harmn', 93, 9, 69, 'ORGAN', 'XP-E 326'),
  MIDIVoice('CathedralSRX', 93, 9, 70, 'ORGAN', 'XP-E 327'),
  MIDIVoice('Harmonium', 93, 9, 71, 'ORGAN', 'XP-E 328'),
  MIDIVoice('ChurchOrgSRX', 93, 9, 72, 'ORGAN', 'XP-E 329'),
  MIDIVoice('OrganChrdSRX', 93, 9, 73, 'ORGAN', 'XP-E 330'),
  MIDIVoice('Musaccordion', 93, 9, 74, 'ACCORDION', 'XP-E 331'),
  MIDIVoice('Mystery Pad', 93, 9, 75, 'PULSATING', 'XP-E 332'),
  MIDIVoice('Psychedelic1', 93, 9, 76, 'SYNTH FX', 'XP-E 333'),
  MIDIVoice('Psychedelic2', 93, 9, 77, 'SYNTH FX', 'XP-E 334'),
  MIDIVoice('Eylsium m7^', 93, 9, 78, 'SYNTH FX', 'XP-E 335'),
  MIDIVoice('Eylsium 9th^', 93, 9, 79, 'SYNTH FX', 'XP-E 336'),
  MIDIVoice('Eylsium +7^', 93, 9, 80, 'SYNTH FX', 'XP-E 337'),
  MIDIVoice('Eylsium b9^', 93, 9, 81, 'SYNTH FX', 'XP-E 338'),
  MIDIVoice('Vln RunUp Mj', 93, 9, 82, 'SYNTH FX', 'XP-E 339'),
  MIDIVoice('Vln RunUp Mn', 93, 9, 83, 'SYNTH FX', 'XP-E 340'),
  MIDIVoice('Vln RunDn Mj', 93, 9, 84, 'SYNTH FX', 'XP-E 341'),
  MIDIVoice('Vln RunDn Mn', 93, 9, 85, 'SYNTH FX', 'XP-E 342'),
  MIDIVoice('Maj/MinHarps', 93, 9, 86, 'SYNTH FX', 'XP-E 343'),
  MIDIVoice('9th/b9 Harps', 93, 9, 87, 'SYNTH FX', 'XP-E 344'),
  MIDIVoice('Harp m7 SRX', 93, 9, 88, 'SYNTH FX', 'XP-E 345'),
  MIDIVoice('Harp 9th SRX', 93, 9, 89, 'SYNTH FX', 'XP-E 346'),
  MIDIVoice('Harp +7 SRX', 93, 9, 90, 'SYNTH FX', 'XP-E 347'),
  MIDIVoice('Harp b9 SRX', 93, 9, 91, 'SYNTH FX', 'XP-E 348'),
  MIDIVoice('Harpm7SclSRX', 93, 9, 92, 'SYNTH FX', 'XP-E 349'),
  MIDIVoice('Harp9thScrlS', 93, 9, 93, 'SYNTH FX', 'XP-E 350'),
  MIDIVoice('Harp+7SclSRX', 93, 9, 94, 'SYNTH FX', 'XP-E 351'),
  MIDIVoice('Harpb9SclSRX', 93, 9, 95, 'SYNTH FX', 'XP-E 352'),
  MIDIVoice('Cluster Gong', 93, 9, 96, 'SYNTH FX', 'XP-E 353'),
  MIDIVoice('Sus.Perc Hit', 93, 9, 97, 'SYNTH FX', 'XP-E 354'),
  MIDIVoice('Prc Ens6-Maj', 93, 9, 98, 'SYNTH FX', 'XP-E 355'),
  MIDIVoice('Prc Ens7-Min', 93, 9, 99, 'SYNTH FX', 'XP-E 356'),
  MIDIVoice('Prc Ens8-Dim', 93, 9, 100, 'SYNTH FX', 'XP-E 357'),
  MIDIVoice('Cluster SRX', 93, 9, 101, 'SYNTH FX', 'XP-E 358'),
  MIDIVoice('HorrorClustr', 93, 9, 102, 'SYNTH FX', 'XP-E 359'),
  MIDIVoice('Hell Section', 93, 9, 103, 'SYNTH FX', 'XP-E 360'),
  MIDIVoice('Legettimare', 93, 9, 104, 'SYNTH FX', 'XP-E 361'),
  MIDIVoice('Limbus SRX', 93, 9, 105, 'SYNTH FX', 'XP-E 362'),
  MIDIVoice('Backword', 93, 9, 106, 'SYNTH FX', 'XP-E 363'),
  MIDIVoice('Dreamseq SRX', 93, 9, 107, 'SYNTH FX', 'XP-E 364'),
  MIDIVoice('Midnight SRX', 93, 9, 108, 'SYNTH FX', 'XP-E 365'),
  MIDIVoice('Colombus SRX', 93, 9, 109, 'SYNTH FX', 'XP-E 366'),
  MIDIVoice('Once Upon A', 93, 9, 110, 'OTHER SYNTH', 'XP-E 367'),
  MIDIVoice('Desert Dream', 93, 9, 111, 'OTHER SYNTH', 'XP-E 368'),
  MIDIVoice('AncientTimes', 93, 9, 112, 'OTHER SYNTH', 'XP-E 369'),
  MIDIVoice('Tension SRX', 93, 9, 113, 'OTHER SYNTH', 'XP-E 370'),
  MIDIVoice('Wreck', 93, 9, 114, 'BRIGHT PAD', 'XP-E 371'),
  MIDIVoice('Eclipse SRX', 93, 9, 115, 'BRIGHT PAD', 'XP-E 372'),
  MIDIVoice('PulsingVox S', 93, 9, 116, 'BRIGHT PAD', 'XP-E 373'),
  MIDIVoice('SynthStr.Pad', 93, 9, 117, 'SOFT PAD', 'XP-E 374'),
  MIDIVoice('Meditate PAD', 93, 9, 118, 'SOFT PAD', 'XP-E 375'),
  MIDIVoice('Choir', 93, 9, 119, 'VOX', 'XP-E 376'),
  MIDIVoice('Angelic Pad', 93, 9, 120, 'VOX', 'XP-E 377'),
  MIDIVoice('BoysChoirSRX', 93, 9, 121, 'VOX', 'XP-E 378'),
  MIDIVoice('Sing! /Mod', 93, 9, 122, 'VOX', 'XP-E 379'),
  MIDIVoice('SmockyVoices', 93, 9, 123, 'VOX', 'XP-E 380'),
  MIDIVoice('Smooth Choir', 93, 9, 124, 'VOX', 'XP-E 381'),
  MIDIVoice('X.. Vox SRX', 93, 9, 125, 'VOX', 'XP-E 382'),
  MIDIVoice('RealChoirSRX', 93, 9, 126, 'VOX', 'XP-E 383'),
  MIDIVoice('StChrMm/Ah S', 93, 9, 127, 'VOX', 'XP-E 384'),
  MIDIVoice('Mmms & Aaahs', 93, 10, 0, 'VOX', 'XP-E 385'),
  MIDIVoice('Choir /Mod', 93, 10, 1, 'VOX', 'XP-E 386'),
  MIDIVoice('Close Mouths', 93, 10, 2, 'VOX', 'XP-E 387'),
  MIDIVoice('Voice Stax', 93, 10, 3, 'VOX', 'XP-E 388'),
  MIDIVoice('MorphieChoir', 93, 10, 4, 'VOX', 'XP-E 389'),
  MIDIVoice('Morph4Choir', 93, 10, 5, 'VOX', 'XP-E 390'),
  MIDIVoice('17th Movemnt', 93, 10, 6, 'VOX', 'XP-E 391'),
  MIDIVoice('Matins', 93, 10, 7, 'VOX', 'XP-E 392'),
  MIDIVoice('Quartet II 5', 93, 10, 8, 'VOX', 'XP-E 393'),
  MIDIVoice('Scat /', 93, 10, 9, 'VOX', 'XP-E 394'),
  MIDIVoice('Scatmen! SRX', 93, 10, 10, 'VOX', 'XP-E 395'),
  MIDIVoice('The Voices', 93, 10, 11, 'VOX', 'XP-E 396'),
  MIDIVoice('VocalCollect', 93, 10, 12, 'VOX', 'XP-E 397'),
  MIDIVoice('GregorianCho', 93, 10, 13, 'VOX', 'XP-E 398'),
  MIDIVoice('Soprano&co.', 93, 10, 14, 'VOX', 'XP-E 399'),
  MIDIVoice('Tenor solo', 93, 10, 15, 'VOX', 'XP-E 400'),
  MIDIVoice('ClarsahHarpS', 93, 10, 16, 'PLUCKED', 'XP-E 401'),
  MIDIVoice('Heavens Harp', 93, 10, 17, 'PLUCKED', 'XP-E 402'),
  MIDIVoice('C.Hrp/padSRX', 93, 10, 18, 'PLUCKED', 'XP-E 403'),
  MIDIVoice('PhaseClarsah', 93, 10, 19, 'PLUCKED', 'XP-E 404'),
  MIDIVoice('ClearHarpSRX', 93, 10, 20, 'PLUCKED', 'XP-E 405'),
  MIDIVoice('Nails Harp', 93, 10, 21, 'PLUCKED', 'XP-E 406'),
  MIDIVoice('Harp SRX', 93, 10, 22, 'PLUCKED', 'XP-E 407'),
  MIDIVoice('Natural Harp', 93, 10, 23, 'PLUCKED', 'XP-E 408'),
  MIDIVoice('Warm Harp', 93, 10, 24, 'PLUCKED', 'XP-E 409'),
  MIDIVoice('Bousouk&Harp', 93, 10, 25, 'PLUCKED', 'XP-E 410'),
  MIDIVoice('Etheral Lute', 93, 10, 26, 'PLUCKED', 'XP-E 411'),
  MIDIVoice('DelicateCOMB', 93, 10, 27, 'PLUCKED', 'XP-E 412'),
  MIDIVoice('St.CymblnSRX', 93, 10, 28, 'PLUCKED', 'XP-E 413'),
  MIDIVoice('CymblnDuoSRX', 93, 10, 29, 'PLUCKED', 'XP-E 414'),
  MIDIVoice('Bohemian SRX', 93, 10, 30, 'PLUCKED', 'XP-E 415'),
  MIDIVoice('Bousouki Pic', 93, 10, 31, 'PLUCKED', 'XP-E 416'),
  MIDIVoice('Bousouki', 93, 10, 32, 'PLUCKED', 'XP-E 417'),
  MIDIVoice('PulcinelaSRX', 93, 10, 33, 'PLUCKED', 'XP-E 418'),
  MIDIVoice('SN Roll SRX/', 93, 10, 34, 'PERCUSSION', 'XP-E 419'),
  MIDIVoice('Perc Ens 1^', 93, 10, 35, 'PERCUSSION', 'XP-E 420'),
  MIDIVoice('Perc Ens 2^', 93, 10, 36, 'PERCUSSION', 'XP-E 421'),
  MIDIVoice('Perc Ens 3^', 93, 10, 37, 'PERCUSSION', 'XP-E 422'),
  MIDIVoice('Perc Ens 4^', 93, 10, 38, 'PERCUSSION', 'XP-E 423'),
  MIDIVoice('Perc Ens 5^', 93, 10, 39, 'PERCUSSION', 'XP-E 424'),
  MIDIVoice('Orch Percs', 93, 10, 40, 'PERCUSSION', 'XP-E 425'),
  MIDIVoice('BodhranSplit', 93, 10, 41, 'PERCUSSION', 'XP-E 426'),
  MIDIVoice('BodhranVel S', 93, 10, 42, 'PERCUSSION', 'XP-E 427'),
  MIDIVoice('CrazyBodhrnS', 93, 10, 43, 'PERCUSSION', 'XP-E 428'),
  MIDIVoice('BodhranMenuS', 93, 10, 44, 'PERCUSSION', 'XP-E 429'),
  MIDIVoice('Perc Mix SRX', 93, 10, 45, 'PERCUSSION', 'XP-E 430'),
  MIDIVoice('MassiveTimpa', 93, 10, 46, 'PERCUSSION', 'XP-E 431'),
  MIDIVoice('4-way Timps', 93, 10, 47, 'PERCUSSION', 'XP-E 432'),
  MIDIVoice('DynaTimpsSRX', 93, 10, 48, 'PERCUSSION', 'XP-E 433'),
  MIDIVoice('TimpaniRoll1', 93, 10, 49, 'PERCUSSION', 'XP-E 434'),
  MIDIVoice('TimpaniRoll2', 93, 10, 50, 'PERCUSSION', 'XP-E 435'),
  MIDIVoice('MultiTimpani', 93, 10, 51, 'PERCUSSION', 'XP-E 436'),
  MIDIVoice('Roll > Klang', 93, 10, 52, 'PERCUSSION', 'XP-E 437'),
  MIDIVoice('Timpani /', 93, 10, 53, 'PERCUSSION', 'XP-E 438'),
  MIDIVoice('Big Orc.Perc', 93, 10, 54, 'PERCUSSION', 'XP-E 439'),
  MIDIVoice('WindChimeSRX', 93, 10, 55, 'PERCUSSION', 'XP-E 440'),
  MIDIVoice('FingerCymSRX', 93, 10, 56, 'PERCUSSION', 'XP-E 441'),
  MIDIVoice('ConcertBDSRX', 93, 10, 57, 'PERCUSSION', 'XP-E 442'),
  MIDIVoice('BD Roll SRX/', 93, 10, 58, 'PERCUSSION', 'XP-E 443'),
  MIDIVoice('Tam Tam SRX', 93, 10, 59, 'PERCUSSION', 'XP-E 444'),
  MIDIVoice('Piatti!! SRX', 93, 10, 60, 'PERCUSSION', 'XP-E 445'),
  MIDIVoice('SleighBellsS', 93, 10, 61, 'PERCUSSION', 'XP-E 446'),
  MIDIVoice('SlapstickS /', 93, 10, 62, 'PERCUSSION', 'XP-E 447'),
  MIDIVoice('TambourineS/', 93, 10, 63, 'PERCUSSION', 'XP-E 448'),
  MIDIVoice('CastanetsS /', 93, 10, 64, 'PERCUSSION', 'XP-E 449'),
]
