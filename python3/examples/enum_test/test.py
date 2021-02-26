#!/usr/bin/env python3

# Add this import, LocatorException and Locator to own file (locator.py?)
import enum

class LocatorException(Exception):
    pass

# From https://stackoverflow.com/a/19300424
class Locator(enum.Enum):
    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, android, ios):
        self.__android = android
        self.__ios = ios

    def for_os(self, os_type):
        if os_type is Os.ANDROID:
            locator = self.__android
        elif os_type is Os.IOS:
            locator = self.__ios
        else:
            raise LocatorException("OS '" + str(os_type) + "' is not supported")

        if locator is None:
            raise LocatorException(\
                "Locator '" + str(self) + "' is not defined for OS '" + str(os_type) + "'")
        return locator

# Add to own file (os.py?)
class Os(enum.Enum):
    ANDROID = 1,
    IOS = 2

# Replace the Locator class in PageAlerts with this one. Define your own enums
class PageAlertLocator(Locator):
    OK_BTN = \
        (1, 'A_OK_BTN'),\
        (5, 'I_OK_BTN')
    CANCEL_BTN = \
        'A_CANCEL_BTN',\
        'I_CANCEL_BTN'
    THE_BTN = OK_BTN
    OTHER_BTN = \
        'asdfasdf',\
        None

# Add to UAXAppBase class
def get_locator(locator):
    os_type = Os.IOS
    return locator.for_os(os_type)

def testLocator(locator):
    print(locator)
    print(repr(locator))
    print(locator.for_os(Os.ANDROID))
    print(locator.for_os(Os.IOS))
    print()

#testLocator(PageAlertLocator.OK_BTN)
#testLocator(PageAlertLocator.CANCEL_BTN)
#testLocator(PageAlertLocator.THE_BTN)
#testLocator(PageAlertLocator.OTHER_BTN)

print(get_locator(PageAlertLocator.OK_BTN))
