# import streamlit as st

# st.set_page_config(page_title="AI Smart Bug Analyzer")

# st.title("AI Smart Bug Analyzer & Fix Advisor")

# st.write("Upload or paste your bug report below.")

# bug_report = st.text_area(
#     "Paste Bug Report"
# )

# uploaded_file = st.file_uploader(
#     "Upload Bug Report / Stack Trace / Log File"
# )

# if st.button("Submit"):
#     st.success("Bug Report Submitted Successfully!")

import streamlit as st

st.set_page_config(page_title="AI Smart Bug Analyzer")

st.title("AI Smart Bug Analyzer & Fix Advisor")

st.write("Upload or paste your bug report below.")

bug_report = st.text_area("Paste Bug Report")

uploaded_file = st.file_uploader(
    "Upload Bug Report / Stack Trace / Log File"
)

if st.button("Submit"):

    if bug_report:
        st.subheader("Submitted Bug Report")
        st.write(bug_report)

    if uploaded_file:
        content = uploaded_file.read().decode("utf-8")
        st.subheader("Uploaded File Content")
        st.text(content[:1000])

    st.success("Bug Submitted Successfully!")