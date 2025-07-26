import streamlit as st

st.set_page_config(page_title="DJ Saitama", page_icon="🎧", layout="wide")

# Hero
st.image("assets/auxplatines.png", use_column_width=True)
st.markdown("<h1 style='text-align: center; color: #e6007a;'>DJ Saitama</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Djing Technician & Liege Party Icon</p>", unsafe_allow_html=True)

# Navigation
menu = st.sidebar.radio("Navigation", ["Accueil", "Biographie", "Dates", "Musique", "Galerie", "Contact"])

if menu == "Biographie":
    st.header("Biographie")
    st.write("Icône liegeoise des soirées urbaines, DJ Saitama fait vibrer les foules depuis plus de 10 ans...")

elif menu == "Dates":
    st.header("Dates de tournée")
    st.table([
        ["24 Août 2025", "Paris, France"],
        ["31 Août 2025", "Berlin, Allemagne"],
        ["7 Sept 2025", "Amsterdam, Pays-Bas"]
    ])

elif menu == "Musique":
    st.header("Derniers morceaux")
    st.markdown(
        '<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" '
        'src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1343537113&color=%23ff0080&auto_play=false&show_artwork=true"></iframe>',
        unsafe_allow_html=True
    )
    st.write("[Spotify](#) | [Apple Music](#) | [Deezer](#)")

elif menu == "Galerie":
    st.header("Galerie")
    cols = st.columns(3)
    cols[0].image("assets/auphone.png", caption="DJ Saitama 1")
    cols[1].image("assets/aumic.png", caption="DJ Saitama 2")
    cols[2].image("assets/fondang.png", caption="DJ Saitama 3")

elif menu == "Contact":
    st.header("Contact")
    with st.form("contact_form"):
        name = st.text_input("Nom")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Envoyer")
        if submitted:
            st.success("Message envoyé !")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: small;'>&copy; 2025 DJ Saitama. Tous droits réservés.</p>", unsafe_allow_html=True)