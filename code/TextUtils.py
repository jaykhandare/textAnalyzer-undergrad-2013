__author__="EKK SPJ"
__version__="1.0"
import os,string,sys

class TextUtils:

    def __init__(self):
        pass

    def find_file(self,filename):

        if filename in os.listdir('.'):
            return './'+filename

        if os.environ.has_key('TextA'):
            csplits=os.environ['TextA'].split(';')
            csplits=map(lambda groupss:groupss.strip(),csplits)

            for enabled_arr in csplits:

                try :

                    if filename in os.listdir(enabled_arr):
                        return enabled_arr+'/'+filename
                except :
                    pass

        if os.environ.has_key('PATH'):
            csplits=os.environ['PATH'].split(';')
            csplits=map(lambda groupss:groupss.strip(),csplits)

            for enabled_arr in csplits:

                try :

                    if filename in os.listdir(enabled_arr):
                        return enabled_arr+'/'+filename
                except :
                    pass
        return ''
