import sys

class CustomPrint(object):
    def __init__(self, prefix, print_type_array, verbosities):
        self.__print_type_array__ = print_type_array
        self.__verbosities__ = verbosities
        for verbosity in verbosities:
            if verbosity not in print_type_array:
                raise Exception("Allowed verbosity must be in the list")

        self.__prefix__ = prefix

    def __call__(self, print_type, *values, **kwargs):
        if print_type not in self.__print_type_array__:
            raise Exception(f"Print type must be one of {self.__print_type_array__}, rather than {print_type}")
        
        if print_type not in self.__verbosities__:
            return

        if self.__prefix__:
            print(f"{print_type} from {self.__prefix__}:", *values, **kwargs)
        else:
            print(*values, **kwargs)

    def use_dict(self, d):
        for print_type in d:
            try:
                self(print_type, d[print_type])
            except:
                continue

class StandardPrint(CustomPrint):
    def __init__(self, prefix, verbosities):
        super().__init__(prefix, ["error", "warning", "notification", "debug"], verbosities)

if __name__ == "__main__":
    __print__ = StandardPrint("aa", ["error", "debug"])
    __print__("huy", print_type= "error", end = "1")