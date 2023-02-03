import streamlit as st
import math
import numpy as np




st.title("Noise Equations")
st.write('#### Created by: Caleb Ginorio MS, CSP')
st.write('Please select an equation from the side bar')


# Create a list of tuples with title and equation
equations = [("Sound Pressure Level", r"SPL = 20 \log \frac{P}{P_0}"),
             ("Sound Intensity Level", r"L_{i} = 10\log\frac{I}{I_0}"), 
             ("Sound Power Level", r"L_{w} = 10\log\frac{W}{W_0}"),
             ("SPL over Distance", r"SPL_{2} = SPL_{1} + 20\log\frac{D_1}{D_2}"),
             ("SPL over Distance in a Free Field", r"L_{p} = L_{w} - 20\log{r} + DI - k + CF"),
             ("Directivity Index", r"DI = 10\log{Q}"),
             ("Noise Dose", r"Dose\left(\%\right) = 100\left(\frac{C_1}{T_1} + \frac{C_2}{T_2} + \cdots + \frac{C_n}{T_n}\right)"),
             ("TWA", r"TWA = 16.61\log\frac{\%D}{100} + 90 dBA"),
             ("TWA(eq)", r"TWA_{eq} = 10\log\frac{\%D}{100} + 85 dBA"),
             ("Allowed Time", r"T_p = T_c / (2^{(L_{as} - L_{c})/ER})")]

col1, col2, col3, col4 = st.beta_columns(4)

# Use the title as the label in the selectbox
selected_equation = st.sidebar.selectbox("Select an equation:", [eq[0] for eq in equations])

# Find the selected equation using the title
selected_eq = next(eq for eq in equations if eq[0] == selected_equation)



# Input fields and calculation

if selected_equation == "":
    st.write("Select an equation from the side bar")

if selected_equation == "Sound Pressure Level":
    col1.latex(r"SPL = 20 \log \frac{P}{P_0}")
    col1.write(" ###### Where:")
    col1.latex("SPL \\ is \\ the \\ sound \\ pressure \\ level \\ in \\ dB")
    col1.latex("P \\ is \\ the \\ sound \\ pressure")
    col1.latex("P_0 \\ is \\ the \\ reference \\ sound \\ pressure \\ , \\ 0.00002 \\ Pa")
    P = st.number_input("Enter sound pressure (P):")
    Po = st.number_input("Enter reference pressure (Po):")
    if P and Po:
        SPL = 20 * math.log10(P/Po)
        st.write(" ##### Sound Pressure Level (SPL) =")
        st.latex("20 log(P/Po) = 20 log({}/{}) = {:.2f} ""dB".format(P, Po, SPL))

if selected_equation == "Sound Intensity Level":
    col1.latex(r"L_{i} = 10\log\frac{I}{I_0}")
    col1.write(" ###### Where:")
    col1.latex(" I \\  is \\ the \\ sound \\ intensity \\ at \\ some \\ distance \\ from  \\ a \\ source")
    col1.latex(" I_0 \\ is \\ the \\ reference \\ sound \\ intensity \\ equal \\ to \\ 10^{-12} \\ W/m^2")
    I = st.number_input("Enter sound intensity (I):")
    Io = st.number_input("Enter reference sound intensity (Io):")
    if I and Io:
        L = 10 * math.log10(I/Io)
        st.latex(" Sound \\ Intensity \\ Level \\ (L_i) =")
        st.latex("10 log(I/Io) = 10 log({}/{}) = {:.2f} ""dB".format(I, Io, L))

if selected_equation == "Sound Power Level":
    col1.latex(r"L_w = 10 \log \frac{W}{W_0}")
    col1.write(" ###### Where:")
    col1.latex(" W \\  is \\ the \\ sound \\ power \\ of \\ the \\ source \\ in \\ Watts")
    col1.latex(" W_0 \\ is \\ the \\ reference \\ sound \\ power \\ equal \\ to \\ 10^{-12} \\ Watts")
    W = st.number_input("Enter sound power (W):")
    Wo = st.number_input("Enter reference sound power (Wo):")
    if W and Wo:
        PWL = 10 * math.log10(W/Wo)
        st.latex(" Sound \\ Power \\ Level \\ (L_w) =")
        st.latex("10 log(W/Wo) = 10 log({}/{}) = {:.2f} ""dB".format(W, Wo, PWL))


