import streamlit as st

from planner_agent import plan_goal
from interview_agent import generate_questions
from coding_agent import review_code
from productivity_agent import create_todo

from pdf_parser import extract_resume_text
from ats_calculator import calculate_ats

st.set_page_config(
    page_title="AI Multi-Agent Assistant",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 AI Multi-Agent Personal Assistant")

st.markdown("""
A smart assistant powered by multiple AI agents.

Features:
- 🎯 Planning
- 📄 Resume Analysis
- 🎤 Interview Preparation
- 💻 Coding Assistance
- 📅 Productivity Tracking
""")

# Dashboard
st.subheader("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("ATS Score", "82%")

with col2:
    st.metric("Skills", "12")

with col3:
    st.metric("Interview Score", "78%")

with col4:
    st.metric("Tasks", "8")

st.progress(78)

st.markdown("---")

# Sidebar
st.sidebar.title("AI Agents")

agent = st.sidebar.selectbox(
    "Choose Agent",
    [
        "Planner",
        "Resume",
        "Interview",
        "Coding",
        "Productivity"
    ]
)

# Planner Agent
if agent == "Planner":

    st.header("🎯 Planner Agent")

    goal_type = st.selectbox(
        "Select Goal Type",
        [
            "Career Goal",
            "Learning Goal",
            "Project Goal"
        ]
    )

    if goal_type == "Career Goal":

        goal = st.selectbox(
            "Choose Career Goal",
            [
                "Get a Machine Learning Internship",
                "Become a Data Scientist",
                "Become an AI Engineer",
                "Get a Python Developer Job"
            ]
        )

    elif goal_type == "Learning Goal":

        goal = st.selectbox(
            "Choose Learning Goal",
            [
                "Learn Python",
                "Learn Machine Learning",
                "Learn Deep Learning",
                "Learn Data Science"
            ]
        )

    else:

        goal = st.selectbox(
            "Choose Project Goal",
            [
                "Build AI Interview Coach",
                "Build Resume ATS Analyzer",
                "Build Chatbot",
                "Build Customer Segmentation Project"
            ]
        )

    if st.button("Generate Plan"):

        plan = plan_goal(goal)

        st.success("Plan Generated Successfully")

        st.write(plan)
# Resume Agent
elif agent == "Resume":

    st.header("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if uploaded_file:

        text = extract_resume_text(
            uploaded_file
        )

        ats_score, skills = calculate_ats(
            text
        )

        st.success(
            "Resume Analysis Complete"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "ATS Score",
                ats_score
            )

        with col2:
            st.metric(
                "Skills Found",
                len(skills)
            )

        st.subheader("Skills Found")

        st.write(skills)

        st.subheader("Candidate Summary")

        st.info(
            f"Resume contains {len(skills)} important technical skills."
        )

        report = f"""
ATS Score: {ats_score}

Skills Found:
{', '.join(skills)}
"""

        st.download_button(
            "📥 Download Report",
            report,
            file_name="resume_report.txt"
        )

# Interview Agent
elif agent == "Interview":

    st.header("🎤 Interview Agent")

    role = st.selectbox(
        "Select Role",
        [
            "Machine Learning",
            "Data Science",
            "Python Developer",
            "AI Engineer"
        ]
    )

    if st.button("Generate Questions"):

        questions = generate_questions(
            role
        )

        st.success(
            "Questions Generated"
        )

        st.subheader(
            "Interview Questions"
        )

        for i, q in enumerate(
            questions,
            start=1
        ):

            st.write(
                f"{i}. {q}"
            )

# Coding Agent
elif agent == "Coding":

    st.header("💻 Coding Agent")

    code = st.text_area(
        "Paste Python Code",
        height=300
    )

    if st.button("Review Code"):

        review = review_code(code)

        st.success(
            "Code Reviewed"
        )

        st.subheader(
            "Feedback"
        )

        st.write(review)

        st.metric(
            "Code Quality Score",
            "85/100"
        )

# Productivity Agent
elif agent == "Productivity":

    st.header("📅 Productivity Agent")

    if st.button("Show Tasks"):

        tasks = create_todo()

        st.success(
            "Tasks Generated"
        )

        for task in tasks:

            st.checkbox(task)

        st.metric(
            "Task Count",
            len(tasks)
        )

# Interview Tips
st.markdown("---")

st.subheader("🎯 Interview Tips")

st.info("""
• Be confident

• Explain your projects clearly

• Revise Machine Learning concepts

• Prepare HR questions
""")

# Projects
st.subheader("🚀 Sample Projects")

st.write("• AI Multi-Agent Personal Assistant")
st.write("• AI Interview Preparation Coach")
st.write("• Jarvis Voice Assistant")
st.write("• Hand Gesture Recognition")

# Footer
st.markdown("---")

st.caption(
    "Built with Python, Streamlit and AI Agents 🚀"
)