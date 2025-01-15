import re
from collections import defaultdict
from random import choice


class Singleton(type):
    class_instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.class_instances:
            cls.class_instances[cls] = super().__call__(*args, **kwargs)
        return cls.class_instances[cls]


class Santa(metaclass=Singleton):
    def __init__(self):
        self.gifts = {}
        self.count_of_xmases = defaultdict(int)
        self.gifts_count = defaultdict(int)
        self.naughty_kids = set()

    def __call__(self, kid_instance, message):
        wish = self.__extract_wish(message)
        self.gifts[kid_instance] = wish
        self.gifts_count[wish] += 1

    def __matmul__(self, letter):
        wish = self.__extract_wish(letter)
        kid_id = int(self.__extract_signature(letter))
        kid = Kid.created_kids.get(kid_id)
        self.gifts[kid] = wish
        self.gifts_count[wish] += 1

    def __iter__(self):
        for gift in self.gifts.values():
            yield gift

    def choose_random_default_gift(self):
        curr_gift_count = 0
        most_wished_gifts = []
        for gift, count in self.gifts_count.items():
            if count > curr_gift_count:
                curr_gift_count = count
                most_wished_gifts = [gift]
            elif count == curr_gift_count:
                most_wished_gifts.append(gift)
        return most_wished_gifts
    
    def reset_christmas(self):
         # Reset gifts values for the new Christmas + incrementing the xmas count by 1
            for kid in self.gifts.keys():
                self.gifts[kid] = ""
                self.count_of_xmases[kid] += 1
                
    def xmas(self):
        if all(count == 0 for count in self.gifts_count.values()):
            self.reset_christmas()
            return
        
        most_wished_gifts = self.choose_random_default_gift()
        default_gift = choice(most_wished_gifts) if most_wished_gifts else None
        
        for kid, gift in self.gifts.items():
            if self.count_of_xmases[kid] >= 5:
                continue

            if kid in self.naughty_kids:
                kid("coal")
            else:
                if gift == "":
                    final_gift = default_gift
                else:
                    final_gift = gift
                    
                if final_gift:
                    kid(final_gift)

        self.reset_christmas()
        self.naughty_kids.clear()
        self.gifts_count = defaultdict(int)

    @staticmethod
    def __extract_wish(message):
        match = re.search(r'["\']([a-zA-Z0-9 ]+)["\']', message)
        return match.group(1)

    @staticmethod
    def __extract_signature(message):
        match = re.search(r'^\s*(\d+)\s*$', message, re.MULTILINE)
        return match.group(1)


class Kid(type):
    created_kids = {}
    
    @classmethod
    def is_naughty(cls, method):
        def wrapper(self, *args, **kwargs):
            try:
                return method(self, *args, **kwargs)
            except Exception:
                Santa().naughty_kids.add(self)
                raise
        return wrapper

    def __new__(cls, name, bases, dct):
        if '__call__' not in dct:
            raise NotImplementedError(
                f"Tova meta dete/klas {name} neshto ne moje da se vika!")

        for attr_name, attr_value in dct.items():
            if callable(attr_value) and not attr_name.startswith("_"):
                dct[attr_name] = cls.is_naughty(attr_value)
        return super().__new__(cls, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        # Saving the (id -> kid) pair of each created kid for an easier access later in __matmul__
        Kid.created_kids[id(instance)] = instance

        # Set default value to each created kid
        santa = Santa()
        if instance not in santa.gifts:
            santa.gifts[instance] = ""
        return instance