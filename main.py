import streamlit as st

import pandas as pd

name = st.text_input("Enter Your Name : ")
fname = st.text_input("Enter Your Father Name : ")
address = st.text_area("Enter Your Text : ")
classdata = st.selectbox("Enter Your Class : ",(1,2,3,4,5,6))


button = st.button("Done")
if button:
    st.markdown(f""""
    Name : {name}
    Father_Name : {fname}
    address : {address}
    Class : {classdata}""")







# dataset = pd.read_csv("titlecsv.csv")
# st.dataframe(dataset)


# st.title("welcome to asim")
# st.header("python")
# st.subheader("java")
# st.markdown("i love python")
# st.code("""for i in range(1,5,1)
#                 print("hello")
#         """)