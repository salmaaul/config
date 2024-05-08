import streamlit as st

# Electron configuration for atoms
electron_config = {
    "Hidrogen[H]": "1s1",
    "Helium[He]": "1s2",
    "Lithium[Li]": "1s2 2s1",
    "Berilium[Be]": "1s2 2s2",
    "Boron[B]": "1s2 2s2 2p1",
    "Karbon[C]": "1s2 2s2 2p2",
    "Nitrogen[Ni]": "1s2 2s2 2p3",
    "Oksigen[O]": "1s2 2s2 2p4",
    "Fluorin[F]": "1s2 2s2 2p5",
    "Neon[Ne]":"1s2 2s2 2p6",
    "Natrium[Na]":"1s2 2s2 2p6 3s1",
    "Magnesium[Mg]":"1s2 2s2 2p6 3s2",
    "Aluminium[Al]":"1s2 2s2 2p6 3s2 3p1",
    "Silikon[Si]":"1s2 2s2 2p6 3s2 3p2",
    "Fosforus[P] ":"1s2 2s2 2p6 3s2 3p3",
    "Belerang[S]": "1s2	2s2	2p6	3s2	3p4",
    "Klorin[Cl]":"1s2 2s2 2p6 3s2 3p5",
    "Argon[Ar]":"1s2 2s2 2p6 3s2 3p6",
    "Kalium[K]":"1s2 2s2 2p6 3s2 3p6 4s1",
    "Kalsium[Ca]":"1s2 2s2 2p6 3s2 3p6 4s2",
    "Skandium[Sc]":"1s2	2s2	2p6	3s2	3p6 3d1 4s2",
    "Titanium[Ti]":"1s2	2s2	2p6	3s2	3p6	3d2	4s2",
    "Vanadium[V]":"1s2 2s2 2p6 3s2 3p6 3d3 4s2",
    "Kromium[Cr]":"1s2 2s2 2p6 3s2 3p6 3d5 4s1",
    "Mangan[Mn]":"1s2 2s2 2p6 3s2 3p6 3d5 4s2",
    "Besi[Fe]":"1s2 2s2	2p6	3s2	3p6	3d6	4s2",
    "Kobalt[Co]":"1s2 2s2 2p6 3s2 3p6 3d7 4s2",
    "Nikel[Ni]":"1s2 2s2 2p6 3s2 3p6 3d8 4s2",
    "Tembaga[Cu]":"1s2 2s2 2p6 3s2 3p6 3d10 4s1",
    "Seng[Zn]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2",
    "Galium[Ga]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2	4p1",
    "Germanium[Ge]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p2",
    "Arsenik[As]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p3",
    "Selenium[Se]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p4",
    "Bromin[Br]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p5",
    "Kripton[Kr]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6",
    "Rubidium[Rb]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 5s1",
    "Stronsium[Sr]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s2",
    "Ittrium[Y]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d1 5s2",
    "Zirkonium[Zr]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d2 5s2",
    "Niobium[Nb]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d4 5s1",
    "Molibdenum[Mo]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s1",
    "Teknisium[Tc]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s2",
    "Rutenium[Ru]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d7 5s1",
    "Rodium[Rh]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d8 5s1",
    "Paladium[Pd]":"1s2	2s2	2p6	3s2	3p6	3d10 4s2 4p6 4d10",
    "Perak[Ag]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s1",
    "Kadmium[Cd]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2",
    "Indium[In]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p1",
    "Timah[Sn]":"1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p2",
}

st.title("Electron Configuration")
st.write("Select an atomic number:")

atomic_number = st.selectbox("Atomic Name", list(electron_config.keys()))

st.write("Electron Configuration:")
st.write(electron_config[atomic_number])