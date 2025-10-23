import streamlit as st

st.title("Volunteer Matching System")

# Example inputs
volunteers = st.text_area("Enter volunteer names (comma-separated):", "Alice, Bob, Charlie")
events = st.text_area("Enter event names (comma-separated):", "Beach Cleanup, Tree Planting, Food Drive")

if st.button("Match Volunteers"):
    vol_list = [v.strip() for v in volunteers.split(",")]
    event_list = [e.strip() for e in events.split(",")]

    st.subheader("Matching Results:")
    for v, e in zip(vol_list, event_list):
        st.write(f"✅ {v} → {e}")
