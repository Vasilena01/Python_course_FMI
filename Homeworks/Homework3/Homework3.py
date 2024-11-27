class Tone:
    TONES_SCALE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    def __init__(self, tone):
        self.tone = tone
    
    def __str__(self):
        return self.tone
    
    def __add__(self, other):
        if isinstance(other, Tone):
            return Chord(self, other)
        elif isinstance(other, Interval):
            start_index = self.TONES_SCALE.index(self.tone)
            new_index = (start_index + other.number_of_semitones) % 12
            
            return Tone(self.TONES_SCALE[new_index])
                
    def __sub__(self, other):
        if isinstance(other, Tone):
            self_index = self.TONES_SCALE.index(self.tone)
            other_index = self.TONES_SCALE.index(other.tone)
            
            semitones_count = (self_index - other_index) % 12
            
            return Interval(semitones_count)
        elif isinstance(other, Interval):
            start_index = self.TONES_SCALE.index(self.tone)
            new_index = (start_index - other.number_of_semitones) % 12
            
            return Tone(self.TONES_SCALE[new_index])


class Interval:
    def __init__(self, number_of_semitones):
        self.number_of_semitones = number_of_semitones
        self.is_positive_direction = True
        
    def __str__(self):
        self.number_of_semitones %= 12
        
        intervals = (
            'unison', 'minor 2nd', 'major 2nd', 'minor 3rd',
            'major 3rd', 'perfect 4th', 'diminished 5th', 'perfect 5th',
            'minor 6th', 'major 6th', 'minor 7th', 'major 7th'
        )
        
        return intervals[self.number_of_semitones]
    
    def __add__(self, other):
        if isinstance(other, Tone):
            raise TypeError("Invalid operation")
        elif isinstance(other, Interval):
            return Interval(self.number_of_semitones + other.number_of_semitones)
    
    def __sub__(self, other):
        if isinstance(other, Tone):
            raise TypeError("Invalid operation")

    def __neg__(self):
        neg_interval = Interval(self.number_of_semitones)
        neg_interval.is_positive_direction = not self.is_positive_direction
        return neg_interval


class Chord:
    TONES_SCALE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    def __init__(self, first_tone, *args, **kwargs):
        all_tones = [str(first_tone)] + [str(tone) for tone in args] + [str(tone) for tone in kwargs.values()]
        self.chord = []
        
        for tone in all_tones:
            if tone not in self.chord:
                self.chord.append(tone)

        if len(self.chord) == 1:
            raise TypeError("Cannot have a chord made of only 1 unique tone")

        self.root = self.chord[0]
        
    def __str__(self):
        root_index = self.TONES_SCALE.index(self.root)
        
        #Order the other tones based on the root.
        sorted_tones = sorted(self.chord, key=lambda tone: (self.TONES_SCALE.index(tone) - root_index) % 12)
        
        return "-".join(sorted_tones)
    
    def __add__(self, other):
        if isinstance(other, Tone):
            new_tones = self.chord[:]
            new_tones.append(other.tone)
            return Chord(self.root, *new_tones)
        elif isinstance(other, Chord):
            return Chord(self.root, *self.chord, *other.chord)
            
    def __sub__(self, other):
        if isinstance(other, Tone):
            curr_tones = list(self.chord)
            
            if other.tone in curr_tones:
                    curr_tones.remove(other.tone)
                    self.root = curr_tones[0]
            else:
                raise TypeError(f"Cannot remove tone {str(other)} from chord {str(self)}")
                
            if len(curr_tones) >= 2:
                return Chord(self.root, *curr_tones)
            else:
                raise TypeError("Cannot have a chord made of only 1 unique tone")
        
    def _has_interval(self, interval):
        """ A private helper method to check if any tone forms a specific interval with the root. """
        
        root_index = self.TONES_SCALE.index(self.root)
        
        for tone in self.chord[1:]:
            tone_index = self.TONES_SCALE.index(tone)
            curr_interval = (tone_index - root_index) % 12
            
            if curr_interval == interval:
                return True
        return False
    
    def is_minor(self):
       return self._has_interval(3)
       
    def is_major(self):
        return self._has_interval(4)

    def is_power_chord(self):
        return not self.is_minor() and not self.is_major()

    def transposed(self, interval):
        if isinstance(interval, Interval):
            transposed_tones = []
            
            for tone in self.chord:
                curr_index = self.TONES_SCALE.index(tone)

                if interval.is_positive_direction:
                    new_index = (curr_index + interval.number_of_semitones) % 12
                else:
                    new_index = (curr_index - interval.number_of_semitones) % 12
                transposed_tones.append(self.TONES_SCALE[new_index])
            
            return Chord(transposed_tones[0], *transposed_tones[1:])