class Foo:

    def __init__(self) -> None:
        self.o = 123

    @property
    def oof_yamete_kudasay(self) -> str:
        return """
___________$$$$$$___________ 
___________$$$$$$___________ 
____________$$$$____________ 
____________$$$$____________ 
____________$$$$____________ 
____________$$$$____________ 
____________$$$$____________ 
____________$$$$____________ 
___________$$$$$$___________ 
___________$$$$$$___________ 
___________$$$$$$___________ 
__________$$$$$$$$__________ 
__________$$$$$$$$__________ 
_____$$$$$$$$$$$$$$$$$$_____ 
____$_____$$$$$$$$_____$____ 
___$______$$$$$$$$______$___ 
___$____________________$___ 
____$__________________$____ 
_____$______$$$$______$_____ 
_____$____$$____$$____$_____ 
____$_____$$____$$_____$____ 
___$________$$$$________$___ 
__$______________________$__ 
_$________________________$_ 
_$________________________$_ 
_$______$$$$$$$$$$$$______$_ 
__$______________________$__ 
___$____________________$___ 
____$$$$____________$$$$____ 
________$$$$$$$$$$$$________
        """
    

a = Foo()
print(
    a.oof_yamete_kudasay
)