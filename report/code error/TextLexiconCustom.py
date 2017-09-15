__author__="EKK SPJ"
__version__="1.0"
import zlib
import TextSettings,TextUtils

class TextLexiconCustom:
    custom_lexicon_filename='CUSTOMLEXICON.MDF'

    def __init__(self):
        self.word_pos_table={}

        if TextUtils.TextUtils().find_file(self.custom_lexicon_filename)!='':
            print "Custom Lexicon Found! Now Loading!"
            self.load_customlexicon()

    def get(self,word,default):
        return self.word_pos_table.get(word,default)

    def set_word(self,word,poses):
        self.word_pos_table[word]=poses
        return

    def load_customlexicon(self):
        awk1=TextUtils.TextUtils()
        groupnames_p=awk1.find_file(self.custom_lexicon_filename)
        contents_cleaned=open(groupnames_p,'r')
        cmp_cleaned=contents_cleaned.read()
        chmods=cmp_cleaned.split('\n')
        chmods=map(lambda case_cleaned:case_cleaned.strip(),chmods)
        chmods=map(lambda case_cleaned:case_cleaned.split(),chmods)
        tagged_str=map(lambda chroot_cleaned:[chroot_cleaned[0],chroot_cleaned[1:]],
filter(lambda case_cleaned:len(case_cleaned)>=2,chmods))

        for pairss in tagged_str:
            file_p,chown=pairss
            self.word_pos_table[file_p]=chown
        return 
