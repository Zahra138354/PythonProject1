import re


class House:
    def __init__(self, room_count, parking, elevator, storage, address, area, floor, plate):
        self.room_count = room_count
        self.parking = parking
        self.elevator = elevator
        self.storage = storage
        self.address = address
        self.area = area
        self.floor = floor
        self.plate = plate

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if isinstance(address, str):
            self._address = address
        else:
            raise ValueError("Invalid Address")

    @property
    def plate(self):
        return self._plate

    @plate.setter
    def plate(self, plate):
        if isinstance(plate, int):
            self._plate = plate
        else:
            raise ValueError("Invalid Plate")


def get_features(self):
    print(f"room_count={self.room_count},"
          f"parking={self.parking},"
          f"elevator={self.elevator},"
          f"storage={self.storage},"
          f"address={self.address},"
          f"area={self.area},"
          f"floor={self.floor},"
          f"plate={self.plate}"
          )


class Customer:
    def __init__(self, name, family, national_id, phone_number, customer_type):
        self.name = name
        self.family = family
        self.national_id = national_id
        self.phone_number = phone_number
        valid_types = ["مستاجر", "مالک", "فروشنده", "خریدار"]
        if customer_type in Customer.valid_types:
            self.customer_type = customer_type
        else:
            raise ValueError("نوع مشتری اشتباه است!!!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Invalid Name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        if isinstance(family, str):
            self._family = family
        else:
            raise ValueError("Invalid Family")

    @property
    def national_id(self):
        return self.national_id

    @national_id.setter
    def national_id(self, national_id):
        if isinstance(national_id, str):
            self.national_id = national_id
        else:
            raise ValueError("Invalid Nationalid")

    @property
    def phone_num(self):
        return self._phone_number

    @phone_num.setter
    def phone_num(self, phone_number):
        if not isinstance(phone_number, str) or re.match(r"^\d\d\d\d\d\d\d\d\d\d\d", phone_number):
            raise ValueError("شماره تلفن اشتباه است")
        else:
            self._phone_number = phone_number


class Contract:
    def __init__(self, contract_id, house_information: House, buyer, seller, price):
        self.contract_id = contract_id
        self.house = house_information
        self.buyer = buyer
        self.seller = seller
        self.price = price

    def show_info(self):
        print("مشخصات قرارداد")
        print(f"کد قرارداد:{self.contract_id}")
        print(f"آدرس ملک:{self.house.address}_متراژ:{self.house.area}")
        print(f"خریدار:{self.buyer}")
        print(f"فروشنده:{self.seller}")
        print(f"مبلغ:{self.price}")
