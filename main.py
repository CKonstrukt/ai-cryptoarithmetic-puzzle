import streamlit as st
from ai import Solver

st.title("Cryptarithmetic Puzzle Solver")

area = st.text_area("Enter the words, seperated by a new line")
factors = [word.strip().lower() for word in area.split('\n') if word.strip() != '']

operator = st.radio("Select the operator", ('\+', '\-', '\*', '\/'))[1]

solution = st.text_input("Enter the solution").lower()

if (st.button("Solve", type="primary")):
    if not area or not solution:
        st.error(f"Do not leave the {'words' if not area else 'solution'} empty")
        st.stop()

    if len(set(solution + ''.join(factors))) > 10:
        st.error("Solution and words can only contain up to 10 unique letters")
        st.stop()

    if len(max(factors, key=len)) > 5 or len(solution) > 5:
        st.error(f"{'Each of the words' if not len(solution) > 5 else 'The solution'} shouldn't be longer than 5 letters")
        st.stop()

    st.markdown("---")
    st.header("Result")

    solver = Solver(factors, operator, solution)

    with st.spinner("Solving..."):
        output = solver.solve()
    
    if not output:
        st.error("No result found")
        st.stop()

    wordsCodeText = f"{''.join([f'{word} {operator} ' if idx != len(factors)-1 else word for (idx, word) in enumerate(factors)])} = {solution}"
    outputCodeText = ''.join([str(output[char]) if char.isalpha() else char for char in wordsCodeText])

    col1, col2 = st.columns(2)
    with col1:
        st.text("from")
        st.code(wordsCodeText)

    with col2:
        st.text("to")
        st.code(outputCodeText)