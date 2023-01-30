import streamlit as st
import math




st.title("Noise Calculator")
st.write('###### Created by: Caleb Ginorio MS, CSP')

# Create a list of tuples with title and equation
equations = [("Sound Pressure Level", r"SPL = 20 \log \frac{P}{Po}"),
             ("Sound Intensity Level", r"Li = 10\log\frac{I}{Io}"), 
             ("Sound Power Level", r"PWL = 10\log\frac{W}{Wo}"),
             ("SPL over Distance", r"SPL2 = SPL1 + 20\log\frac{D1}{D2}"),
             ("SPL over Distance in a Free Field", r"Lp = Lw - 20\log{r} + DI - k + CF"),
             ("Directivity Index", r"DI = 10\log{Q}")]

# Use the title as the label in the selectbox
selected_equation = st.sidebar.selectbox("Select an equation:", [eq[0] for eq in equations])

# Find the selected equation using the title
selected_eq = next(eq for eq in equations if eq[0] == selected_equation)

# Display the selected equation
st.latex(selected_eq[1])

# Input fields and calculation
if selected_equation == "Sound Pressure Level":
    P = st.number_input("Enter sound pressure (P):")
    Po = st.number_input("Enter reference pressure (Po):")
    if P and Po:
        SPL = 20 * math.log10(P/Po)
        st.write(" ##### Sound Pressure Level (SPL) =")
        st.latex("20 log(P/Po) = 20 log({}/{}) = {:.2f} ""dB".format(P, Po, SPL))
    st.write("Where:")
    st.latex(" P \\ is \\ the \\ sound \\ pressure")
    st.latex(" P_0 \\ is \\ the \\ reference \\ sound \\ pressure \\ , \\ 0.00002 \\ Pa")

if selected_equation == "Sound Intensity Level":
    I = st.number_input("Enter sound intensity (I):")
    Io = st.number_input("Enter reference sound intensity (Io):")
    if I and Io:
        L = 10 * math.log10(I/Io)
        st.latex(" Sound \\ Intensity \\ Level \\ (L_i) =")
        st.latex("10 log(I/Io) = 10 log({}/{}) = {:.2f} ""dB".format(I, Io, L))
    st.write("Where:")
    st.latex(" I \\  is \\ the \\ sound \\ intensity \\ at \\ some \\ distance \\ from  \\ a \\ source")
    st.latex(" I_0 \\ is \\ the \\ reference \\ sound \\ intensity \\ equal \\ to \\ 10^{-12} \\ W/m^2")

if selected_equation == "Sound Power Level":
    W = st.number_input("Enter sound power (W):")
    Wo = st.number_input("Enter reference sound power (Wo):")
    if W and Wo:
        PWL = 10 * math.log10(W/Wo)
        st.latex(" Sound \\ Power \\ Level \\ (L_w) =")
        st.latex("10 log(W/Wo) = 10 log({}/{}) = {:.2f} ""dB".format(W, Wo, PWL))
    st.write("Where:")
    st.latex(" W \\  is \\ the \\ sound \\ power \\ of \\ the \\ source \\ in \\ Watts")
    st.latex(" W_0 \\ is \\ the \\ reference \\ sound \\ power \\ equal \\ to \\ 10^{-12} \\ Watts")

if selected_equation == "SPL over Distance in a Free Field":
    Lw = st.number_input("Enter the sound power level (Lw):")
    r = st.number_input("Enter the distance from the source (r):")
    DI = st.number_input("Enter the Directivity Index (DI):")
    k = st.number_input("Enter the k constant (k):")
    CF = st.number_input("Enter the any other Correction Factor (CF):")
    if Lw and r:
        Lp = (Lw - 20 * math.log10(r) + DI - k + CF)
        st.latex("L_p \\ =")
        st.latex("L_w - 20 \\log(r) + DI - k + CF \\ = \\ {} \\ - \\ 20 \\log({}) \\ + \\ {} \\ - \\ {} \\ + \\ {} \\ = \\ {:.2f} \\ dB".format(Lw, r, DI, k, CF, Lp))
    st.write(" Where:")
    st.latex(" L_p \\ is \\ sound \\ pressure \\ level")
    st.latex(" L_w \\ is \\ the \\ sound \\ power \\ level")
    st.latex("r \\ is \\ the \\ distance \\ from \\ the \\ source")
    st.latex("k \\ is \\ 11.0 \\ dB \\ when \\ r \\ is \\ in \\ meters \\ and \\ 0.5 \\ dB \\ when \\ r \\ is \\ in \\ feet")
    st.latex("CF \\ is \\ a \\ correction \\ factor \\ for \\ pressure \\ and \\ temperature")


if selected_equation == "SPL over Distance":
    SPL1 = st.number_input("Enter sound pressure level at D1 (SPL1):")
    D1 = st.number_input("Enter original distance from source (D1):")
    D2 = st.number_input("Enter new distance from source (D2)")
    if SPL1 and D1 and D2:
        SPL2 = SPL1 + 20 * math.log10(D2/D1)
        st.latex(" SPL_2 = SPL_1 + 20 \\log_{10} \\left( \\frac{D_2}{D_1} \\right)")
        st.latex(" = {:.2f} \\text{{dB}}".format(SPL2))
    st.write("Where:")
    st.latex(" SPL_2 \\  is \\ the \\ sound \\ pressure \\ level \\ at \\ D2 ")
    st.latex(" D1 \\ is \\ the \\ original \\ distance \\ from \\ the \\ source")
    st.latex(" D2 \\ is \\ the \\ new \\ distance \\ from \\ the \\ source")


if selected_equation == "Directivity Index":
    Q = st.number_input("Enter Directivity Factor (Q):")
    if Q:
        DI = 10 * math.log10(Q)
        st.latex(" Directivity \\ Index \\ (DI) =")
        st.latex("10 log(Q) = 10 log({}) = {:.2f} """.format(Q, DI))
    st.write("For:")
    st.write("- Sphere: Q = 1")
    st.write("- Hemisphere: Q = 2")
    st.write("- 1/4 Sphere: Q = 4")
    st.write("- 1/8 Sphere: Q = 8")
    
