#abstract  مجرد
from abc import ABCMeta,abstractmethod   #عشان نعرفه ان الكلاس بتاعى abc

class programming(metaclass=ABCMeta):         #سؤال ان جمسع لغات البرمجه فيها اووب ولا لا مهوش سؤال منطقى لكن هو عاطينى مسثود مجرده امشى عليها فى باقى الكلاسز الى هعمل ليها انهرتنس
    @abstractmethod
    def has_oop(self):
        pass  #لان الفانكشن الabsمبتعملش حاجه (مجرده)


class python(programming):   #لكن البايثون منطقى
    def has_oop(self):
        return "yes"


class pascal(programming):    #هنا برضو منطقى
    def has_oop(self):
        return "No"


one=python()
print(one.has_oop())                    