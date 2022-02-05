import streamlit as st

def g(ot):
    gdict = {'א':1, 'ב':2, 'ג':3, 'ד':4, 'ה':5, 'ו':6, 'ז':7, 'ח':8,
             'ט':9, 'י':10, 'כ':20,'ך':20, 'ל':30, 'מ':40, 'ם':40, 'נ':50, 'ן':50, 'ס':60, 'ע':70,
             'פ':80, 'ף':80, 'צ':90, 'ץ':90, 'ק':100, 'ר':200, 'ש':300, 'ת':400}
    
    if ot in gdict:
        return gdict[ot]
    else:
        return 0

mila = st.text_input('כתוב מילה: ')
misparim = [g(ot) for ot in mila if g(ot)>0]

st.write( '+'.join([str(m) for m in misparim]), '=', sum(misparim) )    # sum סכום
                                                                     # str string תהפוך מספר לטקסט
                                                                     # int integer (שלם) תהפוך טקסט למספר 