if selected_equation == "SPL over Distance in a Free Field":
    col1.latex(r"L_{p} = L_{w} - 20\log{r} + DI - k + CF")
    col1.write("###### Where:")
    col1.latex(" L_p \\ is \\ sound \\ pressure \\ level")
    col1.latex(" L_w \\ is \\ the \\ sound \\ power \\ level")
    col1.latex("r \\ is \\ the \\ distance \\ from \\ the \\ source")
    col1.latex("k \\ is \\ 11.0 \\ dB \\ when \\ r \\ is \\ in \\ meters \\ and \\ 0.5 \\ dB \\ when \\ r \\ is \\ in \\ feet")
    col1.latex("CF \\ is \\ a \\ correction \\ factor \\ for \\ pressure \\ and \\ temperature")
    Lw = st.number_input("Enter the sound power level (Lw):")
    r = st.number_input("Enter the distance from the source (r):")
    DI = st.number_input("Enter the Directivity Index (DI):")
    k = st.number_input("Enter the k constant (k):")
    CF = st.number_input("Enter the any other Correction Factor (CF):")
    if Lw and r:
        Lp = (Lw - 20 * math.log10(r) + DI - k + CF)
        st.latex("L_p \\ =")
        st.latex("L_w - 20 \\log(r) + DI - k + CF \\ = \\ {} \\ - \\ 20 \\log({}) \\ + \\ {} \\ - \\ {} \\ + \\ {} \\ = \\ {:.2f} \\ dB".format(Lw, r, DI, k, CF, Lp))


if selected_equation == "SPL over Distance":
    col1.latex(r"SPL_{2} = SPL_{1} + 20\log\frac{D_1}{D_2}")
    col1.write("###### Where:")
    col1.latex(" SPL_2 \\  is \\ the \\ sound \\ pressure \\ level \\ at \\ D_2 ")
    col1.latex(" SPL_1 \\  is \\ the \\ sound \\ pressure \\ level \\ at \\ D_1 ")
    col1.latex(" D_1 \\ is \\ the \\ original \\ distance \\ from \\ the \\ source")
    col1.latex(" D_2 \\ is \\ the \\ new \\ distance \\ from \\ the \\ source")
    SPL1 = st.number_input("Enter sound pressure level at D1 (SPL1):")
    D1 = st.number_input("Enter original distance from source (D1):")
    D2 = st.number_input("Enter new distance from source (D2)")
    if SPL1 and D1 and D2:
        SPL2 = SPL1 + 20 * math.log10(D1/D2)
        st.latex(" SPL_2 = {} + 20log({}/{}) = {:.2f} \\text{{dB}}".format(SPL1, D1, D2, SPL2))


if selected_equation == "Directivity Index":
    col1.latex(r"DI = 10\log{Q}")
    col1.write("###### Where:")
    col1.latex(" DI \\  is \\ the \\ directivity\\ index")
    col1.latex(" Q \\  is \\ the \\ directivity \\ factor")
    Q = st.number_input("Enter Directivity Factor (Q):")
    if Q:
        DI = 10 * math.log10(Q)
        st.latex(" Directivity \\ Index \\ (DI) =")
        st.latex("10 log(Q) = 10 log({}) = {:.2f} """.format(Q, DI))
    st.write("###### For:")
    st.write("- Sphere: Q = 1")
    st.write("- Hemisphere: Q = 2")
    st.write("- 1/4 Sphere: Q = 4")
    st.write("- 1/8 Sphere: Q = 8")


