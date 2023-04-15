#from asyncore import write
import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image



import pickle

st.title("FLOOD Prediction ")
image=Image.open("new_img.jpg")
st.image(image,width=540)

st.subheader('select values')
r1=np.asarray(st.slider('Panchganga',min_value=2000,max_value=5600))
r2=np.asarray(st.slider('Krishna',min_value=3500,max_value=4600))
r3=np.asarray(st.slider('Koyna',min_value=1500,max_value=7500))
r4=np.asarray(st.slider('Gayatri',min_value=1500,max_value=7500))
r5=np.asarray(st.slider('Dudhganga',min_value=1500,max_value=7500))
kol_res=np.asarray(st.slider('Kolhapur Current reserves Level',min_value=1500,max_value=80000))


a=np.asarray([[r1,r2,r3,r4,r5,kol_res]])
#lm=pickle.load(open('TR1_66_mod.h5','rb'))

pkm = pickle.load(open('lr.pkl', 'rb'))



#with open(TR1_66_mod.h5) as fin:
 #   print(pickle.load(fin))

#with open('TR1_66_mod.h5','rb') as file:
   # modl=pickle.load(file)

if st.button('Predict'):
    prd=pkm.predict(a)
    st.write(prd)
    if prd == 0:
        st.write('No flood will occur')

        # plots
     #   sns.set(style="white")
        #make changes  from here
        
        
     
        b=np.asarray([[r1,r2,r3,r4,r5]])
        b1=b.reshape(5,)
        xi=["Panchganga","Krishna","Koyna","Gayatri","Dudhganga"]
        d={"b1":pd.Series(b1,index=xi)}
        df=pd.DataFrame(d)
        
        st.bar_chart(df) 
        
        st.balloons()

    else:
        st.write('High chances of flood')

    #st.write(pkm.predict_proba)


else:
    'Good By'
