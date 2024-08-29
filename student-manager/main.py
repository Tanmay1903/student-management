import streamlit as st
from langchain_utils import process_instruction
from api_utils import add_student, add_score, get_subject, summarize_scores

st.title("Professor's Assistant")

instruction = st.text_input("Enter professor's instruction:")

if st.button("Process Instruction"):
    if instruction:
        # Process the instruction
        result = process_instruction(instruction)
        intent = result.get('intent')
        entities = result.get('entities')

        # Based on intent, call the appropriate API function
        if intent == 'add_student':
            name = entities.get('name')
            student_id = entities.get('id')
            response = add_student(name, student_id)
            if "error" in response:
                st.error(response["error"])
            else:
                st.success(response.get('message', 'Student added successfully!'))

        elif intent == 'add_score':
            student_name = entities.get('name')
            subject = entities.get('subject')
            score = entities.get('score')
            response = add_score(student_name, subject, score)
            if "error" in response:
                st.error(response["error"])
            else:
                st.success(response.get('message', 'Score added successfully!'))

        elif intent == 'get_subject':
            student_name = entities.get('name')
            response = get_subject(student_name)
            if "error" in response:
                st.error(response["error"])
            else:
                st.write(response.get('subjects', 'Subject not found'))

        elif intent == 'summarize_scores':
            subject = entities.get('subject')
            response = summarize_scores(subject)
            if "error" in response:
                st.error(response["error"])
            else:
                st.write(response.get('summary', 'No scores available'))

        else:
            st.error("Unknown instruction or intent.")
    else:
        st.error("Please enter an instruction.")