if selected_equation == "Noise Dose":
    col1.latex(r"Dose\left(\%\right) = 100\left(\frac{C_1}{T_1} + \frac{C_2}{T_2} + \cdots + \frac{C_n}{T_n}\right)")
    col1.write(" ###### Where:")
    col1.latex(" C \\  is \\ the \\ actual \\ time \\ exposed \\ at \\ each \\ dB \\ level")
    col1.latex(" T \\ is \\ the \\ time \\ allowed \\ to \\ be \\ exposed \\ at \\ each \\ dB \\ level")
    def dose(c, t):
        return 100 * sum(ci / ti for ci, ti in zip(c, t))
    st.write("### Dose Calculation")
    n = int(st.number_input("How many C and T values do you want to enter?", step =1))
    c = [st.text_input(f"Enter C{i}") for i in range(1, n + 1)]
    t = [st.text_input(f"Enter T{i}") for i in range(1, n + 1)]
    if all(c) and all(t):
        c = list(map(float, c))
        t = list(map(float, t))
        result = dose(c, t)
        st.latex(" Dose =")
        eq = " + ".join("{:.2f}/{:.2f}".format(ci, ti) for ci, ti in zip(c, t))
        st.latex("100({}) = {:.2f}\%".format(eq, result))
    else:
        st.write("Please enter values for C and T")

if selected_equation == "TWA":
    col1.latex(r"TWA = 16.61\log\frac{\%D}{100} + 90 dBA")
    col1.write(" ###### Where:")
    col1.latex(" TWA \\  is \\ the \\ time \\ weighted \\ average")
    col1.latex(" \%D \\ is \\ the \\ noise \\ dose")
    D = st.number_input("Enter Dose (D):", key="D")
    TWA = st.number_input("Or enter TWA:", key="TWA")
    if TWA and D:
        st.write("Enter either TWA or Dose.")
    else:
        if TWA:
            D_calc = np.exp((TWA - 90 + 16.6) / 16.6) * 100
            st.write("D =", D_calc, "cm")
        if D:
            TWA_calc = 16.6 * np.log10(D / 100) + 90
            st.write("TWA =", TWA_calc, "dB")
  
if selected_equation == "Allowed Time":
    col1.latex(r"T_p = \frac{T_c}{2^{(L_{as} - L_{c})/ER}}")
    col1.write(" ###### Where:")
    col1.latex(" T_p \\  is \\ the \\ maximum \\ permissible \\ exposure \\ time")
    col1.latex(" T_c \\  is \\ the \\ criterion \\ time")
    col1.latex(" L_{as} \\  is \\ the \\ measured \\ sound \\ level")
    col1.latex(" L_c \\  is \\ the \\ criteria \\ level")
    col1.latex(" ER \\  is \\ the \\ exchange \\ rate")
    W = st.number_input("Enter sound power (W):")
    Wo = st.number_input("Enter reference sound power (Wo):")
    if W and Wo:
        PWL = 10 * math.log10(W/Wo)
        st.latex(" Sound \\ Power \\ Level \\ (L_w) =")
        st.latex("10 log(W/Wo) = 10 log({}/{}) = {:.2f} ""dB".format(W, Wo, PWL)) 












    #st.write(" ###### Where:")
    #st.latex(" TWA \\  is \\ the \\ time \\ weighted \\ average")
    #st.latex(" \%D \\ is \\ the \\ noise \\ dose")
    #s = st.number_input("Enter % Dose:")
    #t = st.number_input("Or enter TWA")
    #if s != "":
     #   TWA = 10 * (s)
      #  st.latex(" TWA =")
       # st.latex("10 * s = 10 ({:.2f}) """.format(TWA))
    #else: 
        #Dose = 10 + t
        #st.latex("dose = {}".format(Dose))

    #def twa_equation(t, d):
        #if t != "":
    #    c = float(a) + float(b)
     #   return f"c = {c}"
    #elif a != "" and c != "":
     #   b = float(c) - float(a)
      #  return f"b = {b}"
    #elif b != "" and c != "":
     #   a = float(c) - float(b)
      #  return f"a = {a}"
    #else:
     #   return "Enter values for two variables only"

#st.title("Equation Solver")

#a = st.text_input("Enter the value of a: ")
#b = st.text_input("Enter the value of b: ")
#c = st.text_input("Enter the value of c: ")

#result = solve_equation(a, b, c)

#st.write("The solution is: ", result)
