import streamlit as st
import requests

# Streamlit page settings
st.set_page_config(page_title="FAQ Agent", page_icon="🤖", layout="centered")
st.title("🤖 FAQ Agent")
st.markdown("Ask a question and get an intelligent answer from the agent.")

# Input form
with st.form("faq_form"):
    query = st.text_input("Enter your question:", value="How do I reset my password?")
    style = st.selectbox("Select response style:", options=["default", "friendly", "formal"])
    submit = st.form_submit_button("Ask Agent")

# On submit
if submit:
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Getting response from agent..."):
            try:
                response = requests.post(
                    "http://localhost:8000/agent-ask",
                    json={"query": query, "style": style}
                )
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Answer:")
                    st.write(data["answer"])

                    if data.get("sources"):
                        st.markdown("#### 🔍 Sources")
                        for s in data["sources"]:
                            st.markdown(f"- **{s['source']}**: {s['content']}")
                else:
                    st.error(f"❌ Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"⚠️ Request failed: {e}")