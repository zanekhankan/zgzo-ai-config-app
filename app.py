import streamlit as st
import json
import os

st.set_page_config(page_title="ZGZO.AI GC Config Creator", layout="centered")
st.title("🛠️ ZGZO.AI - GC Profile Configurator")

# Input form
st.subheader("Enter GC Information")

gc_name = st.text_input("GC Company Name")
license_number = st.text_input("License Number")
contact_email = st.text_input("Contact Email")
phone_number = st.text_input("Phone Number (optional)")
markup_percent = st.number_input("Markup Percentage", min_value=0, max_value=100, value=10)
tone = st.selectbox("Preferred Tone", ["Professional", "Aggressive", "Friendly"])
signature_block = st.text_area("Signature Block", height=100)
legal_text = st.text_area("Custom Legal Language (optional)", height=100)
logo = st.file_uploader("Upload GC Logo (optional)", type=["png", "jpg", "jpeg"])

# Save profile
if st.button("Save GC Profile"):
    config = {
        "gc_name": gc_name,
        "license": license_number,
        "contact": contact_email,
        "phone": phone_number,
        "markup_percent": markup_percent,
        "tone": tone.lower(),
        "signature": signature_block,
        "legal": legal_text,
        "logo_filename": logo.name if logo else ""
    }

    # Save config JSON
    config_dir = "gc_profiles"
    os.makedirs(config_dir, exist_ok=True)
    config_path = os.path.join(config_dir, f"{gc_name.replace(' ', '_').lower()}_config.json")

    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    # Save logo file
    if logo:
        with open(os.path.join(config_dir, logo.name), "wb") as f:
            f.write(logo.read())

    st.success(f"Profile for {gc_name} saved successfully!")

st.markdown("---")
st.markdown("✅ This config will now auto-fill your bid outputs inside ZGZO.AI.")
st.markdown("Use this screen to set up clients, customize their voice, markup, and branding.")
