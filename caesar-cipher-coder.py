import streamlit as st

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

st.title("🕵️‍♂️ Secret Agent Caesar Cipher 🕵️‍♀️")

st.write("🔐 **Type 'encode' to encrypt or 'decode' to decrypt:**")
direction = st.text_input("Your mission:").lower()
st.write("📝 **Enter the text you want to encrypt/decrypt:**")
text = st.text_input("Secret message:").lower()
st.write("🔢 **Enter the shift value:**")
shift = st.number_input("Shift value:", min_value=0, max_value=25, step=1)

def encrypt(text, shift):
    result = ""   
    for i in text:
        if i in alphabet:   
            position = alphabet.index(i)
            new_position = (position + shift) % 26
            result += alphabet[new_position]
        else:
            result += i
    return result
    
def decrypt(text, shift):
    result = ""
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position - shift) % 26
            result += alphabet[new_position]
        else:
            result += i
    return result

if st.button("🕵️‍♂️ Start Mission 🕵️‍♀️"):
    if direction == 'encode':
        result = encrypt(text, shift)
        st.write("🔒 **Encoded Text:**", result)
    elif direction == 'decode':
        result = decrypt(text, shift)
        st.write("🔓 **Decoded Text:**", result)
    else:
        st.write("❌ **Invalid direction. Please type 'encode' or 'decode'.**")
