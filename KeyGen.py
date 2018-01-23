# Wing IDE Professional 6.x KeyGen
# made to run on Python3.x and Python2.7 

from __future__ import print_function
try:
    from future import standard_library
except ImportError as e:
    try:
        m = "Probably something with module 'future' not found"
        m = e.message
    finally:
        input ('ImportError: ' + m + ' \nrun [c:\Python27\Scripts\]\n'
               '-> pip install future\n'
           'To install python 2/3 compatibility layer')
    exit()

standard_library.install_aliases()
from future.builtins import (input, str, range)

import string
import random
import hashlib


def randomstring(size = 20, chars = string.ascii_uppercase + string.digits):
    return ''.join(( random.choice( chars ) for _ in range(size) ) )


def BaseConvertHex( number, to_digits, 
                    ignore_negative = True):
    # isNegative = number < 0

    # if isNegative and not ignore_negative:
    #     number = abs( number )

    # make an integer out of the number
    x = int( number, 16)


    # create the result in base 'len(to_digits)'
    res = ''
    toDigitsLen   = len( to_digits )
    
    while x > 0:  # divide of /seperate digit's from x until it's empty
        digit =   x % toDigitsLen
        res   =   to_digits[ digit ] + res
        x   //=   toDigitsLen

    #  if isNegative:
    #      res = - res

    return res

def AddHyphens( code ):
    """Insert hyphens into given license id or activation request to
    make it easier to read"""
    return code[   : 5 ] + '-' + \
           code[  5:10 ] + '-' + \
           code[ 10:15 ] + '-' + \
           code[ 15:   ]


def ToBase30( digest ):

    
    result = BaseConvertHex( digest .upper(),  BASE30)


    return result .rjust( KeyLen, '1' )


def mulHash16( ecx, lichash ):
    part = 0
    for c in lichash:
        part *= ecx  
        part += ord( c ) 
        part &= 0xFFFFF

    return format( part, '05x' )

def GenRandomLicID():
    LicenseId   = AddHyphens( Prefix_LicenseId + 
                        #BASE30[1] * (KeyLen + 1) )
                        randomstring( 18, BASE30))
    return LicenseId


def GetRequestCode(Prefix_requestCode):
    RequestCode = input( \
        'Enter request code : ' ).upper()


    if RequestCode.startswith(Prefix_requestCode) == False:
        print(
                (' '*19) + '  ' + Prefix_requestCode.ljust(5,"x") + '-xxxxx'*3 + '\n' +
                (' '*14) + 'OOPS : Your request code should start with: ' + Prefix_requestCode + '...\n' +
                (' '*14) + '       You probably made a mistake, \n' +
                (' '*14) + ' ...or didn\'t enter anything at all.\n' +
                (' '*14) + '       Like this the activation code WON\'T WORK !\n' 
            )
    return RequestCode


def GenActivationCode( LicenseId, RequestCode):
    # 1. Gen SHA1 from 'activation code' and 'LicenseId'
    hasher                  = hashlib.sha1( (RequestCode + LicenseId) .encode() ) \
                                     .hexdigest()

    # 2. Take only every second diget; starting with the first
    Every2ndDigest = ''.join( [ c for i, c in enumerate( hasher ) if i % 2 == 0 ] )

    lichash = ToBase30( Every2ndDigest ) 
    
    # 3. Apply mulhash
    part5   = ''.join( [               \
                mulHash16( key,  lichash)  \
                 for key in KeyLicVer     ])

    part5   = Prefix_ActivationCode + \
              ToBase30( part5 ) 
    return AddHyphens ( part5 )

#kOSRequestCodes = {
 #'win32': 'W', # -> RW...
 #'linux': 'L',
 #'darwi': 'M',
 #'sunos': 'N',
 #'freeb': 'F',
 #'tru64': 'T',
 #'netbs': 'E',
 #'openb': 'B'
#}
#OSRequestCodes[sys.platform[:5]]

#########################################################
##
##  M a i n
##
# Key vectors for Wing IDE Professional x
#<Wing IDE 6.0>\bin\ide-2.7\src\process\pycontrol.pyo
KeyLicVer2            = [ 123, 202,  97, 211 ]
KeyLicVer3            = [ 127,  45, 209, 198 ] 
KeyLicVer4            = [ 240,   4,  47,  98 ]
KeyLicVer5            = [   7, 123,  23,  87 ]
KeyLicVer6            = [  23, 161,  47,   9 ]

#Gen for Ver6
KeyLicVer             = KeyLicVer6
WingVer               = 6

Prefix_LicenseId      = 'CN'
Prefix_requestCode    = 'R' # 'RP' -> linux   os.uname = 'ppc', 'ppc64'
Prefix_ActivationCode = 'AXX'
KeyLen                = 17

BASE16 = '0123456789ABCDEF'
BASE30 = BASE16[1:] +'GH''JKLMNPQR''T''VWXY' # no I,S,U



print('Wing IDE Professional ' + str(WingVer) + '.x - Keygen v1\n' + \
      '=' * 37 + '\n')


#0. ModuleTesting: 
assert(                    Prefix_ActivationCode + "23-QB7YB-6RG4M-YFQ86" == \
        GenActivationCode( Prefix_LicenseId + "222-22222-22222-22222", "") )


# 1. Gen random LicID
LicenseId      = GenRandomLicID()
print('License id         : ' + LicenseId)

# 2. GetRequestCode
RequestCode    = GetRequestCode(Prefix_requestCode)
    
# 3. Gen activation code
ActivationCode = GenActivationCode( LicenseId, RequestCode )
print('Activation    code : ' +  ActivationCode )

input('\nGood luck !                             cw2k [at] gmx [dot] net')

